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
        value = self.head.value          # copy the value to a local variable
        self.head = self.head.next       # shift the head (i.e., the front of the queue)
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


