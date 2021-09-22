The requirement for this problem is the time complexity must be O(n); Since the given array only contains values of
0, 1, 2, we can use a few pointers to move around the values at the current/last index while moving along the index,
move any 0's to the front of the given array, and move any 2's to the end of the array, that leaves any 1's in the
between. since we are doing in-place swapping values (no new list needed), thus the space complexity is O(1).

Time Complexity: <b>O(n)</b> <br>
Space Complexity: <b>O(1)</b>