#!/usr/bin/env python2
import copy

class NFArrayList(object):
    def __init__(self):
        self.arraylist = []

    # Informal string representation
    def __str__(self):
        if not self.arraylist:
            return "[]"
        return str(self.arraylist)

    # Iterator special method
    def __iter__(self):
        for i in self.arraylist:
            yield i

    # Len special method
    def __len__(self):
        return self.length()

    # Return length of arraylist
    def length(self):
        return len(self.arraylist)

    # Clone the array list
    def clone(self):
        return copy.copy(self)

    # Add data to the end of the list, or to the specified position
    def add(self, data, position=None):
        if position or position == 0:
            if position > self.length():
                difference = position - self.length()
                self.arraylist += [None for _ in xrange(difference+1)] + [data]
            else:
                left = self.arraylist[:position]
                right = self.arraylist[position:]
                self.arraylist = left + [data] + right
        else:
            self.arraylist.append(data)

    # Add all elements of the collection to the end of the arraylist
    def add_all(self, collection):
        for i in collection:
            self.add(i)

    # Clear the arraylist
    def clear(self):
        self.arraylist = []

    # Checks for element in the arraylist
    def contains(self, data):
        return data in self.arraylist

    # Returns the element at the given index
    def get(self, index):
        if index >= self.length() or abs(index) > self.length():
            raise IndexError("Index %s is out of range for arraylist with length %s" % (index, self.length()))
        else:
            return self.arraylist[index]

    # Returns the first index of the given element or -1 if it is not found
    def index_of(self, element):
        for i, data in enumerate(self.arraylist):
            if data == element:
                return i
        return -1

    # Returns the last index of the given element or -1 if it is not found
    def last_index(self, element):
        current_index = -1
        for i, data in enumerate(self.arraylist):
            if data == element:
                current_index = i
        return current_index

    # Checks if the arraylist is empty
    def is_empty(self):
        return self.length() == 0

    # Remove element at index
    def remove(self, index):
        if index >= self.length() or abs(index) > self.length():
            raise IndexError("Index %s is out of range for arraylist with length %s" % (index, self.length()))
        elif index == self.length() - 1 or index == -1:
            self.arraylist = self.arraylist[:index]
        else:
            self.arraylist = self.arraylist[:index] + self.arraylist[index + 1:]

    # Remove range of elements from inclusive start index to exclusive end index
    # - Iteration always happens from left to right, i.e. self.arraylist[start:end:-1] will not be implemented
    def remove_range(self, start, end):
        if ((start > 0 and end > 0) or (start < 0 and end < 0)) and start > end:
            raise IndexError("Start index %s is greater than end index %s" % (start, end))
        elif start == end:
            raise IndexError("Start index %s and end index %s are the same" % (start, end))
        elif start >= self.length():
            raise IndexError("Start index %s is out of range for arraylist with length %s" % (start, self.length()))
        elif end > self.length(): # Allow end to be equal to length in order to include deletion of last index
            raise IndexError("End index %s is out of range for arraylist with length %s" % (end, self.length()))
        else:
            self.arraylist = self.arraylist[:start] + self.arraylist[end:] 

    # Removes all instances of found element from given collection
    def remove_all(self, collection):
        new_arraylist = []
        for i in self.arraylist:
            if i not in collection:
                new_arraylist.append(i)
        self.arraylist = new_arraylist

    # Retains only the elements in this list that are contained in the given collection
    def retain_all(self, collection):
        new_arraylist = []
        for i in self.arraylist:
            if i in collection:
                new_arraylist.append(i)
        self.arraylist = new_arraylist

    # Set element at given index to given data
    def set(self, index, data):
        if index >= self.length() or abs(index) > self.length():
            raise IndexError("Index %s is out of range for arraylist with length %s" % (index, self.length()))
        self.arraylist[index] = data

    # Returns a view of the portion of this list between the specified start, inclusive, and end, exclusive.
    def sub_list(self, start, end):
        if ((start > 0 and end > 0) or (start < 0 and end < 0)) and start > end:
            raise IndexError("Start index %s is greater than end index %s" % (start, end))
        elif start == end:
            raise IndexError("Start index %s and end index %s are the same" % (start, end))
        elif start >= self.length():
            raise IndexError("Start index %s is out of range for arraylist with length %s" % (start, self.length()))
        elif end > self.length(): # Allow end to be equal to length in order to include deletion of last index
            raise IndexError("End index %s is out of range for arraylist with length %s" % (end, self.length()))
        else:
            return self.arraylist[start:end]

