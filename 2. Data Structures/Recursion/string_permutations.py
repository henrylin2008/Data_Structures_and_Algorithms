# String Permutations
# Problem Statement
# Given an input string, return all permutations of the string in an array.
#
# Example 1:
# string = 'ab'
# output = ['ab', 'ba']

# Example 2:
# string = 'abc'
# output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
#
# The Idea
# Starting with a blank list, add each character of original input string at all possible positions.
#
#
# For example, take "abc" as the original string:
#
# 1.Start with a blank list() object. This is actually the last call of recursive function stack. Pick a character 'c'
# of original string, making the output as ['c']
#
# 2.Pick next character b of original input string, and place the current character at different indices of the each
# sub-string of previous output. We can make use of the sub-string of previous output, to create a new sub-string.
# Now, the output will become ['bc', 'cb'].
#
# 3.Pick next character a of original input string, and place the current character at different indices of the each
# sub-string of previous output. Now, the output will become ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']. .

def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    """
    return return_permutations(string, 0)

def return_permutations(string, index):
    # output to be returned
    output = list()

    # Termination / Base condition
    if index >= len(string):
        return [""]

    # Recursive function call
    small_output = return_permutations(string, index + 1)
    # Pick a character
    current_char = string[index]
    # Iterate over each sub-string available in the list returned from previous call
    for subString in small_output:
        # place the current character at different indices of the sub-string
        for index in range(len(small_output[0]) + 1):
            # Make use of the sub-string of previous output, to create a new sub-string.
            new_sub_string = subString[0: index] + current_char + subString[index:]
            output.append(new_sub_string)
    return output


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


