#!/usr/bin/env python2

import trie

def test():
    t = trie.NFTrie()
    for string in ["foo", "foobar", "foobarbaz", "footest1", "footest2", "foobartest", "bar", "bartest", "barbaz", "barbazbat"]:
        t.insert(string)
        print "Inserted %s - total words: %s - total nodes: %s" % (string, t.total_words, t.total_nodes)
    for string in ["test1", "foo", "foobar", "foobarbaz", "foobarbazbat"]:
        print "contains(%s): %s" % (string, t.contains(string))
    print "\nSearching for 'foo':"
    for word in t.search("foo"):
        print "- Found word: %s" % word
    print "\nSearching for 'bar':"
    for word in t.search("bar"):
        print "- Found word: %s" % word
    print "\nSearching for 'test':"
    for word in t.search("test"):
        print "- Found word: %s" % word
    print "\nGenerating all words:"
    for word in t.generate_all():
        print "- Found word: %s" % word

test()
