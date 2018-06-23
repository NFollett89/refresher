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

    # Tests while empty
    my_arraylist = a.NFArrayList()
    print "\nTesting NFArrayList() while empty"
    run_test("length()", "0", len(my_arraylist))
    run_test("contains(0)", "False", my_arraylist.contains(0))
    run_test("is_empty()", "True", my_arraylist.is_empty())
    run_test("clear(), length()", "0", len(my_arraylist))
    my_arraylist.add(1)
    run_test("add(1)", "[1]", my_arraylist)

    # Tests while not empty
    print "\nTesting NFArrayList() while NOT empty"
    my_arraylist.add(0, 0)
    run_test("add(0, 0)", "[0, 1]", my_arraylist)
    my_arraylist.add(2, 2)
    run_test("add(2, 2)", "[0, 1, 2]", my_arraylist)
    for i, arraylist_i in enumerate(my_arraylist):
        run_test("__iter__()", str(arraylist_i), str(i))    
    my_arraylist.add_all([3, 4, 5])
    run_test("add_all([3, 4, 5]", "[0, 1, 2, 3, 4, 5]", my_arraylist)
    run_test("contains(10)", "False", my_arraylist.contains(10))
    run_test("contains(2)", "True", my_arraylist.contains(2))
    run_test("get(2)", "2", my_arraylist.get(2))
    my_arraylist.set(3, 2)
    run_test("set(3, 2)", "[0, 1, 2, 2, 4, 5]", my_arraylist)
    my_arraylist.set(-6, 11)
    run_test("set(-6, 11)", "[11, 1, 2, 2, 4, 5]", my_arraylist)
    my_arraylist.add(10, 9)
    run_test("add(10)", "[11, 1, 2, 2, 4, 5, None, None, None, None, 10]", my_arraylist)
    my_arraylist.remove(0)
    run_test("remove(0)", "[1, 2, 2, 4, 5, None, None, None, None, 10]", my_arraylist)
    my_arraylist.remove(4)
    run_test("remove(4)", "[1, 2, 2, 4, None, None, None, None, 10]", my_arraylist)
    my_arraylist.remove(8)
    run_test("remove(8)", "[1, 2, 2, 4, None, None, None, None]", my_arraylist)
    run_test("index_of(2)", "1", my_arraylist.index_of(2))
    run_test("last_index(2)", "2", my_arraylist.last_index(2))
    run_test("index_of(9001)", "-1", my_arraylist.index_of(9001))
    run_test("lastindex(9001)", "-1", my_arraylist.last_index(9001))
    run_test("is_empty()", "False", my_arraylist.is_empty())
    my_arraylist.remove_all([None])
    run_test("remove_all([None])", "[1, 2, 2, 4]", my_arraylist)
    my_arraylist.retain_all([1, 2])
    run_test("retain_all([1, 2])", "[1, 2, 2]", my_arraylist)
    my_arraylist.remove_all([2, 'a'])
    run_test("remove_all([2, 'a'])", "[1]", my_arraylist)
    my_arraylist.clear()
    run_test("clear(), length()", "0", len(my_arraylist))

    # Test methods with exceptions
    print "\nTesting NFArrayList() methods with exceptions"
    my_arraylist_2 = a.NFArrayList()
    for i in xrange(10):
        my_arraylist_2.add(i)
    print "  New arraylist: %s" % my_arraylist_2
    try:
        run_test("get(20)", None, None)
        my_arraylist.get(20)
        print "\tFail | Check the integer in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    try:
        run_test("remove(20)", None, None)
        my_arraylist.remove(20)
        print "\tFail | Check the integer in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    try:
        run_test("remove_range(3, 1)", None, None)
        my_arraylist_tmp = my_arraylist_2.clone()
        my_arraylist_tmp.remove_range(3, 1)
        print "\tFail | Check integers in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    try:
        run_test("remove_range(-1, -3)", None, None)
        my_arraylist_tmp = my_arraylist_2.clone()
        my_arraylist_tmp.remove_range(-1, -3)
        print "\tFail | Check integers in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    try:
        run_test("remove_range(1, 1)", None, None)
        my_arraylist_tmp = my_arraylist_2.clone()
        my_arraylist_tmp.remove_range(1, 1)
        print "\tFail | Check integers in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    try:
        run_test("remove_range(9000, 9001)", None, None)
        my_arraylist_tmp = my_arraylist_2.clone()
        my_arraylist_tmp.remove_range(9000, 9001)
        print "\tFail | Check integers in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    try:
        run_test("remove_range(1, 9001)", None, None)
        my_arraylist_tmp = my_arraylist_2.clone()
        my_arraylist_tmp.remove_range(1, 9001)
        print "\tFail | Check integers in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    try:
        run_test("sub_list(3, 1)", None, None)
        my_arraylist_tmp = my_arraylist_2.clone()
        my_arraylist_tmp.sub_list(3, 1)
        print "\tFail | Check integers in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    try:
        run_test("sub_list(-1, -3)", None, None)
        my_arraylist_tmp = my_arraylist_2.clone()
        my_arraylist_tmp.sub_list(-1, -3)
        print "\tFail | Check integers in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    try:
        run_test("sub_list(1, 1)", None, None)
        my_arraylist_tmp = my_arraylist_2.clone()
        my_arraylist_tmp.sub_list(1, 1)
        print "\tFail | Check integers in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    try:
        run_test("sub_list(9000, 9001)", None, None)
        my_arraylist_tmp = my_arraylist_2.clone()
        my_arraylist_tmp.sub_list(9000, 9001)
        print "\tFail | Check integers in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    try:
        run_test("sub_list(1, 9001)", None, None)
        my_arraylist_tmp = my_arraylist_2.clone()
        my_arraylist_tmp.sub_list(1, 9001)
        print "\tFail | Check integers in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    try:
        run_test("set(9000, 1)", None, None)
        my_arraylist_tmp = my_arraylist_2.clone()
        my_arraylist_tmp.set(9000, 1)
        print "\tFail | Check integers in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    try:
        run_test("set(-11, -11)", None, None)
        my_arraylist_tmp = my_arraylist_2.clone()
        my_arraylist_tmp.set(-11, -11)
        print "\tFail | Check integers in the test"
        full_pass = False
    except IndexError as err:
        print "\tPass | Exception: %s" % err
    my_arraylist_tmp = my_arraylist_2.clone()
    my_arraylist_tmp.remove_range(3, 7)
    run_test("remove_range(3, 7)", "[0, 1, 2, 7, 8, 9]", my_arraylist_tmp)        
    my_arraylist_tmp = my_arraylist_2.clone()
    my_arraylist_tmp.remove_range(-3, -1)
    run_test("remove_range(-3, -1)", "[0, 1, 2, 3, 4, 5, 6, 9]", my_arraylist_tmp)        
    my_arraylist_tmp = my_arraylist_2.clone()
    my_arraylist_tmp.remove_range(0, -1)
    run_test("remove_range(0, -1)", "[9]", my_arraylist_tmp)        
    my_arraylist_tmp = my_arraylist_2.clone()
    my_arraylist_tmp.remove_range(0, my_arraylist_tmp.length())
    run_test("remove_range(0, length())", "[]", my_arraylist_tmp)        
    my_arraylist_tmp = my_arraylist_2.clone()
    run_test("sub_list(3, 7)", "[3, 4, 5, 6]", my_arraylist_tmp.sub_list(3, 7))        
    my_arraylist_tmp = my_arraylist_2.clone()
    run_test("sub_list(-3, -1)", "[7, 8]", my_arraylist_tmp.sub_list(-3, -1))        
    my_arraylist_tmp = my_arraylist_2.clone()
    run_test("sub_list(0, -1)", "[0, 1, 2, 3, 4, 5, 6, 7, 8]", my_arraylist_tmp.sub_list(0, -1))
    my_arraylist_tmp = my_arraylist_2.clone()
    run_test("sub_list(0, length())", "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]", my_arraylist_tmp.sub_list(0, my_arraylist_tmp.length()))

 
    print "\nFinal result: %s" % ("Pass" if full_pass else "Fail")

test()
