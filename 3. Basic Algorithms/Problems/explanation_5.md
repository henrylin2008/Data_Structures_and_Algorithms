Autocomplete with Tries is surrounding the development of the Trie data structure

### Insert Method: 
Inserting a new word into the Trie usually takes O(1) time; However in the worse case, when there's no word had any 
common prefix, then it'd take O(n) runtime. The space complexity for Insert method depends on the size of the words (n), 
and that requires n iterations, which resulted in O(n) space.  

* Time Complexity: <b>O(n)</b> <br>
* Space Complexity: <b>O(n)</b>

### Find Method:
The find method requires a runtime of O(n), as it needs to traverse the all the nodes in the worse case. No additional 
space needed, as we are not creating any new nodes.

* Time Complexity: <b>O(n)</b> <br>
* Space Complexity: <b>O(1)</b>

### Suffixes Method:
The Suffixes method runs recursively to check if the given character in its children, which it requires to run the
entire Trie nodes, thus its runtime is O(n); For the space complexity, we need a new list to store any new suffixes, n 
is the total number of words in the tree, then the space complexity is O(n). 

* Time Complexity: <b>O(n)</b> <br>
* Space Complexity: <b>O(n)</b>

### Overall:
The total time/space complexity of Trie/TrieNode classes is the sum of all above methods
* Time Complexity: O(n) + O(n) + O(n) = O(3n) ==> <b>O(n)</b> <br>
* Space Complexity: O(n) + O(1) + O(n) = O(2n + 1) ==> <b>O(n)</b>