# A palindrome is a word that is the reverse of itself—that is, it is the same word when read forwards and backwards.
# "madam" is a palindrome
# "abba" is a palindrome
# "cat" is not
# "a" is a trivial case of a palindrome

def is_palindrome(input_str):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input_str(str): input to be checked if it is palindrome
    """

    # Termination / Base condition
    if len(input_str) <= 1:
        return True
    else:
        first_char = input_str[0]
        last_char = input_str[-1]

        # substring is input with first and last char removed
        substring = input_str[1:-1]

        # recursive call, if first and last char are identical, else return False
        return (first_char == last_char) and is_palindrome(substring)
