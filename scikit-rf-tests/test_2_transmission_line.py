#!/usr/bin/env python3
"""
Test 2: Transmission Line Analysis
Tests transmission line modeling with phase and loss analysis.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import scikit_rf as rf

def test_transmission_line():
    """Test transmission line network analysis"""
    print("=== Test 2: Transmission Line Analysis ===")

    # Create frequency range
    freq = rf.Frequency(start=1, stop=10, npoints=101, unit='ghz')

    # Create a 50-ohm coaxial transmission line media
    coax_50 = rf.media.Coaxial(frequency=freq, z0=50)
    print(f"50Ω coax media created: {coax_50}")

    # Create lines of different lengths
    lengths = [0.05, 0.1, 0.2, 0.5]  # 5cm, 10cm, 20cm, 50cm
    lines = {}

    print("\nTransmission line analysis:")
    for length in lengths:
        line = coax_50.line(d=length, unit='m', name=f'{length*100:.0f}cm')
        lines[length] = line
        
        # Analyze at different frequencies
        loss_1ghz = line.s_db[0,1,0]
        loss_5ghz = line.s_db[50,1,0] 
        loss_10ghz = line.s_db[100,1,0]
        
        print(f"{length*100:2.0f}cm: S21 = {loss_1ghz:.2f}/{loss_5ghz:.2f}/{loss_10ghz:.2f} dB @ 1/5/10 GHz")

    # Detailed phase analysis for 10cm line
    line_10cm = lines[0.1]
    phase_1ghz = np.angle(line_10cm.s[0,1,0], deg=True)
    phase_5ghz = np.angle(line_10cm.s[50,1,0], deg=True) 
    phase_10ghz = np.angle(line_10cm.s[100,1,0], deg=True)
    
    print(f"\n10cm line phase analysis:")
    print(f"Phase shift: {phase_1ghz:.1f}°/{phase_5ghz:.1f}°/{phase_10ghz:.1f}° @ 1/5/10 GHz")

    # Calculate electrical length
    elec_length_5ghz = abs(phase_5ghz) / 360  # in wavelengths
    print(f"Electrical length at 5 GHz: {elec_length_5ghz:.3f} λ")

    # Plot transmission line characteristics
    plt.figure(figsize=(15, 10))

    # S21 magnitude vs frequency for different lengths
    plt.subplot(2,2,1)
    for length, line in lines.items():
        line.plot_s_db(m=1, n=0, label=f'{length*100:.0f}cm')
    plt.title('S21 Magnitude vs Frequency')
    plt.ylabel('|S21| (dB)')
    plt.legend()
    plt.grid(True)

    # S21 phase vs frequency
    plt.subplot(2,2,2)
    for length, line in lines.items():
        line.plot_s_deg(m=1, n=0, label=f'{length*100:.0f}cm')
    plt.title('S21 Phase vs Frequency')
    plt.ylabel('∠S21 (degrees)')
    plt.legend()
    plt.grid(True)

    # S11 (input reflection) vs frequency
    plt.subplot(2,2,3)
    for length, line in lines.items():
        line.plot_s_db(m=0, n=0, label=f'{length*100:.0f}cm')
    plt.title('S11 (Input Reflection)')
    plt.ylabel('|S11| (dB)')
    plt.legend()
    plt.grid(True)

    # Smith chart showing input impedance
    plt.subplot(2,2,4)
    for length, line in lines.items():
        line.plot_s_smith(m=0, n=0, label=f'{length*100:.0f}cm')
    plt.title('Input Impedance (Smith Chart)')
    plt.legend()

    plt.tight_layout()
    plt.savefig('test_2_transmission_line.png', dpi=150, bbox_inches='tight')
    print("✓ Plot saved as 'test_2_transmission_line.png'")

    print("✓ Transmission line network analysis completed\n")
    return True

if __name__ == "__main__":
    test_transmission_line()