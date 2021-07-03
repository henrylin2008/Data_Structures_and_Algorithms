# Recursion is a technique for solving problems where the solution to a particular problem depends on the solution to
# a smaller instance of the same problem.

# Let's look at the recursive function power_of_2, which calculates  2𝑛 .
def power_of_2(n):
    if n == 0:
        return 1

    return 2 * power_of_2(n - 1)


print(power_of_2(5))    # 32

