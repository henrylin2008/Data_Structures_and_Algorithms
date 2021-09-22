# Dutch National Flag Problem
# Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to
# use any sorting function that Python provides.
#
# Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still
# be an O(n) solution but it will not count as single traversal.
#
# Here is some boilerplate code and test cases to start with:
#
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    idx = 0
    last_zero_idx = 0
    last_idx = len(input_list) - 1

    while idx <= last_idx:
        if input_list[idx] == 0:
            input_list[idx] = input_list[last_zero_idx]
            input_list[last_zero_idx] = 0
            last_zero_idx += 1
            idx += 1
        elif input_list[idx] == 2:
            temp_value = input_list[last_idx]
            input_list[last_idx] = 2
            input_list[idx] = temp_value
            last_idx -= 1
        else:
            idx += 1
    return input_list


def t_fn(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array, end=': ')
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


print("Test cases:")
t_fn([0, 0, 2, 2, 2, 0, 0, 1, 2, 0, 2])
t_fn([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
t_fn([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
