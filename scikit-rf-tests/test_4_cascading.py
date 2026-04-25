#!/usr/bin/env python3
"""
Test 4: Network Cascading and De-embedding
Tests network cascading using ** operator and de-embedding using .inv method.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import scikit_rf as rf

def test_cascading():
    """Test network cascading and de-embedding"""
    print("=== Test 4: Network Cascading and De-embedding ===")

    freq = rf.Frequency(start=1, stop=5, npoints=101, unit='ghz')
    coax_50 = rf.media.Coaxial(frequency=freq, z0=50)

    # Create component networks
    cable1 = coax_50.line(d=0.05, unit='m', name='5cm_cable')  # 5cm cable
    cable2 = coax_50.line(d=0.1, unit='m', name='10cm_cable')   # 10cm cable

    # Create 3dB attenuator manually
    s_atten = np.zeros((len(freq), 2, 2), dtype=complex)
    # 3dB = 10^(-3/20) ≈ 0.708
    s21 = s12 = 10**(-3/20)  # -3dB insertion loss
    s11 = s22 = 0  # Matched attenuator

    s_atten[:, 0, 0] = s11
    s_atten[:, 0, 1] = s21  
    s_atten[:, 1, 0] = s12
    s_atten[:, 1, 1] = s22

    attenuator = rf.Network(frequency=freq, s=s_atten, name='3dB_attenuator', z0=50)

    print("Individual components:")
    print(f"Cable1 (5cm):  S21 @ 3GHz = {cable1.s_db[50,1,0]:.2f} dB")
    print(f"Cable2 (10cm): S21 @ 3GHz = {cable2.s_db[50,1,0]:.2f} dB") 
    print(f"Attenuator:    S21 @ 3GHz = {attenuator.s_db[50,1,0]:.2f} dB")

    # Cascade networks: Cable1 ** Attenuator ** Cable2
    cascaded = cable1 ** attenuator ** cable2
    cascaded.name = 'Cascaded_System'

    print(f"\nCascaded system S21 @ 3GHz = {cascaded.s_db[50,1,0]:.2f} dB")

    # Verify cascade is approximately sum of individual losses
    total_loss = cable1.s_db[50,1,0] + attenuator.s_db[50,1,0] + cable2.s_db[50,1,0]
    print(f"Sum of individual losses:    {total_loss:.2f} dB")
    print(f"Cascade calculation:         {cascaded.s_db[50,1,0]:.2f} dB")

    # De-embedding test: Remove cable1 from cascaded measurement
    deembedded = cable1.inv ** cascaded
    deembedded.name = 'Deembedded_AttenuatorAndCable2'

    # Compare with known result
    known_result = attenuator ** cable2

    print(f"\nDe-embedding test:")
    print(f"Known (Attenuator + Cable2): S21 @ 3GHz = {known_result.s_db[50,1,0]:.2f} dB")
    print(f"De-embedded result:          S21 @ 3GHz = {deembedded.s_db[50,1,0]:.2f} dB")
    error = abs(known_result.s_db[50,1,0] - deembedded.s_db[50,1,0])
    print(f"De-embedding error:          {error:.4f} dB")

    # Create visualization
    plt.figure(figsize=(16, 12))

    # S21 magnitude comparison
    plt.subplot(2,3,1)
    cable1.plot_s_db(m=1, n=0, label='Cable1 (5cm)')
    attenuator.plot_s_db(m=1, n=0, label='Attenuator (3dB)')
    cable2.plot_s_db(m=1, n=0, label='Cable2 (10cm)')
    cascaded.plot_s_db(m=1, n=0, label='Cascaded', linewidth=2)
    plt.title('S21 Magnitude - Individual vs Cascaded')
    plt.ylabel('|S21| (dB)')
    plt.legend()
    plt.grid(True)

    # S21 phase
    plt.subplot(2,3,2)
    cable1.plot_s_deg(m=1, n=0, label='Cable1')
    attenuator.plot_s_deg(m=1, n=0, label='Attenuator')
    cable2.plot_s_deg(m=1, n=0, label='Cable2')
    cascaded.plot_s_deg(m=1, n=0, label='Cascaded', linewidth=2)
    plt.title('S21 Phase')
    plt.ylabel('∠S21 (degrees)')
    plt.legend()
    plt.grid(True)

    # De-embedding verification
    plt.subplot(2,3,3)
    known_result.plot_s_db(m=1, n=0, label='Known (Att+Cable2)')
    deembedded.plot_s_db(m=1, n=0, label='De-embedded', linestyle='--', linewidth=2)
    plt.title('De-embedding Verification')
    plt.ylabel('|S21| (dB)')
    plt.legend()
    plt.grid(True)

    # S11 (input reflection) cascaded system
    plt.subplot(2,3,4)
    cascaded.plot_s_db(m=0, n=0, label='Cascaded S11')
    plt.title('Cascaded System Input Reflection')
    plt.ylabel('|S11| (dB)')
    plt.legend()
    plt.grid(True)

    # Smith chart showing input impedance transformation
    plt.subplot(2,3,5)
    cable1.plot_s_smith(m=0, n=0, label='Cable1 input')
    cascaded.plot_s_smith(m=0, n=0, label='Cascaded input')
    plt.title('Input Impedance Transformation')
    plt.legend()

    # Network parameter conversion demonstration
    plt.subplot(2,3,6)
    test_net = attenuator
    
    # Plot different parameter representations
    freq_ghz = test_net.frequency.f / 1e9
    s21_mag = np.abs(test_net.s[:, 1, 0])
    z21_mag = np.abs(test_net.z[:, 1, 0])
    y21_mag = np.abs(test_net.y[:, 1, 0])
    
    plt.plot(freq_ghz, 20*np.log10(s21_mag), label='|S21| (dB)')
    plt.plot(freq_ghz, 20*np.log10(z21_mag/50), label='|Z21|/50 (dB)')  # Normalize
    plt.plot(freq_ghz, 20*np.log10(y21_mag*50), label='|Y21|*50 (dB)')  # Normalize
    plt.title('Parameter Representations')
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('Magnitude (dB)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('test_4_cascading.png', dpi=150, bbox_inches='tight')
    print("✓ Plot saved as 'test_4_cascading.png'")

    # Test network conversions
    print(f"\n=== Parameter Conversions ===")
    test_net = attenuator

    print(f"S-parameters @ 3GHz: S11 = {test_net.s[50,0,0]:.4f}, S21 = {test_net.s[50,1,0]:.4f}")

    # Convert to different representations
    z_params = test_net.z[50]  # Z-parameters at 3GHz  
    y_params = test_net.y[50]  # Y-parameters at 3GHz

    print(f"Z-parameters: Z11 = {z_params[0,0]:.2f} Ω, Z21 = {z_params[1,0]:.2f} Ω")
    print(f"Y-parameters: Y11 = {y_params[0,0]*1000:.2f} mS, Y21 = {y_params[1,0]*1000:.2f} mS")

    # Mismatch example
    print(f"\n=== Mismatch Analysis ===")
    # 50Ω to 75Ω impedance step
    gamma_step = (75 - 50) / (75 + 50)
    vswr_step = (1 + abs(gamma_step)) / (1 - abs(gamma_step))
    return_loss_db = -20 * np.log10(abs(gamma_step))

    print(f"50Ω to 75Ω step:")
    print(f"  Reflection coefficient: Γ = {gamma_step:.3f}")  
    print(f"  VSWR = {vswr_step:.2f}")
    print(f"  Return loss = {return_loss_db:.1f} dB")

    print("✓ Network cascading and de-embedding completed\n")
    return True

if __name__ == "__main__":
    test_cascading()