# M12 — Data Structures and Algorithms: Course Plan

> **Status: DRAFT — lecturer approval required.** Prepared from the three-page official Ascencia Malta M12 Module Descriptor provided on 22 October 2026. This is a teaching proposal, **not** an amendment to academic rules.

## 1. Module Requirements Summary

### A. Official requirements — fixed by the descriptor

| Item | Official requirement |
|---|---|
| Institution/programme | Ascencia Malta — Master of Science (MSc) in Computer Science |
| Module code/title | M12 — Data Structures and Algorithms |
| MQF/EQF / ECTS | Level 7 / 12 ECTS |
| Total student workload | **300 hours** |
| Contact teaching | **60 hours: 20 face-to-face sessions of 3 hours** |
| Self-study | **212 hours** |
| Assessment hours | **28 hours** |
| Teaching approaches | Lectures, lab sessions, tutorials |
| Status | Compulsory for CS track; elective for other MSc tracks |
| Assessment | Closed-book written exam **60%** (2.5 hours); **four programming assignments 40% in total** |
| Official assignment slots | Assignment 1 at **S05**; Assignment 2 at **S10**; Assignment 3 at **S15**; Assignment 4 at **S19** |
| Implementation | **Python and C++**; correctness and empirical performance analysis across assignments |
| Final teaching session | Competitive-programming workshop plus exam preparation |

**Official module scope:** ADTs and arrays, dynamic arrays, linked lists, stacks, queues, BSTs, AVL trees, red-black trees, B-trees, splay trees, heaps, hash tables, graphs and disjoint sets; Big-O / Big-Omega / Big-Theta, amortised analysis (aggregate/accounting/potential), recurrences and Master Theorem, loop invariants and correctness; insertion, merge, quick, heap, counting, radix and bucket sorts; searching/selection; DP (Fibonacci, matrix chain, LCS, 0/1 knapsack); greedy (activity selection and Huffman); BFS, DFS, topological sort, Dijkstra, Bellman–Ford, Floyd–Warshall, Prim and Kruskal; NP-completeness and approximation. Includes real-world memory/cache trade-offs and Python/C++ performance profiling.

**Official assessment specifics (preserved):**

1. **S05, Assignment 1:** array-based, linked-list-based and BST-based symbol tables, correctness and empirical comparison.
2. **S10, Assignment 2:** heapsort, quicksort with **three-way partitioning**, and mergesort; benchmark input sizes from **10^4 to 10^7**.
3. **S15, Assignment 3:** implement **LCS, matrix-chain multiplication and 0/1 knapsack with memoisation**.
4. **S19, Assignment 4:** implement **BFS, DFS, Dijkstra, Kruskal and Prim** on a **real-world dataset**, for example a road network or social graph.
5. **Written exam:** 2.5 hours, closed book; algorithm analysis and recurrences, data-structure complexity and proofs, sorting/graph traces, DP formulation and NP-completeness.

The four assignment weights **within the 40%** and the meaning of the specified session numbers (release, workshop, submission or due date) are **not defined** in the supplied descriptor. Do not impose equal weights or submission deadlines without institutional/lecturer approval.

### Official learning outcomes — reference key

The descriptor presents outcomes under three headings, without official IDs. The labels below are **local planning references only** and do not change their wording or status.

**Competences:**

- **C1:** Design and implement fundamental data structures with correct time and space complexity.
- **C2:** Select appropriate data structures and algorithms for a given problem, justifying the choice analytically.
- **C3:** Analyse algorithm correctness using loop invariants and recurrence relations.
- **C4:** Apply dynamic programming and greedy paradigms to optimisation problems.
- **C5:** Implement and evaluate graph algorithms for shortest path, spanning tree, and traversal problems.
- **C6:** Measure and compare empirical performance of algorithms against theoretical predictions.

**Knowledge and understanding:**

- **K1:** Define arrays, linked lists, stacks, queues, trees, heaps, hash tables, and graphs as abstract data types.
- **K2:** Recall Big-O, Big-Omega, Big-Theta notation and apply them to classify algorithm complexity.
- **K3:** Describe the Master Theorem and apply it to divide-and-conquer recurrences.
- **K4:** Identify the properties of comparison-based sorting lower bounds (Omega(n log n)).
- **K5:** Understand the P vs NP relationship and its implications for algorithm design.
- **K6:** Recall amortised analysis methods: aggregate, accounting, and potential methods.

**Skills:**

- **S1:** Implement binary search trees, AVL trees, and hash tables with chaining and open addressing.
- **S2:** Trace quicksort, mergesort, and heapsort on sample inputs, accounting for worst/average/best cases.
- **S3:** Write dynamic programming solutions with memoisation and bottom-up tabulation.
- **S4:** Apply BFS and DFS systematically, including cycle detection and topological ordering.
- **S5:** Run Dijkstra's and Bellman-Ford shortest path algorithms on weighted directed graphs.
- **S6:** Profile Python and C++ implementations and interpret performance benchmarks.

**Official core reading:**

