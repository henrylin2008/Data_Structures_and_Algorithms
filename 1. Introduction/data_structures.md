### List Methods:
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
