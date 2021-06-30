# Build a queue using a linked list
#
# It's good to try implementing the same data structures in multiple ways. This helps you to better understand the
# abstract concepts behind the data structure, separate from the details of their implementation—and it also helps
# you develop a habit of comparing pros and cons of different implementations.
#
# With both stack and queues, we saw that trying to use arrays introduced some concerns regarding the time
# complexity, particularly when the initial array size isn't large enough and we need to expand the array in order to
# add more items.
#
# With our stack implementation, we saw that linked lists provided a way around this issue—and exactly the same thing
# is true with queues.

# Time Complexity:
# When we use `enqueue`, we simply create a new node and add it to the tail of the list. And when we
# `dequeue` an item, we simply get the value from the head of the list and then shift the `head` variable so that it
# refers to the next node over.
# Both of these operations happen in constant time—that is, they have a time-complexity of O(1).
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node  # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next  # shift the tail (i.e., the back of the queue)
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value  # copy the value to a local variable
        self.head = self.head.next  # shift the head (i.e., the front of the queue)
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


# tests:
# Setup
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
#
# # Test size
# print("Pass" if (q.size() == 3) else "Fail")    # Pass
#
# # Test dequeue
# print("Pass" if (q.dequeue() == 1) else "Fail")     # Pass
#
# # Test enqueue
# q.enqueue(4)
# print("Pass" if (q.dequeue() == 2) else "Fail")     # Pass
# print("Pass" if (q.dequeue() == 3) else "Fail")     # Pass
# print("Pass" if (q.dequeue() == 4) else "Fail")     # Pass
# q.enqueue(5)
# print("Pass" if (q.size() == 1) else "Fail")        # Pass