- Cormen, Leiserson, Rivest & Stein (2022), *Introduction to Algorithms*, 4th ed., MIT Press.
- Goodrich, Tamassia & Goldwasser (2013), *Data Structures and Algorithms in Python*, Wiley.
- Sedgewick & Wayne (2011), *Algorithms*, 4th ed., Addison-Wesley.
- Skiena (2020), *The Algorithm Design Manual*, 3rd ed., Springer.

### B. Decisions requiring lecturer/institutional approval

| Decision | Proposed default | Why it remains open |
|---|---|---|
| Primary lecture language | Teach/program first in Python, validate selected implementations/benchmarks in C++ | Both Python and C++ are required; exact use per assessed deliverable is unspecified |
| Environment | Python 3 + Jupyter/Colab for small labs; C++17 locally or in an approved browser compiler | Student devices, access and institutional policies not specified |
| Four assignment weights | **TBD**, summing to the official 40% | Equal 10% each would be a new rule, not part of the descriptor |
| Assignment meaning of S05/S10/S15/S19 | Teaching/workshop checkpoints at the listed sessions; deadlines **TBD** | Descriptor does not define whether dates are releases or deadlines |
| Examination calendar | **TBD**; keep its 2.5-hour duration and 60% weight | Descriptor does not say whether examination occurs within the 60 contact hours |
| Assessment-hour allocation | **TBD**, preserving 28 hours in total | Descriptor does not split 28 hours between assignments and exam |
| Lab submissions and marking rubrics | Standardised tests + complexity reasoning + performance evidence; detailed rubrics **TBD** | Descriptor fixes topics, not precise rubric or submission format |
| Python/C++ distribution across assignments | Require clear engagement with both languages; verify assignment-by-assignment requirements before setting tasks | Avoid silently weakening the descriptor's dual-language emphasis |
| Real-world graph dataset | Choose one documented, legally reusable graph with reproducible loading | Dataset/size/edge-weight semantics must be approved |
| Large sorting benchmarks | Preserve official 10^4–10^7 range, with staged or provided hardware to avoid excluding students | 10^7 may exceed memory/time on some student machines |
| Exact class schedule, prerequisite courses and academic policies | **TBD** | Not included in the supplied descriptor |
| Repository default branch | Use a **single** default branch; prefer `main` if renamed before publication | Newly inspected repository is empty but its current default is `master` |

### C. Optional pedagogical enhancements (not academic requirements)

- Open each session with a two-minute prediction question; end with an exit ticket testing algorithm choice, correctness or complexity.
- Alternate explanation, diagram tracing, short pair work and hands-on tasks; use projected editable diagrams rather than dense bullet slides.
- Provide small supplied datasets, deterministic random seeds, explicit edge-case tests and timing instructions.
- Use offline-ready Python scripts and C++ files as fallback if Colab or connectivity fails.
- Prepare a separate **private** instructor solutions archive; never publish answer keys alongside student assignments.
- Add an exam-style tracing question after each major section, while protecting the official 60%/40% assessment scheme.

## 2. Course-level instructional design (proposed)

**Progression:** reasoning and memory structures (S01–S07) → sorting and selection (S08–S11) → greedy/DP design (S12–S15) → graph algorithms (S16–S19) → complexity limits and synthesis (S20).

**Teaching pattern:** the ordinary 180-minute session is planned as 15 minutes retrieval/prediction, 45 minutes illustrated explanation, 45 minutes algorithm walk-through, 60 minutes supervised exercise and 15 minutes wrap-up/exit ticket. In assessed-studio sessions, allow 10 minutes briefing, 25 minutes targeted review, 35 minutes guided example, 95 minutes practical work and 15 minutes check-out. Break arrangements must follow institution policy and may require adapting these timings.

**Source-of-truth order:** official descriptor → approved course plan → approved `lecture.md` → slides, exercises and practical lab. Keep approved files stable; changes should be justified in clear direct-to-default-branch commits after professor approval. Each session package will later provide a 3-hour agenda, a detailed `lecture.md`, editable 16:9 PPTX with speaker notes, `exercises.md` without solutions, and a lab only when appropriate. No session packages are generated at this initial phase.

**Self-study allocation:** an **illustrative** distribution, not a mandated weekly quota, assigns 10 hours to each of 16 regular sessions and 13 hours to each of the four assignment checkpoint sessions = **212 hours**. The official **28 assessment hours** are a separate workload category and are **not allocated here** pending clarification. The three official categories total 60 + 212 + 28 = **300 hours**.

**Programming strategy:** Python is used for rapid visualisation, tracing, correctness tests and accessible exercises. C++ is used for explicit memory/allocator/cache discussions and comparable profiled implementations. For fair benchmarking, disclose interpreter/compiler versions, optimisation flags, machine specs, input distributions, warm-up and repeated-run procedure. Timing comparisons are evidence of observed behaviour, not proof of asymptotic complexity. Do not claim Python and C++ are directly comparable without controlling for algorithm, data and run conditions.

