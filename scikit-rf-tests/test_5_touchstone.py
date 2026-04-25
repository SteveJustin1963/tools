#!/usr/bin/env python3
"""
Test 5: Touchstone File I/O
Tests reading and writing industry-standard Touchstone (.s1p, .s2p) files.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import scikit_rf as rf

def test_touchstone_io():
    """Test Touchstone file I/O capabilities"""
    print("=== Test 5: Touchstone File I/O ===")

    freq = rf.Frequency(start=1, stop=10, npoints=101, unit='ghz')

    # Create a test network - bandpass filter approximation
    # Simple LC ladder filter response
    center_freq = 5e9  # 5 GHz
    q_factor = 10

    s_data = np.zeros((len(freq), 2, 2), dtype=complex)

    for i, f in enumerate(freq.f):
        # Simple bandpass response: |H(jω)| = 1 / (1 + Q²((ω/ω₀) - (ω₀/ω))²)
        x = q_factor * ((f/center_freq) - (center_freq/f))
        magnitude = 1 / np.sqrt(1 + x**2)
        phase = -np.arctan(x)
        
        s21 = magnitude * np.exp(1j * phase)
        s12 = s21  # Reciprocal network
        s11 = s22 = 0.1 * np.exp(1j * phase/2)  # Small reflection
        
        s_data[i, 0, 0] = s11
        s_data[i, 0, 1] = s21
        s_data[i, 1, 0] = s12  
        s_data[i, 1, 1] = s22

    filter_net = rf.Network(frequency=freq, s=s_data, name='BPF_5GHz', z0=50)

    print("Created bandpass filter network:")
    print(f"  Center frequency: {center_freq/1e9} GHz")
    print(f"  S21 @ 5 GHz: {filter_net.s_db[50,1,0]:.2f} dB")
    print(f"  S21 @ 1 GHz: {filter_net.s_db[0,1,0]:.2f} dB")  
    print(f"  S21 @ 10 GHz: {filter_net.s_db[100,1,0]:.2f} dB")

    # Save as Touchstone files
    print("\n=== Saving Touchstone Files ===")

    # Save as .s2p (2-port S-parameter file)
    s2p_filename = 'test_bandpass_filter.s2p'
    filter_net.write_touchstone(s2p_filename)
    print(f"✓ Saved 2-port network as: {s2p_filename}")

    # Save as .s1p for S11 only (input reflection)
    s11_net = filter_net.s11
    s1p_filename = 'test_filter_s11.s1p'  
    s11_net.write_touchstone(s1p_filename)
    print(f"✓ Saved S11 data as: {s1p_filename}")

    # Read back the files to verify
    print("\n=== Reading Touchstone Files ===")

    # Read back the .s2p file
    loaded_s2p = rf.Network(s2p_filename)
    print(f"Loaded .s2p file: {loaded_s2p.name}")
    print(f"  Frequency range: {loaded_s2p.frequency.start/1e9:.1f} - {loaded_s2p.frequency.stop/1e9:.1f} GHz")
    print(f"  Number of ports: {loaded_s2p.number_of_ports}")
    print(f"  S21 @ 5 GHz: {loaded_s2p.s_db[50,1,0]:.2f} dB")

    # Read back the .s1p file
    loaded_s1p = rf.Network(s1p_filename)
    print(f"Loaded .s1p file: {loaded_s1p.name}")  
    print(f"  Number of ports: {loaded_s1p.number_of_ports}")
    print(f"  S11 @ 5 GHz: {loaded_s1p.s_db[50,0,0]:.2f} dB")

    # Verify data integrity
    s21_diff = abs(filter_net.s[50,1,0] - loaded_s2p.s[50,1,0])
    s11_diff = abs(filter_net.s[50,0,0] - loaded_s1p.s[50,0,0])

    print(f"\n=== Data Integrity Check ===")
    print(f"S21 difference (original vs loaded): {s21_diff:.2e}")
    print(f"S11 difference (original vs loaded): {s11_diff:.2e}")

    if s21_diff < 1e-6 and s11_diff < 1e-6:
        print("✓ File I/O integrity verified - differences within numerical precision")
        integrity_ok = True
    else:
        print("⚠ Significant differences detected in file I/O")
        integrity_ok = False

    # Create comprehensive plots
    plt.figure(figsize=(16, 12))

    # Original filter response
    plt.subplot(2,3,1)
    filter_net.plot_s_db(m=1, n=0, label='S21 (original)')
    filter_net.plot_s_db(m=0, n=0, label='S11 (original)')
    plt.title('Original Filter Response')
    plt.ylabel('Magnitude (dB)')
    plt.legend()
    plt.grid(True)

    # Loaded filter response comparison
    plt.subplot(2,3,2)
    filter_net.plot_s_db(m=1, n=0, label='Original S21')
    loaded_s2p.plot_s_db(m=1, n=0, label='Loaded S21', linestyle='--')
    plt.title('File I/O Verification - S21')
    plt.ylabel('Magnitude (dB)')
    plt.legend()
    plt.grid(True)

    # S11 comparison
    plt.subplot(2,3,3)
    filter_net.plot_s_db(m=0, n=0, label='Original S11')
    loaded_s1p.plot_s_db(m=0, n=0, label='Loaded S11', linestyle='--')
    plt.title('File I/O Verification - S11')
    plt.ylabel('Magnitude (dB)')
    plt.legend()
    plt.grid(True)

    # Phase response
    plt.subplot(2,3,4)
    filter_net.plot_s_deg(m=1, n=0, label='S21 phase')
    filter_net.plot_s_deg(m=0, n=0, label='S11 phase')
    plt.title('Phase Response')
    plt.ylabel('Phase (degrees)')
    plt.legend()
    plt.grid(True)

    # Smith chart
    plt.subplot(2,3,5)
    filter_net.plot_s_smith(m=0, n=0, label='S11')
    filter_net.plot_s_smith(m=1, n=1, label='S22')
    plt.title('Smith Chart (Input/Output)')
    plt.legend()

    # Group delay
    plt.subplot(2,3,6)
    # Calculate group delay from phase
    freq_hz = filter_net.frequency.f
    s21_phase = np.unwrap(np.angle(filter_net.s[:, 1, 0]))
    group_delay = -np.gradient(s21_phase, freq_hz) / (2 * np.pi)
    
    plt.plot(freq_hz/1e9, group_delay*1e9, label='Group Delay')
    plt.title('Group Delay')
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('Group Delay (ns)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('test_5_touchstone.png', dpi=150, bbox_inches='tight')
    print("✓ Plot saved as 'test_5_touchstone.png'")

    # Display file contents preview
    print(f"\n=== Touchstone File Format Preview ===")
    print("First few lines of .s2p file:")
    try:
        with open(s2p_filename, 'r') as f:
            lines = f.readlines()[:10]  
            for i, line in enumerate(lines):
                print(f"{i+1:2d}: {line.rstrip()}")
    except Exception as e:
        print(f"Error reading file: {e}")

    print("\n=== Advanced Touchstone Features ===")
    
    # Test different frequency units and formats
    print("Testing different frequency units:")
    
    # Save in MHz
    filter_net_mhz = filter_net.copy()
    filter_net_mhz.frequency.unit = 'mhz'
    mhz_filename = 'test_filter_mhz.s2p'
    filter_net_mhz.write_touchstone(mhz_filename)
    
    # Read back and verify
    loaded_mhz = rf.Network(mhz_filename)
    print(f"MHz file: {loaded_mhz.frequency.start/1e6:.0f}-{loaded_mhz.frequency.stop/1e6:.0f} MHz")
    
    # Test with different impedance
    filter_75ohm = filter_net.copy()
    filter_75ohm.z0 = 75
    ohm75_filename = 'test_filter_75ohm.s2p'
    filter_75ohm.write_touchstone(ohm75_filename)
    
    loaded_75ohm = rf.Network(ohm75_filename)
    print(f"75Ω file: Z0 = {loaded_75ohm.z0[0]:.0f} Ω")

    print("✓ Touchstone file I/O testing completed\n")
    return integrity_ok

if __name__ == "__main__":
    test_touchstone_io()