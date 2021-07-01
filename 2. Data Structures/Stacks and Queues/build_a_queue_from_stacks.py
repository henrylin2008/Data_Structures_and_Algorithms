# Build a Queue From Stacks
class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    def __init__(self):
        self.in_storage = Stack()  # for enqueue new items
        self.out_storage = Stack()  # for dequeue the first item

    def size(self):
        return self.out_storage.size() + self.in_storage.size()

    def enqueue(self, item):
        self.in_storage.push(item)

    def dequeue(self):
        if not self.out_storage.items:  # if out_storage is not empty
            while self.in_storage.items:  # while in_storage has items
                self.out_storage.push(self.in_storage.pop())
                # remove top item in in_storage and add it to out_storage
        return self.out_storage.pop()  # return top item from out_storage


# test cases
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
#
# # Test size
# print("Pass" if (q.size() == 3) else "Fail")    # Pass
#
# # Test dequeue
# print("Pass" if (q.dequeue() == 1) else "Fail")
# # initial in_storage: [1, 2, 3]  ==>    end of dequeue loop: []
# # initial out_storage: []        ==>    end of dequeue loop: [3, 2, 1]      => last item: 1
#
# # Test enqueue
# q.enqueue(4)
# print("Pass" if (q.dequeue() == 2) else "Fail")     # Pass
# # ini in_storage: [4]
# # ini out_storage: [3, 2]  => dequeue (2)
# print("Pass" if (q.dequeue() == 3) else "Fail")     # Pass
# print("Pass" if (q.dequeue() == 4) else "Fail")     # Pass
# q.enqueue(5)
# print("Pass" if (q.size() == 1) else "Fail")        # Pass

