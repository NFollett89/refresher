#!/usr/bin/env python2

class NFNode(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class NFSinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Get informal string representation
    def __str__(self):
        if not self.head:
            return "[]"
        data = [self.head.data]
        current = self.head
        while current.next:
            current = current.next
            if current.data:
                data.append(current.data)
        return str(data)

    # Get length of the collection
    def __len__(self):
        return self.length()

    # Get length of the list
    def length(self):
        if not self.head:
            return 0
        length = 1
        current = self.head
        while current.next:
            length += 1
            current = current.next
        return length

    # Clone the linked list
    def clone(self):
        return copy.copy(self)

    # Get the node at given index
    def get_index(self, index):
        current = self.head
        for _ in xrange(index-1):
            if current.next:
                current = current.next
            else:
                raise IndexError("Given index out of range")
        return current.next

    # Get the last node of the list
    def get_tail(self):
        current = self.head
        while current.next:
            current = current.next
        return current

    # Add a new node to the head of the list
    def push(self, data):
        new_node = NFNode(data)
        new_node.next = self.head
        self.head = new_node

    # Add a new node at the given list index
    def insert(self, index, data):
        new_node = NFNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        for _ in xrange(index-1):
            if current.next:
                current = current.next
            else:
                current.next = new_node
                return
        new_node.next = current.next
        current.next = new_node

    # Add a new node to the end of the list
    def append(self, data):
        new_node = NFNode(data)
        if not self.head:
            self.head = new_node
        else:
            self.get_tail().next = new_node

    # Delete the head of the list
    def delete_head(self):
        self.head = self.head.next

    # Delete the tail of the list
    def delete_tail(self):
        current = self.head
        while current.next:
            previous = current
            current = current.next
        previous.next = None

    # Delete a node from given index
    def delete_index(self, index):
        if index == 0:
            return self.delete_head()
        current = self.head
        for _ in xrange(index-1):
            if current.next:
                current = current.next
            else:
                raise IndexError("Given index out of range")
        tmp = current.next
        current.next = current.next.next
        tmp.next = None

