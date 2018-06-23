#!/usr/bin/env python2

import stack as s

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

    my_stack = s.NFStack()
    print "\nTesting NFStack()"
    run_test("length()", "0", len(my_stack))
    run_test("pop()", "None", my_stack.pop())
    run_test("peek()", "None", my_stack.peek())
    run_test("contains(0)", "False", my_stack.contains(0))
    my_stack.clear()
    run_test("clear()", "[]", my_stack)
 
    for i in xrange(10):
        my_stack.push(i) 
    for i, stack_i in enumerate(my_stack):
        run_test("__iter__()", str(stack_i), str(abs(i-len(my_stack))-1))
    run_test("lenth()", "10", len(my_stack))
    run_test("__str__()", "[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]", my_stack)
    run_test("contains(0)", "True", my_stack.contains(0))
    run_test("contains(9001)", "False", my_stack.contains(9001))
    run_test("length()", "10", len(my_stack))
    run_test("peek()", "9", my_stack.peek())
    run_test("pop()", "9", my_stack.pop())
    run_test("pop()", "8", my_stack.pop())
    my_stack.clear()
    run_test("clear()", "[]", my_stack)
    
    print "\nFinal result: %s" % ("Pass" if full_pass else "Fail")

test()
