#!/usr/bin/env python2

import singly_linked_list as sll

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

def test():
    global full_pass

    # Tests for NFSinglyLinkedList()
    sll_1 = sll.NFSinglyLinkedList()
    print "\nTesting NFSinglyLinkedList()"
    print "- Length while empty %s:" % sll_1
    run_test("length()", "0", sll_1.length())
    try:
        run_test("index(0)", None, None)
        sll_1.index(1)
        print "\tFail | Check index integer"
        full_pass = False
    except Exception as err:
        print "\t%s" % err

    print"\n- Additions while empty %s:" % sll_1
    sll_1.push(1)
    run_test("push(1)", "[1]", sll_1)
    sll_1 = sll.NFSinglyLinkedList()
    sll_1.append(1)
    run_test("append(1)", "[1]", sll_1)
    sll_1 = sll.NFSinglyLinkedList()
    try:
        run_test("insert(1, 1)", None, None)
        sll_1.insert(1, 1)
        print "\tFail | Check index integer"
        full_pass = False
    except Exception as err:
        print "\t%s" % err
    sll_1 = sll.NFSinglyLinkedList()
    sll_1.insert(1, 0)
    run_test("insert(1, 0)", "[1]", sll_1)

    print "\n- Additions while not empty %s:" % sll_1
    sll_1.push(0)
    run_test("push(0)", "[0, 1]", sll_1)
    sll_1.append(3)
    run_test("append(3)", "[0, 1, 3]", sll_1)
    sll_1.insert(2, 2)
    run_test("insert(2, 2)", "[0, 1, 2, 3]", sll_1)
    sll_1.insert(-1, 0)
    run_test("insert(-1, 0)", "[-1, 0, 1, 2, 3]", sll_1)
    sll_1.insert(4, 5)
    run_test("insert(4, 5)", "[-1, 0, 1, 2, 3, 4]", sll_1)
    try:
        run_test("insert(5, 7)", None, None)
        sll_1.insert(6, 7)
        print "\tFail | Check index integer! %s" % sll_1
        full_pass = False
    except Exception as err:
        print "\t%s" % err

    print "\n- Getters while not empty %s:" % sll_1
    run_test("len(sll_1)", "6", len(sll_1))
    run_test("length()", "6", sll_1.length())
    run_test("head.data", "-1", sll_1.head.data)
    run_test("get_tail().data", "4", sll_1.get_tail().data)
    run_test("index(0).data", "-1", sll_1.index(0).data)
    run_test("index(3).data", "2", sll_1.index(3).data)
    run_test("index(5).data", "4", sll_1.index(5).data)
    try:
        run_test("index(6).data", None, None)
        sll_1.index(6).data
        print "\tFail | Check index integer"
        full_pass = False
    except Exception as err:
        print "\t%s" % err

    sll_1 = sll.NFSinglyLinkedList()
    for i in xrange(10):
        sll_1.append(i)

    print "\n- Test iteration on new list %s" % sll_1
    for i, sll_i in enumerate(sll_1):
        run_test("iter()", i, sll_i.data)

    print "\n- Remove nodes from list %s:" % sll_1
    sll_1.delete_head()
    run_test("delete_head()", "[1, 2, 3, 4, 5, 6, 7, 8, 9]", sll_1)
    sll_1.delete_tail()
    run_test("delete_tail()", "[1, 2, 3, 4, 5, 6, 7, 8]", sll_1)
    sll_1.delete(0)
    run_test("delete(0)", "[2, 3, 4, 5, 6, 7, 8]", sll_1)
    sll_1.delete(1)
    run_test("delete(1)", "[2, 4, 5, 6, 7, 8]", sll_1)
    sll_1.delete(5)
    run_test("delete(5)", "[2, 4, 5, 6, 7]", sll_1)
    run_test("length()", "5", sll_1.length())

    print "\nFinal result: %s" % ("Pass" if full_pass else "Fail")

test()
