class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:

    def __init__(self, initial_size=15):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31         # a prime numbers
        self.num_entries = 0
        self.load_factor = 0.7

    '''
     Separate chaining:
     In case of collision, the `put()` function uses the same bucket to store a linked list of key-value pairs. 
     Every bucket will have it's own separate chain of linked list nodes.
     '''

    def put(self, key, value):  # The key is a string, and value is numeric
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)  # Create a node
        head = self.bucket_array[
            bucket_index]  # Create a reference that points to the existing bucket at position bucket_index

        # Check if key is already present in the map, and UPDATE it's value
        # Remember, a key should always be unique.
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        '''
        If the key is a new one, hence not found in the chain (LinkedList), then following two cases arise:
         1. The key has generated a new bucket_index
         2. The key has generated an existing bucket_index. 
            This event is a Collision, i.e., two different keys have same bucket_index.

        In both the cases, we will prepend the new node (key, value) at the beginning (head) of the chain (LinkedList).
        Remember that each `bucket` at position `bucket_index` is actually a chain (LinkedList) with 1 or more nodes.  
        '''
        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node  # Prepend the new node in the beginning of the linked list
        self.num_entries += 1

        # check for load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()

    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    # Returns the bucket_index
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index     # The returned hash code will be the bucket_index

    # Returns the hash code
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)    # length of array to be used in Mod operation
        current_coefficient = 1      # represents (self.p^0) which is 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets  # compress hash_code (Mod operation)
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets  # compress coefficient
        return hash_code % num_buckets  # one last compression before returning

    def size(self):
        return self.num_entries

    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]

        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.put(key, value)  # we can use our put() method to rehash
                head = head.next

    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]

        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next

    # Helper function to see the hashmap
    def __repr__(self):
        output = "\nLet's view the hash map:"

        node = self.bucket_array
        for bucket_index, node in enumerate(self.bucket_array):
            if node is None:
                output += '\n[{}] '.format(bucket_index)
            else:
                output += '\n[{}]'.format(bucket_index)
                while node is not None:
                    output += ' ({} , {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next

        return output


# Test the collision resolution technique
hash_map = HashMap()

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)       # Collision: The key "three" will generate the same bucket_index as that of the key "two"
hash_map.put("neo", 11)        # Collision: The key "neo" will generate the same bucket_index as that of the key "one"

print("size: {}".format(hash_map.size()))   # size: 4

print("one: {}".format(hash_map.get("one")))    # one: 1
print("neo: {}".format(hash_map.get("neo")))    # neo: 11
print("three: {}".format(hash_map.get("three")))    # three: 3

hash_map                          # call to the helper function to see the hashmap
# Let's view the hash map:
# [0]
# [1]
# [2] (neo , 11)  -->  (one , 1)
# [3]
# [4]
# [5]
# [6] (three , 3)  -->  (two , 2)
# [7]
# [8]
# [9]


# Test Rehashing
# We have reduced the size of the hashmap array to increase the load factor (> 0.7)
# and hence trigger the rehash() function
hash_map = HashMap(5)

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))   # size: 4


print("one: {}".format(hash_map.get("one")))    # one: 1
print("neo: {}".format(hash_map.get("neo")))    # neo: 11
print("three: {}".format(hash_map.get("three")))    # three: 3
print("size: {}".format(hash_map.size()))       # size: 4

hash_map                          # call to the helper function to see the hashmap
# Let's view the hash map:
# [0]
# [1]
# [2] (one , 1)  -->  (neo , 11)
# [3]
# [4]
# [5]
# [6] (two , 2)  -->  (three , 3)
# [7]
# [8]
# [9]


# Test delete operation
hash_map = HashMap(7)

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))   # size: 4

print("one: {}".format(hash_map.get("one")))    # one: 1
print("neo: {}".format(hash_map.get("neo")))    # neo: 11
print("three: {}".format(hash_map.get("three")))    # three: 3
print("size: {}".format(hash_map.size()))       # size: 4
hash_map                          # call to the helper function to see the hashmap

hash_map.delete("one")
hash_map                          # call to the helper function to see the hashmap

print(hash_map.get("one"))    # None
print(hash_map.size())        # 3
