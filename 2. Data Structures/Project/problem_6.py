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


def union(llist_1, llist_2):
    # Return the set of elements which are in A, in B, or in both A and B.
    union_set = set()

    current_node = llist_1.head
    while current_node:
        union_set.add(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node:
        union_set.add(current_node.value)
        current_node = current_node.next

    union_list = LinkedList()
    for item in union_set:
        union_list.append(item)

    return union_list


def intersection(llist_1, llist_2):
    # return the set of all objects that are members of both the sets A and B
    set1 = set()
    current_node = llist_1.head
    while current_node:
        set1.add(current_node.value)
        current_node = current_node.next

    set2 = set()
    current_node = llist_2.head
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

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