**Technical quality gates (for later sessions):** check mathematical claims and asymptotic assumptions; execute code/test edge cases; verify speaker notes and slide readability; confirm GitHub/Colab relative links; cite source material; clearly distinguish teaching simplifications from formal claims; obtain lecturer academic approval separately from technical checks.

## 3. Session-by-session map

All 20 sessions have **3 contact hours**, for a total of **60**. Outcome codes are local references defined above. Session 5/10/15/19 are descriptor-prescribed assignment checkpoints; all timings and other session placements are proposals.

| Session | Topic | Contact | Self-study* | Core outcomes | Deliverable or emphasis |
|---|---|---:|---:|---|---|
| S01 | Algorithmic thinking, abstract data types and asymptotic analysis | 3 h | 10 h | C2, C3, C6, K1, K2 | Concepts, tracing and hands-on lab |
| S02 | Recursion, recurrences, Master Theorem and binary search | 3 h | 10 h | C2, C3, K2, K3 | Concepts, tracing and hands-on lab |
| S03 | Arrays, dynamic arrays, linked lists and amortised costs | 3 h | 10 h | C1, C2, C6, K1, K6, S6 | Concepts, tracing and hands-on lab |
| S04 | Stacks, queues, binary search trees and symbol tables | 3 h | 10 h | C1, C2, K1, S1 | Concepts, tracing and hands-on lab |
| S05 | Assignment 1 studio — symbol-table implementations and benchmarking | 3 h | 13 h | C1, C2, C6, S1, S6 | **A1 checkpoint** |
| S06 | Balanced search trees: AVL, red-black, splay and B-trees | 3 h | 10 h | C1, C2, K6, S1 | Concepts, tracing and hands-on lab |
| S07 | Hash tables: chaining, open addressing and memory trade-offs | 3 h | 10 h | C1, C2, K1, S1 | Concepts, tracing and hands-on lab |
| S08 | Heaps, priority queues, insertion sort and sorting lower bounds | 3 h | 10 h | C1, C2, K4, S2 | Concepts, tracing and hands-on lab |
| S09 | Merge sort, quicksort and three-way partitioning | 3 h | 10 h | C3, C6, K3, K4, S2 | Concepts, tracing and hands-on lab |
| S10 | Assignment 2 studio — sorting benchmarks at scale | 3 h | 13 h | C6, K4, S2, S6 | **A2 checkpoint** |
| S11 | Linear-time sorting, searching and selection | 3 h | 10 h | C2, C3, K4, S2 | Concepts, tracing and hands-on lab |
| S12 | Greedy design: activity selection and Huffman coding | 3 h | 10 h | C2, C3, C4 | Concepts, tracing and hands-on lab |
| S13 | Dynamic programming foundations: state, recurrence and evaluation order | 3 h | 10 h | C3, C4, S3 | Concepts, tracing and hands-on lab |
| S14 | Dynamic programming: LCS, matrix-chain multiplication and 0/1 knapsack | 3 h | 10 h | C3, C4, S3 | Concepts, tracing and hands-on lab |
| S15 | Assignment 3 studio — dynamic programming implementation and analysis | 3 h | 13 h | C3, C4, C6, S3 | **A3 checkpoint** |
| S16 | Graphs: representations, BFS, DFS, cycles and topological order | 3 h | 10 h | C2, C5, K1, S4 | Concepts, tracing and hands-on lab |
| S17 | Shortest paths: Dijkstra, Bellman–Ford and Floyd–Warshall | 3 h | 10 h | C3, C5, S5 | Concepts, tracing and hands-on lab |
| S18 | Minimum spanning trees, disjoint sets and graph engineering | 3 h | 10 h | C2, C5, S4, S5 | Concepts, tracing and hands-on lab |
| S19 | Assignment 4 studio — graph algorithms on a real-world dataset | 3 h | 13 h | C5, C6, S4, S5, S6 | **A4 checkpoint** |
| S20 | NP-completeness, approximation, competitive programming and exam review | 3 h | 10 h | C2, C3, C4, C5, K5 | Capstone and exam preparation |

\* Illustrative allocation; not an official requirement.

## 4. Detailed session briefs

### S01 — Algorithmic thinking, abstract data types and asymptotic analysis

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C2, C3, C6, K1, K2.
- **Prerequisite knowledge:** Comfort with variables, loops, functions and elementary maths.
- **Core concepts/data structures/algorithms:** Algorithm specifications and input size; abstract data type (ADT) versus implementation; best, average and worst case; Big-O, Big-Omega and Big-Theta; time and auxiliary-space complexity; introduction to loop invariants.
- **Mathematical/computational foundations:** Counting operations; growth-rate comparisons; elementary bounds and proof obligations.
- **Guided practical activity:** Trace linear search and duplicate detection; time small Python and C++ loops on increasing inputs; discuss measurement noise.
- **Real-world application:** Why a seemingly simple membership check becomes expensive at scale.
- **Student exercise:** Classify five code snippets, state their assumptions, and justify an invariant for a search loop.
- **Expected learning achievement:** Explain asymptotic bounds and distinguish empirical timings from complexity proofs.
- **Independent study/homework:** Review logarithms, growth functions and correctness arguments; complete complexity trace problems.

