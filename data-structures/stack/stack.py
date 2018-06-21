#!/usr/bin/env python2

class NFStack(object):
    def __init__(self):
        self.stack = []

    # Informal string representation of the Stack
    def __str__(self):
        return "%s" % self.stack[::-1]

    # Iterator implementation
    def __iter__(self):
        for data in self.stack[::-1]:
            yield data

    # Len special method
    def __len__(self):
        return self.length()

    # Return length of stack
    def length(self):
        return len(self.stack)

    # Add data to the back of the stack
    def push(self, data):
        self.stack.append(data)

    # Remove data from the front of the stack and return it
    def pop(self):
        if len(self.stack) == 0:
            return None
        data = self.stack[-1]
        self.stack = self.stack[:-1]
        return data

    # Return data from the front of the stack
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    # Clear the stack
    def clear(self):
        self.stack = []

    # Checks if stack contains data
    def contains(self, data):
        return data in self.stack

