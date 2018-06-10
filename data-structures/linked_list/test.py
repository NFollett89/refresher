#!/usr/bin/env python2

import singly_linked_list

def test():
    # Basic tests for NFNode()
    print "Testing NFNode()"
    node_1 = singly_linked_list.NFNode()
    print "- Should be None: %s" % node_1.get_data()
    print "- Should be None: %s" % node_1.get_next_node()
    node_1.set_data(9001)
    print "- Should be 9001: %s" % node_1.get_data()
    node_2 = singly_linked_list.NFNode(9002)
    node_1.set_next_node(node_2)
    print "- Should be 9002: %s" % node_1.get_next_node().get_data()

test()
