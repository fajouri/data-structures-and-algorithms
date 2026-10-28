# S03 Exercises — Student worksheet

These are ungraded practice exercises, not an assignment. Show intermediate states, justify complexity claims and state assumptions. No instructor solutions are included.

## A. Understand the ADT and array operations

### 1. Contract or representation?
A sequence supports length, get(i), append(x) and remove(i).
- Which statements describe observable behaviour, and which describe implementation?
- State preconditions and invalid-index behaviour.
- Give one representation that supports indexed access and one that does not.

### 2. Trace array insertion and removal
Start with [4, 9, 12, 20, 25].
- Show every state when inserting 10 at index 2.
- Count shifted elements.
- Remove the element at index 1 and show the result and shift count.
- Give the worst-case bound for insertion/removal at index i in a sequence of size n.

### 3. Complexity by operation
Explain why array indexed access is Θ(1), unsorted search is Θ(n), and insertion at the beginning is Θ(n). Name the counted operation and state whether input storage is included in auxiliary space.

## B. Dynamic arrays and amortised analysis

### 4. Capacity trace
Assume an initially empty dynamic array has capacity 1 and doubles when full.
- Complete a table for appends 1 through 12: size before, capacity before, resize yes/no, copied elements and capacity after.
- Count total copies.
- Explain why a resize is expensive but the sequence of appends is linear total work.

### 5. Prove amortised append
Use the aggregate method for n appends to a dynamic array that doubles capacity.
- Count writes for the n new elements.
- Bound copied elements with a geometric sum.
- Derive total Θ(n) work and amortised Θ(1) work per append.
- Explain why this is not an average-case probability argument.

### 6. Change the growth policy
Suppose capacity increases by exactly one slot whenever full.
- Write the sequence of copy counts for n appends.
- Find the total number of copies.
- Compare total and per-append costs with geometric growth.

## C. Linked lists

### 7. Trace pointer updates
Given head → 10 → 20 → 30 → null:
- Insert 15 after the node containing 10; draw before and after.
- Remove the node containing 20; draw before and after.
- State the pointer update order needed to preserve the suffix.
- State the representation invariant.

### 8. Operation costs depend on what is known
Analyse insert at head, append with/without a tail pointer, insert after a known predecessor, insert after the first value x, and access index i. Separate location-finding cost from link-update cost.

### 9. Implement and test
Implement a singly linked list or use the lab. Test empty/singleton lists, head and middle insertion/removal, missing values, duplicates and traversal after repeated mutations. Explain how tests check the invariant; do not rely only on printed output.

## D. Application and challenge

### 10. Select a representation
Recommend a dynamic array or linked list for:
- Read-heavy sequence with random access and occasional append.
- Queue-like workload with frequent front insertion/removal.
- Sequence edited around nodes already referenced elsewhere.
- Sequence where every edit first requires a value search.
Discuss operation mix, memory locality, per-element overhead and assumptions.

### 11. Amortised versus worst-case
A teammate says: “Dynamic-array append is constant time because its amortised cost is Θ(1).”
Explain what is incomplete, give an expensive individual append, and state both the worst-case and amortised claims under geometric growth.

### 12. Challenge: potential method
For a dynamic array with size n and capacity m, propose a non-negative potential that grows as spare capacity is consumed. Define amortised cost as actual cost plus change in potential. Explain what must be shown for a valid proof.

## Self-check expectations

Your work should contain array states, copy counts, linked-node diagrams, preconditions, correctness invariants, and time/auxiliary-space bounds. For every Θ(1) claim, state whether the location is already known and whether the claim is worst-case or amortised.