### S02 — Recursion, recurrences, Master Theorem and binary search

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C2, C3, K2, K3.
- **Prerequisite knowledge:** S01 complexity notation and loop invariants.
- **Core concepts/data structures/algorithms:** Recursion and call stacks; induction; recurrence construction; substitution/recursion tree intuition; Master Theorem with applicability conditions; iterative and recursive binary search.
- **Mathematical/computational foundations:** T(n)=aT(n/b)+f(n); O(log n); proof of binary-search correctness and termination.
- **Guided practical activity:** Draw recursion trees; code binary search with boundary tests; compare recursive and iterative memory use.
- **Real-world application:** Search in sorted catalogues, range lookups and divide-and-conquer design.
- **Student exercise:** Trace recursive calls, solve supported recurrences and debug an off-by-one binary-search defect.
- **Expected learning achievement:** Build and solve common divide-and-conquer recurrences and justify binary search.
- **Independent study/homework:** Work recurrence exercises and explain cases where the Master Theorem does not apply.

### S03 — Arrays, dynamic arrays, linked lists and amortised costs

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C1, C2, C6, K1, K6, S6.
- **Prerequisite knowledge:** S01–S02 analysis; basic references and collections.
- **Core concepts/data structures/algorithms:** Contiguous storage; fixed and resizable arrays; singly and doubly linked lists; indexing, insert/delete and traversal; geometric resizing; cache locality, allocation and pointer overhead.
- **Mathematical/computational foundations:** Amortised analysis by aggregate, accounting and potential methods; worst-case versus amortised append.
- **Guided practical activity:** Implement a minimal dynamic array or instrument Python list growth; implement linked-list insert/remove; compare access and append costs.
- **Real-world application:** Resizable buffers versus frequent middle insertions in data pipelines.
- **Student exercise:** Predict memory access patterns, trace reallocations and choose array versus list for given workloads.
- **Expected learning achievement:** Defend data-structure choices using operation costs and practical memory effects.
- **Independent study/homework:** Prove amortised append under a stated resizing policy and benchmark sequential traversal.

### S04 — Stacks, queues, binary search trees and symbol tables

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C1, C2, K1, S1.
- **Prerequisite knowledge:** S02 recursion and S03 sequential structures.
- **Core concepts/data structures/algorithms:** Stack and queue ADTs; LIFO/FIFO operations and implementations; symbol-table interface; unbalanced BST invariants, search, insert, delete and traversal; degenerate-tree cases.
- **Mathematical/computational foundations:** O(h) BST operations; balanced versus worst-case height; operation-level correctness invariants.
- **Guided practical activity:** Use stacks for delimiter matching, queues for task dispatch, and build a minimal BST-backed key/value symbol table.
- **Real-world application:** Compilers, task scheduling and ordered key lookup.
- **Student exercise:** Trace BST insertion and deletion; compare array-, linked-list- and BST-based symbol-table operations.
- **Expected learning achievement:** Implement and explain the three implementations required for Assignment 1.
- **Independent study/homework:** Prepare small correctness tests and baseline symbol-table benchmark harness.

### S05 — Assignment 1 studio — symbol-table implementations and benchmarking

- **Duration and linked outcomes:** 3 contact hours; 13 proposed independent-study hours; C1, C2, C6, S1, S6.
- **Prerequisite knowledge:** S03–S04 arrays, linked lists, BSTs and benchmarking.
- **Core concepts/data structures/algorithms:** Comparable symbol-table APIs; correctness criteria; input distributions; benchmark fairness; reporting trade-offs.
- **Mathematical/computational foundations:** Expected and worst-case operation costs; measured scaling with input size; BST shape dependency.
- **Guided practical activity:** Assignment 1 checkpoint: implement and compare array-, linked-list- and BST-backed symbol tables; run reproducible Python/C++ experiments where appropriate.
- **Real-world application:** Choosing in-memory indexes for small versus large collections.
- **Student exercise:** Peer-review test cases, compare timings and explain surprising results.
- **Expected learning achievement:** Produce evidence that implementation correctness and observed performance can both be evaluated.
- **Independent study/homework:** Complete the official Assignment 1 deliverable according to the institution-approved release/deadline policy.

### S06 — Balanced search trees: AVL, red-black, splay and B-trees

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C1, C2, K6, S1.
- **Prerequisite knowledge:** S04 BST invariant and S03 amortised reasoning.
- **Core concepts/data structures/algorithms:** Tree rotations; AVL balance and insertion; red-black properties and bounded height; splay operations and amortised access; B-tree nodes and disk-aware indexing.
- **Mathematical/computational foundations:** Balanced-tree height O(log n); rotation cases; amortised versus worst-case guarantees for splay trees.
- **Guided practical activity:** Implement AVL insertion/rotation cases; use traces or supplied demonstrators for red-black, splay and B-tree behaviour.
- **Real-world application:** Ordered maps, filesystem/database indexes and locality-aware storage.
- **Student exercise:** Trace rotations; choose a tree for workloads requiring predictability, locality or working-set performance.
- **Expected learning achievement:** Implement core AVL operations and explain the different guarantees of four balanced-tree families.
- **Independent study/homework:** Study red-black and B-tree invariants and construct a splay trace; full implementations are extension work.

