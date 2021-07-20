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

class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

