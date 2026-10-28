# S03 Lecture — Arrays, dynamic arrays, linked lists and amortised costs

## 1. Why representation matters

Consider a service storing appointment IDs, product codes or event records. It may retrieve position i, append values, insert near the beginning, or remove a known item. The sequence is the abstract behaviour; the representation determines the cost.

Choose by operation mix: frequency of each operation, size, whether the location is already known, and memory locality. No representation is universally fastest.

Unless stated otherwise, use a unit-cost RAM model: reading/writing one machine-sized element, comparing values, and following one pointer each cost Θ(1). Allocation and garbage collection are excluded; values are assumed to have constant-size operations.

## 2. Sequence ADT versus representation

A sequence ADT specifies ordered values and observable operations such as length, get(i), set(i,x), append(x), insert(i,x), remove(i), and iteration. Its contract should define valid indices, duplicates and invalid-index behaviour.

A Python list and C++ std::vector are dynamic-array representations. A singly linked list uses nodes connected by links. Similar operation names do not imply similar costs.

A **representation invariant** is a condition that must remain true. For a dynamic array, 0 ≤ size ≤ capacity and the first size slots contain the logical sequence in order. For a singly linked list, following next from head visits every stored element once, in sequence, and then reaches null. If a tail pointer is maintained, it identifies the last node, or is null exactly when the list is empty.

## 3. Fixed arrays and contiguous memory

An array stores elements in contiguous slots. If each element occupies w bytes and the base address is B, index i is conceptually at B + i·w. Address calculation and indexed access are Θ(1) under the model. Nearby elements also tend to benefit from cache locality, although cache effects influence real timings rather than the basic asymptotic bound.

### Trace: insert into an array

Start with [10, 20, 30, 40]. Insert 25 at index 2. Shift 40 right, then 30 right, then write 25 at index 2. The result is [10, 20, 25, 30, 40]. Two existing values shifted.

Inserting at index i into n elements may shift n−i values; worst-case insertion is Θ(n). Removing index i similarly shifts later values left, Θ(n) worst case. Indexed read/write is Θ(1), and unsorted search is Θ(n). A fixed-size array also needs spare capacity or a new allocation to grow.

## 4. Dynamic arrays: size and capacity

A dynamic array has a backing array whose capacity may exceed its logical size. Only indices 0 through size−1 are elements. Appending with spare capacity writes at index size and increments size, Θ(1). When full, the implementation allocates a larger backing array and copies elements; that individual append costs Θ(n).

Assume for analysis that capacity doubles when full. This trace is illustrative, not a benchmark:

| Append | Size before | Capacity before | Action | Capacity after |
|---:|---:|---:|---|---:|
| 1 | 0 | 1 | Write | 1 |
| 2 | 1 | 1 | Copy 1 and append | 2 |
| 3 | 2 | 2 | Copy 2 and append | 4 |
| 4 | 3 | 4 | Write | 4 |
| 5 | 4 | 4 | Copy 4 and append | 8 |
| 6–8 | 5–7 | 8 | Write | 8 |
| 9 | 8 | 8 | Copy 8 and append | 16 |

The exact initial capacity and growth policy depend on the implementation.

## 5. Amortised cost of append

These claims are compatible:
- One append that resizes can cost Θ(n).
- An append without resizing costs Θ(1).
- n appends to an initially empty dynamic array with geometric growth cost Θ(n) total, or Θ(1) amortised per append.

**Amortised analysis is not average-case probability.** It bounds a sequence of operations without assuming a probability distribution. Individual worst-case append remains Θ(n).

### Aggregate argument

Assume capacity doubles. Each of n appended values is written once. Resizing copies form a geometric sum: 1 + 2 + 4 + … + 2ᵏ, which is less than 2ᵏ⁺¹. Since final capacity is a power of two smaller than a constant multiple of n (apart from small initial cases), the total number of copied values is O(n). The n writes give an Ω(n) lower bound, so total work is Θ(n). Dividing by n operations gives Θ(1) amortised work per append.

If capacity grew by exactly one slot each time, appending n values could copy 1 + 2 + … + (n−1) = Θ(n²) elements. The growth policy is therefore important.

The potential method is another accounting view: define a non-negative potential that grows as spare capacity is consumed, then use accumulated credit to pay for resizing. A formal proof must state the potential and verify its properties. The aggregate proof above is sufficient for this session.

## 6. Singly linked lists

Each node stores a value and a link to the next node. Nodes need not be adjacent in memory. Head identifies the first node; the last node points to null.

For 10 → 20 → 30 → null, accessing index 2 follows two links from head. Access by index i costs Θ(i), hence Θ(n) worst case. A list does not support array-style random access.

To insert 15 after the node containing 10, set the new node's next to the old successor (20), then set the 10-node's next to the new node. If the predecessor is already known, changing links is Θ(1). Finding it by index or value can take Θ(n). Inserting at the head is Θ(1). Appending is Θ(1) with a maintained tail pointer, otherwise Θ(n) to find the last node.

Removing after a known predecessor is Θ(1): redirect predecessor.next to the removed node's successor. Searching for a value or index first costs Θ(n). A node reference alone is not generally sufficient to remove a node in a singly linked list in constant time.

### Correctness invariant

After each operation, following links from head must visit exactly the logical sequence in order, without skipping or repeating a node, and terminate at null. During insertion, preserve the old successor before redirecting the predecessor. Test empty and singleton transitions explicitly.

## 7. Cost comparison

Worst-case bounds under the stated model:

| Operation | Array/dynamic array | Singly linked list |
|---|---:|---:|
| Access by index | Θ(1) | Θ(n) |
| Unsorted search | Θ(n) | Θ(n) |
| Replace by index | Θ(1) | Θ(n) to reach node |
| Insert/remove at front | Θ(n) due to shifts | Θ(1) |
| Insert after known predecessor | Θ(n) shifts in general | Θ(1) |
| Append | Dynamic array Θ(n) worst-case, Θ(1) amortised | Θ(1) with tail; otherwise Θ(n) |
| Per-element overhead | Backing slots; spare capacity possible | Link(s), node allocation overhead |

These bounds describe operations, not universal runtime rankings. Arrays often have better locality and lower per-element overhead. Linked lists avoid shifting and can splice nodes efficiently when locations are known, but require pointer storage and traversal. Library guarantees can differ; consult their contracts.

## 8. Choose for the workload

Choose a dynamic array when indexed reads, iteration and append dominate. Consider a linked list when frequent edits happen around already-known node positions. If each edit first searches by value, traversal may erase the benefit. Frequent key lookups may call for a different ADT such as a hash table or tree.

Benchmark only after analysis. Record language/compiler version, input sizes, input generation, repetitions and timing method. Do not infer asymptotic complexity from one noisy timing.

## 9. Misconceptions

- “Array append is always O(1).” A resize can cost Θ(n); under geometric growth the amortised cost is Θ(1).
- “A linked list inserts in O(1) anywhere.” Only when the relevant location is already known.
- “Capacity equals size.” Capacity is allocated slots; size is logical elements.
- “Amortised means average over random inputs.” It is a deterministic sequence bound.
- “ADT and implementation are synonyms.” The ADT is the contract; representation is storage and invariant.

## References

- Official M12 — Data Structures and Algorithms Module Descriptor, for scope and outcomes.
- Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 4th ed. (2022), elementary data structures and amortised analysis.
- Goodrich, Tamassia and Goldwasser, Data Structures and Algorithms in Python (2013), sequence and linked structures.
- Sedgewick and Wayne, Algorithms, 4th ed. (2011), elementary data structures.
