As the problem states the requirement runtime is O(log(n)), thus I would need to use the binary search. With a binary 
search data structure, it reduces the size in half on each iteration (O(log(n)) runtime), and the algorithm would 
repeatedly update its left/right point based off the conditions. For space complexity, since we are not creating any new 
array/list, but modifying the pointers, then it is O(1).

Time Complexity: <b>O(log(N))</b> <br>
Space Complexity: <b>O(1)</b>