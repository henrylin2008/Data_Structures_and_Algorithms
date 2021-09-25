This problem is an extension of the problem 5, instead of auto-complete check, we are checking on a given path. The 
Router class dealing with splitting the given path and add it to the handler, and perform lookup a given path. The 
add handler function requires O(n) runtime, as it needs to split the given path into a list, then insert all split 
paths into the route, which it needs O(n) space to store all the items. The lookup function runs in O(n) runtime in the 
worse case, as the lookup item could be the last item in the list, the space complexity for the lookup function is O(1), 
as it does not need to store any item, simply lookup and return the matched path. The overall time/space complexity
is summed up as the following:

* Time Complexity: <b>O(n)</b> <br>
* Space Complexity: <b>O(n)</b>
