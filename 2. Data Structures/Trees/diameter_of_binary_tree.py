# Problem statement
# Given the root of a binary tree, find the diameter.
#
# Note: Diameter of a Binary Tree is the maximum distance between any two nodes

# You can use the following function to test your code with custom test cases. The function
# convert_arr_to_binary_tree takes an array input representing level-order traversal of the binary tree.
#                       1
#                     /   \
#                    2     3
#                   /     /
#                  4     5
#
# The above tree would be represented as arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
#
# Notice that the level order traversal of the above tree would be [1, 2, 3, 4, 5].
#
# Note the following points about this tree:

# -None represents the lack of a node. For example, 2 only has a left node; therefore, the next node after 4 (in
# level order) is represented as None
#
# -Similarly, 3 only has a left node; hence, the next node after 5 (in level order) is represted as None.

# -Also, 4 and 5 don't have any children. Therefore, the spots for their children in level order are represented by
# four None values (for each child of 4 and 5).
from queue import Queue

class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def diameter_of_binary_tree(root):
    return diameter_of_binary_tree_func(root)[1]

def diameter_of_binary_tree_func(root):
    """
    Diameter for a particular BinaryTree Node will be:
        1. Either diameter of left subtree
        2. Or diameter of a right subtree
        3. Sum of left-height and right-height
    :param root:
    :return: [height, diameter]
    """
    # Base case: Tree is empty
    if root is None:
        return 0, 0

    # recursive calls on the left subtree
    left_height, left_diameter = diameter_of_binary_tree_func(root.left)
    # recursive calls on the right subtree
    right_height, right_diameter = diameter_of_binary_tree_func(root.right)

    # current height, +1 to include visited node
    current_height = max(left_height, right_height) + 1
    height_diameter = left_height + right_height
    current_diameter = max(left_diameter, right_diameter, height_diameter)
    return current_height, current_diameter


def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree
    """
    index = 0
    length = len(arr)

    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1

        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)

        right_child = arr[index]
        index += 1

        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root

