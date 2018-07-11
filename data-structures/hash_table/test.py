#!/user/bin/env python2

import os
import hash_table as ht

test_data = {}
full_pass = True

def run_test(call, expected, actual):
    global full_pass
    if str(expected):
        result = "Pass" if str(expected) == str(actual) else "Fail"
        if result == "Fail":
            full_pass = False
            print "  - %s | %s : %s should be %s" % (result, call, actual, expected)
        else:
            print "  - %s | %s : %s == %s" % (result, call, actual, expected)
    else:
        print "  - %s : %s" % (call, actual)


def load_data():
    # Load test data into a dictionary for comparisson
    global test_data
    with open('data.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        key = line.split(':')[0]
        value = line.split(':')[1]
        test_data[key] = value


def test_size(size):
    global full_pass
    global test_data

    print "\nTesting NFHashTable(%s)" % size
    # Test giving a non-integer size
    try:
        print " - Testing __init__()"
        ht_1 = ht.NFHashTable(size)
        if not isinstance(size, int):
            print "   - Fail | %s" % ht_1
            full_pass = False
            return
        else:
            print "   - Pass"
    except TypeError as err:
        print "    Pass | %s" % err
    except Exception as err:
        print "    Fail | %s" % err
        full_pass = False
        return

    # Store test data in table with given size
    try:
        print " - Storing data in table with size %s" % size
        for key, value in test_data.items():
            ht_1.set(key, value)
        print "   - Pass"
    except Exception as err:
        print "   - Fail | %s" % err
        full_pass = False

    # Test keys() for completion and uniqueness
    keys = ht_1.keys()
    for key in test_data.keys():
        if key not in keys:
            print "   - Missing key: %s" % key
            full_pass = False

    # Test values() for completion
    values = ht_1.values()
    for value in test_data.values():
        if value not in values:
            print "   - Missing value: %s" % value
            full_pass = False 

    # Test iteration
    print " - Testing iteration:"
    try:
        for key, value in ht_1:
            continue
        print "   - Pass"
    except Exception as err:
        print "   - Fail: %s" % err
        full_pass = False

    # Test some valid/invalid keys
    print " - Testing invalid key:"
    try:
        ht_1.get(9001)
        print "   - Fail"
    except Exception as err:
        print "   - Pass | %s" % err

    # Get utilization and waste
    print " - Utilization:"
    print "   - items:        %s" % len(ht_1)
    print "   - empty_spaces: %s" % ht_1.empty_spaces()
    print "   - collisions:   %s" % ht_1.collisions() 

    # Give new values to existing keys

    # Remove keys
    # TODO
    
load_data()
test_size(5)
#test_size(20)
#test_size(40)

print "\nFinal summary: %s" % ("Pass" if full_pass else "Fail")