### S07 — Hash tables: chaining, open addressing and memory trade-offs

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C1, C2, K1, S1.
- **Prerequisite knowledge:** S04 symbol-table ADT and S03 memory concepts.
- **Core concepts/data structures/algorithms:** Hash functions, capacity and load factor; collision handling with chaining and probing; tombstones; rehashing; expected versus worst-case complexity; cache implications.
- **Mathematical/computational foundations:** Expected O(1) under hashing assumptions; probe sequences; resizing amortisation.
- **Guided practical activity:** Implement a chained table and an open-addressed table with tests for collisions, deletion and resizing.
- **Real-world application:** Caches, dictionaries, deduplication and high-volume lookup.
- **Student exercise:** Diagnose a failed probing sequence and evaluate BST versus hashing when ordering matters.
- **Expected learning achievement:** Implement both required collision-resolution approaches and articulate assumptions behind performance.
- **Independent study/homework:** Benchmark hit/miss operations across load factors and document distributions used.

### S08 — Heaps, priority queues, insertion sort and sorting lower bounds

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C1, C2, K4, S2.
- **Prerequisite knowledge:** S03 arrays and S01 complexity.
- **Core concepts/data structures/algorithms:** Binary heap invariants; sift-up/sift-down; heap construction; priority-queue interface; heapsort; insertion sort; comparison-sort decision-tree intuition.
- **Mathematical/computational foundations:** Heapify O(n); extract O(log n); heapsort O(n log n); comparison lower bound Omega(n log n).
- **Guided practical activity:** Implement a binary heap, run a heap-sort trace and compare insertion-sort cases.
- **Real-world application:** Schedulers and priority-driven systems.
- **Student exercise:** Hand-trace heap operations, identify stable/unstable sorts and justify when insertion sort wins for tiny inputs.
- **Expected learning achievement:** Implement heapsort and explain the lower bound for comparison sorting.
- **Independent study/homework:** Prepare trace tables and benchmark small-input insertion sort versus heapsort.

### S09 — Merge sort, quicksort and three-way partitioning

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C3, C6, K3, K4, S2.
- **Prerequisite knowledge:** S02 recurrences and S08 sorting principles.
- **Core concepts/data structures/algorithms:** Divide-and-conquer sorting; merge sort; quicksort; pivot selection; Lomuto/Hoare concepts; Dutch national flag three-way partition; stability and memory trade-offs.
- **Mathematical/computational foundations:** Merge T(n)=2T(n/2)+Theta(n); quicksort best/average/worst-case reasoning; recursion-stack usage.
- **Guided practical activity:** Trace and implement merge sort and quicksort with three-way partitioning; design duplicate-heavy datasets.
- **Real-world application:** Sorting log data with different key distributions.
- **Student exercise:** Explain a quadratic quicksort case and select a sort given memory or stability constraints.
- **Expected learning achievement:** Trace both algorithms accurately and justify input-sensitive performance differences.
- **Independent study/homework:** Prepare reproducible generators for random, sorted, reversed and duplicate-heavy inputs.

### S10 — Assignment 2 studio — sorting benchmarks at scale

- **Duration and linked outcomes:** 3 contact hours; 13 proposed independent-study hours; C6, K4, S2, S6.
- **Prerequisite knowledge:** S08–S09 heapsort, mergesort and three-way quicksort.
- **Core concepts/data structures/algorithms:** Benchmark protocol; input size scaling; warm-up, repeated runs and timing variability; memory exhaustion and reproducibility.
- **Mathematical/computational foundations:** Theoretical n log n versus quadratic trends; log-log or normalised timing analysis.
- **Guided practical activity:** Assignment 2 checkpoint: test heapsort, three-way quicksort and mergesort; benchmark across the mandated 10^4 to 10^7 size range with appropriate hardware planning.
- **Real-world application:** Selecting sorting strategies for production workloads.
- **Student exercise:** Prepare a benchmark report with plots, method, limitations and observed deviations.
- **Expected learning achievement:** Interpret empirical evidence without confusing observed runtimes with formal bounds.
- **Independent study/homework:** Complete Assignment 2 analysis, including resource-aware repeatable large-input measurements.

### S11 — Linear-time sorting, searching and selection

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C2, C3, K4, S2.
- **Prerequisite knowledge:** S08–S10 sorting and recurrence analysis.
- **Core concepts/data structures/algorithms:** Counting, radix and bucket sorts; assumptions for non-comparison sorting; linear versus binary search review; quickselect and order statistics.
- **Mathematical/computational foundations:** Counting O(n+k); radix O(d(n+k)) under explicit model; quickselect expected versus worst-case bounds.
- **Guided practical activity:** Code a counting/radix example for bounded integer keys; implement/trace quickselect.
- **Real-world application:** Integer identifier pipelines and percentile extraction.
- **Student exercise:** Decide when counting/radix/bucket sorting is legal and advantageous, including key-range and distribution caveats.
- **Expected learning achievement:** Explain why linear-time sorting does not contradict comparison lower bounds.
- **Independent study/homework:** Compare asymptotic cost, extra memory and domain assumptions in a selection/sorting worksheet.

