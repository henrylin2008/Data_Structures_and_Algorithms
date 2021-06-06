# String Methods
str1 = "Udacity"

print(len(str1))	    # 7
print(str1.lower())		# udacity
print(str1.upper())		# UDACITY
print(str1[1:6]) 		# dacit
print(str1[:6])			# Udacit. A blank index means "all from that end"
print(str1[1:])			# dacity
print(str1[-6:-1])		# dacit
print(str1.replace('y', "B"))   # UdacitB

str2 = "    Udacity    "
print(str2.strip())		# Udacity

str3 = "Welcome, Constance!"
print(str3.split(","))      # ['Welcome', ' Constance!']

print(str3 + " " + str1)    # Welcome, Constance! Udacity
print(sorted(str3))  # [' ', '!', ',', 'C', 'W', 'a', 'c', 'c', 'e', 'e', 'e', 'l', 'm', 'n', 'n', 'o', 'o', 's', 't']


# Reverse Strings
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

