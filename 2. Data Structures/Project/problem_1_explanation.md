To solve this problem, I decided to use a combination of a hashmap and a double-linked list data structure. The hashmap 
allowed for instant retrieval of the node/key and the value; while double-linked list allowed fast operation on 
the head/tail node, most recently used/least recently used respectively, and shuffling the most recently used node/head 
to the tail of the double-linked list. 

<h3> Time Complexity </h3>
-get(): <b>O(1)</b>; only conditional check, no loops, thus constant time </br>   
-set(): <b>O(1)</b>; only conditional check, no loops, thus constant time </br>
<h3> Space Complexity: </h3>
-get(): <b>O(1)</b>; only conditional check, no loops, constant time </br>
-set(): <b>O(n)</b>; space could get larger as the stored keys/values getting larger in the hashmap
