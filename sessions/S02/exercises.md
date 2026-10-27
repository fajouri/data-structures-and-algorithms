# S02 Exercises — Student worksheet

These are practice exercises for learning and discussion, not a graded assignment. Show reasoning and intermediate states. Do not submit only a complexity label or final index.

## A. Recursion and call-stack traces

### 1. Trace a recursive function
Consider:

```python
def mystery(n):
    if n <= 0:
        return 0
    return n + mystery(n - 2)
```

For inputs 5, 2, 1 and 0:
- Draw the sequence of calls and the return order.
- Record the value returned by each call.
- State the base case and a progress measure.
- Explain whether negative values are valid inputs under this function's contract.

### 2. Find the defect
A colleague writes:

```python
def countdown(n):
    if n == 0:
        print("done")
    countdown(n - 1)
```

Identify at least two problems. Rewrite the function's logic in pseudocode, state the intended input domain, and explain why your version terminates.

## B. Build and solve recurrences

For each algorithm description, define T(n), include a base condition, and state your assumptions.

### 3. Single recursive call
An algorithm makes one recursive call on n−1 and performs constant additional work. Expand the recurrence for three levels and give a tight asymptotic bound with a brief justification.

### 4. Divide into two halves
An algorithm recursively processes two halves and then scans all n elements to combine the results.
- Write its recurrence.
- Draw the first four levels for n=16.
- Calculate the total non-recursive work at each level.
- Give a tight bound and explain how leaf work affects the total.

### 5. Master Theorem classification
For each recurrence, calculate (p=log_b a), compare f(n) with nᵖ, state whether the standard Master Theorem applies, and justify the case. Do not assume applicability without checking conditions.

a. (T(n)=2T(n/2)+Theta(1))  
b. (T(n)=2T(n/2)+Theta(n))  
c. (T(n)=4T(n/2)+Theta(n))  
d. (T(n)=2T(n/2)+Theta(n^2))  
e. (T(n)=T(n/2)+T(n/3)+n)

For item (e), explain why the simple equal-subproblem form is not appropriate and name what information a more general analysis would need.

### 6. Spot an unjustified theorem use
A student claims: “The Master Theorem says (T(n)=2T(n/2)+nlog n) is Θ(n log n), because the non-recursive work is n log n.” Identify the reasoning error. State the correct asymptotic result and show which comparison matters.

## C. Binary search: implementation and correctness

### 7. Trace the search
For sorted array [1, 3, 4, 6, 8, 10, 14, 17] and target 10:
- Record lo, hi, mid, values[mid] and the action for every iteration using [lo, hi).
- Repeat for targets 2, 1 and 17.
- Include the empty-array case.

### 8. Debug the boundary update
A binary-search implementation uses `lo = mid` when `values[mid] < target`. Give a minimal sorted input and target that can cause no progress. Explain the invariant and write the correct update for a half-open interval.

### 9. Correctness argument
Write a short proof for iterative binary search with [lo, hi):
- State the precondition and loop invariant.
- Show initialization.
- Explain why each branch preserves the invariant.
- Show why a match is correct and why termination with an empty interval proves absence.
- State a termination measure.

### 10. Compare implementations
Implement iterative and recursive binary search in Python or C++17. Your test matrix must include:
- empty and singleton arrays;
- first and last element;
- a present middle element;
- an absent value below, between and above stored values;
- duplicate values;
- a larger sorted input.

State whether duplicates return the first, last or any matching index. Report worst-case time and auxiliary space, distinguishing stack space from input storage.

## D. Application and challenge

### 11. Choose the strategy
For each situation, choose linear search, binary search, or a different approach and justify:
- One lookup in a short unsorted list.
- Thousands of lookups in a large, mostly static sorted array.
- Repeated lookups in a linked list.
- Data that changes frequently and must remain searchable.

Discuss preprocessing cost, update cost, memory layout and the number of queries.

### 12. Challenge: recurrence outside the basic form
Consider (T(n)=T(n/2)+T(n/4)+n).
- Explain why the basic equal-subproblem Master Theorem does not directly apply.
- Draw the first levels of a recursion tree and estimate the work by level.
- Propose a suitable analysis method and state any assumptions before concluding.

## Self-check expectations

A complete submission to yourself should contain call traces, recurrence equations with base conditions, justified theorem conditions, binary-search state tables, edge-case tests, a correctness argument, and explicit time/auxiliary-space assumptions. If a test fails, minimise the failing input and identify which invariant or boundary assumption was violated.
