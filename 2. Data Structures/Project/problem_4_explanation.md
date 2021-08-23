This problem is similar to problem 2, we don't know how deep of the groups is in the active directory, thus it makes 
sense to use recursion to solve this problem. Each time that we are at a folder, we would check if any group exists in 
the group; if so, we would recursively call the function, until we are reaching the base case, where there are only user
or no user in the group. 

<h3> Time Complexity: </h3>
<b>O(n)</b>; because we are using a for loop to loop through the subgroups. 

<h3> Space Complexity: </h3>
<b>O(n)</b>; The function checks if an user or group exists in the current user/group list, in the worse case, the
item that we are looking for is at the last in the list, thus it'd would be O(n)  