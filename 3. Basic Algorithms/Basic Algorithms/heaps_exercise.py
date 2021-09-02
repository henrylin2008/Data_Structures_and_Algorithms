# Priority Queues - Intuition
# Consider the following scenario -
#
# A doctor is working in an emergency wing at a hospital. When patients come in, a nurse checks their symptoms and
# based on the severity of the illness, sends them to the doctor. For e.g. a guy who has had an accident is sent
# before someone who has come with a runny nose. But there is a slight problem. There is only one nurse and only one
# doctor. In the amount of time nurse takes to check the symptoms, the doctor has to work alone with the patients,
# hurting their overall productivity.
#
# You are a ninja programmer. The doctor comes to you for help. Your job is to write a small software in which
# patients will enter their symptoms and will receive a priority number based on their illness. The doctor has given
# you a list of common ailments, and the priority in which he would prefer seeing them. How would you solve the
# priority problem?

# Priority Queues

# Like the name suggests, a priority queue is similar to a regular queue, except that each element in the queue has a
# priority associated with it. A regular queue is a FIFO data structure, meaning that the first element to be added
# to the queue is also the first to be removed.
#
# With a priority queue, this order of removal is instead based on the priority. Depending on how we choose to set up
# the priority queue, we either remove the element with the most priority, or an element of the least priority.
#
# For the sake of discussion, let's focus on removing the element of least priority for now.


# Functionality
# If we were to create a PriorityQueue class, what methods would it need to have?
#
# Here are the two key methods:
#
# insert - insert an element
# remove - remove an element
# And we can also add the same utility methods that we had in our regular Queue class:
#
# front - returns the element at the front of the queue
# size - returns the number of elements present in the queue
# is_empty - returns True if there are no elements in the queue, and False otherwise
# As part of this functionality, we will need a way of assigning priorities to the items.
#
# A very common way to solve the patient-doctor problem mentioned above would be to assign each ailment a priority.
# For e.g.
#
# * A running nose may be assigned priority 1
# * Fever may be assigned 2
# * Accident may get a priority 10
# You will find this theme recurring in all of programming. We use numbers to effectively represent data.
#
# For the sake of simplicity, let's only consider integers here. Let us assume a scenario where we get integers as
# input and we assign a priority on how large / small they are. Let us say the smaller the number, the smaller its
# priority. So, in our simplified version of the problem statement the value of the integer serves as a priority.
#
# Our goal is to create a queue where the element with the lowest priority is removed first. Therefore, the remove
# method will remove the smallest number from the priority queue. Thus, the largest number will be the last to be
# removed from the priority queue and the smallest number will be the first to be removed.
#
# How should we implement it?
# What we've described above is just the abstract characteristics that we expect from
# this data structure. As with stacks and queues (and other abstract data types), there is more than one way that we
# could implement our priority queue such that it would exhibit the above behaviors.
#
# However, not all implementations are ideal. When we implemented a regular queue earlier, you may remember the
# enqueue and dequeue methods had a time complexity of  𝑂(1) . Similarly, we would like the insert and remove
# methods on our priority queue to be fast.
#
# So, what underlying structure should we use to implement the priority queue such that it will be as efficient as
# possible? Let's look at some different structures and consider the pros and cons.

# Arrays

# Earlier, we saw that one way to implement a queue was by using an array. We could do a similar thing for priority
# queues. We could use the array to store our data.
#
# Insertion in an array is very fast. Unless the array is full, we can do it in O(1) time.
#
# Note: When the array is full, we will simply create a new array and copy all the elements from our old array to new
# array. It's exactly similar to what we do for our queue's implementation using arrays.
#
# What about removal? We always want to remove the smallest or highest priority data from the array, depending on if
# this is a max-heap or min-heap. In the worst case, we will have to search the entire array, which will take O(n)
# time. Thus, to remove the element, the time complexity would be O(n).
#
# This also creates an additional problem for us. The index from which we removed the element is now empty. We cannot
# leave empty indices in our array. Over the course of operations, we will be wasting a lot of space if we did that.
#
# Therefore, insertion no longer happens in O(1) time. Rather, every time we insert, we will have to look for these
# empty indices and put our new element in the first empty index we find. In the worst case, this also takes O(n)
# time. Therefore, our time complexity with arrays (for both insertion and removal) would be O(n).

# LinkedList
# Insertion is very easy in a linked list. If we maintain a variable to keep track of the tail of the
# linked list, then we can simply add a new node at this location. Thus, insertion takes O(1) time.
#
# For removal, we will have to traverse the entire list and find the smallest element, which will require O(n) time.
#
# Note that with linked lists, unlike arrays, we do not have to worry about empty indices.
#
# A linked linked certainly seems to be a better option than an array. Although they have the same time complexity
# for removal, the time complexity for insertion is better.
#
# HashMap
# The same problem lies in HashMap as well. We can insert in O(1) time. Although, we can remove an element from a
# HashMap in O(1) time but we have to first search for the smallest element in the map. This will again take O(n)
# time. Therefore, the time complexity of remove is O(n) for hashmaps.

# Binary Search Trees
# Binary Search Trees are laid out according to the value of the node that we want to insert. All elements greater
# than the root go to the right of the root, and all elements smaller than the root go to the left of the root.
#
# If we assume that our Binary Search tree is balanced, insertion would require O(h) time in the worst case.
# Similarly, removal would also require O(h) time. Here h is the height of the binary search tree.
#                   4
#                 /    \
#               2        7
#             /   \     /  \
#            1     3   5    8

# A Binary Tree is called a Balanced Binary Tree when the difference between the heights of it's left subtree and
# right subtree do not differ by more than one. Additionally, to be balanced, all the subtrees of the binary tree
# must also be balanced.
#
# For a balanced tree, we can safely approximate the height of the tree h to log(n). Thus, both insertion and removal
# require O(log(n)) time in a binary search tree.
#
# However, in the worst case, our binary search tree might just be a sequential list of nodes (stretching to the
# right or to the left). Consider the following tree:
#       1
#          \
#            2
#              \
#                3
#                  \
#                    4

# In such a scenario the binary search tree effectively turns into a linked list. In this case, the time complexity
# would be O(n)
#
# To avoid this situation, we would need a self-balancing tree which include additional complexity.
#
# We could use any of the above data structures to implement our priority queue—and they would work, in the sense
# that they would exhibit the outward behavior we expect in a priority queue.
#
# However, none of them acheived our goal of having  𝑂(1)  time complexity for both insert and remove. To do that,
# we will need to explore something new: A heap.
