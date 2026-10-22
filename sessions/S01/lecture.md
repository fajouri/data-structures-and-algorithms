# S01 lecture — Algorithmic thinking, ADTs and asymptotic analysis

## 1. Why this matters

A membership check looks trivial until a service repeats it for millions of requests. If a catalogue has `n` identifiers, a sequential scan may inspect all `n` entries for one query. A different representation can change the work per query, but building that representation also has a cost. We therefore need two kinds of reasoning: **correctness** (does a method return the right answer?) and **cost** (under what assumptions is it a good choice?). Measured runtime is useful evidence about an implementation; it is not a proof about every input or machine.

For this session, an algorithm is a finite, unambiguous sequence of steps with specified inputs, outputs and assumptions. An analysis should say what `n` means, which operation is counted and whether it describes one operation or a sequence of operations. We will use one in-memory sequence of values, with equality comparisons treated as constant cost unless stated otherwise. For long strings or expensive user-defined equality, that assumption does not hold.

### Algorithm specification: membership

- **Input:** a finite sequence `A` of length `n ≥ 0` and a target `x`.
- **Output:** the smallest index `i` such that `A[i] == x`, or `-1` if no such index exists.
- **Preconditions:** indexing from zero and equality defined for each element-target pair. The sequence need not be sorted.
- **Postcondition:** if the result is `i ≥ 0`, then `0 ≤ i < n`, `A[i] == x`, and no earlier index matches. If it is `-1`, no element matches.

The smallest-index condition matters for duplicates. A boolean membership ADT would promise only present or absent, but this algorithm promises a position and a particular position when values repeat.

## 2. ADT contract and implementation

An **abstract data type (ADT)** specifies values and operations with their behaviour. A **representation** describes how those values live in memory. For example, a sequence ADT can offer `length`, `get(i)`, `append(v)` and iteration. A contiguous dynamic array and a linked list can support much of this contract while giving different costs for indexed access and insertion. A set ADT could offer `contains(x)`, `insert(x)` and `remove(x)` without promising insertion order or a position. A hash table or balanced tree may implement such a set, subject to additional assumptions and implementation details taught later.

Keep three layers separate:

1. **Contract:** what the caller can observe, including duplicates, order and failure behaviour.
2. **Representation invariant:** facts the concrete storage must preserve, such as valid indices for an array or consistent links for a list.
3. **Algorithm:** steps used to fulfil one operation, such as a scan for `contains`.

An array is commonly used both for a concrete contiguous representation and, informally, for an indexed collection. State which meaning you intend. The descriptor names several structure families under the ADT outcome; S01 establishes the distinction, while later sessions examine their contracts and implementations in detail. A real system chooses a representation for its *operation mix*: a one-off query on unsorted input may justify a scan, while many queries may justify paying to build an index. Do not assume a hash lookup is always constant time; collision patterns and key-equality costs matter.

## 3. Linear search: trace and correctness

```text
LINEAR-SEARCH(A, x)
    for i from 0 to length(A) - 1
        if A[i] == x
            return i
    return -1
```

Trace `A = [7, 4, 7, 9]`, `x = 7`: before the first comparison, no earlier indices exist; compare index 0; return `0`. The second `7` is deliberately ignored because the specification requests the first match. For `x = 9`, comparisons occur at indices 0, 1, 2, 3 and the result is `3`. For `x = 2`, all four comparisons fail and the result is `-1`. For `A = []`, the loop body never runs and the result is `-1`.

The useful **loop invariant** is: *immediately before testing index `i`, no index in `0..i-1` contains `x`*. Initially `i = 0`, so the prefix is empty and the claim is true. If `A[i]` is not `x`, then the prefix through `i` also has no match, establishing the claim for the next iteration. If `A[i] == x`, the invariant rules out an earlier match, so returning `i` meets the postcondition. When the loop finishes without returning, the invariant covers all indices `0..n-1`; returning `-1` is correct. The loop terminates because `i` increases by one and is bounded by finite `n`.

This is a proof about the algorithm under its preconditions, not a claim inferred from passing examples. Testing empty, singleton, duplicate and absent inputs is still valuable for finding implementation mistakes.

### Cost of linear search

Let one equality test cost one unit. For a present target first seen at index `j`, exactly `j + 1` equality tests occur. For an absent target, exactly `n` occur. For `n > 0`, the best case is one test, `Θ(1)`; the worst case is `n` tests, `Θ(n)`. For `n = 0`, there are zero tests and a fixed amount of control work. The algorithm uses `Θ(1)` **auxiliary** space beyond the input; counting storage for the input itself would give `Θ(n)` total storage.

An average case needs a probability model. If the target is guaranteed present and its *first matching position* is uniformly distributed over `0..n-1`, the mean comparison count is `(n + 1)/2`, so expected work is `Θ(n)`. Duplicate-rich data or a different query distribution changes that mean. If absent queries have probability `q` and present first positions follow the uniform model otherwise, the expected comparison count is `q·n + (1-q)·(n+1)/2` for `n > 0`. This formula is a teaching model, not a universal workload law.

## 4. Duplicate detection: a second trace

For a sequence whose elements support equality, a simple method compares each value with all later values:

```text
HAS-DUPLICATE(A)
    for i from 0 to n - 1
        for j from i + 1 to n - 1
            if A[i] == A[j]
                return true
    return false
```

