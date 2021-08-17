To solve this problem, we need a combination of a hashmap and a double-linked list; the hashmap allowed for instant
retrieval of the node/key and the value; while double-linked list allowed fast operation time on the head/tail node, 
most recently used/least recently respectively, and shuffling the most recently used/head to the back of the 
double linked list. 

<h3> Time Complexity </h3>
-get(): <b>O(1)</b>; only conditional check, no loops, thus constant time </br>   
-set(): <b>O(1)</b>; only conditional check, no loops, thus constant time </br>
<h3> Space Complexity: </h3>
-get(): <b>O(1)</b>; only conditional check, no loops, constant time </br>
-set(): <b>O(n)</b>; space could get larger as the stored keys/values getting larger in the hashmap
