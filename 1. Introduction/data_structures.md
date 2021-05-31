### List Methods:
- Constructor: [] or list()
- Ordered: Yes 
- Mutable: Yes  
- len() returns how many elements are in a list.
- max() returns maximum elements in the list
    - if number: return maximum number
    - if string: return last string if it's sorted alphabetically
- min() returns the smallest element in the list 
- sorted() returns a copy of a list in order from smallest to largest, leaving the list unchanged
- join: Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list 
  elements joined by a separator string.
    - ex: new_str = "\n".join(["fore", "aft", "starboard", "port"])
        - fore 
        - aft 
        - starboard 
        - port
- append: adds an element to the end of a list.
    - letters = ['a', 'b', 'c', 'd']
    - letters.append('z')
    - print(letters)
        - ['a', 'b', 'c', 'd', 'z']


### Tuples
- data type for immutable ordered sequences of elements
- Constructor: ( ) or tuple()
- Ordered: Yes
- Mutable: No  
- can be indexed and sliced like a list  
- Tuple unpacking
    - dimensions = 52, 40, 100
    - length, width, height = dimensions


### Sets: 
- mutable unordered collections of unique elements
- Constructor: {1,2,3} or set(); {} creates an empty dictionary  
- Ordered: No
- Mutable: Yes
- add(): add an element to a set (in random order)
- pop(): remove a random element from a set
- set(): define an empty set  
    - ex: fruit = {"apple", "banana", "orange"}  # define a set


### Dictionaries:
- a mutable data type that stores mappings of unique keys to values
- Constructor: { } or dict()
- Ordered: No
- Mutable: No; Dictionary itself is mutable, but individual keys must be immutable
- Dictionaries can have keys of any immutable type, like integers or tuples, not just strings.
    - dict_example = {key1: value1, key2: value2, key3: value3}  # define a dictionary
- is: evaluates if both sides have the same identity
- is not: evaluates if both sides have different identities
- get(): looks up values in a dictionary; 
    - key not found: returns None
- dict(): define an empty dictionary     
    