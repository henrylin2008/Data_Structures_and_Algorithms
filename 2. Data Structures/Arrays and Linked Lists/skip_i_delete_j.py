# Problem Statement
# You are given the head of a linked list and two integers, i and j. You have to retain the first i nodes and then
# delete the next j nodes. Continue doing so until the end of the linked list.
#
# Example:
#
# linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
# i = 2
# j = 3
# Output = 1 2 6 7 11 12


# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



