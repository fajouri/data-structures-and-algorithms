# S07 + S08 — Lecture notes

## S07 — Hash tables (C1, C2, K1, S1)

A symbol table is a map from unique keys to values. `put(k,v)` inserts or replaces, `get(k)` retrieves, and `delete(k)` removes; missing keys raise `KeyError` in our demo. Hashing implements this contract using an array of capacity m. A key's hash is mapped to an index, for example `hash(k) % m`. Equal keys must have equal hash values; distinct keys can collide. Keys must remain hash/equality-stable while stored. A good distribution reduces collisions but never eliminates them in general. For integers 1, 9, 17 and m=8, all map to index 1. A cache uses this design for exact-key access; an ordered index has different requirements.

### Separate chaining
Each bucket holds a collection of key-value pairs. Compute the index, scan the bucket for equality, replace an existing value or append a new pair. A search scans only its bucket. Delete removes the matching pair. Trace with m=8: after put(1,A), put(9,B), put(17,C), bucket 1 contains [(1,A),(9,B),(17,C)]; deleting 9 leaves [(1,A),(17,C)]. Invariant: each live pair is in its designated bucket, with one pair per key. Searching that bucket is therefore complete. Scans terminate at the end of the finite bucket.

Load factor α=n/m. Under simple uniform hashing, assuming constant-time hash/equality, expected search work is O(1+α), worst O(n). Best O(1); insertion here checks for duplicates, so it has the same lookup cost except on resize. Space Θ(m+n); allocations and indirections may degrade locality depending on representation. Geometrically growing capacity maintains bounded load and yields expected amortised O(1) insertion under the stated hashing assumptions; a resize is O(n) expected at bounded load but pathological collisions can make reinsertion quadratic in this implementation.

### Open addressing: linear probing
Store records directly in slots; use `(h(k)+j) mod m` for j=0,...,m−1. A slot has three states: never occupied (EMPTY), live record, or deleted (TOMBSTONE). Search stops at a matching key, a never-used slot or after m probes. It must continue across tombstones. To insert, remember the first tombstone but continue until finding the key or proving absence; reuse that tombstone only after the duplicate check. Maintain live count and used count (live+tombstones); grow or rebuild when occupancy threatens performance. A rebuild reinserts live records under the new capacity; it cannot simply copy slots.

Trace (m=8): insert 1 at 1, 9 at 2, 17 at 3. Delete 9, marking slot 2 as a tombstone. Searching 17 probes 1,2,3 and succeeds. If deletion wrote EMPTY, search would incorrectly stop at 2. Put(17,new) must update slot 3 rather than create a duplicate at slot 2. Put(25,D) finds no duplicate and may reuse slot 2. Wrap-around: keys 7 and 15 occupy slots 7 and 0. Invariant: no EMPTY occurs before a live key along its probe sequence. Finite bounded probing ensures termination, including full tables. Rehash restores the invariant after capacity changes. Linear probing can exhibit primary clustering; expected O(1) per ordinary operation only under suitable hash distribution and occupancy bounded away from one. Worst O(m), including failed lookups; rebuilding has expected O(n+m) and can cost O(n²+m) under extreme collisions. The geometric-growth argument gives expected amortised O(1) inserts under those assumptions. Space Θ(m). Contiguous slots can improve locality, but language/object overhead matters; Python list references are not inline C++ records. Measure rather than assume.

### Selection and measurement
Use a hash map for exact lookups when ordering is irrelevant; a balanced BST gives worst-case logarithmic operations and supports sorted iteration/range queries. Choose based on adversarial keys, memory budget, ordering, and latency guarantees. Compare hit and miss probe counts at α=0.25,0.50,0.65 with deterministic random integer keys; also test deliberately colliding keys. Document m, live and used occupancy, seed, hash behavior, repeats, and whether a resize occurred. Counts test the implementation's behavior, not a proof of expected complexity.

## S08 — Heaps and sorting (C1, C2, K4, S2)

### Priority queue and binary heap
A priority queue ADT supports insert, peek and extract by priority, not FIFO. A max-heap stores a complete binary tree in an array with parent (i−1)//2 (i>0), left 2i+1, right 2i+2 (when in range). Each parent is ≥ its children. The root is maximum by transitivity, but siblings and unrelated nodes are not sorted. Equal priorities are allowed; stability requires an explicit tie-breaker, such as an insertion counter. A min-heap reverses the comparison. Applications include task scheduling and top-k queries.

