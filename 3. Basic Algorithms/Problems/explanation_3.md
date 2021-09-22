The required runtime for this problem is O(nlog(n)); among all the sorting algorithms, only the merge sort met this 
requirement, thus merge sort is been used to solve this problem.
The process is divide and conquer, split out the given array until it reaches the base case (single element), then 
compare two neighbor elements and sort it out, and then merge into one sorted array. The array is sorted from the 
largest to the smallest values, and the sum of the first and second digit would produce the largest sum. 
Sorting the list requires O(n) time, and O(log(n)) time for the height of the (merge) sorting process, thus the total
runtime is O(n Log(n)); We need to create a new list to store sorted items, thus that's O(n) space. 

Time Complexity: <b>O(n log(N))</b> <br>
Space Complexity: <b>O(n)</b>