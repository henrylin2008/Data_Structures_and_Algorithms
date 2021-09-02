# Overview - Data Compression
#
# In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (
# data). The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender
# encodes the data, and the receiver decodes the encoded data. As part of this problem, you have to implement the
# logic for both encoding and decoding.
#
# A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a
# loss (lossy) or no loss (lossless) of information. The Huffman Coding is a lossless data compression algorithm. Let
# us understand the two phases - encoding and decoding with the help of an example.
#
# A. Huffman Encoding
# Assume that we have a string message AAAAAAABBBCCCCCCCDDEEEEEE comprising of 25 characters to
# be encoded. The string message can be an unsorted one as well. We will have two phases in encoding - building the
# Huffman tree (a binary tree), and generating the encoded data. The following steps illustrate the Huffman encoding:
#
# Phase I - Build the Huffman Tree
# A Huffman tree is built in a bottom-up approach.
#
# 1. First, determine the frequency of each character in the message. In our example, the following table presents the
# frequency of each character.
# (Unique) Character	Frequency
#             A	            7
#             B	            3
#             C	            7
#             D	            2
#             E	            6

# 2. Each row in the table above can be represented as a node having a character, frequency, left child,
# and right child. In the next step, we will repeatedly require to pop-out the node having the lowest frequency.
# Therefore, build and sort a list of nodes in the order lowest to highest frequencies. Remember that a list
# preserves the order of elements in which they are appended.
#
# We would need our list to work as a priority queue, where a node that has lower frequency should have a higher
# priority to be popped-out. The following snapshot will help you visualize the example considered above:
#
#
# Can you come up with other data structures to create a priority queue? How about using a min-heap instead of a
# list? You are free to choose from anyone.
#
# 3. Pop-out two nodes with the minimum frequency from the priority queue created in the above step.

# 4. Create a new node with a frequency equal to the sum of the two nodes picked in the above step. This new node
# would become an internal node in the Huffman tree, and the two nodes would become the children. The lower frequency
# node becomes a left child, and the higher frequency node becomes the right child. Reinsert the newly created node
# back into the priority queue.
#
# Do you think that this reinsertion requires the sorting of priority queue again? If yes, then a min-heap could be a
# better choice due to the lower complexity of sorting the elements, every time there is an insertion.
#
# 5. Repeat steps #3 and #4 until there is a single element left in the priority queue. The snapshots below present
# the building of a Huffman tree.
#
# 6. For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child. See the final Huffman
# tree for our example:
#
# Phase II - Generate the Encoded Data

# Based on the Huffman tree, generate unique binary code for each character of our string message. For this purpose,
# you'd have to traverse the path from root to the leaf node.
# (Unique) Character	Frequency	Huffman Code
#               D	        2	        000
#               B	        3	        001
#               E	        6	        01
#               A	        7	        10
#               C	        7	        11

# Points to Notice
#
# -Notice that the whole code for any character is not a prefix of any other code. Hence, the Huffman code is called a
# Prefix code.
# -Notice that the binary code is shorter for the more frequent character, and vice-versa.
# -The Huffman code is generated in such a way that the entire string message would now require a much lesser amount
# of memory in binary form.
# -Notice that each node present in the original priority queue has become a leaf node in the final Huffman tree.
#
# This way, our encoded data would be 1010101010101000100100111111111111111000000010101010101
#
# B. Huffman Decoding
# Once we have the encoded data, and the (pointer to the root of) Huffman tree, we can easily decode the encoded data
# using the following steps:
#
# 1.Declare a blank decoded string
# 2.Pick a bit from the encoded data, traversing from left to right.
# 3.Start traversing the Huffman tree from the root.
#    -If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the
#     current bit is 1.
#    -If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
# 4.Repeat steps #2 and #3 until the encoded data is completely traversed.

# You will have to implement the logic for both encoding and decoding in the following template. Also, you will need
# to create the sizing schemas to present a summary.

