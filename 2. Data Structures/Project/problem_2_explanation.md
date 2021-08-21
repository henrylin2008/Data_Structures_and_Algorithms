I decided to use recursion for this problem, as we don't know how deep of each directory; the recursion would allow
us to recursive check on each directory and its subdirectories. Using an array/list to store files that's ending 
with the searching suffix, and return the list of the paths.

<h3> Time Complexity: </h3>
<b>O(df)</b>; d: number of directories, f: files in each directory; the function needs to check on each 
directories/subdirectories and the files in each directory  

<h3> Space Complexity: </h3>
<b>O(n)</b>; a list of files with searching suffix 