# Least Recently Used Cache
# We have briefly discussed caching as part of a practice problem while studying hash maps.
#
# The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.
#
# While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however,
# the entry is not found, it is known as a cache miss.
#
# When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to
# add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put(
# ) operation to insert the new element. The remove operation should also be fast.
#
# For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An
# LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its
# limit. For the current problem, consider both get and set operations as an use operation.
#
# Your job is to use an appropriate data structure(s) to implement the cache.
#
# In case of a cache hit, your get() operation should return the appropriate value.
# In case of a cache miss, your get() should return -1.
# While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full,
# you must write code that removes the least recently used entry first and then insert the element.
# All operations must take O(1) time.
#
# For the current problem, you can consider the size of cache = 5.
#
# Here is some boiler plate code and some example test cases to get you started on this problem:
class DoubleLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = {}             # using a hashmap to store key and value
        self.current_size = 0
        self.list_head = None
        self.list_tail = None

    # O(1) time | O(1) space
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.set_head(node)
            return node.value
        return -1

    # O(1) time | O(n) space
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.current_size == self.capacity:
            self.remove_LRU()
        new_node = DoubleLinkedNode(value)
        self.cache[key] = new_node
        self.set_head(new_node)
        self.current_size += 1

    def remove_LRU(self):
        node = self.list_tail
        del self.cache[node.value]
        self.remove_node(node)
        self.current_size -= 1

    def remove_node(self, node):
        if node == self.list_head:  # case when the node is the head of the linked list
            self.list_head = self.list_head.previous
            self.list_head.next = None
        elif node == self.list_tail:    # case when the node is the tail of the linked list
            self.list_tail.next.previous = None
            self.list_tail = self.list_tail.next
        elif self.current_size == 1:
            self.list_head = None
            self.list_tail = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous

    def set_head(self, node):
        if self.list_head is None:
            self.list_head = node
            self.list_tail = node
        else:
            self.list_head.next = node
            node.previous = self.list_head
            if self.list_head.previous is None:
                self.list_head = self.list_head
            self.list_head = node


