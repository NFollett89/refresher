#!/usr/bin/env python2

import hashlib
import copy

class NFHashTable(object):
    """ Hash table using chain method """
    def __init__(self, capacity=1000):
        if not isinstance(capacity, int):
            raise TypeError("%s is not an integer" % capacity)
        self.table = [[] for _ in xrange(capacity)]
        self.capacity = capacity
        self.empty = capacity
        self.size = 0

    # Informal string representation
    def __str__(self):
        s = "{"
        for chain in self.table:
            for item in chain:
                s += "%s: %s, " % (item[0], item[1])
        # Remove the trailing comma and space before closing
        if len(s) > 1:
            s = s[:-2]
        s += "}"
        return s

    # Length special method
    def __len__(self):
        return self.size

    # Iterator which generates items
    def __iter__(self):
        for chain in self.table:
            if chain:
                for item in chain:
                    yield item[0], item[1]

    # Returns items as a list of key, value tuples
    def items(self):
        items = []
        for chain in self.table:
            if chain:
                for item in chain:
                    items.append((item[0], item[1]))
        return items

    # Returns a list of keys
    def keys(self):
        keys = []
        for chain in self.table:
            if chain:
                for item in chain:
                    keys.append(item[0])
        return keys

    # Returns a list of values
    def values(self):
        values = []
        for chain in self.table:
            if chain:
                for item in chain:
                    values.append(item[1])
        return values

    # Hash a key
    def _hash(self, key):
        key = str(key).strip()
        hash_val = int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16)
        return hash_val

    # Store key:value pair in the hash table
    def set(self, key, value):
        hash_val = self._hash(key)
        index = hash_val % self.capacity
        self._set_index(index, key, value) 

    # Helper function to set a key-value pair as part of chain method
    def _set_index(self, index, key, value):
        chain = self.table[index]
        for item in chain:
            if item[0] == key:
                item[1] = value
                return
        chain.append((key, value))
        self.size += 1
        if len(chain) == 1:
            self.empty -= 1
            
    # Retrieve value for the given key
    def get(self, key):
        hash_val = self._hash(key)
        index = hash_val % self.capacity
        return self._get_index(index, key)

    # Helper function to get a value based on index and key
    def _get_index(self, index, key):
        chain = self.table[index]
        if chain:
            for item in chain:
                if item[0] == key:
                    return item[1]
        raise KeyError("Invalid key: %s" % key)

    # Delete key
    def delete(self, key):
        hash_val = self._hash(key)
        index = hash_val % self.capacity
        self._delete_index(index, key)

    def _delete_index(self, index, key):
        chain = self.table[index]
        if chain:
            for i, item in enumerate(chain):
                if item[0] == key:
                    del chain[i]
                    self.size -= 1
                    if len(chain) == 0:
                        self.empty += 1
                return
        raise KeyError("Invalid key: %s" % key)

    # Returns number of empty spaces
    def empty_spaces(self):
        return self.empty

    # Returns number of collisions
    def collisions(self):
        return self.size - (self.capacity - self.empty)

