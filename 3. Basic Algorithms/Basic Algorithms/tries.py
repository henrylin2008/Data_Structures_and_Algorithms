# Trie
# You've learned about Trees and Binary Search Trees. In this notebook, you'll learn about a new type of Tree
# called Trie. Before we dive into the details, let's talk about the kind of problem Trie can help with.
#
# Let's say you want to build software that provides spell check. This software will only say if the word is valid or
# not. It doesn't give suggested words. From the knowledge you've already learned, how would you build this?
#
# The simplest solution is to have a hashmap of all known words. It would take O(1) to see if a word exists,
# but the memory size would be O(n*m), where n is the number of words and m is the length of the word. Let's see how
# a Trie can help decrease the memory usage while sacrificing a little on performance.
#
# Basic Trie
# Let's look at a basic Trie with the following words: "a", "add", and "hi"
