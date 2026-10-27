# S02 Lecture — Recursion, recurrences, Master Theorem and binary search

## 1. Why this session matters

Many algorithms solve a problem by reducing it to smaller instances of the same problem. Recursion describes this program structure; a recurrence describes its cost. Binary search is a compact example: each comparison discards approximately half the remaining search interval. Understanding both the execution and the recurrence lets us explain not only that an algorithm is fast, but why.

The analysis in these notes uses a unit-cost RAM model unless stated otherwise: a comparison, index calculation, assignment and arithmetic operation on machine-sized values count as constant time. This model is useful for algorithm design but does not capture all effects of cache misses, allocation, interpreter overhead or arbitrary-precision integer arithmetic.

## 2. Recursive functions and the call stack

A recursive function calls itself directly or indirectly. A well-designed recursive procedure specifies:

- **Base case:** a smallest case solved without another recursive call.
- **Recursive case:** transforms the current problem into strictly smaller subproblems.
- **Progress measure:** a quantity that moves toward a base case.
- **Combination step:** any work needed after recursive calls return.

Consider factorial for a non-negative integer n:

```python
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

Mathematically, (0! = 1) and (n! = n(n-1)!) for (n ge 1). The base case is n ≤ 1; the progress measure is n, which decreases by one. Negative input is rejected rather than allowed to recurse indefinitely.

For `factorial(4)`, the calls descend as:

```text
factorial(4)
  -> 4 * factorial(3)
       -> 3 * factorial(2)
            -> 2 * factorial(1)
                 -> 1
