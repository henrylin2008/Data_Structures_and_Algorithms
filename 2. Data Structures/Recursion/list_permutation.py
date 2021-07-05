# Question - Let's use recursion to help us solve the following permutation problem:
#
# Given a list of items, the goal is to find all of the permutations of that list. For example,
# Given a list like: [0, 1, 2]
# Permutations: [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
#
# Notice that the expected output is a list of permutation with each permuted item being represented by a list. Such
# an object that contains other object is called "compound" object.

# The Idea
# Build a compoundList incrementally starting with a blank list, and permute (add) each element of original input
# list at all possible positions.
#
# For example, take [0, 1, 2] as the original input list:
#
# 1. Start with a blank compoundList [[]]. This is actually the last call of recursive function stack. Pick the element
# 2 of original input list, making the compoundList as [[2]]
#
# 2. Pick next element 1 of original input list, and add this element at position 0, and 1 for each list of previous
# compoundList. We will require to create copy of all lists of previous compoundList, and add the new element. Now,
# the compoundList will become [[1, 2], [2, 1]].
#
# 3. Pick next element 0 of original input list, and add this element at position 0, 1, and 2 for each list of previous
# compoundList. Now, the compoundList will become [[0, 1, 2], [1, 0, 2], [1, 2, 0], [0, 2, 1], [2, 0, 1], [2, 1, 0]] .

# Recursive Solution
"""
Args: myList: list of items to be permuted
Returns: compound list: list of permutation with each permuted item being represented by a list
"""
import copy  # We will use `deepcopy()` function from the `copy` module


def permute(input_list):
    # a compound list
    final_compound_list = []  # compoundList to be returned

    # Termination / Base condition
    if len(input_list) == 0:
        final_compound_list.append([])

    else:
        first_element = input_list[0]  # Pick one element to be permuted
        after_first = slice(1, None)  # `after_first` is an object of type 'slice' class
        rest_list = input_list[after_first]  # convert the `slice` object into a list

        # Recursive function call
        sub_compound_list = permute(rest_list)

        # Iterate through all lists of the compoundList returned from previous call
        for a_list in sub_compound_list:
            # Permuted the `first_element` at all positions 0, 1, 2 ... len(a_list) in each iteration
            for j in range(0, len(a_list) + 1):
                # A normal copy/assignment will change a_list[j] element
                b_list = copy.deepcopy(a_list)

                # A new list with size +1 as compared to a_list
                # is created by inserting the `first_element` at position j in b_list
                b_list.insert(j, first_element)

                # Append the newly created list to the final_compound_list
                final_compound_list.append(b_list)

    return final_compound_list
