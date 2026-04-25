#!/usr/bin/env python3
"""
Test 1: Basic S-parameter Creation and Plotting
Tests fundamental scikit-rf functionality for creating networks and basic plotting.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import scikit_rf as rf

def test_basic_sparameters():
    """Test basic S-parameter creation and plotting"""
    print("=== Test 1: Basic S-parameter Creation ===")
    print(f"scikit-rf version: {rf.__version__}")

    # Create frequency range
    freq = rf.Frequency(start=1, stop=10, npoints=101, unit='ghz')
    print(f"Frequency range: {freq.start/1e9:.1f} to {freq.stop/1e9:.1f} GHz, {freq.npoints} points")

    # Create simple networks - short and open circuits
    short = rf.Network(frequency=freq, s=np.zeros((101, 1, 1)), name='Short')
    short.s[:,0,0] = -1  # S11 = -1 for perfect short

    open_circuit = rf.Network(frequency=freq, s=np.ones((101, 1, 1)), name='Open')
    # S11 = +1 for perfect open

    print(f"Short circuit S11 at 5 GHz: {short.s[50,0,0]:.3f}")
    print(f"Open circuit S11 at 5 GHz:  {open_circuit.s[50,0,0]:.3f}")

    # Create matched load
    matched = rf.Network(frequency=freq, s=np.zeros((101, 1, 1)), name='Matched')
    # S11 = 0 for perfect match

    print(f"Matched load S11 at 5 GHz:  {matched.s[50,0,0]:.3f}")

    # Basic plotting
    plt.figure(figsize=(15, 5))

    # Magnitude plot
    plt.subplot(1,3,1)
    short.plot_s_db(label='Short')
    open_circuit.plot_s_db(label='Open') 
    matched.plot_s_db(label='Matched')
    plt.title('S11 Magnitude')
    plt.ylabel('|S11| (dB)')
    plt.legend()
    plt.grid(True)

    # Phase plot
    plt.subplot(1,3,2)
    short.plot_s_deg(label='Short')
    open_circuit.plot_s_deg(label='Open')
    matched.plot_s_deg(label='Matched')
    plt.title('S11 Phase')
    plt.ylabel('∠S11 (degrees)')
    plt.legend()
    plt.grid(True)

    # Smith chart
    plt.subplot(1,3,3)
    short.plot_s_smith(label='Short')
    open_circuit.plot_s_smith(label='Open')
    matched.plot_s_smith(label='Matched')
    plt.title('Smith Chart')
    plt.legend()

    plt.tight_layout()
    plt.savefig('test_1_basic_s_params.png', dpi=150, bbox_inches='tight')
    print("✓ Plot saved as 'test_1_basic_s_params.png'")

    print("✓ Basic S-parameter creation and plotting completed\n")
    return True

if __name__ == "__main__":
    test_basic_sparameters()