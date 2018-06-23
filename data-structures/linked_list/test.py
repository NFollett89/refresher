#!/usr/bin/env python2

import singly_linked_list as sll

full_pass = True

def run_test(call, expected, actual):
    global full_pass
    if expected:
        result = "Pass" if str(expected) == str(actual) else "Fail"
        if result == "Fail":
            full_pass = False
        print "  - %s | %s : %s vs. %s" % (result, call, actual, expected)
    else:
        print "  - %s : %s" % (call, actual)

def test():
    global full_pass

    # Tests for NFSinglyLinkedList()
    print "\nTesting NFSinglyLinkedList()"
    print "- Length while empty:"
    sll_1 = sll.NFSinglyLinkedList()
    run_test("length()", "0", sll_1.length())

    print"\n- Additions while empty:"
    sll_1.push(1)
    run_test("push(1)", "[1]", sll_1)
    sll_1 = sll.NFSinglyLinkedList()
    sll_1.append(1)
    run_test("append(1)", "[1]", sll_1)
    sll_1 = sll.NFSinglyLinkedList()
    sll_1.insert(0, 1)
    run_test("insert(0, 1)", "[1]", sll_1)
    sll_1 = sll.NFSinglyLinkedList()
    sll_1.insert(9001, 1)
    run_test("insert(9001, 1)", "[1]", sll_1)

    print "\n- Additions while not empty:"
    sll_1.push(0)
    run_test("push(0)", "[0, 1]", sll_1)
    sll_1.append(3)
    run_test("append(3)", "[0, 1, 3]", sll_1)
    sll_1.insert(2, 2)
    run_test("insert(2, 2)", "[0, 1, 2, 3]", sll_1)
    sll_1.insert(9001, 4)
    run_test("insert(9001, 5)", "[0, 1, 2, 3, 4]", sll_1)

    print "\n- Getters while not empty:"
    run_test("len(sll_1)", "5", len(sll_1))
    run_test("length()", "5", sll_1.length())
    run_test("get_head().get_data()", "0", sll_1.get_head().get_data())
    run_test("get_tail().get_data()", "4", sll_1.get_tail().get_data())
    run_test("get_index(2).get_data()", "2", sll_1.get_index(2).get_data())
    try:
        run_test("get_index(9001).get_data()", None, None)
        sll_1.get_index(9001).get_data()
        print "\tFail | Check index integer"
        full_pass = False
    except Exception as err:
        print "\t%s" % err
    
    print "\n- Remove nodes:"
    sll_1.delete_head()
    run_test("delete_head()", "[1, 2, 3, 4]", sll_1)
    sll_1.delete_tail()
    run_test("delete_tail()", "[1, 2, 3]", sll_1)
    sll_1.delete_index(1)
    run_test("delete_index(1)", "[1, 3]", sll_1)
    sll_1.delete_index(1)
    run_test("delete_index(1)", "[1]", sll_1)
    sll_1.delete_index(0)
    run_test("delete_index(0)", "[]", sll_1)
    run_test("length()", "0", sll_1.length())

    print "\nFinal result: %s" % ("Pass" if full_pass else "Fail")

test()
