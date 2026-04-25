#!/usr/bin/env python3
"""
Run All scikit-rf Tests
Executes all test scripts in sequence and provides summary.
"""

import sys
import traceback
from datetime import datetime

# Import all test modules
from test_1_basic import test_basic_sparameters
from test_2_transmission_line import test_transmission_line
from test_3_smith_chart import test_smith_chart
from test_4_cascading import test_cascading
from test_5_touchstone import test_touchstone_io

def run_all_tests():
    """Run all scikit-rf tests and provide summary"""
    print("=" * 60)
    print("scikit-rf → matplotlib Tool Chain Test Suite")
    print("=" * 60)
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Define all tests
    tests = [
        ("Test 1: Basic S-parameters", test_basic_sparameters),
        ("Test 2: Transmission Lines", test_transmission_line),
        ("Test 3: Smith Charts", test_smith_chart),
        ("Test 4: Cascading/De-embedding", test_cascading),
        ("Test 5: Touchstone I/O", test_touchstone_io),
    ]

    results = []
    
    # Run each test
    for test_name, test_func in tests:
        print(f"Running {test_name}...")
        try:
            success = test_func()
            if success:
                print(f"✓ {test_name} PASSED")
                results.append((test_name, "PASSED", None))
            else:
                print(f"✗ {test_name} FAILED")
                results.append((test_name, "FAILED", "Test returned False"))
        except Exception as e:
            print(f"✗ {test_name} ERROR: {str(e)}")
            results.append((test_name, "ERROR", str(e)))
            # Print traceback for debugging
            traceback.print_exc()
        
        print("-" * 40)

    # Print summary
    print()
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = 0
    failed = 0
    errors = 0
    
    for test_name, status, error in results:
        if status == "PASSED":
            print(f"✓ {test_name:<30} PASSED")
            passed += 1
        elif status == "FAILED":
            print(f"✗ {test_name:<30} FAILED")
            failed += 1
        else:  # ERROR
            print(f"⚠ {test_name:<30} ERROR")
            errors += 1
    
    print()
    print(f"Total tests: {len(tests)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Errors: {errors}")
    
    if passed == len(tests):
        print()
        print("🎉 ALL TESTS PASSED! scikit-rf → matplotlib tool chain verified!")
        print()
        print("Generated files:")
        print("  - test_1_basic_s_params.png")
        print("  - test_2_transmission_line.png") 
        print("  - test_3_smith_chart.png")
        print("  - test_4_cascading.png")
        print("  - test_5_touchstone.png")
        print("  - test_bandpass_filter.s2p")
        print("  - test_filter_s11.s1p")
        print("  - test_filter_mhz.s2p")
        print("  - test_filter_75ohm.s2p")
        return True
    else:
        print()
        print("❌ Some tests failed. Check errors above.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)