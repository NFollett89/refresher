#!/usr/bin/env python2

class NFNode(object):
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        return None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next
        

class NFSinglyLinkedList(object):
    def __init__(self):
        self.head = None
        return self.head

    # Get length of the collection
    def __len__(self):
        return self.length()

    # Get length of the list
    def length(self):
        length = 0
        current = self.head
        while current.get_next_node():
            length += 1
            current = current.get_next_node()
        return length

    # Get the i'th node of the list
    def index(self, index):
        current = self.head
        for _ in xrange(index):
            if current.get_next_node():
                current = current.get_next_node()
            else:
                return break
        return current

    # Get the first node of the list
    def head(self):
        return self.head

    # Get the last node of the list
    def tail(self):
        current = self.head
        while current.get_next_node():
            current = current.get_next_node()
        return current

    # Add a new node to the head of the list
    def push(self, data):
        new_node = NFNode(data)
        new_node.set_next_node(self.head)
        self.head = new_node

    # Add a new node at the given list index
    def insert(self, index, data):
        new_node = NFNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        for _ in xrange(index):
            if current.get_next_node():
                current = current.get_next_node()
            else:
                break
        current.set_next_node(new_node)

    # Add a new node to the end of the list
    def append(self, data)
        new_node = NFNode(data)
        if not self.head:
            self.head = new_node
        else:
            self.get_last_node().set_next_node(new_node)

