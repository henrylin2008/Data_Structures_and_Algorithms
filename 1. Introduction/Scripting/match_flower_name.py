# Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The
# main (separate) function should take user input (user's first name and last name) and parse the user input to
# identify the first letter of the first name. It should then use it to print the flower name with the same first
# letter (from dictionary created in the first function).
#
# Sample Output:
#
# >>> Enter your First [space] Last name only: Bill Newman
# >>> Unique flower name with the first letter: Bellflower
# function that creates a flower_dictionary from filename
def get_flowers(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            initial = line.split(": ")[0]
            flower = line.split(": ")[1].strip()
            flower_dict[initial] = flower
    return flower_dict


def main():
    """Prompts for user input, parses out the first letter of first name and print out corresponding flower"""
    flower_d = get_flowers("flowers.txt")
    name = input("Enter your first [space] Last name only: ")
    first_letter = name.title()[0]
    if flower_d[first_letter]:
        print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))


if __name__ == '__main__':
    main()
