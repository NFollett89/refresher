#!/user/bin/env python2

import os
import hash_table as ht

control_data = {}
full_pass = True

def load_data():
    # Generate key:value pairs from the data file
    with open('data.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        key = line.split(':')[0]
        value = line.split(':')[1]
        yield key, value


def load_control():
    # Load test data into a dictionary for control comparisson
    global control_data
    for key, value in load_data():
        control_data[key] = value


def test_size(size):
    global full_pass
    global control_data

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
        for key, value in load_data():
            ht_1.set(key, value)
        print "   - Pass"
    except Exception as err:
        print "   - Fail | %s" % err
        full_pass = False

    # Test keys() for completion and uniqueness
    keys = ht_1.keys()
    for key in control_data.keys():
        if key not in keys:
            print "   - Missing key: %s" % key
            full_pass = False

    # Test values() for completion
    values = ht_1.values()
    for value in control_data.values():
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
        full_pass = False
    except Exception as err:
        print "   - Pass | %s" % err

    # Get utilization and waste
    print " - Utilization:"
    print "   - items:        %s" % len(ht_1)
    print "   - empty_spaces: %s" % ht_1.empty_spaces()
    print "   - collisions:   %s" % ht_1.collisions() 

    # Give new values to existing keys
    print " - Replace value of existing keys:"
    print "   - Setting ('18', 'EIGHTEEN')"
    print "   - Before: %s" % ht_1.get('18')
    ht_1.set('18', 'EIGHTEEN')
    set_result = ht_1.get('18')
    print "   - After:  %s" % set_result
    print "     - %s" % ("Pass" if set_result == "EIGHTEEN" else "Fail")
    full_pass = False if set_result != "EIGHTEEN" else full_pass

    # Delete keys
    print " - Deleting '18':"
    ht_1.delete('18')
    try:
        remove_result = ht_1.get('18')
        print "   - Fail | %s" % remove_result
    except KeyError as err:
        print "   - Pass | %s" % err
    print "   - New size: %s" % len(ht_1)
    print "     - %s" % ("Pass" if len(ht_1) == 19 else "Fail")
    full_pass = False if len(ht_1) != 19 else full_pass
    print " - Deleting remainder of keys:"
    for key in ht_1.keys():
        ht_1.delete(key)
    print "   - New size: %s" % len(ht_1)
    print "     - %s" % ("Pass" if len(ht_1) == 0 else "Fail")
    full_pass = False if len(ht_1) != 0  else full_pass
    print "   - Empty spaces: %s" % ht_1.empty_spaces()
    print "     - %s" % ("Pass" if len(ht_1) == 0 else "Fail")
    full_pass = False if ht_1.empty_spaces() != size else full_pass

    
load_data()
test_size(5)
test_size(20)
test_size(1000)

print "\nFinal summary: %s" % ("Pass" if full_pass else "Fail")

