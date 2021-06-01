# while loops are ideal when the iterations need to continue until a condition is met.

# Quiz: Count By
# Suppose you want to count from some number start_num by another number count_by until you hit a
# final number end_num. Use break_num as the variable that you'll change each time through the loop. For simplicity,
# assume that end_num is always larger than start_num and count_by is always positive.
#
# Before the loop, what do you want to set break_num equal to? How do you want to change break_num each time through
# the loop? What condition will you use to see when it's time to stop looping?
#
# After the loop is done, print out break_num, showing the value that indicated it was time to stop looping. It is
# the case that break_num should be a number that is the first number larger than end_num.
start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)    # 101


# Quiz: Nearest Square
# Write a while loop that finds the largest square number less than an integer limit and stores
# it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36
# is a square number because it equals 6*6.
#
# For example, if limit is 40, your code should set the nearest_square to 36.
limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)   # 36
