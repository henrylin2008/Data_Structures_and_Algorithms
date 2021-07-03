# Recursion is a technique for solving problems where the solution to a particular problem depends on the solution to
# a smaller instance of the same problem.

# Let's look at the recursive function power_of_2, which calculates  2𝑛 .
def power_of_2(n):
    if n == 0:
        return 1

    return 2 * power_of_2(n - 1)


print(power_of_2(5))    # 32

# Implement sum_integers(n) to calculate the sum of all integers from  1  to  𝑛  using recursion. For example,
# sum_integers(3) should return  6  ( 1+2+3 ).
def sum_integers(n):
    if n == 1:
        return 1

    return n + sum_integers(n - 1)


print(sum_integers(3))  # 6


# Slicing the array with recursion
# Time: O(k *n); k: number of elements to copy; polynomial
# Space: O(k * n)
def sum_array(array):
    # Base Case
    if len(array) == 1:
        return array[0]

    return array[0] + sum_array(array[1:])


arr = [1, 2, 3, 4]
print(sum_array(arr))   # 10


# Time: linear
def sum_array_index(array, index):
    # Base Cases
    if len(array) - 1 == index:
        return array[index]

    return array[index] + sum_array_index(array, index + 1)


arr = [1, 2, 3, 4]
print(sum_array_index(arr, 0))


# Iterative
def sum_array_iter(array):
    result = 0

    for x in array:
        result += x

    return result


arr = [1, 2, 3, 4]
print(sum_array_iter(arr))
