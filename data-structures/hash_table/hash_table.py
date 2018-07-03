#!/usr/bin/env python2

import hashlib
import copy

class NFHashTable(object):
    """ Hash table using chain method """
    def __init__(self, size=100):
        if not isinstance(size, int):
            raise TypeError("%s is not an integer" % size)
        self.table = [None for _ in xrange(size)]

    # Informal string representation
    def __str__(self):
        s = "{"
        for item in self.table:
            if item:
                s += "%s: %s, " % (item[0], item[1])
        # Remove the trailing comma and space before closing
        if len(s) > 1:
            s = s[:-2]
        s += "}"
        return s

    # Iterator which generates items
    def __iter__(self):
        for item in self.table:
            if item:
                if isinstance(item, list):
                    for sub_item in item:
                        yield sub_item[0], sub_item[1]
                else:
                    yield item[0], item[1]

    # Returns a list of keys
    def keys(self):
        keys = []
        for item in self.table:
            if item:
                if isinstance(item, list):
                    for sub_item in item:
                        keys.append(sub_item[0])
                else:
                    keys.append(item[0])
        return keys

    # Returns a list of values
    def values(self):
        values = []
        for item in self.table:
            if item:
                if isinstance(item, list):
                    for sub_item in item:
                        values.append(sub_item[1])
                else:
                    values.append(item[1])
        return values

    # Return a clone of the hash table
    def clone(self):
        return copy.copy(self)

    # Hash a key
    def _hash(self, key):
        return

    # Store key:value pair in the hash table
    def store(self, key, value):
        return

    # Retrieve value for the given key
    def retrieve(self, key):
        return

