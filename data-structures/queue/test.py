#!/usr/bin/env python2

import queue as q

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
    my_queue = q.NFQueue()
    print "\nTesting NFQueue()"
    run_test("length()", "0", len(my_queue))
    run_test("dequeue()", "None", my_queue.dequeue())
    run_test("peek()", "None", my_queue.peek())
    run_test("contains(0)", "False", my_queue.contains(0))
    try:
        my_queue.clear()
        run_test("clear()", "[]", my_queue)
    except Exception as err:
        print err
 
    for i in xrange(10):
        my_queue.enqueue(i) 
    for i, queue_i in enumerate(my_queue):
        run_test("__iter__()", str(queue_i), str(i))
    run_test("lenth()", "10", len(my_queue))
    run_test("__str__()", "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]", my_queue)
    run_test("contains(0)", "True", my_queue.contains(0))
    run_test("contains(9001)", "False", my_queue.contains(9001))
    run_test("length()", "10", len(my_queue))
    run_test("peek()", "0", my_queue.peek())
    run_test("dequeue()", "0", my_queue.dequeue())
    run_test("dequeue()", "1", my_queue.dequeue())
    try:
        my_queue.clear()
        run_test("clear()", "[]", my_queue)
    except Exception as err:
        print err
    
    print "\nAll tests passed: %s" % full_pass

test()
