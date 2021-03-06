# Breadth First Search: visits the tree one level at a time
# BFS ex:
#               apple
#             /       \
#          banana     cherry
#          /
#        dates

# 1) start at the root node
# 2) visit the root node's left child (banana), then right child (cherry)
# 3) visit the left and right children of (banana) and (cherry)

class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

from collections import deque


class Queue:
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


q = Queue()
q.enq("apple")
q.enq("banana")
q.enq("cherry")
print(q)

# <enqueue here>
# _________________
# cherry
# _________________
# banana
# _________________
# apple
# _________________
# <dequeue here>


def bfs(tree):
    q = Queue()  # queue
    visit_order = list()    # visit_order
    node = tree.get_root()  # start at root
    q.enq(node)     # add root to queue
    while len(q) > 0:   # while queue is not empty
        node = q.deq()  # dequeue the node
        visit_order.append(node)    # visit that node
        if node.has_left_child():   # add left child if exists
            q.enq(node.get_left_child())
        if node.has_right_child():  # add right child if exists
            q.enq(node.get_right_child())
    return visit_order      # [Node(apple), Node(banana), Node(cherry), Node(dates)]


# Define the print function for the Tree class. Nodes on the same level are printed on the same line.
#
# For example, the tree we've been using would print out like this:
#
# Node(apple)
# Node(banana) | Node(cherry)
# Node(dates) | <empty> | <empty> | <empty>
# <empty> | <empty>

class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while len(q) > 0:
            node, level = q.deq()
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))
            if node.has_right_child():
                q.enq((node.get_right_child(), level+1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:  # if level is the same
                s += " | " + str(node)   # keep it on the same row
            else:
                s += "\n " + str(node)   # add new line
                previous_level = level
        return s
