# Flattening a nested linked list
# Suppose you have a linked list where the value of each node is a sorted linked list
# (i.e., it is a nested list). Your task is to flatten this nested list—that is, to combine all nested lists into a
# single (sorted) linked list.

# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones.
# User defined class
class Node:
    def __init__(self,
                 value):  # <-- For simple LinkedList, "value" argument will be an int, whereas,
        # for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


# User defined class
class LinkedList:
    def __init__(self, head):  # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''

    def append(self, value):

        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the current LinkedList
        while node.next is not None:
            node = node.next

        # Append the newly created Node at the end of the current LinkedList
        node.next = Node(value)

    '''We will need this function to convert a LinkedList object into a Python list of integers'''

    def to_list(self):
        out = []  # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object

        while node:  # <-- Iterate until we have nodes available
            out.append(int(str(
                node.value)))  # <-- node.value is actually of type Node, therefore convert it into int before
            # appending to the Python list
            node = node.next

        return out


def merge(list1, list2):
    # Merge the two linked lists in a single, sorted linked list.
    """
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    """
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt.value)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt.value)
            list2_elt = list2_elt.next
    return merged


''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''
class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)  # <-- self.head is a node for NestedLinkedList

    '''  A recursive function '''
    def _flatten(self, node):
        # A termination condition
        if node.next is None:
            return merge(node.value, None)  # <-- First argument is a simple LinkedList

        # _flatten() is calling itself untill a termination condition is achieved
        return merge(node.value, self._flatten(node.next))  # <-- Both arguments are a simple LinkedList each


''' Test merge() function'''
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    # This will print 1 2 3 4 5
    print(node.value)
    node = node.next

# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    # This will print 1 3 5
    print(node.value)
    node = node.next

''' Test flatten() function'''
# Create a nested linked list with one node.
# The node itself is a simple linked list as 1-->3-->5 created previously
nested_linked_list = NestedLinkedList(Node(linked_list))

# Append a node (a linked list as 2-->4) to the existing nested linked list
nested_linked_list.append(second_linked_list)

# Call the `flatten()` function
flattened = nested_linked_list.flatten()

# Logic to print the flattened list
node = flattened.head
while node is not None:
    # This will print 1 2 3 4 5
    print(node.value)
    node = node.next


# Computational Complexity
# Lets start with the computational complexity of merge. Merge takes in two lists. Let's say
# the lengths of the lists are  𝑁1  and  𝑁2 . Because we assume the inputs are sorted, merge is very efficient. It
# looks at the first element of each list and adds the smaller one to the returned list. Every time through the loop
# we are appending one element to the list, so it will take  𝑁1+𝑁2  iterations until we have the whole list.
#
# The complexity of flatten is a little more complicated to calculate. Suppose our NestedLinkedList has  𝑁  linked
# lists and each list's length is represented by  𝑀1,𝑀2,...,𝑀𝑁 .
#
# We can represent this recursion as:
#
# 𝑚𝑒𝑟𝑔𝑒(𝑀1,𝑚𝑒𝑟𝑔𝑒(𝑀2,𝑚𝑒𝑟𝑔𝑒(...,𝑚𝑒𝑟𝑔𝑒(𝑀𝑁−1,𝑚𝑒𝑟𝑔𝑒(𝑀𝑁,𝑁𝑜𝑛𝑒))))) Let's start from the
# inside. The inner most merge returns the  𝑛𝑡ℎ  linked list. The next merge does  𝑀𝑁−1+𝑀𝑁  comparisons. The
# next merge does  𝑀𝑁−2+𝑀𝑁−1+𝑀𝑁  comparisons.
#
# Eventually we will do  𝑁  comparisons on all of the  𝑀𝑁  elements. We will do  𝑁−1  comparisons on  𝑀𝑁−1  elements.
#
# This can be generalized as:
#
# 𝑁
# ∑𝑛 ∗ 𝑀𝑛
# n
