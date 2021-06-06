# String Methods
str1 = "Udacity"

print(len(str1))  # 7
print(str1.lower())  # udacity
print(str1.upper())  # UDACITY
print(str1[1:6])  # dacit
print(str1[:6])  # Udacit. A blank index means "all from that end"
print(str1[1:])  # dacity
print(str1[-6:-1])  # dacit
print(str1.replace('y', "B"))  # UdacitB

str2 = "    Udacity    "
print(str2.strip())  # Udacity

str3 = "Welcome, Constance!"
print(str3.split(","))  # ['Welcome', ' Constance!']

print(str3 + " " + str1)  # Welcome, Constance! Udacity
print(sorted(str3))  # [' ', '!', ',', 'C', 'W', 'a', 'c', 'c', 'e', 'e', 'e', 'l', 'm', 'n', 'n', 'o', 'o', 's', 't']


# Exercise 1: Reverse Strings
def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    new_string = ""
    for i in range(len(our_string)):
        new_string += our_string[(len(our_string) - 1) - i]
    return new_string


# Test Cases
print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")


# Exercise 2: Anagrams
def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other
    An anagram is a word (or phrase) that is formed by rearranging the letters of another word (or phrase).

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    # Clean strings and convert to lower case
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    # Compare the length of both strings
    if len(str1) == len(str2):
        # Sort each string and compare
        if sorted(str1) == sorted(str2):
            return True

    return False


# Test Cases
print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")  # Pass
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")  # Pass
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")  # Pass
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")  # Pass
print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")  # Pass


# Exercise 3: Reverse the words in sentence
def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): Strings to have individual words flip
    Returns:
       string: String with words flipped
    """

    word_list = our_string.split(" ")

    for idx in range(len(word_list)):
        word_list[idx] = word_list[idx][::-1]

    return " ".join(word_list)


# test cases
print("Pass" if ('retaw' == word_flipper('water')) else "Fail")    # Pass
print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")   # Pass
print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail") # Pass