### S12 — Greedy design: activity selection and Huffman coding

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C2, C3, C4.
- **Prerequisite knowledge:** S01 proof intuition and S11 ordering.
- **Core concepts/data structures/algorithms:** Greedy-choice property; optimal substructure; exchange arguments; counterexamples; activity selection; Huffman coding with priority queues.
- **Mathematical/computational foundations:** Correctness arguments using exchange proofs; sort-plus-scan and heap complexity.
- **Guided practical activity:** Implement activity selection and trace Huffman tree construction.
- **Real-world application:** Meeting scheduling and prefix-code compression.
- **Student exercise:** Invent a counterexample to an invalid greedy rule; contrast greedy and exhaustive search.
- **Expected learning achievement:** State assumptions under which a greedy strategy is correct and recognise when it fails.
- **Independent study/homework:** Write one concise exchange proof and solve additional greedy-choice counterexamples.

### S13 — Dynamic programming foundations: state, recurrence and evaluation order

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C3, C4, S3.
- **Prerequisite knowledge:** S02 recursion and S12 optimisation concepts.
- **Core concepts/data structures/algorithms:** Overlapping subproblems; optimal substructure; defining a state; recurrence and base cases; Fibonacci; memoisation versus bottom-up tabulation; reconstruction.
- **Mathematical/computational foundations:** Time/space of naive recursion versus memoisation/tabulation; correctness by induction on states.
- **Guided practical activity:** Implement Fibonacci three ways and convert a memoised solution to tabulation.
- **Real-world application:** Repeated subproblem evaluation in planning and optimisation.
- **Student exercise:** Find missing base cases, design state tables and justify evaluation order.
- **Expected learning achievement:** Derive a dynamic-programming recurrence rather than merely copying a template.
- **Independent study/homework:** Prepare state definitions and test cases for LCS, matrix chain and knapsack.

### S14 — Dynamic programming: LCS, matrix-chain multiplication and 0/1 knapsack

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C3, C4, S3.
- **Prerequisite knowledge:** S13 DP fundamentals.
- **Core concepts/data structures/algorithms:** LCS state/transition and reconstruction; matrix-chain parenthesisation; 0/1 knapsack capacity recurrence; memoisation and iterative alternatives.
- **Mathematical/computational foundations:** LCS O(mn); matrix chain O(n^3) standard DP; knapsack O(nW) pseudo-polynomial; space trade-offs.
- **Guided practical activity:** Trace 2D DP tables and code the three official Assignment 3 problems with memoisation.
- **Real-world application:** Sequence comparison, computation ordering and constrained resource allocation.
- **Student exercise:** Select states and justify transitions; test ties, empty inputs, zero capacity and repeated elements.
- **Expected learning achievement:** Formulate, implement and analyse three standard DP families.
- **Independent study/homework:** Build assignment-ready correctness tests and compare memoised with tabulated versions.

### S15 — Assignment 3 studio — dynamic programming implementation and analysis

- **Duration and linked outcomes:** 3 contact hours; 13 proposed independent-study hours; C3, C4, C6, S3.
- **Prerequisite knowledge:** S13–S14 recurrences and all three required DP problems.
- **Core concepts/data structures/algorithms:** Problem decomposition and tests; reconstructed solutions; recursion depth; pseudo-polynomial limitations.
- **Mathematical/computational foundations:** Proof of recurrence coverage and complexity for LCS, matrix chain and 0/1 knapsack.
- **Guided practical activity:** Assignment 3 checkpoint: implement LCS, matrix-chain multiplication and 0/1 knapsack with memoisation.
- **Real-world application:** Resource allocation and computational cost optimisation.
- **Student exercise:** Review edge cases and compare state-space growth against input size.
- **Expected learning achievement:** Submit explainable, tested solutions and articulate complexity and design choices.
- **Independent study/homework:** Complete official Assignment 3 submission; optionally add bottom-up comparison.

### S16 — Graphs: representations, BFS, DFS, cycles and topological order

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C2, C5, K1, S4.
- **Prerequisite knowledge:** S04 queues/stacks, S07 dictionaries and S01 complexity.
- **Core concepts/data structures/algorithms:** Directed/undirected and weighted graphs; adjacency lists/matrices; BFS and DFS; traversal forests; connectedness; directed cycle detection; topological sorting.
- **Mathematical/computational foundations:** BFS/DFS O(V+E) with adjacency lists; matrix representation trade-offs; traversal invariants.
- **Guided practical activity:** Implement BFS and DFS; derive topological order or identify a directed cycle.
- **Real-world application:** Dependency scheduling and social-network traversal.
- **Student exercise:** Predict traversal sequences with explicit neighbour ordering and detect invalid topological claims.
- **Expected learning achievement:** Choose graph representations and perform correct traversal, cycle detection and topological ordering.
- **Independent study/homework:** Prepare a well-documented graph dataset loader and tests for disconnected graphs.

