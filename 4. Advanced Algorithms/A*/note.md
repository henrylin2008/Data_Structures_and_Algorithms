The route finding problem can be formulated as follows: <br>
<li><b>Initial state</b>, denoted by S0, is any state that can be designated as the starting point. </li>
<li><b>Actions</b>, denoted by: {a1, a2, a3, ...}, is a set of the possible actions available to the agent at any given state. </li>
<li><b>Results</b>, denoted by S', is the new stage where the agent ends up after taking an action at a given state. </li>
<li><b>Goal Test</b>, denoted by a boolean of True or False, checks whether the current state is the goal state. </li>
<li><b>Path Cost</b> is the sum of the cost of the individual steps. In the route finding problem, the cost could be the distance between two cities.</li>


### Route finding:
<li><b>Frontier</b>: farest point/s that has been explored</li>
<li><b>Explored</b>: area that has been visited</li>
<li><b>Unexplored</b>: area that has yet been visited </li>


### Uniform Cost
<li><b>Uniform Cost search</b> - expands out equally in all directions, may expend additional effort getting to a fairly direct path to the goal.</li>
<li><b>Greedy best-first search</b> - expands outward toward locations estimated as closer to the goal. If a direct path is available, 
expends much less effort than Uniform Cost; however, it does not consider any routes in which it may need to temporarily take a further away path in order to arrive at an overall shorter path.</li>
<li><b>A* Search</b> - utilizes both of these - will try to optimize with both the shortest path and the goal in mind. We'll see how this works in the next video.</li>


### A* Search
<b>Minimum value</b><br>
- f = g + h  <br>
- g(path) = path cost  <br>
- h (path) = h(s) = estimated distance to goal <br>

Result: search strategy that is the best possible. Finds the shortest length path while expanding minimum number of the 
paths possible <br>
- AKA: Best estimated total path cost first <br>

A* finds the lowest cost path if: 
- It depends on the h function
- h(s) < true cost
- h should never overestimate distance to goal
  - h is optimistic
  - h is admissible 