```

The return phase unwinds the stack: factorial(2) returns 2, factorial(3) returns 6, factorial(4) returns 24. Each active call needs a stack frame containing its local state and return point. A recursive call does not erase the caller; the caller waits until the child returns.

**Termination argument:** for valid input n ≥ 0, each non-base call decreases n by one. After at most n decrements, the base case is reached. This argument depends on the input precondition and the progress measure.

**Common failure modes**

- No base case, or a base case that cannot be reached.
- A recursive call with an unchanged or larger problem.
- A base case that returns the wrong value.
- Forgetting that pending operations run after a recursive call returns.
- Exceeding the language/runtime's stack limit for deep recursion.

Python integers have arbitrary precision, so multiplication cost is not truly constant as n grows; the familiar Θ(n) time statement for factorial counts n multiplications under a simplified unit-cost arithmetic model. The recursion uses Θ(n) stack frames. An iterative factorial can reduce auxiliary stack space to Θ(1).

## 3. From recursive code to a recurrence

A **recurrence relation** defines a quantity in terms of smaller inputs, together with base values. To analyse an algorithm, T(n) usually denotes its running time on an input of size n.

A useful modelling checklist:

1. How many recursive calls occur?
2. What is the size of each recursive subproblem?
3. What work happens outside those calls?
4. What are the base-case costs?
5. What input and cost model are assumed?

### Example A: one smaller call

The factorial procedure performs one recursive call on n−1 and constant additional work:

[
T(n)=T(n-1)+Theta(1),quad T(0)=Theta(1).
]

Expanding:

[
T(n)=T(n-2)+2Theta(1)=dots=T(0)+nTheta(1)=Theta(n).
]

There are n+1 levels up to constant differences. Stack depth is Θ(n).

### Example B: halve the problem

Binary search makes at most one recursive call on roughly half of the current interval, after constant work:

[
T(n)=T(lfloor n/2floor)+Theta(1),quad T(1)=Theta(1).
]

After k reductions, the interval size is at most n/2ᵏ. Stop when it is at most one, so  n/2ᵏ ≤ 1, equivalently k ≥ log₂ n. Thus T(n)=Θ(log n) in the worst case. Recursive binary search has Θ(log n) auxiliary stack space; an iterative version has Θ(1) auxiliary space.

### Example C: two half-size calls

Merge sort recursively sorts two halves and merges them in linear time:

[
T(n)=2T(n/2)+Theta(n),quad T(1)=Theta(1)
]

Assume for the clean derivation that n is a power of two. At level i, there are 2ᶦ subproblems, each of size n/2ᶦ. The total non-recursive work at that level is 2ᶦ · Θ(n/2ᶦ)=Θ(n). There are log₂ n levels of splitting, plus a constant-cost leaf level per item. The total is Θ(n log n).

For non-powers of two, floor/ceiling subproblem sizes change details but not the asymptotic result for the standard merge-sort algorithm.

## 4. Recursion trees and expansion

A recursion tree visualises the calls. Each node's label is the non-recursive work done by that call; children represent recursive subproblems. The total cost is the sum of work across all nodes.

For (T(n)=2T(n/2)+cn), with n a power of two:

| Level | Number of nodes | Work per node | Total level work |
|---:|---:|---:|---:|
| 0 | 1 | cn | cn |
| 1 | 2 | c(n/2) | cn |
| 2 | 4 | c(n/4) | cn |
| i | 2ᶦ | c(n/2ᶦ) | cn |
| log₂ n | n leaves | Θ(1) | Θ(n) |

The internal levels contribute Θ(n log n); leaves contribute Θ(n). Total: Θ(n log n).

Compare three patterns:

- (T(n)=T(n-1)+Theta(1)): a chain with Θ(n) nodes and Θ(n) total work.
- (T(n)=T(n/2)+Theta(1)): a chain with Θ(log n) nodes and Θ(log n) total work.
- (T(n)=2T(n/2)+Theta(n)): Θ(log n) levels, Θ(n) work per internal level, Θ(n log n) total.

A recursion tree is an intuition and a derivation aid, not automatically a complete proof. State the level costs and number of levels, including leaf work.

## 5. The Master Theorem

The Master Theorem gives asymptotic bounds for recurrences of the form

[
T(n)=aT(n/b)+f(n),
]

where a ≥ 1 is a constant number of subproblems, b > 1 is a constant shrink factor, and f(n) is the asymptotic non-recursive work. The standard introductory version assumes well-behaved non-negative costs and the relevant regularity conditions. Define (p=log_b a).

### Case 1: recursive work dominates

If (f(n)=O(n^{p-epsilon})) for some constant ε > 0, then

[
T(n)=Theta(n^p).
]

Example: (T(n)=4T(n/2)+Theta(n)). Here p=log₂4=2 and n is polynomially smaller than n², so T(n)=Θ(n²).

### Case 2: work is balanced

If (f(n)=Theta(n^plog^k n)) for a constant k ≥ 0, the standard form gives

[
T(n)=Theta(n^plog^{k+1}n).
]

The common case (f(n)=Theta(n^p)) is k=0, giving Θ(nᵖ log n).

Example: (T(n)=2T(n/2)+Theta(n)). Here p=1, so T(n)=Θ(n log n).

### Case 3: non-recursive work dominates

If (f(n)=Omega(n^{p+epsilon})) for some constant ε > 0 and the regularity condition (a f(n/b)le c f(n)) holds for some constant c<1 and sufficiently large n, then

[
T(n)=Theta(f(n)).
]

Example: (T(n)=2T(n/2)+Theta(n^2)). Here p=1 and n² is polynomially larger than n. The regularity condition holds for the usual quadratic term, so T(n)=Θ(n²).

### When not to apply it mechanically

The standard theorem does not directly cover every recurrence. Be cautious when:

- the subproblems have substantially unequal sizes;
- a or b is not a constant in the required form;
- f(n) falls into a gap between the cases;
- the required regularity condition for Case 3 has not been established;
- the recurrence includes unusual oscillatory or non-polynomial terms outside the theorem's stated assumptions.

For example, (T(n)=T(n/2)+T(n/3)+n) is not in the simple equal-subproblem form (aT(n/b)+f(n)). It may be analysed with other methods, but do not force it into the Master Theorem. Always write the theorem's form, calculate p, compare f(n) with nᵖ, and verify the applicable case conditions.

## 6. Binary search

**Problem:** given a sequence sorted in non-decreasing order and a target x, return an index containing x, or report that it is absent.

Precondition: the sequence is sorted according to the same ordering used by comparisons. Without that precondition, binary search is not correct. If duplicates exist, the standard implementation below may return any matching index, not necessarily the first or last.

### Iterative implementation

Use a half-open interval [lo, hi): lo is included and hi is excluded.

```python
def binary_search(values, target):
    lo, hi = 0, len(values)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return -1
