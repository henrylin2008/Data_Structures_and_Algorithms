<h3>Summary</h3>

Divide and Conquer approach is suitable to solve a <b>big (scale) problem</b> by breaking it into smaller sub-problems, where each sub-problem looks exactly similar to the original problem. In general, there are three phases:

1. Divide - Break the given problem into smaller sub-problems
2. Conquer - Solve each sub-problem using recursion. The smallest sub-problem (base case) would have a simple straightforward solution.
3. Combine - This phase will automatically execute as a part of the recursion call stack, which combines the solution of smaller sub-problems to generate the final solution.

Quicksort and Mergesort are a few examples that follow the Divide and Conquer approach. There are a few points to note while deciding if one should go for <b>faster</b> Divide and Conquer approach:

1. The problem should be on a bigger scale.
2. The sub-problem must look precisely similar to the original problem in hand.
3. Use recursion to solve the problem. It means that the solution will be built for the smallest sub-problem (base case) first.
4. There is a trade-off between memory usage and speed of execution. Recursion comes with a price of extra memory usage for executing the call stack. But, if you use multi-threading, you can compute the solution even much faster.
5. In case if many sub-problems look precisely the same, then we don't want to re-execute the same again and again. In such cases, you can consider storing the results of the execution, and thus reuse them whenever required. This strategy is called <b>Memoization</b> (in Dynamic Programming approach).