import sys
import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq, left_child=None, right_child=None):
        self.char = char
        self.freq = freq
        self.left = left_child
        self.right = right_child

    def __lt__(self, other):  # less than function
        if other is None:
            return False
        if not isinstance(other, Node):
            return False
        return self.freq < other.freq

    def __eq__(self, other):  # equal function
        if other is None:
            return False
        if not isinstance(other, Node):
            return False
        return self.freq == other.freq

    def __gt__(self, other):  # greater than function
        if other is None:
            return False
        if not isinstance(other, Node):
            return False
        return self.freq > other.freq


class HuffmanCoding:

    def __init__(self):
        self.min_heap = []
        self.codes = {}

    def create_codes(self, tree):  # create codes from the tree
        if tree.left is None and tree.right is None:
            return {tree.char: "0"}
        return self.create_codes_recursive(tree, "")

    def create_codes_recursive(self, root, current_node):
        if root is None:
            return {}
        if root.char is not None:
            self.codes[root.char] = current_node

        left_codes = self.create_codes_recursive(root.left, current_node + "0")
        right_codes = self.create_codes_recursive(root.right, current_node + "1")
        self.codes.update(left_codes)
        self.codes.update(right_codes)
        return self.codes

    def get_encoded_text(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text

    def huffman_encoding(self, data):
        # Edge cases
        if data == "" or data is None:
            return "", None

        # Create a dictionary to store characters frequency
        frequency_dict = defaultdict()
        for char in data:
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1

        # build a min heap queue, ordered from the smallest to the largest
        for key in frequency_dict:
            current_node = Node(key, frequency_dict[key])
            heapq.heappush(self.min_heap, current_node)

        # Build Huffman tree, merging 2 min nodes recursively
        while len(self.min_heap) > 1:
            min_node1 = heapq.heappop(self.min_heap)
            min_node2 = heapq.heappop(self.min_heap)
            merged_node = Node(None, min_node1.freq + min_node2.freq)  # merging of the 2 min nodes
            merged_node.left = min_node1  # left child
            merged_node.right = min_node2  # right child
            heapq.heappush(self.min_heap, merged_node)  # insert new node into the min_heap
        if len(self.min_heap) == 1:              # edge case when only one node left
            current_node = heapq.heappop(self.min_heap)
            new_node = Node(None, current_node.freq)
            new_node.left = current_node
            heapq.heappush(self.min_heap, new_node)

        tree = heapq.heappop(self.min_heap)
        codes = self.create_codes(tree)
        encoded_text = self.get_encoded_text(data)
        return encoded_text, tree

    def huffman_decoding(self, data, tree):
        decoded_text = ""
        if data == "":
            return decoded_text

        tree_node = tree
        for char in data:
            if char == '0':
                tree_node = tree_node.left
            elif char == '1':
                tree_node = tree_node.right
            if tree_node.char is not None:
                decoded_text += tree_node.char
                tree_node = tree
        return decoded_text


if __name__ == "__main__":
    huffman_coding = HuffmanCoding()
    count = 0
    test_sentences = ["The bird is the word", "", "a", "aaaaaa", "AAaaCCcc", "12342345"]
    sentence_desc = ["a regular sentence", "an empty string", "a single letter", "duplicate letters",
                     "duplicate upper and lower letters", "numbers"]

    for sentence in test_sentences:
        print(f"----- Test case {count + 1}: {sentence_desc[count]} -----\n")

        print(f"The size of the data is: {sys.getsizeof(sentence)}")
        print(f"The content of the data is: {sentence}\n")

        encoded_data, tree = huffman_coding.huffman_encoding(sentence)
        if encoded_data is not None and tree is not None:
            print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
            print(f"The content of the encoded data is: {encoded_data}\n")

            decoded_data = huffman_coding.huffman_decoding(encoded_data, tree)
            print(f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
            print(f"The content of the encoded data is: {decoded_data}\n")

        else:
            print("Invalid input or an empty string\n")

        count += 1