```

Why half-open bounds? The initial interval [0,n) contains every valid index. The condition lo < hi means there is at least one candidate. If the midpoint is too small, every index ≤ mid is too small in a sorted array, so the new interval is [mid+1, hi). If the midpoint is too large, every index ≥ mid is too large, so the new interval is [lo, mid). Both updates strictly shrink the interval.

**Loop invariant:** if the target occurs in the original array, then at the start of every iteration at least one occurrence remains inside the candidate interval [lo, hi). The invariant is true initially. Each comparison removes only indices that cannot contain the target, preserving it. On a match, the returned index is valid. On termination with lo=hi, the interval is empty; by the invariant, no occurrence exists, so returning −1 is correct.

**Termination:** the non-negative interval length hi−lo strictly decreases whenever no match is returned. Therefore the loop terminates.

### Trace

For values [2, 4, 7, 9, 13, 18, 21] and target 13:

| Step | lo | hi | mid | values[mid] | Action |
|---:|---:|---:|---:|---:|---|
| 1 | 0 | 7 | 3 | 9 | 9 < 13, set lo=4 |
| 2 | 4 | 7 | 5 | 18 | 18 > 13, set hi=5 |
| 3 | 4 | 5 | 4 | 13 | Return index 4 |

For target 8, the interval shrinks until lo=hi=3 and the algorithm returns −1. For an empty array, hi starts at 0 and the loop is never entered.

### Complexity

Each iteration uses constant work and reduces the interval to at most about half. The worst-case number of iterations is Θ(log n) for n≥1; best case is Θ(1) if the first midpoint matches. Auxiliary space is Θ(1) for this iterative implementation. Recursive binary search also takes Θ(log n) worst-case time but Θ(log n) stack space in a conventional implementation.

Binary search is not always the best practical choice: the data must already be sorted, sorting may cost Θ(n log n), and a linked list does not provide constant-time midpoint indexing. For one lookup in an unsorted array, a linear scan may be more appropriate. For many lookups, sorting or maintaining an ordered/indexed structure may pay off.

## 7. Recursive binary search and a common defect

A recursive version must pass the shrinking interval and define an empty-interval base case. Use the same half-open interval convention to avoid mixing boundary styles.

```python
def binary_search_recursive(values, target, lo=0, hi=None):
    if hi is None:
        hi = len(values)
    if lo >= hi:
        return -1
    mid = lo + (hi - lo) // 2
    if values[mid] == target:
        return mid
    if values[mid] < target:
        return binary_search_recursive(values, target, mid + 1, hi)
    return binary_search_recursive(values, target, lo, mid)
```

A classic off-by-one bug sets `lo = mid` after proving values[mid] < target. If the interval has two elements, mid may equal lo; the next call receives the same interval and does not make progress. Use mid+1 when excluding the midpoint. Boundary conventions must be consistent: this implementation uses [lo, hi), so hi is excluded.

## 8. Choosing a method and measuring it

| Method | Preconditions | Worst-case time | Auxiliary space |
|---|---|---:|---:|
| Linear search | No ordering required | Θ(n) | Θ(1) |
| Iterative binary search | Random-access sorted sequence | Θ(log n) | Θ(1) |
| Recursive binary search | Random-access sorted sequence | Θ(log n) | Θ(log n) stack |

These bounds count comparisons and basic operations in the stated model. They do not mean binary search is always faster for tiny inputs; constant factors and data layout matter. Do not claim empirical superiority without documenting the environment, input sizes, distribution, repeat count and measurement method.

## 9. Check your understanding

Before leaving, be able to answer:

1. What are the base case and progress measure in a recursive algorithm?
2. What information is captured by T(n), and why do we need a base condition?
3. For (T(n)=3T(n/2)+n), what is (p=log_2 3), and which Master-Theorem case applies?
4. Why does (T(n)=T(n/2)+T(n/3)+n) not fit the simple equal-subproblem Master form?
5. State the binary-search invariant and explain why each boundary update preserves it.
6. Why does recursive binary search use more auxiliary space than the iterative version?

## References

- Official *M12 — Data Structures and Algorithms Module Descriptor*.
- Cormen, Leiserson, Rivest and Stein, *Introduction to Algorithms*, 4th ed. (2022), chapters on divide-and-conquer and asymptotic analysis.
- Sedgewick and Wayne, *Algorithms*, 4th ed. (2011), binary search.
