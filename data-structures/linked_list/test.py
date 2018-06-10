#!/usr/bin/env python2

import singly_linked_list

def run_test(call, expected, actual):
    if expected:
        result = "Pass" if str(expected) == str(actual) else "Fail"
        print "  - %s | %s : %s == %s" % (result, call, expected, actual)
    else:
        print "  - %s : %s" % (call, actual)

def test():
    # Tests for NFSinglyLinkedList()
    print "\nTesting NFSinglyLinkedList()"
    print "- Getters while empty:"
    sll = singly_linked_list.NFSinglyLinkedList()
    run_test("length()", "0", sll.length())
    run_test("get_head().get_data()", None, sll.get_head().get_data())
    try:
        run_test("get_index(1).get_data()", None, None)
        sll.get_index(1).get_data()
    except Exception as err:
        print "\t%s" % err
    run_test("get_tail().get_data()", None, sll.get_tail().get_data())

    print"\n- Additions while empty:"
    sll.push(1)
    run_test("push(1)", "[1]", sll)
    sll = singly_linked_list.NFSinglyLinkedList()
    sll.append(1)
    run_test("append(1)", "[1]", sll)
    sll = singly_linked_list.NFSinglyLinkedList()
    sll.insert(0, 1)
    run_test("insert(0, 1)", "[1]", sll)

    print "\n- Additions while not empty:"
    sll.push(0)
    run_test("push(0)", "[0, 1]", sll)
    sll.append(3)
    run_test("append(3)", "[0, 1, 3]", sll)
    sll.insert(2, 2)
    run_test("insert(2, 2)", "[0, 1, 2, 3]", sll)

    print "\n- Getters while not empty:"
    run_test("len(sll)", "4", len(sll))
    run_test("length()", "4", sll.length())
    run_test("get_head().get_data()", "0", sll.get_head().get_data())
    run_test("get_tail().get_data()", "3", sll.get_tail().get_data())
    run_test("get_index(2).get_data()", "2", sll.get_index(2).get_data())
    try:
        run_test("get_index(9001).get_data()", None, None)
        sll.get_index(9001).get_data()
    except Exception as err:
        print "\t%s" % err
"""
    print "\n- Remove nodes:"
    sll.delete_head()
    run_test("delete_head()", "[1, 3]", sll)
    sll.delete_index(2)
    sll.delete_tail

    print"\n- Remove nodes while empty:"
    sll.delete_head()
    sll.delete_index(1)
    sll.delete_tail()
"""

#    print "\nTests finished\n"

test()
