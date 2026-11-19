# S05 — Lecturer's Detailed Teaching Script

**Teaching mode:** 3-hour workshop; simple academic English, frequent prediction questions, explicit board traces and a live Colab demonstration. The code is not an assignment answer key.

## 0. Instructor preparation (before students arrive)
Open `slides.pptx` in presenter mode and the standalone notebook in Colab. Check Python execution, keep the starter/test/benchmark files available offline, and prepare to draw three identical keys in three different representations. Never announce unapproved deadlines, percentages for Assignment 1, submission format or grading criteria. Verify that every student can run the baseline cells even if their own implementations remain unfinished.

## 1. Orientation: one contract, three implementations (00:00–00:10)
**Say:** “Last time, we learned how stacks, queues, and binary search trees work. Today, we are engineers comparing three ways of implementing the *same* service: a symbol table. We will check whether it gives the right answers before we claim that one implementation is faster.” Ask what happens when a key is inserted twice and what should happen for a missing key. Distinguish a teaching agreement from the official assignment brief: this is a checkpoint studio. Official assignment specifications and marking rules require institutional confirmation.

A symbol table is an **abstract data type** (ADT), not a `dict`, a list or a tree. Its externally observable *contract* should remain constant while its internal representation changes. In this workshop, select **comparable integer keys**, arbitrary values, unique logical keys, `put` updating existing values, `get`/`delete` raising `KeyError` when absent, `contains` returning bool, and `len(table)` counting unique keys. This is a **teaching convention for the examples**, not a mandated graded API. Clearly say that the eventual official interface could differ.

## 2. The contract, representations, and invariants (00:10–00:35)

### 2.1 Compare equal operations
Example sequence:
```text
put(20, "A")      -> table has {20: "A"}; size 1
put(40, "B")      -> {20: "A", 40: "B"}; size 2
put(20, "C")      -> {20: "C", 40: "B"}; size STILL 2
get(20)           -> "C"
contains(30)      -> False
delete(40)        -> removes 40; size 1
get(40)           -> KeyError
```
**Ask:** “If one implementation returns `None` for absent keys and another raises `KeyError`, is the benchmark a fair comparison?” The answer is no: we are then comparing different behaviours.

### 2.2 Array-based symbol table
Use a teaching example of an **unsorted array/list of pairs**, not the final implementation: `[(20, "C"), (40, "B")]`. To find a key, inspect pairs until a match or exhaustion. **Invariant:** each key appears at most once and `size` equals the number of bindings; entries can be stored in any order. In the worst case, lookup, update (search first), new insertion with uniqueness check and deletion (search plus potential shifts) take Θ(n). If using a dynamic backing array, the physical append may be amortized O(1), but confirming absence costs O(n). A *sorted* array has different search costs but shifting still matters; explicitly say that students must document which variant they chose under approved rules.

### 2.3 Linked-list symbol table
Draw `head → [20:C] → [40:B] → None`. **Invariant:** the chain is finite and acyclic, contains no duplicate keys, and size matches reachable nodes. Lookup scans nodes; at most n comparisons. Prepending a *known new* node is O(1), but enforcing uniqueness requires an O(n) scan unless another index exists. Deletion must re-link the predecessor's `next` (or update head); never discard the remaining chain. Traversal is typically less cache-friendly than a contiguous array, but do not state a guaranteed measured slowdown without experiment.

### 2.4 BST symbol table
Draw `40:B` root, `20:C` left. **Invariant:** for every node, *all* keys in the left subtree are less, *all* keys in the right subtree are greater; keys remain unique. Plain BST search, insert and delete take O(h+1), where h is the longest root-to-leaf edge count. A shape with h≈log₂n can be fast; sorted input can make h=n−1. **Expected time claims need an explicit input/random-tree model**; never describe every BST as O(log n). Two-child delete must preserve both key **and** value when replacing the target with the in-order successor. Recursion may use O(h+1) stack; iterative lookup can use O(1) additional space.

### 2.5 Cost comparison under a unit-cost key-comparison model
| Representation | Lookup worst case | `put` worst case (unique keys) | `delete` worst case | Notes |
|---|---|---|---|---|
| Unsorted array of pairs | Θ(n) | Θ(n) with duplicate check | Θ(n) | Contiguous references, possible shifts |
| Unsorted singly linked list | Θ(n) | Θ(n) with duplicate check | Θ(n) | Link updates O(1) **after finding target** |
| Plain BST | O(h+1), O(n) worst case | O(h+1) | O(h+1) | Shape depends on input; not automatically balanced |

The model treats fixed-size integer comparisons and pointer operations as O(1); Python allocation, garbage collection and cache effects are outside the asymptotic model. Student implementations may have different constants or memory footprints.

## 3. How to test correctness before measuring speed (00:35–00:52)
Ask students to first write **examples of expected behaviour**, then a test. A strong starting matrix: empty lookup (missing), empty delete (missing), single insertion and retrieval, update existing key, two different keys, delete first/head/root, delete one-child and two-child BST nodes, repeated operations, size invariant, contains absent/present, sorted insertion (degenerate BST), negative/zero key, allowed arbitrary values including `None`. If values may be `None`, membership must not be inferred from `get` returning `None`.