### S17 — Shortest paths: Dijkstra, Bellman–Ford and Floyd–Warshall

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C3, C5, S5.
- **Prerequisite knowledge:** S16 graphs and S08 priority queues.
- **Core concepts/data structures/algorithms:** Relaxation; Dijkstra and non-negative weights; Bellman–Ford with negative edges/cycle detection; Floyd–Warshall all-pairs shortest paths.
- **Mathematical/computational foundations:** Priority-queue Dijkstra O((V+E)log V) under common binary-heap assumptions; Bellman–Ford O(VE); Floyd–Warshall O(V^3).
- **Guided practical activity:** Trace and implement Dijkstra and Bellman–Ford; inspect an all-pairs Floyd–Warshall example.
- **Real-world application:** Routing with differing edge-weight and query requirements.
- **Student exercise:** Diagnose why Dijkstra fails with negative weights and interpret negative-cycle detection.
- **Expected learning achievement:** Select and justify appropriate shortest-path algorithms for graph constraints.
- **Independent study/homework:** Benchmark sparse versus dense graphs and design negative-edge tests.

### S18 — Minimum spanning trees, disjoint sets and graph engineering

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C2, C5, S4, S5.
- **Prerequisite knowledge:** S16–S17 traversal, weighted graphs and heaps.
- **Core concepts/data structures/algorithms:** Disjoint-set union (union-find); path compression/rank; spanning trees; cut property; Kruskal and Prim; connected versus disconnected graphs; data validation.
- **Mathematical/computational foundations:** Amortised near-constant union-find operations; MST correctness and common implementation complexity bounds.
- **Guided practical activity:** Implement disjoint-set operations; implement or extend Kruskal and Prim on a representative weighted graph.
- **Real-world application:** Infrastructure network design and clustering.
- **Student exercise:** Trace edge selections, identify cycles and compare results on disconnected networks.
- **Expected learning achievement:** Explain correctness and trade-offs of two MST strategies and apply union-find appropriately.
- **Independent study/homework:** Prepare a sourced, reproducible real-world dataset and document edge semantics.

### S19 — Assignment 4 studio — graph algorithms on a real-world dataset

- **Duration and linked outcomes:** 3 contact hours; 13 proposed independent-study hours; C5, C6, S4, S5, S6.
- **Prerequisite knowledge:** S16–S18 BFS, DFS, Dijkstra, Kruskal and Prim.
- **Core concepts/data structures/algorithms:** Dataset provenance and reproducibility; algorithm preconditions; connected components; weighted paths; spanning forests; validation and performance reporting.
- **Mathematical/computational foundations:** Complexity as a function of vertices/edges; relation between density and runtimes.
- **Guided practical activity:** Assignment 4 checkpoint: implement BFS, DFS, Dijkstra, Kruskal and Prim on a real-world road or social-network dataset with a legitimate weight model.
- **Real-world application:** Network analytics and routing; avoid interpreting social-graph edges as road-distance weights.
- **Student exercise:** Validate connectivity and edge cases and explain graph-representation trade-offs.
- **Expected learning achievement:** Integrate multiple graph algorithms into a defensible real-data investigation.
- **Independent study/homework:** Complete Assignment 4 report and compare predicted versus observed performance.

### S20 — NP-completeness, approximation, competitive programming and exam review

- **Duration and linked outcomes:** 3 contact hours; 10 proposed independent-study hours; C2, C3, C4, C5, K5.
- **Prerequisite knowledge:** Entire course; especially greedy/DP and graph problems.
- **Core concepts/data structures/algorithms:** Decision problems; P, NP, NP-hard and NP-complete; reductions at a conceptual level; tractable versus intractable scaling; approximation idea and limits; integrated algorithm-choice review.
- **Mathematical/computational foundations:** Polynomial reductions and simple approximation-ratio reasoning; complexity trade-offs; exam-style recurrence/trace review.
- **Guided practical activity:** Time-boxed competitive-programming workshop with arrays/graphs/DP tasks, followed by exam tracing and justification questions.
- **Real-world application:** Deciding when exact optimisation is impractical and a justified approximation may be useful.
- **Student exercise:** Classify candidate strategies, discuss reduction claims and complete a mixed closed-book practice paper.
- **Expected learning achievement:** Explain the P vs NP distinction, recognise complexity limits and synthesise course methods.
- **Independent study/homework:** Finish the exam-revision checklist and independently solve mixed complexity, DP and graph-trace problems.

## 5. Assessment alignment and integrity

