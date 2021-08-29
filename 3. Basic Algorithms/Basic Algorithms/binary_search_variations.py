# # Variations on Binary Search
#
# Now that you've gone through the work of building a binary search function, let's take some time to try out a few
# exercises that are variations (or extensions) of binary search. We'll provide the function for you to start:
def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source) - 1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center + 1:], left + center + 1)
    else:
        return recursive_binary_search(target, source[:center], left)


# Find First
# The binary search function is guaranteed to return an index for the element you're looking for in an
# array, but what if the element appears more than once?
#
# Consider this array:
#
# [1, 3, 5, 7, 7, 7, 8, 11, 12]
#
# Let's find the number 7:
multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12]
recursive_binary_search(7, multiple)  # 4
