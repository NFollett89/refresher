#!/usr/bin/env python2

class NFQueue(object):
    def __init__(self):
        self.queue = []

    # Informal string representation of the Queue
    def __str__(self):
        return "%s" % self.queue

    # Iterator implementation
    def __iter__(self):
        for data in self.queue:
            yield data

    # Len special method
    def __len__(self):
        return self.length()

    # Return length of queue
    def length(self):
        return len(self.queue)

    # Add data to the back of the queue
    def enqueue(self, data):
        self.queue.append(data)

    # Remove data from the front of the queue and return it
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        data = self.queue[0]
        self.queue = self.queue[1:]
        return data

    # Return data from the front of the queue
    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    # Clear the queue
    def clear(self):
        self.queue = []

    # Checks if queue contains data
    def contains(self, data):
        return data in self.queue

