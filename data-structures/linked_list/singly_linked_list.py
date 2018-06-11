#!/usr/bin/env python2

class NFNode(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
        

class NFSinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Get informal string representation
    def __str__(self):
        if not self.head:
            return "[]"
        data = [self.head.get_data()]
        current = self.head
        while current.get_next():
            current = current.get_next()
            if current.get_data():
                data.append(current.get_data())
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
        while current.get_next():
            length += 1
            current = current.get_next()
        return length

    # Get the node at given index
    def get_index(self, index):
        current = self.head
        for _ in xrange(index-1):
            if current.get_next():
                current = current.get_next()
            else:
                raise IndexError("Given index out of range")
        return current.get_next()

    # Get the first node of the list
    def get_head(self):
        return self.head

    # Get the last node of the list
    def get_tail(self):
        current = self.head
        while current.get_next():
            current = current.get_next()
        return current

    # Add a new node to the head of the list
    def push(self, data):
        new_node = NFNode(data)
        new_node.set_next(self.head)
        self.head = new_node

    # Add a new node at the given list index
    def insert(self, index, data):
        new_node = NFNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        for _ in xrange(index-1):
            if current.get_next():
                current = current.get_next()
            else:
                current.set_next(new_node)
                return
        new_node.set_next(current.get_next())
        current.set_next(new_node)

    # Add a new node to the end of the list
    def append(self, data):
        new_node = NFNode(data)
        if not self.head:
            self.head = new_node
        else:
            self.get_tail().set_next(new_node)

    # Delete the head of the list
    def delete_head(self):
        self.head = self.head.get_next()

    # Delete the tail of the list
    def delete_tail(self):
        current = self.head
        while current.get_next():
            previous = current
            current = current.get_next()
        previous.set_next(None)

    # Delete a node from given index
    def delete_index(self, index):
        if index == 0:
            return self.delete_head()
        current = self.head
        for _ in xrange(index-1):
            if current.get_next():
                current = current.get_next()
            else:
                raise IndexError("Given index out of range")
        tmp = current.get_next()
        current.set_next(current.get_next().get_next())
        tmp.set_next(None)

