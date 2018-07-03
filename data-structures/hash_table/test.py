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

    # Test giving a non-integer size
    try:
        ht_1 = ht.NFHashTable(size)
        if not instanceof(size, int):
            print "  - Fail | %s" % ht_1
            full_pass = False
            return
    except TypeError as err:
        print "  - Pass | %s" % err
    except Exception as err:
        print "  - Fail | %s" % err
        full_pass = False
        return

    # Store test data in table with given size
    try:
        print "Storing data in table with size %s" % size
        # TODO
        print "  - Pass"
    except Exception as err:
        print "  - Fail | %s" % err
        full_pass = False

    # Test keys() for completion and uniqueness

    # Test values() for completion

    # Test iteration for correct length of items

    # Test clone

    
load_data()
test(5)
test(13)
