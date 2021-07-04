# Problem Statement
# You are given a non-negative number in the form of list elements. For example, the number 123
# would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.
#
# Example 1:
# input = [1, 2, 3]
# output = [1, 2, 4]

# Example 2:
# input = [1, 2, 9]
# output = [1, 3, 0]

# Example 3:
# input = [9, 9, 9]
# output = [1, 0, 0, 0]

def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits representing (x + 1)
    """
    # Base case
    if arr == [9]:
        return [1, 0]

    # A simple case, where we just need to increment the last digit
    if arr[-1] < 9:
        arr[-1] += 1

    # Case when the last digit is 9.
    else:
        '''Recursive call'''
        # We have used arr[:-1], that means all elements of the list except the last one.
        # Example, for original input arr=[1,2,9], we will pass [1,2] in next call.
        arr = add_one(arr[:-1]) + [0]
        # ex: [9, 9, 9]
        # [9, 9] + [0],  # recursive call
        # [9] + [0, 0]   # recursive call
        # [1, 0] + [0, 0] # base case + recursive call
    return arr

