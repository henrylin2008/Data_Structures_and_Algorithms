# Question - Let's use recursion to help us solve the following permutation problem:
#
# Given a list of items, the goal is to find all of the permutations of that list. For example,
# Given a list like: [0, 1, 2]
# Permutations: [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
#
# Notice that the expected output is a list of permutation with each permuted item being represented by a list. Such
# an object that contains other object is called "compound" object.

# The Idea
# Build a compoundList incrementally starting with a blank list, and permute (add) each element of original input
# list at all possible positions.
#
# For example, take [0, 1, 2] as the original input list:
#
# 1. Start with a blank compoundList [[]]. This is actually the last call of recursive function stack. Pick the element
# 2 of original input list, making the compoundList as [[2]]
#
# 2. Pick next element 1 of original input list, and add this element at position 0, and 1 for each list of previous
# compoundList. We will require to create copy of all lists of previous compoundList, and add the new element. Now,
# the compoundList will become [[1, 2], [2, 1]].
#
# 3. Pick next element 0 of original input list, and add this element at position 0, 1, and 2 for each list of previous
# compoundList. Now, the compoundList will become [[0, 1, 2], [1, 0, 2], [1, 2, 0], [0, 2, 1], [2, 0, 1], [2, 1, 0]] .

# Recursive Solution
"""
Args: myList: list of items to be permuted
Returns: compound list: list of permutation with each permuted item being represented by a list
"""
