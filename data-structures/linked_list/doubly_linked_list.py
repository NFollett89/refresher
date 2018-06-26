#!/usr/bin/env python2

import copy

class NFNode(object):
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node


class NFDoublyLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        if head:
            self.tail = self._find_tail()
        else:
            self.tail = None

    # Informal string representation
    def __str__(self):
        l = []
        current = self.head
        while current:
            l.append(current.data)
            current = current.next
        return str(l)

    # Len special method
    def __len__(self):
        return self.length()

    # Find length of the list
    def length(self):
        if not self.head:
            return 0
        current = self.head
        length = 1
        while current.next:
            length += 1
            current = current.next
        return length

    # Find tail of the current DLL
    def _find_tail(self):
        current = self.head
        while current.next:
            current = current.next
        self.tail = current
        return tail

    # Add a node to the front of the list
    def push(self, data):
        new_head = NFNode(data, self.head)
        self.head = new_head

    # Insert a node at the given index
    def insert(self, data, index):
        if index > self.length():
            raise IndexError("Index %s out of bounds for DLL with length %s" % (index, self.length()))
        if not self.head:
            new_node = NFNode(data)
            self.head = new_node
            self.tail = new_node
        else:
            for _ in xrange(index-1):
                current = current.next
            new_node = NFNode(data, current.next, current)
            current.next = new_node
            new_node.next.prev = new_node

    # Append a node to the end of the list
    def append(self, data):
        new_node = NFNode(data, None, self.tail)
        if not self.head:
            self.head = new_node
        self.tail = new_node

    # Delete head of the list
    def delete_head(self):
        old_head = self.head
        self.head = old_head.next
        old_head.next = None

    # Delete node at the given index
    def delete(self, index):
        return

    # Delete tail of the list
    def delete_tail(self):
        old_tail = self.tail
        self.tail = old_tail.prev
        old_tail.prev = None

