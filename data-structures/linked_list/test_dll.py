#!/usr/bin/env python2

import doubly_linked_list as dll

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

    # Tests for NFDoublyLinkedList()
    print "\nTesting NFDoublyLinkedList()"
    print "- Length while empty:"
    dll_1 = dll.NFDoublyLinkedList()
    run_test("length()", "0", dll_1.length())

    print"\n- Additions while empty:"
    dll_1.push(1)
    run_test("push(1)", "[1]", dll_1)
    dll_1 = dll.NFDoublyLinkedList()
    dll_1.append(1)
    run_test("append(1)", "[1]", dll_1)
    dll_1 = dll.NFDoublyLinkedList()
    dll_1.insert(1, 0)
    run_test("insert(1, 0)", "[1]", dll_1)
    return #TODO: Remove

    print "\n- Additions while not empty:"
    dll_1.push(0)
    run_test("push(0)", "[0, 1]", dll_1)
    dll_1.append(3)
    run_test("append(3)", "[0, 1, 3]", dll_1)
    dll_1.insert(2, 2)
    run_test("insert(2, 2)", "[0, 1, 2, 3]", dll_1)
    dll_1.insert(9001, 4)
    run_test("insert(9001, 5)", "[0, 1, 2, 3, 4]", dll_1)

    print "\n- Getters while not empty:"
    run_test("len(dll_1)", "5", len(dll_1))
    run_test("length()", "5", dll_1.length())
    run_test("head.data", "0", dll_1.head.data)
    run_test("get_tail().data", "4", dll_1.get_tail().data)
    run_test("get_index(2).data", "2", dll_1.get_index(2).data)
    try:
        run_test("get_index(9001).data", None, None)
        dll_1.get_index(9001).data
        print "\tFail | Check index integer"
        full_pass = False
    except Exception as err:
        print "\t%s" % err
    
    print "\n- Remove nodes:"
    dll_1.delete_head()
    run_test("delete_head()", "[1, 2, 3, 4]", dll_1)
    dll_1.delete_tail()
    run_test("delete_tail()", "[1, 2, 3]", dll_1)
    dll_1.delete_index(1)
    run_test("delete_index(1)", "[1, 3]", dll_1)
    dll_1.delete_index(1)
    run_test("delete_index(1)", "[1]", dll_1)
    dll_1.delete_index(0)
    run_test("delete_index(0)", "[]", dll_1)
    run_test("length()", "0", dll_1.length())

    print "\nFinal result: %s" % ("Pass" if full_pass else "Fail")

test()