Push appends a value then sifts up while it exceeds its parent. Only the ancestor path can violate order. Extract saves the root, moves the last element to the root and sifts it down by swapping with the larger child while needed. Only one descending path can violate order at a time. Both loops move strictly along finite paths. With n elements, peek Θ(1), push/extract best Θ(1), worst O(log n) comparisons; dynamic array growth can make an individual push O(n), while growth has amortised constant overhead. A heap is Θ(n) storage; iterative sift uses O(1) auxiliary space. Empty peek/extract raises `IndexError` in the demonstration.

Trace: start [9,5,7,2,3], append 8 -> [9,5,7,2,3,8], swap with 7 -> [9,5,8,2,3,7], stop at root 9. Extract 9, replace root with 7 -> [7,5,8,2,3], swap with 8 -> [8,5,7,2,3].

### Bottom-up heap construction
Leaves already satisfy the invariant. Process internal nodes from n//2−1 down to zero, sifting down. When each is processed its child subtrees are heaps; inductively the entire tree becomes a heap. For [3,1,6,5,2,4], sift at index 2 (no change), index 1 -> [3,5,6,1,2,4], index 0 -> [6,5,4,1,2,3]. A node of height h costs O(h); there are O(n/2^h) such nodes. Summing the geometric weighted series yields Θ(n) time for bottom-up heapify, not Θ(n log n). Repeated insertion has O(n log n) worst-case time. Auxiliary space O(1) for in-place iterative heapify.

### Heapsort
Build max-heap; swap its root with the last active item; shrink active heap by one and sift the new root down. Invariant: prefix is a max-heap, suffix sorted ascending and every prefix element ≤ every suffix element. Each iteration places the maximum remaining item in its final position and decreases the active size. Worst-case Θ(n log n); average Θ(n log n) for random distinct inputs. Best depends on keys and implementation (all equal can take Θ(n) with early-stop sift); O(n log n) upper bound for all inputs. In-place O(1) auxiliary space, not stable in general.

### Insertion sort
Maintain a sorted prefix. For each next element, shift strictly larger earlier elements right and place the key into the gap. The invariant is a sorted permutation of the processed elements. The outer loop grows the prefix and inner loop decreases the index. Best Θ(n) for already sorted data, average/worst Θ(n²) for random distinct/reverse data; O(n+I) time where I is inversion count. O(1) auxiliary storage, stable when equal keys are not moved past each other. Often useful for small or nearly sorted inputs; constant factors must be measured.

### Why comparisons have a lower bound
For n distinct items, a comparison-based sorting algorithm must distinguish n! input orderings. Its binary decision tree has at least n! leaves, so height ≥ ceil(log2(n!)) = Ω(n log n) in the worst case. For uniformly random permutations, average comparisons are also Ω(n log n). This is not a lower bound on every individual input; it does not apply to non-comparison methods under different key assumptions. Heapsort meets the worst-case comparison-order bound, whereas insertion sort does not. Stability is a separate property; sorting identical keys with labelled records is a useful counterexample exercise.

### Experiment
Use same input arrays for both sorts and copy outside timing. Warm up, repeat five times, report median and correctness against Python sorted; random seed 42, sizes 32/128/512, random/sorted/reversed. Record machine and Python version if presenting results. Timing is not proof of complexity. The tiny-input exercise prepares for the larger sorting benchmark in S10 but introduces no graded instructions.

## References
- Cormen, Leiserson, Rivest & Stein (2022). *Introduction to Algorithms*, 4th ed., MIT Press. Hash tables, heapsort, sorting lower bounds.
- Goodrich, Tamassia & Goldwasser (2013). *Data Structures and Algorithms in Python*, Wiley. Maps, priority queues and sorting.
- Sedgewick & Wayne (2011). *Algorithms*, 4th ed., Addison-Wesley. Hash tables and priority queues.
- Approved course plan: https://github.com/fajouri/data-structures-and-algorithms/blob/master/course-plan.md
