#!/usr/bin/env python2

class NFTrieNode(object):
    def __init__(self, key=None):
        self.children = {}
        self.key = key
        self.end_of_word = False


class NFTrie(object):
    def __init__(self):
        self.root = NFTrieNode()
        self.nodes = {}
        self.total_words = 0
        self.total_nodes = 0

    # Inserts a new word into the trie
    def insert(self, string):
        node = self.root
        for i, char in enumerate(str(string)):
            if char not in node.children:
                node.children[char] = NFTrieNode(char)
                self.total_nodes += 1
            node = node.children[char]
        node.end_of_word = True
        self.total_words += 1

    # Generator which searches for a word by walking down the search_root and starting traversal once reached
    def search(self, search_root):
        search_root_found = True
        node = self.root
        for char in str(search_root):
            if char in node.children:
                node = node.children[char]
            else:
                search_root_found = False
                break
        if search_root_found:
            for word in self._traverse(node, search_root):
                yield word

    # Generates all words in the trie
    def generate_all(self):
        for word in self._traverse(self.root, ""):
            yield word

    # Recursive helper generator for finding words
    def _traverse(self, node, search_root):
        if node.end_of_word:
            yield search_root
        for key in node.children.keys():
            for word in self._traverse(node.children[key], search_root + str(key)):
                yield word

    # Checks if the trie contains given string, returns boolean
    def contains(self, string):
        node = self.root
        for char in str(string):
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.end_of_word

