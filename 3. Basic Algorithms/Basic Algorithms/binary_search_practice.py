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
