# Implement a stack using an array
class Stack:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]  # create an array with all 0's
        self.next_index = 0
        self.num_elements = 0

    def push(self, data):
        """Add an item to the top of the stack"""
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()  # increase the array size

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    def pop(self):
        """removes an item from the top of the stack"""
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

    def size(self):
        """returns the size of the stack"""
        return self.num_elements

    def is_empty(self):
        """returns True if the stack is empty and False otherwise"""
        return self.num_elements == 0

    def _handle_stack_capacity_full(self):
        """double the original array size"""
        old_arr = self.arr

        self.arr = [0 for _ in range(2 * len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element
