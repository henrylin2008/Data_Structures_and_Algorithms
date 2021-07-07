# Keypad Combinations
# A keypad on a cellphone has alphabets for all numbers between 2 and 9, as shown in the figure below:
#
# You can make different combinations of alphabets by pressing the numbers.
#
# For example, if you press 23, the following combinations are possible:
#
# ad, ae, af, bd, be, bf, cd, ce, cf
#
# Note that because 2 is pressed before 3, the first letter is always an alphabet on the number 2. Likewise,
# if the user types 32, the order would be
#
# da, db, dc, ea, eb, ec, fa, fb, fc
#
# Given an integer num, find out all the possible strings that can be made using digits of input num. Return these
# strings in a list. The order of strings in the list does not matter. However, as stated earlier, the order of
# letters in a particular string matters.

def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


# Recursive Solution
def keypad(num):
    # Base case
    if num <= 1:
        return [""]

    # If `num` is single digit, get the LIST having one element - the associated string
    elif 1 < num <= 9:
        return list(get_characters(num))

    # Otherwise `num` >= 10. Find the unit's (last) digits of `num`
    last_digit = num % 10

    '''Step 1'''
    # Recursive call to the same function with “floor” of the `num//10`
    small_output = keypad(num // 10)  # returns a LIST of strings; returns from the previous (recursive) output

    '''Step 2'''
    # Get the associated string for the `last_digit`
    keypad_string = get_characters(last_digit)  # returns a string

    '''Permute the characters of result obtained from Step 1 and Step 2'''
    output = list()

    '''
    The Idea:
    Each character of keypad_string must be appended to the 
    end of each string available in the small_output
    '''
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            output.append(new_item)

    return output  # returns a LIST of strings
