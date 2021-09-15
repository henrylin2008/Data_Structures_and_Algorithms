<h3>Basic Approach</h3>
-Divide & Conquer: QuickSort Style

<h4>QuickSort(A):</h4> 
1. Choose a pivot P
2. Partition A into A<P, A=P, A>P
3. Recursively sort A<P & A>P 

Search Example: Pivot </n>

ex: A = [5, 2, 20, 17, 11, 13, 8, 9, 11] </br>
    say P = 11  </br>
    A<P = [5, 2, 8, 9];  A=P = [11, 11];   A>P = [20, 17, 13]
* if K <= 4 then we want kth smallest in A<P
* if 4 <K <= 6 then we output 11
* if K > 6 then we want (k-6)th smallest in A>P

<b>Reverse Engineering</b><br>
Aim: O(n) running time  <br>
    T(n) = T(n/2) + O(n)  <br>
    Quiz: T(n) = O(n)   <br>
    Need: P = median(A) <br>
<br>
Approximate median: n/4 < median < 3n/4 <br>
    T(n) = T(3n/4) + O(n) = O(n)    <br>
    T(n) = T(.99n) + O(n) = O(n)    <br>
<br>
Aim: find a good pivot in O(n) time  <br>
    T(n) = T(3n/4) + O(n) = O(n)    <br>
    slack: T(.24n)  <br>
    T(n) = T(3/4n) + T(n/5) + O(n) = O(n); T(n/5) + O(n) => good pivot  <br>
choose a subset S of A where |S| = n/5 <br>
set P = Median(s)
<br>

<b>Pseudocode</b>   <br>
<u>FastSelect(A,k)</u>
1. Break A into n/5 groups, G1, G2,..., Gn/5   ==> O(n) time
2. For i = 1 --> n/5: sort Gi & let mi = median(Gi)   ==> O(1)/group * n groups => O(n) 
3. Let S={m1, m2,..., mn/5}   ==> T(n/5)
4. P = FastSelect(S, A/10)
5. Partition A into A < P, A = P, A > P 
6. Recurse on A < P or A > P or output P:   ==> T(3/4 n)
   1. If k <= |A<P| then return FastSelect(A<P, k)
   2. If k > |A<P| + |A=P| then return FastSelect(A>P, k - |A<P| - |A=P|)
   3. else output p

claim: P is a good pivot   <br>
T(n) = T(3/4 n) + T(n/5) + O(n) = O(n) time     <br>
        3/4 + 1/5 < 1   <br>

Notes:
1. The algorithm starts with an assumption that "pivot p is good" and in the end, it is able to solve the problem in O(n) time. This proves that the assumption was correct.
2. In step 2 shown in the video, even if we consider that it takes O(k) time for finding the median of a group (of size 5 elements), the overall algorithm will have an O(n) time complexity in the worst case.

