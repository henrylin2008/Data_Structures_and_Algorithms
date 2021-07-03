# The factorial function is a mathematical function that multiplies a given number,  𝑛 , and all of the whole
# numbers from  𝑛  down to 1.
# n! = n * (n−1)!
# factorial(n) = n * factorial(n-1)

def factorial(n):
    """
    Calculate n!

    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    if n == 0:
        return 1  # by definition of 0!
    return n * factorial(n - 1)


print("Pass" if (1 == factorial(0)) else "Fail")    # Pass
print("Pass" if (1 == factorial(1)) else "Fail")    # Pass
print("Pass" if (120 == factorial(5)) else "Fail")  # Pass
