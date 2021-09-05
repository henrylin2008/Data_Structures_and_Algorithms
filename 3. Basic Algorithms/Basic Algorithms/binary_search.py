# Guess the number
# This notebook simulates a classic game where you have to guess a random number from within a certain range.
# Typically, you might have to guess a number from 1 to 10, and have three guesses to get the right answer.
#
# In this case, you'll need to guess a random number between 1 and 100, and you will have 7 tries.
#
# Try running it and playing a round or two. Notice that the game always tells you whether your guess was too high or
# too low. This information allows you to rule out some of the numbers (so that you don't waste time guessing those
# numbers).
#
# With this fact in mind, try to make your guesses in the most efficient way you can. Specifically, try to make
# guesses that rule out the largest number of possibilities each time.
import random


def guess_the_number(total_tries, start_range, end_range):
    if start_range > end_range:
        start_range, end_range = end_range, start_range

    random_number = random.randint(start_range, end_range)
    try_count = 0
    success_message = "Awesome! You guessed correctly"
    failure_message = "Sorry! No more retries left"
    miss_message = "Oops! That's incorrect"

    num_tries = 0
    while num_tries < total_tries:
        attempt = int(input("Guess the number: "))

        if attempt == random_number:
            print(success_message)
            return
        print(miss_message)
        if attempt < random_number:
            print("Go higher!")
        else:
            print("Go lower!")
        num_tries += 1
    print(failure_message)


total_tries = 7
start_range = 1
end_range = 100
guess_the_number(total_tries, start_range, end_range)


# Linear Search:
# We have no idea about the order of the words, so we simply have to flip through the pages, one by one,
# until we find the word we are looking for.

# What would the time complexity be for linear search?
# (Think about the worst case scenario, where the word you're looking for is on the last page of the dictionary.)
# O(n)

# Time Complexity for linear search? O(n)


# You're going to make your first guess about which page the word might be on. Then you'll open the dictionary and
# take a look to see if you're right.
#
# Which page should you look at first? (Assuming you want to find the word as quickly as possible.)
# The middle page (halfway through the dictionary)

# In summary:
# -Binary search is a search algorithm where we find the position of a target value by comparing the middle value
# with this target value.
# -If the middle value is equal to the target value, then we have our solution (we have found the position of our
# target value).
# -If the target value comes before the middle value, we look for the target value in the left half.
# -Otherwise, we look for the target value in the right half.
# -We repeat this process as many times as needed, until we find the target value.
