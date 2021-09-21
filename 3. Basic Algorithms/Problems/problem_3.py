# Rearrange Array Elements
# Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can
# assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by
# more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity
# is O(nlog(n)).
#
# for e.g. [1, 2, 3, 4, 5]
#
# The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when
# there are more than one possible answers, return any one.
#
# Here is some boilerplate code and test cases to start with:

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    middle_idx = len(input_list) // 2
    left = merge_sort(input_list[:middle_idx])
    right = merge_sort(input_list[middle_idx:])
    return merge(left, right)

def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] >= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged += left[left_idx:]
    merged += right[right_idx:]

    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    The expected time complexity is O(nlog(n))
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = merge_sort(input_list)  # sorted the input_list from the largest to the smallest with a merge sort
    even_idx_value = 0
    odd_idx_value = 0

    for idx, value in enumerate(sorted_list):  #
        if idx % 2 == 0:  # even indexes
            even_idx_value = even_idx_value * 10 + value    # add new value to the end of the existing even_idx_value
        else:  # odd indexes
            odd_idx_value = odd_idx_value * 10 + value
    return even_idx_value, odd_idx_value

def t_fn(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


print("Test Cases:")
print("Input: [1, 2, 3, 4, 5]; Output: [542, 31]: ", end='')
t_fn([[1, 2, 3, 4, 5], [542, 31]])
print("Input: [4, 6, 2, 5, 9, 8]; Output: [964, 852]: ", end='')
t_fn([[4, 6, 2, 5, 9, 8], [964, 852]])
