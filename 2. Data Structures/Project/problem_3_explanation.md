I decided to use a dictionary to store characters and its frequencies for fast retrieval, then building a min heap to 
retrieve first 2 minimal nodes recursively, and create a new merged node from the 2 minimum nodes recursively, until we 
reach to the end of the character frequency dictionary. Then we build code recursively from popped out nodes of the 
min heap, and replace characters with code and return it. The time complexity for most functions are O(n), however the
encoding function is O(nLogn).

<h2>Encoding:</h2>
<h3>Time Complexity: </h3>
<b>O(nLogn)</b>; Most operations take O(n), min heap takes O(Logn), thus encoding takes O(nLogn)

<h3> Space Complexity: </h3>
<b>O(n)</b>; space is based off the given string

<h2>Decoding:</h2>
<h3>Time Complexity: </h3>
<b>O(n)</b>; Looping through every character from the given takes O(n)

<h3> Space Complexity: </h3>
<b>O(1)</b>; one variable to store and return  
