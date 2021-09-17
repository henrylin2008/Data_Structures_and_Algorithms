Given the requirement of the expected Time Complexity is O(log(n)), we'd have to use binary search; first, we need to find a midpoint between the current start and end point, 
then run power of 2 on the midpoint to check if it matches the target number; if it matches the target, then we just return the midpoint. 
Otherwise, we'd compare the midpoint power of 2 with the target number, then recursive run the same process on the left half or the right half of the midpoint, 
until we reach a number that's close to the target number. 

Time Complexity: <b>O(log(N))</b> <br>
Space Complexity: <b>O(1)</b>