With `[3, 8, 5, 8]`, inspect pairs `(0,1)`, `(0,2)`, `(0,3)`, `(1,2)`, then `(1,3)`: the last pair matches, so the method returns `true`. With `[3, 8, 5]`, inspect `(0,1)`, `(0,2)`, `(1,2)` and return `false`. An empty or singleton input has no pair and returns `false`.

Before inspecting a pair, all earlier pairs in the stated lexicographic loop order have been tested and found unequal. A matching pair justifies `true`; exhaustion means every pair has been checked, so no duplicate exists. Both indices progress through finite ranges, which gives termination. This also shows why a single early match is enough and why `false` requires exhaustive work.

For `n` distinct elements, the exact number of comparisons is `n(n-1)/2`, which is `Θ(n²)` for growing `n`. A duplicate in the first pair gives one comparison, `Θ(1)` for `n ≥ 2`; the worst case remains `Θ(n²)`. There is no single average-case bound without an input distribution, including the probability and location of duplicates. Auxiliary space is `Θ(1)`. A hash-based method can often reduce expected time to `Θ(n)` but adds `Θ(n)` space and requires hashing assumptions; a sort-then-scan method can reduce comparison growth but may reorder data or need copied storage. These are choices to investigate later, not interchangeable guarantees.

## 5. Bounds and growth

For a nonnegative cost function `T(n)` and an eventually nonnegative comparison function `g(n)`:

- `T(n) ∈ O(g(n))` means there are constants `c > 0` and `n₀` such that `T(n) ≤ c g(n)` for all `n ≥ n₀`.
- `T(n) ∈ Ω(g(n))` means there are constants `c > 0` and `n₀` such that `T(n) ≥ c g(n)` for all `n ≥ n₀`.
- `T(n) ∈ Θ(g(n))` means both bounds hold, possibly with different constants.

Big-O is an eventual upper bound, not inherently a worst-case label. You must first select the cost function, for example the worst-case comparison count of linear search, and then describe a bound on it. For `T(n)=3n²+5n+7`, `T(n) ∈ Θ(n²)` because the quadratic term eventually bounds the others and is itself a lower bound. It is also in `O(n³)`, although that is a loose upper bound. A constant-time first match does not contradict `O(n)` worst-case cost because those refer to different cases.

Under the unit-cost RAM model, a single loop of `n` constant-time operations is `Θ(n)`; two consecutive such loops remain `Θ(n)`; a triangular nested loop with total `1+2+...+(n-1)` iterations is `Θ(n²)`. If a loop repeatedly halves a positive integer input, the number of iterations grows as `Θ(log n)`; the logarithm base changes only a constant factor. Do not call a loop `O(1)` merely because a small benchmark appears flat. State whether you count comparisons, assignments, elapsed time, or memory, and whether a library call hides additional work.

**Best, average and worst** describe different input sets or distributions for a fixed `n`. **Time and space** describe different resources. Auxiliary space excludes the given input and, unless stated otherwise, the returned scalar. Machine caches, interpreter dispatch, allocation and compiler optimisation affect elapsed time even when two implementations have the same asymptotic comparison count.

## 6. Measurements and a fair comparison

`lab.py`, `lab.cpp` and the notebook use deterministic inputs, warm-up, repeated observations and a result sink to make accidental dead-code elimination less likely. Record language/runtime or compiler, optimisation flags, hardware, input sizes, query placement, repeat count and the statistic reported. Compare a run with the same algorithm and input design as `n` changes. Small runs are particularly noisy because timer resolution, scheduling, memory allocation and runtime start-up may dominate.

The Python and C++ demonstrations illustrate how to run analogous experiments. Raw times across languages cannot isolate an algorithmic difference: interpreter overhead, compiler optimisation, container representation and hardware effects also differ. Comparison counts support a more controlled prediction. Neither timings nor a fitted curve prove a bound; the argument follows from the loops and assumptions above.

## 7. Trade-offs and common mistakes

- **One query or many?** A scan requires no index construction. An index may pay off over many queries, but construction, memory and updates must be included.
- **ADT versus implementation:** `contains` is a contract-level operation. A Python list scan, linked-list scan, tree search and hash lookup are implementations with different preconditions and costs.
- **Duplicates:** a first-index search must return the earliest match; a boolean membership check need not return any index.
- **No specified average distribution:** do not state a numeric average without a workload model.
- **Asymptotic notation:** `O(n)` does not mean “exactly linear”; `Θ(n)` is a tight bound on a specified function.
- **Input costs:** equality of long strings may not be constant time. If an equality test takes up to `L`, a worst-case scan is `O(nL)` under that model.
- **Memory:** `Θ(1)` auxiliary space for these scans does not make the input free to store.
- **Proof versus test:** edge-case tests check code behaviour on chosen cases; the invariant explains all permitted finite inputs.

## References and continuation

This lecture follows the scope and outcomes of the official *M12 Module Descriptor*, pp. 1–3, and the approved S01 course-plan brief. For deeper reading, see Cormen, Leiserson, Rivest and Stein (2022), *Introduction to Algorithms*, 4th ed., chapters 1–3, and Goodrich, Tamassia and Goldwasser (2013), *Data Structures and Algorithms in Python*, introductory chapters. S02 develops recurrences and the Master Theorem; S03 studies array and linked-list implementations in detail.
