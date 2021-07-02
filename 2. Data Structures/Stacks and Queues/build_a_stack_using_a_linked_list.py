# Implement a stack using a linked list
# Time Complexity:
# pop and push have a time complexity of O(1).
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):  # Time: O(1)
        # create a new Node object with this value and link it to the list
        # add new items at the head of the stack, not the tail!
        # Once a new node is added, then increment num_elements
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head  # place the new node at the head of the linked list (top)
            self.head = new_node

        self.num_elements += 1

    def pop(self):  # Time: O(1)
        # Check if the stack is empty and, if it is, return None
        # Get the value from the head node and put it in a local variable
        # Move the head so that it refers to the next item in the list
        # Return the value we got earlier
        if self.is_empty():
            return

        value = self.head.value  # copy data to a local variable
        self.head = self.head.next  # move head pointer to point to next node (top is removed by doing so)
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


# Tests
# # Setup
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)
# stack.push(50)

# # Test size
# print("Pass" if (stack.size() == 5) else "Fail")    # Pass
#
# # Test pop
# print("Pass" if (stack.pop() == 50) else "Fail")    # Pass
#
# # Test push
# stack.push(60)
# print("Pass" if (stack.pop() == 60) else "Fail")    # Pass
# print("Pass" if (stack.pop() == 40) else "Fail")    # Pass
# print("Pass" if (stack.pop() == 30) else "Fail")    # Pass
# stack.push(50)
# print("Pass" if (stack.size() == 3) else "Fail")    # Pass
