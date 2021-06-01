# Quiz: Fruit Basket - Task 1
# You would like to count the number of fruits in your basket. In order to do this,
# you have the following dictionary and list of fruits. Use the dictionary and list to count the total number of
# fruits, but you do not want to count the other items in your basket.
#
# # You would like to count the number of fruits in your basket.
# # In order to do this, you have the following dictionary and list of
# # fruits.  Use the dictionary and list to count the total number
# # of fruits, but you do not want to count the other items in your basket.
#
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for fruit, count in basket_items.items():
    if fruit in fruits:
        result += count

print("There are {} fruits in the basket.".format(result))  # There are 23 fruits in the basket.


# Quiz: Fruit Basket - Task 3
# So, a couple of things about the above examples:
#
# It is a bit annoying having to copy and paste all the code to each spot - wouldn't it be nice to have a way to
# repeat the process without copying all the code? Don't worry! You will learn how to do this in the next lesson!
#
#
# It would be nice to keep track of both the number of fruits and other items in the basket.
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for fruit, count in basket_items.items():
    if fruit in fruits:
       fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))