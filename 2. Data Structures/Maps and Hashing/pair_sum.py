# Problem statement

# Given an input_list and a target, return the pair of indices in the list that holds the values which sum to the
# target. For example,
#
# input_list = [1, 5, 9, 7] and target = 8, the answer would be [0, 3]
#
# Note
# 1.The best solution takes O(n) time. This means that you cannot traverse the given list more than once. Hint - Think
# of an additional data structure that you should use here.
# 2.You can assume that the list does not have any duplicates.
def pair_sum_to_target(input_list, target):
    # Create a dictionary.
    # Each element of the input_list would become a "key", and
    # the corresponding index in the input_list would become the "value"
    index_dict = dict()

    # Traverse through the input_list
    for index, element in enumerate(input_list):

        # `in` is the way to test for the existence of a "key" in a dictionary
        if (target - element) in index_dict:
            # Return the TWO indices that sum to the target
            return [index_dict[target - element], index]

        index_dict[element] = index

    return [-1, -1]  # If the target is not achieved
