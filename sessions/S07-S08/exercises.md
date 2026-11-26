# Student practice — S07 + S08 (ungraded)

## In-class S07 (15 min)
1. With capacity 7 and h(k)=k mod 7, insert keys 5,12,19,6 with values equal to their keys. Draw separate chaining and linear probing tables. Show wrap-around. Delete 12; show probes for get(19) and a miss get(26). Explain why EMPTY and TOMBSTONE differ.
2. A service supports exact user-ID lookup and sorted date-range queries. Choose a data structure for each operation and justify memory, ordering and worst-case costs. State hashing assumptions.

## In-class S08 (15 min)
3. Starting with max-heap [12,8,10,3,5,9], insert 11 and extract the maximum. Show all swaps and check every parent-child pair. What happens on empty extraction?
4. Trace insertion sort for [4,2,4,1] with the equal 4s labelled A/B. Compare with heapsort; explain stability and nearly sorted input behavior. For four distinct keys, explain the minimum worst-case number of binary comparisons from a decision tree.

## Independent implementation and application
5. Implement a chained map and a linear-probing map from the lecture contracts without copying the demo. Test update, duplicate keys, deliberate collisions, wrap-around, missing keys, deletion, tombstone reuse, resize, negative integers and empty map. Match a Python dict oracle; report expected/worst bounds and assumptions. Optional: use C++17 `std::vector` and compare representation overhead with Python.
6. Benchmark lookup hits/misses across three controlled occupancies (0.25, 0.50, 0.65). Use capacity 4096, a fixed seed and distinct random keys; report mean and median probe counts separately. Repeat with colliding keys, record live and used load, avoid automatic resizing during measurement. Explain clustering and limitations.
7. Implement heap push/pop and bottom-up heapify. Input: list of integers; output: extracted items in descending order. Validate against sorted(reverse=True) for empty/singleton/duplicates/negative/random input. Add an insertion counter for FIFO tie handling in a scheduler (use tagged records rather than bare ints).
8. Implement heapsort and stable insertion sort independently. Compare empty, singleton, equal, sorted, reverse and random inputs; use sorted as oracle. Benchmark at n=32,128,512 with the same arrays, five repetitions, median time and machine/Python metadata. Explain empirical versus asymptotic results. Optional: count comparisons or measure crossover using more sizes.

## Exit ticket
- What assumptions make hash lookup expected constant time?
- Why is bottom-up heapify linear while heapsort is O(n log n)?
- Why does the comparison lower bound not contradict linear best-case insertion sort?
