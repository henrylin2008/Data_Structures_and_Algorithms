# Max and Min in a Unsorted Array
# In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should
# run in O(n) time. Do not use Python's inbuilt functions to find min and max.
#
# Bonus Challenge: Is it possible to find the max and min in a single traversal?
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    if len(ints) == 1:
        return (ints[0], ints[0])

    min_val = ints[0]
    max_val = ints[0]

    for idx, value in enumerate(ints):
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return (min_val, max_val)


# Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
l2 = [i for i in range(-343, 100)]
random.shuffle(l2)

print("Test Cases")
print("Random values 1 <= 9:", end=' ')
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Random values -343 <= 99:", end=' ')
print("Pass" if ((-343, 99) == get_min_max(l2)) else "Fail")


print("\nEdge Cases:")
l3 = []
print("[]:", end=' ')
print("Pass" if (None is get_min_max(l3)) else "Fail")
l4 = [1]
print('[1]:', end=' ')
print("Pass" if ((1, 1) == get_min_max(l4)) else "Fail")
l4 = [0]
print('[0]:', end=' ')
print("Pass" if ((0, 0) == get_min_max(l4)) else "Fail")

# Output:
# Test Cases
# Random values 1 <= 9: Pass
# Random values -343 <= 99: Pass
#
# Edge Cases:
# []: Pass
# [1]: Pass
# [0]: Pass
