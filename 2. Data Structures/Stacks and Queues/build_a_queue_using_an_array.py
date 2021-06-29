# Implement a queue using an array

# Functionality
# Once implemented, our queue will need to have the following functionality:
#
# enqueue - adds data to the back of the queue
# dequeue - removes data from the front of the queue
# front - returns the element at the front of the queue
# size - returns the number of elements present in the queue
# is_empty - returns True if there are no elements in the queue, and False otherwise
# _handle_full_capacity - increases the capacity of the array, for cases in which the queue would otherwise overflow
class Queue:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0
