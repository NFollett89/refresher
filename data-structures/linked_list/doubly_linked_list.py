#!/usr/bin/env python2

import copy

class NFNode(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class NFDoublyLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        if head:
            self.tail = self._find_tail()
        else:
            self.tail = None
        self.list_length = 0

    # Iterator
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    # Reverse iterator
    def reverse_iter(self):
        current = self.tail
        while current:
            yield current
            current = current.prev

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
        return self.list_length

    # Get the node at given index
    def index(self, index):
        if self.list_length == 0 or index >= self.list_length or index < 0:
            raise IndexError("Given index %s out of range for linked list with length %s" % (index, self.list_length))
        elif index == 0:
            return self.head
        current = self.head
        for _ in xrange(index-1):
            current = current.next
        return current.next

    # Find tail of the current DLL
    def _find_tail(self):
        current = self.head
        while current.next:
            current = current.next
        self.tail = current
        return tail

    # Add a node to the front of the list
    def push(self, data):
        new_node = NFNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.list_length += 1

    # Insert a node at the given index
    def insert(self, data, index):
        if index > self.length() or index < 0:
            raise IndexError("Index %s out of bounds for DLL with length %s" % (index, self.length()))
        elif index == 0:
            return self.push(data)
        elif index == self.length():
            return self.append(data)
        new_node = NFNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        current = self.head
        for _ in xrange(index-1):
            current = current.next
        new_node.prev = current
        if current.next:
            new_node.next = current.next
            new_node.next.prev = new_node
            current.next = new_node
        else:
            current.next = new_node
            self.tail = new_node
        self.list_length += 1

    # Append a node to the end of the list
    def append(self, data):
        new_node = NFNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.tail
            new_node.prev = self.tail
            self.tail = new_node
            temp.next = self.tail
        self.list_length += 1

    # Delete head of the list
    def delete_head(self):
        old_head = self.head
        self.head = old_head.next
        old_head = None
        self.list_length -= 1

    # Delete node at the given index
    def delete(self, index):
        if index > self.length() or index < 0:
            raise IndexError("Index %s out of bounds for DLL with length %s" % (index, self.length()))
        elif index == 0:
            return self.delete_head()
        elif index == self.length() - 1:
            return self.delete_tail()
        current = self.head
        for _ in xrange(index-1):
            current = current.next
        del_node = current.next
        current.next = current.next.next
        current.next.prev = current
        del_node = None
        self.list_length -= 1

    # Delete tail of the list
    def delete_tail(self):
        old_tail = self.tail
        self.tail = old_tail.prev
        self.tail.next = None
        old_tail = None
        self.list_length -= 1

