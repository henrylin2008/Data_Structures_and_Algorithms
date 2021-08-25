# Union and Intersection of Two Linked Lists

# Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is
# the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩
# B, is the set of all objects that are members of both the sets A and B.
#
# You will take in two linked lists and return a linked list that is composed of either the union or intersection,
# respectively. Once you have completed the problem you will create your own test cases and perform your own run time
# analysis on the code.
#
# We have provided a code template below, you are not required to use it:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(list_1, list_2):
    # Return the set of elements which are in A, in B, or in both A and B.
    union_set = set()

    current_node = list_1.head
    while current_node:
        union_set.add(current_node.value)
        current_node = current_node.next

    current_node = list_2.head
    while current_node:
        union_set.add(current_node.value)
        current_node = current_node.next

    union_list = LinkedList()
    for item in union_set:
        union_list.append(item)

    return union_list


def intersection(list_1, list_2):
    # return the set of all objects that are members of both the sets A and B
    set1 = set()
    current_node = list_1.head
    while current_node:
        set1.add(current_node.value)
        current_node = current_node.next

    set2 = set()
    current_node = list_2.head
    while current_node:
        set2.add(current_node.value)
        current_node = current_node.next

    intersection_set = set1.intersection(set2)
    intersection_list = LinkedList()
    for item in intersection_set:
        intersection_list.append(item)
    return intersection_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)
for i in element_2:
    linked_list_2.append(i)

print("Test case 1:")
print("Union:", union(linked_list_1, linked_list_2))
print("Intersection:", intersection(linked_list_1, linked_list_2))
print("")

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)
for i in element_2:
    linked_list_4.append(i)

print("Test case 2: no common number")
print("Union:", union(linked_list_3, linked_list_4))
print("Intersection:", intersection(linked_list_3, linked_list_4))
print("")

# Test case 3   - A empty list
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1, 8, 9, 4, 5, 6, 4]
for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("Test case 3: an empty list")
print("Union:", union(linked_list_5, linked_list_6))
print("Intersection:", intersection(linked_list_5, linked_list_6))
print("")

# Test case 4 - 2 empty lists
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []
for i in element_1:
    linked_list_7.append(i)
for i in element_2:
    linked_list_8.append(i)

print("Test case 4: two empty lists")
print("Union:", union(linked_list_7, linked_list_8))
print("Intersection:", intersection(linked_list_7, linked_list_8))
print("")

# Test case 5 - same numbers
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [1, 1, 1, 1]
element_2 = [1, 1, 1, 1]
for i in element_1:
    linked_list_9.append(i)
for i in element_2:
    linked_list_10.append(i)

print("Test case 5: same number on both lists")
print("Union:", union(linked_list_9, linked_list_10))
print("Intersection:", intersection(linked_list_9, linked_list_10))
print("")
