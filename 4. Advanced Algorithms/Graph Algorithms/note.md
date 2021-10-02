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


### Dijkstra's algorithm: 
- Time: <b>O(|v|^2)</b>; In worst case, visit every node once or twice, every time we visit, we need to find the minimum element 

- Optimal Time: <b> O(|E| + |V|log(|V|)) </b>

-note: <br>
Dijkstra's algorithm can solve the single-source shortest path only when the edges have non-negative weights. In other words, Dijkstra's algorithm can not work if: <br>
1. There are edges with negative weights.
2. There are negative cycles (in directed graphs). A negative cycle is one that has negative weights. It can reduce the cost of the "shortest path" every time the cycle is traversed. However, the algorithm works fine with positive cycles.