# Search in a Rotated Sorted Array
# You are given a sorted array which is rotated at some random pivot point.
#
# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of
# O(log n).
#
# Example:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
#
# Here is some boilerplate code and test cases to start with:

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list or len(input_list) == 0:  # edge cases
        return -1

    left, right = 0, len(input_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if input_list[mid] == number:   # when the target number is the mid value, return the mid value
            return mid

        if input_list[left] <= input_list[mid]:     # first value <= mid value
            if input_list[left] <= number < input_list[mid]:    # if target number is on the left half (before mid)
                right = mid - 1
            else:           # if target number is right side of the mid point
                left = mid + 1
        else:       # first value > mid value
            if input_list[mid] < number <= input_list[right]:   # if target number is on the right half (after mid)
                left = mid + 1
            else:
                right = mid - 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(case):
    input_list = case[0]
    number = case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Test case
print("Regular Cases:")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[7, 8, 1, 2, 3, 4, 6], 5])
test_function([[7, 8, 1, 2, 3, 4, 6], 4])
print("")
# edge cases
print("Edge cases:")
test_function([[], -1])
test_function([[6], 0])
test_function([[], 2])

# Regular Cases:
# Pass
# Pass
# Pass
# Pass
# Pass
# Pass
# Pass
#
# Edge cases:
# Pass
# Pass
# Pass
