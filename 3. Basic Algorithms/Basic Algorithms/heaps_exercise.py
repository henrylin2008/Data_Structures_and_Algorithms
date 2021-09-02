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

