class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    if self.head is None:
        self.head = Node(value)
        return

    new_head = Node(value)
    new_head.next = self.head
    self.head = new_head


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend


# Test prepend
# linked_list = LinkedList()
# linked_list.prepend(1)
# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"


def append(self, value):
    """ Append a value to the end of the list. """
    if self.head is None:
        self.head = Node(value)
        return

    node = self.head
    while node.next:
        node = node.next

    node.next = Node(value)


LinkedList.append = append

# # Test append - 1
# linked_list.append(3)
# linked_list.prepend(2)
# print(linked_list.to_list())  # [2, 1, 3]
# assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"


# Test append - 2
# linked_list = LinkedList()
# linked_list.append(1)     # [1]
# print(linked_list.to_list())
# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
# linked_list.append(3)     # [1, 3]
# print(linked_list.to_list())
# assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    if self.head is None:
        return None

    node = self.head
    while node:
        if node.value == value:
            return node
        node = node.next

    raise ValueError("Value not found in the list.")


LinkedList.search = search

# Test search
# linked_list.prepend(2)
# linked_list.prepend(1)
# linked_list.append(4)
# linked_list.append(3)
# print(linked_list.to_list())  # [1, 2, 1, 3, 4, 3]
# assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
# assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"


def remove(self, value):
    """ Remove first occurrence of value. """
    if self.head is None:
        return

    if self.head.value == value:
        self.head = self.head.next
        return

    node = self.head
    while node.next:
        if node.next.value == value:
            node.next = node.next.next
            return
        node = node.next

    raise ValueError("Value not found in the list.")


LinkedList.remove = remove

# Test remove
# linked_list.remove(1)     # [2, 1, 3, 4, 3]
# assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
# linked_list.remove(3)     # [2, 1, 4, 3]
# assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
# linked_list.remove(3)     # [2, 1, 4]
# assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

def pop(self):
    """ Return the first node's value and remove it from the list. """
    if self.head is None:
        return None

    node = self.head
    self.head = self.head.next

    return node.value


LinkedList.pop = pop

# Test pop
# value = linked_list.pop()
# print(linked_list.to_list())  # [1, 4]
# assert value == 2, f"list contents: {linked_list.to_list()}"
# assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"


def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
    if self.head is None:
        self.head = Node(value)
        return

    if pos == 0:
        self.prepend(value)
        return

    index = 0
    node = self.head
    while node.next and index <= pos:
        if (pos - 1) == index:
            new_node = Node(value)
            new_node.next = node.next
            node.next = new_node
            return

        index += 1
        node = node.next
    else:
        self.append(value)


LinkedList.insert = insert

# Test insert
# linked_list.insert(5, 0)
# print(linked_list.to_list())  # [5, 1, 4]
# assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
# linked_list.insert(2, 1)
# print(linked_list.to_list())  # [5, 2, 1, 4]
# assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
# linked_list.insert(3, 6)
# print(linked_list.to_list())  # [5, 2, 1, 4, 3]
# assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

