# Binary Search Practice
# Let's get some practice doing binary search on an array of integers. We'll solve the problem two different
# ways—both iteratively and recursively.
#
# Here is a reminder of how the algorithm works:
#
# Find the center of the list (try setting an upper and lower bound to find the center)
# Check to see if the element at the center is your target.
# If it is, return the index.
# If not, is the target greater or less than that element?
# If greater, move the lower bound to just above the current center
# If less, move the upper bound to just below the current center

# Repeat steps 1-6 until you find the target or until the bounds are the same or cross (the upper bound is less than
# the lower bound).
# Problem statement:
# Given a sorted array of integers, and a target value, find the index of the
# target value in the array. If the target value is not present in the array, return -1.
#
# Iterative solution
# First, see if you can code an iterative solution (i.e., one that uses loops). If you get stuck, the solution is below.
def binary_search(array, target):
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2  # integer division in Python 3

        mid_element = array[mid_index]

        if target == mid_element:  # we have found the element
            return mid_index

        elif target < mid_element:  # the target is less than mid element
            end_index = mid_index - 1  # we will only search in the left half

        else:  # the target is greater than mid element
            start_index = mid_element + 1  # we will search only in the right half

    return -1

def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)