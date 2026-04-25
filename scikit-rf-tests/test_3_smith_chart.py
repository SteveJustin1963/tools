#!/usr/bin/env python3
"""
Test 3: Smith Chart with Different Impedances
Tests Smith chart generation with various load impedances and VSWR calculations.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import scikit_rf as rf

def test_smith_chart():
    """Test Smith Chart with different impedances"""
    print("=== Test 3: Smith Chart Analysis ===")

    freq = rf.Frequency(start=0.1, stop=5, npoints=201, unit='ghz')
    z0 = 50  # Reference impedance

    # Various load impedances to plot on Smith chart
    loads = {
        'Short': 0+0j,
        'Open': np.inf+0j,
        'Match': 50+0j,
        'Inductive': 50+50j,    # +j50Ω
        'Capacitive': 50-50j,   # -j50Ω  
        'High Z': 100+0j,       # 100Ω resistive
        'Low Z': 25+0j,         # 25Ω resistive
        'Complex': 75+25j       # 75+j25Ω
    }

    # Convert to S11 (reflection coefficient) networks
    networks = {}
    print("Load impedance analysis:")
    
    for name, z_load in loads.items():
        if z_load == np.inf:
            # Open circuit
            gamma = np.ones(len(freq), dtype=complex)  # Γ = +1
        elif z_load == 0:
            # Short circuit  
            gamma = -np.ones(len(freq), dtype=complex)  # Γ = -1
        else:
            # Calculate reflection coefficient: Γ = (Z_L - Z0) / (Z_L + Z0)
            gamma = (z_load - z0) / (z_load + z0)
            gamma = np.full(len(freq), gamma, dtype=complex)
        
        s_data = np.zeros((len(freq), 1, 1), dtype=complex)
        s_data[:, 0, 0] = gamma
        
        net = rf.Network(frequency=freq, s=s_data, name=name, z0=z0)
        networks[name] = net
        
        # Calculate VSWR
        gamma_mag = abs(gamma[0])
        if gamma_mag < 1:
            vswr = (1 + gamma_mag) / (1 - gamma_mag)
        else:
            vswr = np.inf
        
        print(f"{name:>12}: Z = {z_load}, Γ = {gamma[0]:.3f}, VSWR = {vswr:.2f}")

    # Create comprehensive Smith chart plots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 16))

    # Main Smith chart with all impedances
    for name, net in networks.items():
        net.plot_s_smith(ax=ax1, label=name)
    ax1.set_title('Smith Chart - Various Load Impedances')
    ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # Return loss plot (exclude infinite cases)
    for name, net in networks.items():
        if name not in ['Short', 'Open']:  # Skip infinite return loss cases
            net.plot_s_db(ax=ax2, label=name)
    ax2.set_title('Return Loss vs Frequency')
    ax2.set_ylabel('|S11| (dB)')
    ax2.set_xlabel('Frequency (GHz)')
    ax2.grid(True)
    ax2.legend()

    # VSWR plot
    for name, net in networks.items():
        if name not in ['Short', 'Open']:
            # Calculate VSWR from S11
            s11_mag = np.abs(net.s[:,0,0])
            vswr = (1 + s11_mag) / (1 - s11_mag)
            vswr = np.clip(vswr, 1, 10)  # Clip for plotting
            ax3.plot(net.frequency.f/1e9, vswr, label=name)
    ax3.set_title('VSWR vs Frequency')
    ax3.set_ylabel('VSWR')
    ax3.set_xlabel('Frequency (GHz)')
    ax3.set_ylim(1, 5)
    ax3.grid(True)
    ax3.legend()

    # Smith chart coordinates demonstration
    test_impedances = [25+0j, 50+0j, 100+0j, 50+50j, 50-50j]
    smith_coords_r = []
    smith_coords_i = []
    labels = []

    for z in test_impedances:
        # Convert to reflection coefficient
        gamma = (z - z0) / (z + z0)
        smith_coords_r.append(gamma.real)
        smith_coords_i.append(gamma.imag)
        labels.append(f'{z}Ω')

    ax4.scatter(smith_coords_r, smith_coords_i, s=100, alpha=0.7)
    for i, label in enumerate(labels):
        ax4.annotate(label, (smith_coords_r[i], smith_coords_i[i]), 
                     xytext=(5, 5), textcoords='offset points')
    
    # Draw unit circle (Smith chart boundary)
    theta = np.linspace(0, 2*np.pi, 100)
    ax4.plot(np.cos(theta), np.sin(theta), 'k-', alpha=0.3)
    ax4.set_xlim(-1.2, 1.2)
    ax4.set_ylim(-1.2, 1.2)
    ax4.set_aspect('equal')
    ax4.grid(True)
    ax4.set_title('Smith Chart Coordinates (Γ plane)')
    ax4.set_xlabel('Real(Γ)')
    ax4.set_ylabel('Imag(Γ)')

    plt.tight_layout()
    plt.savefig('test_3_smith_chart.png', dpi=150, bbox_inches='tight')
    print("✓ Plot saved as 'test_3_smith_chart.png'")

    # Display Smith chart coordinate conversions
    print("\n=== Smith Chart Coordinates ===")
    for z in test_impedances:
        # Convert to normalized impedance
        z_norm = z / z0
        
        # Convert to Smith chart coordinates (real, imag of Γ)
        gamma = (z - z0) / (z + z0)
        smith_real = gamma.real
        smith_imag = gamma.imag
        
        print(f"Z = {z:>8} Ω → z_norm = {z_norm:.2f} → Γ = ({smith_real:+.3f}, {smith_imag:+.3f}j)")

    print("✓ Smith chart analysis completed\n")
    return True

if __name__ == "__main__":
    test_smith_chart()