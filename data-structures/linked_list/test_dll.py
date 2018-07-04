#!/usr/bin/env python2

import doubly_linked_list as dll

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

    # Tests for NFDoublyLinkedList()
    dll_1 = dll.NFDoublyLinkedList()
    print "\nTesting NFDoublyLinkedList()"
    print "- Length while empty %s:" % dll_1
    run_test("length()", "0", dll_1.length())
    try:
        run_test("index(0)", None, None)
        dll_1.index(0)
        print "\tFail | Check index integer"
        full_pass = False
    except Exception as err:
        print "\t%s" % err

    print "\n- Additions while empty %s:" % dll_1
    dll_1.push(1)
    run_test("push(1)", "[1]", dll_1)
    dll_1 = dll.NFDoublyLinkedList()
    dll_1.append(1)
    run_test("append(1)", "[1]", dll_1)
    dll_1 = dll.NFDoublyLinkedList()
    try:
        run_test("insert(1, 1)", None, None)
        dll_1.insert(1, 1)
        print "\tFail | Check index integer"
        full_pass = False
    except Exception as err:
        print "\t%s" % err
    dll_1 = dll.NFDoublyLinkedList()
    dll_1.insert(1, 0)
    run_test("insert(1, 0)", "[1]", dll_1)

    print "\n- Additions while not empty %s:" % dll_1
    dll_1.push(0)
    run_test("push(0)", "[0, 1]", dll_1)
    dll_1.append(3)
    run_test("append(3)", "[0, 1, 3]", dll_1)
    dll_1.insert(2, 2)
    run_test("insert(2, 2)", "[0, 1, 2, 3]", dll_1)
    dll_1.insert(-1, 0)
    run_test("insert(-1, 0)", "[-1, 0, 1, 2, 3]", dll_1)
    dll_1.insert(4, 5)
    run_test("insert(4, 5)", "[-1, 0, 1, 2, 3, 4]", dll_1)
    try:
        run_test("insert(5, 7)", None, None)
        dll_1.insert(6, 7)
        print "\tFail | Check index integer! %s" % dll_1
        full_pass = False
    except Exception as err:
        print "\t%s" % err

    print "\n- Getters while not empty %s:" % dll_1
    run_test("len(dll_1)", "6", len(dll_1))
    run_test("length()", "6", dll_1.length())
    run_test("head.data", "-1", dll_1.head.data)
    run_test("tail.data", "4", dll_1.tail.data)
    run_test("index(0).data", "-1", dll_1.index(0).data)
    run_test("index(3).data", "2", dll_1.index(3).data)
    run_test("index(5).data", "4", dll_1.index(5).data)
    try:
        run_test("index(6).data", None, None)
        dll_1.index(6).data
        print "\tFail | Check index integer"
        full_pass = False
    except Exception as err:
        print "\t%s" % err

    dll_1 = dll.NFDoublyLinkedList()
    for i in xrange(10):
        dll_1.append(i)

    print "\n- Test iteration of new list %s:" % dll_1
    for i, dll_i in enumerate(dll_1):
        run_test("iter()", i, dll_i.data)

    print "\n- Test reverse iteration of list %s:" % dll_1
    for i, dll_i in enumerate(dll_1.reverse_iter()):
        rev_i = (i * -1) - 1
        run_test("iter()", rev_i, dll_i.data)

    print "\n- Remove nodes from list %s:" % dll_1
    dll_1.delete_head()
    run_test("delete_head()", "[1, 2, 3, 4, 5, 6, 7, 8, 9]", dll_1)
    dll_1.delete_tail()
    run_test("delete_tail()", "[1, 2, 3, 4, 5, 6, 7, 8]", dll_1)
    dll_1.delete(0)
    run_test("delete(0)", "[2, 3, 4, 5, 6, 7, 8]", dll_1)
    dll_1.delete(1)
    run_test("delete(1)", "[2, 4, 5, 6, 7, 8]", dll_1)
    dll_1.delete(5)
    run_test("delete(5)", "[2, 4, 5, 6, 7]", dll_1)
    run_test("length()", "5", dll_1.length())

    print "\nFinal result: %s" % ("Pass" if full_pass else "Fail")

test()