**Differential testing:** use a fresh Python `dict` as an observable-behaviour oracle for a scripted operation sequence, adapting its missing-key semantics where necessary. Oracle agreement on sampled cases is **evidence**, not a mathematical proof. Never compare internal traversal order when the contract does not promise one. Use a deterministic seed and fail fast on the first mismatch.

**Correctness reasoning:** Array invariant is preserved if overwrites replace rather than append; list invariant if each new key is absent and links remain connected; BST invariant if every comparison chooses the appropriate subtree and delete reconnects children correctly. Termination follows when scans advance to the next item or BST descent follows one child per step in a finite acyclic structure. Show one counterexample each: duplicate keys in array, lost `next` during list deletion, successor copied without value in BST.

## 4. Demonstrate reproducible performance measurement (00:52–01:10)
**Say:** “A fast wrong answer is not a valid success. We test correctness first; only then do we time.” Explain the measurement pipeline:

1. Choose **the same operation and same input keys** for all implementations.
2. Define n (number of bindings) and a workload: building the table, hit lookup, miss lookup, update, deletion. Measure these **separately**; do not hide setup cost inside a lookup if comparing lookups.
3. Use `random.Random(42)` to generate **once**, then reuse immutable input sequences. Include sorted, random-order and miss-heavy distributions.
4. **Warm up**, repeat e.g. 5–9 times, report a **median** instead of relying on one noisy sample. This is a teaching default, not an assignment rubric.
5. Use `time.perf_counter_ns()` and enough operations to exceed timer resolution. Record environment, Python version, hardware, OS, number of operations, n, random seed and units.
6. Verify output or checksum **outside timed region** where possible; otherwise prevent an “optimised-away”/missing-work measurement. In Python, avoid timed printing and notebook display.
7. Plot **median time per operation** (microseconds) against n, or use time ratios such as T(2n)/T(n). Explain noise, cache and allocation effects. No plot proves an asymptotic class by itself.

**Live demo:** first time successful lookups of a built-in `dict`; then compare a simple list scan for the *same* hit keys. Describe this as a **methodology demonstration**, not a stand-in for the official three-implementation benchmark. Build the data before starting lookup timings. Run on moderate sizes to keep Colab responsive. Record, do not invent, observed outcomes.

## 5. Guided 95-minute studio (01:10–02:45)
Use the notebook in this order. Students can work in pairs for *peer review*, but keep ownership of their own work under institution rules (not yet specified for grading).

**Phase A — 20 minutes: API and tests.** Student writes the chosen missing-key behaviour, invariants and two tests for each operation. Run the supplied baseline tests. Identify one failing boundary case that a superficially correct implementation could miss.

**Phase B — 30 minutes: scaffold.** In `starter.py` or notebook, implement one operation at a time: array `get` then `put` then `delete`; linked-list search plus head/non-head delete; BST iterative search, insert, then deletion cases. Do not distribute a finished code solution. Pair-share an invariant before each destructive update. The instructor offers *hints* (e.g., “What should point to the node after the deleted one?”), not completed methods.

**Phase C — 25 minutes: data generation and fair run.** Choose n such as 100, 500, 1000 for a quick teaching trial; after correctness passes, use the benchmark helper on each finished table. Measure both sorted and shuffled insertions for the plain BST, count comparisons or height if timings are noisy, and retain the same random seed for each trial.

**Phase D — 20 minutes: peer review and report.** A peer verifies one missing-key test, one BST deletion case and benchmark fairness. Students produce a table with n, workload, implementation, median time, repetitions and one caveat. If a structure remains unfinished, label data **not measured** rather than inventing a number. Explain what would convince them of the correctness argument beyond a handful of tests.

**Offline fallback:** use graph paper to trace the same operation sequence and count key comparisons for n=4,8,16. This is analytical/trace evidence, not a hardware benchmark.

## 6. Wrap-up and individual next steps (02:45–03:00)
Ask each student for one **contract invariant**, one **edge-case test**, and one **benchmark confounder**. Have them complete: “For workload ___, I would choose ___, provided ___; a limitation is ___.” Encourage careful documentation and precise negative results. Reiterate: pending institution-approved rules govern the actual graded assignment.

## 7. Suggested instructor prompts and likely misconceptions
- “Does O(1) list prepend make the **entire** `put` O(1) when duplicates must be rejected?” No: checking uniqueness may take O(n).
- “Why is `None` not a reliable not-found marker?” It might be a legitimate stored value.
- “Why is a plain BST not guaranteed logarithmic?” Its height can be linear with ordered insertions.
- “Why separate build time from lookup?” Otherwise the result mixes costs and cannot isolate a chosen operation.
- “Can a single Colab run prove Θ(n)?” No. Complexity requires a model/argument; measurements only support or challenge hypotheses.
- “What if an operation fails a correctness test but is faster?” Exclude it from a performance conclusion about conforming implementations.
- “How should I describe surprising measurements?” Record units, workload, n, environment, repeats and variance before interpreting.

## 8. References and academic notes
Official M12 Module Descriptor (3 contact hours, Assignment 1 scope); approved `course-plan.md` S05. CLRS, *Introduction to Algorithms*, 4th ed. (2022), binary search trees and experimental reasoning; Goodrich et al. (2013), linear structures and map ADTs; Sedgewick & Wayne (2011), symbol tables. All examples and diagrams in this package are original teaching material. No official marking rubric, weight per assignment, due date or compulsory implementation language is asserted.
