# In an encryption system where ASCII lower case letters represent numbers in the pattern a=1, b=2, c=3... and so on,
# find out all the codes that are possible for a given input number.
#
# Example 1
#
#   -number = 123
#   -codes_possible = ["aw", "abc", "lc"]
#
# Explanation: The codes are for the following number:
#
#   - 1 . 23 = "aw"
#   - 1 . 2 . 3 = "abc"
#   - 12 . 3 = "lc"
#
# Example 2
#
#   -number = 145
#   -codes_possible = ["ade", "ne"]
#
# Return the codes in a list. The order of codes in the list is not important.
#
# Note: you can assume that the input number will not contain any 0s

# Logic:
# -You can first break the number like: 1, 23 where 1 represents a and 23 represents w i.e it will return aw
# -You can also break the number as 1, 2, 3, where 1 represents a, 2 represents b and 3 will represents c, so, it will
# return abc.
# -Also, You can break it as 12, 3, where 12 represents l and 3 represents c i.e it will return lc.
#
# So, for number = 123the output will be codes_possible = ["aw", "abc", "lc"].

def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember:
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(number + 96)


def all_codes(number):
    if number == 0:
        return [""]

    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder = number % 100
    output_100 = list()
    # if 2 right-most digits <= 26 (ex: 123->23, 112->12) & recursive calls on the number
    if remainder <= 26 and number > 9:

        # get all codes for the remaining number
        output_100 = all_codes(number // 100)
        alphabet = get_alphabet(remainder)

        for index, element in enumerate(output_100):
            output_100[index] = element + alphabet

    # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    remainder = number % 10

    # get all codes for the remaining number
    output_10 = all_codes(number // 10)
    alphabet = get_alphabet(remainder)  # get the alphabet representation of the remainder

    for index, element in enumerate(output_10):
        output_10[index] = element + alphabet

    output = list()
    output.extend(output_100)
    output.extend(output_10)

    return output
