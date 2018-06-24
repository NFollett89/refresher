#!/usr/bin/env python2

class NFTrieNode(object):
    def __init__(self, key=None):
        self.children = {}
        self.key = key


class NFTrie(object):
    def __init__(self):
        self.root = NFTrieNode('*')
        self.nodes = {}

    def insert(self, string):
        node = self.root
        for char in string:
            if char not in node.children:
                node.children[char] = NFTrieNode(char)
            node = node.children[char]

    def find(self, string):
        return

