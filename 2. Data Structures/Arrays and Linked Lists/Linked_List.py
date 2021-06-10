# Create a Node class with value and next attributes
# Use the class to create the head node with the value 2
# Create and link a second node containing the value 1
# Try printing the values (1 and 2) on the nodes you created (to make sure that you can access them!)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(2)
head.next = Node(1)

print(head.value)
print(head.next.value)

# Step 3. Write a function that loops through the nodes of the list and prints all of the values
def print_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


print_linked_list(head)     # 2, 1, 4, 3, 5


# Step 4. See if you can write the code for the create_linked_list function below
# -The function should take a Python list of values as input and return the head of a linked list that has those values
# runtime: O(n^2); due to for and while loops
def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            current_node = head
            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(value)

    return head

# better version of linked list: O(n) time
def create_linked_list_better(input_list):
    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head

        else:
            tail.next = Node(value)
            tail = tail.next
    return head


# Single Linked Lists:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):
        """Converts a linked list to a list"""
        new_list = []

        node = self.head
        while node:
            new_list.append(node.value)
            node = node.next

        return new_list


# Double Linked Lists
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        # Move to the tail (the last node)
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return


# Circular Linked Lists
# Circular linked lists occur when the chain of nodes links back to itself somewhere. For example
# NodeA -> NodeB -> NodeC -> NodeD -> NodeB is a circular list because NodeD points back to NodeB creating a loop
# NodeB -> NodeC -> NodeD -> NodeB.

