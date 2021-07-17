# Problem statement
# Given an array arr and a target element target, find the last index of occurrence of target in arr
# using recursion. If target is not present in arr, return -1.
#
# For example:
#
# For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 5, output = 6
#
# For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 7, output = -1

def last_index(arr, target):
    # we start looking from the last index
    return last_index_arr(arr, target, len(arr) - 1)


def last_index_arr(arr, target, index):
    if index < 0:
        return -1

    # check if target is found
    if arr[index] == target:
        return index

    # else make a recursive call to the rest of the array
    return last_index_arr(arr, target, index - 1)