| Assessment | Fixed descriptor scope | Programme outcomes primarily demonstrated | Instructor decision still open |
|---|---|---|---|
| A1 — S05 | Array, linked list, BST symbol table; benchmarking | C1, C2, C6, S1, S6 | Relative weighting, submission format/deadline and bilingual implementation policy |
| A2 — S10 | Heapsort, 3-way quicksort, mergesort; 10^4–10^7 benchmarks | C3, C6, K4, S2, S6 | Hardware access, benchmarking protocol, submission format/deadline and weighting |
| A3 — S15 | LCS, matrix chain, 0/1 knapsack with memoisation | C3, C4, S3 | Marking method for state derivation, reconstruction and edge cases; weighting/deadline |
| A4 — S19 | BFS, DFS, Dijkstra, Kruskal, Prim on real-world data | C2, C5, C6, S4, S5, S6 | Dataset, edge semantics, rubric, weighting/deadline |
| Written exam — 60% | Closed-book 2.5 hours; complexity, proofs, sorting/graph traces, DP, NP | C2–C5, K2–K5, S2–S5 | Exact date, sample-paper availability and local examination logistics |

**Proposed common assignment evidence, subject to approval:** correct implementations, documented input assumptions, runnable tests including edge cases, theoretical complexity justification, reproducible performance measurements where applicable, and a short interpretation of results. Do not pre-publish full worked solutions in a public repo.

## 6. Repository layout and publishing workflow (proposal)

```text
data-structures-and-algorithms/
├── README.md
├── COURSE_STATUS.md
├── course-plan.md
├── module-descriptor/
│   └── original-descriptor.pdf
├── sessions/
│   ├── S01/
│   │   ├── README.md
│   │   ├── lecture.md
│   │   ├── slides.pptx
│   │   ├── exercises.md
│   │   └── lab.ipynb          # only for a session that needs Python/Colab
│   ├── S02/
│   └── ...                    # create session directories when content exists
└── resources/
    └── references.md
```

**Important:** the tree above is illustrative: no empty directories/files, dummy slide decks or placeholder notebooks should be created. C++ labs can use `lab.cpp` (plus any minimal instructions) instead of `lab.ipynb`, or both if educationally necessary. A public repo contains student-facing materials only. Keep instructor answer keys separate and private. The original three-page descriptor is stored verbatim at the proposed destination `module-descriptor/original-descriptor.pdf` if publication is approved.

**Minimal lifecycle:** draft files locally → lecturer reviews → revise same files → explicit lecturer approval → commit approved content directly on the sole default branch (ideally `main`) → update `COURSE_STATUS.md`. No feature branches, pull requests, issue-per-task tracking, Kanban board, multi-agent hierarchy or governance paperwork.

**Observed initial state on 22 October 2026:** `fajouri/data-structures-and-algorithms` is an empty **public** GitHub repository with default branch `master`. Decide whether to retain the sole `master` branch or change the default to `main` before publishing; do not create parallel permanent branches. The drafts in this document have **not** been committed.

## 7. Risks, omissions and decisions that matter

1. **Dense Level-7 syllabus:** broad balanced-tree families, multiple sorts, DP, graphs and NP-completeness all compete for 60 hours. S06 and S20 are especially compressed; use required independent reading and targeted traces instead of pretending every advanced structure receives a full coding lab.
2. **Assessment timing ambiguity:** official slots S05/S10/S15/S19 may refer to assigning, discussing or submitting work; confirm the institution's interpretation before advertising deadlines.
3. **Exam versus contact-hour accounting:** a 2.5-hour exam and the 28 assessment hours may be administratively distinct from teaching sessions; do not replace a 3-hour lecture with the exam without approval.
4. **Dual-language expectations:** Python-only coursework would underrepresent the descriptor; the exact Python/C++ submission requirement must be agreed before publishing assignments.
5. **10^7-input benchmark feasibility:** provide a supported route to large-input experiments, preserve honest memory/time limitations and never silently reduce the official range.
6. **Assignment-grade composition missing:** preserve 40% collectively, with individual weights pending approval.
7. **Unstated entry prerequisites:** S01–S03 explicitly review mathematical reasoning and programming basics to support mixed cohorts, but no official prerequisites can be claimed.
8. **Public student repository:** ensure solutions, exam-answer keys, private student work and unreleased assessment materials are not uploaded.
9. **Dataset integrity:** confirm legal access, source citation, directed/undirected semantics, non-negative weight assumptions for Dijkstra, and connectivity needs for MSTs.

## 8. Approval checkpoint and next action

**Academic decision requested:** approve or amend the 20-session progression, Python/C++ teaching strategy, and one-branch repository workflow. The lecturer/institution must additionally settle assignment weights, deadlines, exam scheduling and data/hardware policies before graded materials are published.

**Once the course plan is explicitly approved:** set plan status to **APPROVED**, retain it as the planning source of truth, publish the two approved Markdown files plus the exact descriptor on the agreed default branch, then create the **S01** teaching package (`README.md`, `lecture.md`, `slides.pptx` with notes, `exercises.md`, and an appropriate Python lab). Update `COURSE_STATUS.md` after each reviewed and approved artifact; do not generate every session's slides in advance.