# Problem Statement
# You have been given an array of length = n. The array contains integers from 0 to n - 2. Each
# number in the array is present exactly once except for one number which is present twice. Find and return this
# duplicate number present in the array
#
# Example:
#
# arr = [0, 2, 3, 1, 4, 5, 3]
# output = 3 (because 3 is present twice)
# The expected time complexity for this problem is O(n) and the expected space-complexity is O(1).

# own solution: use a dictionary to store the values from the array; if the occurrence of the value more than once, then
# return the value that has appeared more than once.
def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    arr_dict = {}
    for i in arr:
        if i not in arr_dict:
            arr_dict[i] = 1
        else:
            arr_dict[i] += 1
            return i

