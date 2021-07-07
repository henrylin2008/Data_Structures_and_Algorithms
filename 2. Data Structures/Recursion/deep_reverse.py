# Problem Statement
# Define a procedure, deep_reverse, that takes as input a list, and returns a new list that is the deep reverse of
# the input list.
# This means it reverses all the elements in the list, and if any of those elements are lists
# themselves, reverses all the elements in the inner list, all the way down.
#
# Note: The procedure must not change the input list itself.
#
# Example
# Input: [1, 2, [3, 4, 5], 4, 5]
# Output: [5, 4, [5, 4, 3], 2, 1]
#
# Hint
#
# 1.Begin with a blank final list to be returned.
# 2.Traverse the given list in the reverse order.
#   -If an item in the list is a list itself, call the same function.
#   -Otheriwse, append the item to the final list.

