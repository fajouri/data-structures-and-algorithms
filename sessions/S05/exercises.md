# S05 — Student Studio Exercises (Teaching Practice, Not a Graded Brief)

**Instructions:** predict, implement in your own words, test, measure and explain. Show your assumptions. Use comparable integer keys and the teaching-only `put/get/delete/contains/len` contract from S05. **No answer key is provided.** Assessment rules will be published only after institutional confirmation.

## A · Understand and trace (recommended: 20 minutes)

**1. Contract trace.** Start with an empty map and apply `put(8,"red")`, `put(3,"blue")`, `put(8,"green")`, `get(8)`, `delete(3)`, `contains(3)` and `len(table)`. Write the expected observable outcome and size after each operation. Explain why representation must not change this answer.

**2. Same data, three representations.** Draw key–value pairs `(40,"a"), (20,"b"), (60,"c"), (10,"d")` as an unsorted array, a head-inserted singly linked list and a BST built in the given insertion order. Draw each successful lookup path for 10. Identify what must remain true after an update to key 20.

**3. Complexity: qualify each claim.** Is an array append O(1), a linked-list insertion O(1), or a BST search O(log n)? For each claim, specify **the exact operation, assumptions, and whether the statement covers duplicate detection**. Give a counterexample to an overgeneralized claim.

## B · Correctness by specification (recommended: 25 minutes)

**4. Test matrix.** Write an expected-result table for empty get/delete, singleton, duplicate-key update, missing key, delete head, delete root, BST node with zero/one/two children, negative key and a value equal to `None`. For each case, say which invariant or contract clause it checks.

**5. Implement or complete an array-backed table.** Use an unsorted resizable array/list of key–value pairs. Support `put/get/delete/contains/__len__` under the teaching contract. Constraints: avoid duplicate logical keys; raise `KeyError` on missing get/delete; do not rely on Python `dict` as the storage mechanism. Explain the worst-case search and deletion costs and the difference between appending a known new entry and checking that it is new.

**6. Implement or complete a singly linked list-backed table.** Use a node object with `key/value/next`, plus a head pointer and size. Show a hand trace of removing the head, an interior node and a missing key. Draw the `next` changes; explain why you need to retain the predecessor while searching for deletion.

**7. Implement or complete a plain BST-backed table.** Define node key/value/left/right. Implement `put/get/delete/contains/__len__` using the strict BST ordering invariant. Cover deleting an empty tree key, a leaf, a one-child node and a two-child node. In the two-child case, if you use the successor, preserve **both its key and value**. Do not assume self-balancing.

**8. Differential testing.** For fixed seed 42, generate a repeatable mix of `put/get/delete/contains`. Compare your table's result, exception type and `len` after every operation against a fresh `dict` oracle. State a scenario for which such testing is still not a proof.

## C · Experiment design (recommended: 30 minutes)

**9. Define three workloads.** Choose (i) insertion/build, (ii) successful lookup, (iii) unsuccessful lookup, and optionally deletion/update. Explain whether construction, generation, and correctness checking occur inside the timed section. Use same key sequences across finished implementations.

**10. Input distribution.** Compare shuffled and ascending key insertion orders, especially for an unbalanced BST. At n=8, draw or estimate the BST height first. Later measure height or comparisons alongside timings. Explain the difference between one particular random seed and an expected-time theorem.

**11. Reproducibility.** Record Python interpreter/OS, hardware if known, seed, n, number of operations, warm-up policy, repeats and statistic (e.g. median). Explain two sources of measurement noise. Use `time.perf_counter_ns()` or equivalent; do not invent readings.

**12. Result interpretation.** Produce a table with columns `structure, n, workload, median_us/op, repetitions, correctness_passed, comment`. Explain one observation without pretending that an empirical curve mathematically proves an asymptotic bound. If a table failed a contract test, mark its timing as invalid or not measured.

## D · Peer review and exit (recommended: 20 minutes)

**13. Peer code review.** Exchange a **small excerpt** or pair-review an operation. Check: (a) duplicate keys, (b) missing behaviour, (c) link preservation, (d) BST invariant, (e) measured workload equivalence. Give one actionable suggestion rather than a generic grade.

**14. Decision memo.** Write 120–180 words for a service that performs many unsuccessful lookups, rare deletions and occasional bulk loads. Recommend one of the three structures *under stated input assumptions*. Explain one trade-off or missing piece of evidence.

**15. Exit ticket.** Give one invariant, one counterexample that catches a bug, and one condition necessary for a fair benchmark.

## Optional advanced challenge
Instrument **key comparison counts** in addition to elapsed time. Plot counts per operation for sorted and shuffled BST insertion orders. Discuss how this separates shape effects from interpreter and memory-allocation noise. For C++17, compare matching semantics with a controlled compiler/optimization setting; do not treat Python-vs-C++ wall-clock measurements as a direct complexity comparison.

**Suggested output of today's ungraded practice:** annotated contract, test matrix, implementation progress, a measured table only where correctness passed, and a short limitations paragraph. **No official grade, deadline, or submission format is assigned by this worksheet.**
