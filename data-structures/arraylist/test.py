#!/usr/bin/env python2

import arraylist as a

full_pass = True

def run_test(call, expected, actual):
    global full_pass
    if expected:
        result = "Pass" if str(expected) == str(actual) else "Fail" 
        if result == "Pass":
            print "  - %s | %s : %s == %s" % (result, call, actual, expected)
        else:
            print "  - %s | %s : %s should be %s" % (result, call, actual, expected)
            full_pass = False
    else:
        print "  - %s : %s" % (call, actual)

def test():
    global full_pass

    # Tests for NFSinglyLinkedList()
    my_arraylist = a.NFArrayList()
    print "\nTesting NFQueue()"
    run_test("length()", "0", len(my_arraylist))
    run_test("contains(0)", "False", my_arraylist.contains(0))
    run_test("is_empty()", "True", my_arraylist.is_empty())

    my_arraylist.add(1)
    run_test("add(1)", "[1]", my_arraylist)
    my_arraylist.add(0, 0)
    run_test("add(0, 0)", "[0, 1]", my_arraylist)
    my_arraylist.add(2, 2)
    run_test("add(2, 2)", "[0, 1, 2]", my_arraylist)
    for i, arraylist_i in enumerate(my_arraylist):
        run_test("__iter__()", str(arraylist_i), str(i))    
    my_arraylist.add_all([2, 4, 5])
    run_test("add_all([2, 4, 5]", "[0, 1, 2, 2, 4, 5]", my_arraylist)
    run_test("contains(10)", "False", my_arraylist.contains(10))
    run_test("contains(2)", "True", my_arraylist.contains(2))
    run_test("get(2)", "2", my_arraylist.get(2))
    try:
        run_test("get(6)", None, None)
        my_arraylist.get(6)
        print "\tFail | Check the integer in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | %s" % err
    my_arraylist.add(10, 9)
    run_test("add(10)", "[0, 1, 2, 2, 4, 5, None, None, None, None, 10]", my_arraylist)
    run_test("index_of(2)", "2", my_arraylist.index_of(2))
    run_test("last_index(2)", "3", my_arraylist.last_index(2))
    run_test("index_of(9001)", "-1", my_arraylist.index_of(9001))
    run_test("is_empty()", "False", my_arraylist.is_empty())

    my_arraylist.clear()
    run_test("clear()", "0", len(my_arraylist))
 
    print "\nFinal result: %s" % ("Pass" if full_pass else "Fail")

test()
