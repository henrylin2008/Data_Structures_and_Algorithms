### DFS - Depth First Search:
- Seen: mark a node has seen
- Stack: add unseen node to the Stack, if it's a seen node, go back to the previous node, and pop the last added item from the stack
- Repeat the process until all nodes have been marked as seen
- Recursive case: node has no unseen nodes 

Time Complexity:<b> O(|E| + |V|) </b> 
- E: number of edges; V: number of vertices 


### BFS - Breadth First Search:
- Seen: mark a node has seen
- Queue: add unseen node to the Stack, if it's a seen node, go back to the previous node, and remove the first item from the queue

Time Complexity:<b> O(|E| + |V|) </b> 
- E: number of edges; V: number of vertices 