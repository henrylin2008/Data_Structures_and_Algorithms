# Write a function that takes a queue as an input and returns a reversed version of it.
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

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def front(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def reverse_queue(queue):
    """
    Reverse the input queue

    Args:
       queue(queue),str2(string): Queue to be reversed
    Returns:
       queue: Reversed queue
    """
    stack = Stack()
    while not queue.is_empty():     # when queue is not empty
        stack.push(queue.dequeue())     # add first item of queue to the stack

    while not stack.is_empty():     # when (temp) stack is not empty
        queue.enqueue(stack.pop())      # add popped out/top item to the queue
    # ex: steps in ()
    #    given queue          temp stack              return queue
    #       1 (s1) head        4 (s4) (n1) top         4 (n1) head
    #       2 (s2)             3 (s3) (n2)             3 (n2)
    #       3 (s3)             2 (s2) (n3)             2 (n3)
    #       4 (s4) tail        1 (s1) (n4)             1 (n4)  tail
