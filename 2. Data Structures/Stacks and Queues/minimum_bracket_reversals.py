# Problem Statement
# Given an input string consisting of only { and }, figure out the minimum number of reversals required to make the
# brackets balanced.
#
# For example:
#
# For input_string = "}}}}, the number of reversals required is 2.
# For input_string = "}{}}, the number of reversals required is 1.
# If the brackets cannot be balanced, return -1 to indicate that it is not possible to balance them.
class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0