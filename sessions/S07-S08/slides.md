# Editable slide source — S07 + S08

## Slide 01 — Hash tables, heaps & sorting
Outcome: C1, C2, K1, S1
Visible: M12: S07 + S08 / 90 minutes each / Python demonstrations
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 3 minutes. Introduce key lookup versus priority retrieval. Ask students for a real example.

## Slide 02 — Map ADT
Outcome: C1, C2, K1, S1
Visible: put: insert or replace / get: retrieve / delete: remove
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 7 minutes. Recall S04 symbol tables. Ask whether ordering is required.

## Slide 03 — Hash functions
Outcome: C1, C2, K1, S1
Visible: index = hash(key) mod m / equal keys hash equally / collisions are possible
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 8 minutes. For m=8, ask where keys 1,9,17 land. Explain key stability.

## Slide 04 — Separate chaining
Outcome: C1, C2, K1, S1
Visible: bucket 1: 1 → 9 → 17 / scan one bucket / update without duplication
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 9 minutes. Trace deleting 9. State bucket invariant and termination.

## Slide 05 — Load factor
Outcome: C1, C2, K1, S1
Visible: α = n/m / expected O(1+α) lookup / worst O(n)
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 8 minutes. Explain uniform hashing and constant hash cost assumptions. Geometric growth gives expected amortised constant insertion.

## Slide 06 — Linear probing
Outcome: C1, C2, K1, S1
Visible: 1: key 1 / 2: key 9 / 3: key 17 / 4: EMPTY
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 8 minutes. Trace modulo wrap-around. Discuss primary clustering and bounded m probes.

## Slide 07 — Tombstones
Outcome: C1, C2, K1, S1
Visible: 1: key 1 / 2: DELETED / 3: key 17 / 4: EMPTY
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 7 minutes. Ask why deletion cannot write EMPTY. Update 17 without duplicate; then reuse a tombstone.

## Slide 08 — Resize & choice
Outcome: C1, C2, K1, S1
Visible: rehash records / track live and used slots / BST supports ordered queries
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 5 minutes. Compare chaining space Θ(m+n) with probing Θ(m). Cache locality depends on representation. Worst probing O(m).

## Slide 09 — Guided Python demo
Outcome: C1, C2, K1, S1
Visible: insert collisions / delete and update / verify resize
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 20 minutes. Run notebook map classes and tests. Predict outputs before execution. Discuss bounded probes.

## Slide 10 — Pair exercise
Outcome: C1, C2, K1, S1
Visible: capacity 7; keys 5,12,19,6 / delete 12 / trace hit and miss
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 15 minutes. Use exercises 1–2, then compare answers orally. Do not display an answer key.

## Slide 11 — Priority queue ADT
Outcome: C1, C2, K4, S2
Visible: insert / peek / extract highest priority
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 10 minutes. Use a task scheduler. Distinguish priority from FIFO and discuss equal priority tie-breaking.

## Slide 12 — Binary heap invariant
Outcome: C1, C2, K4, S2
Visible: parent ≥ children / complete binary tree / root is maximum
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 7 minutes. Draw array [9,5,7,2,3]. Parent (i−1)//2, children 2i+1 and 2i+2. Heap is not sorted.

## Slide 13 — Sift up & down
Outcome: C1, C2, K4, S2
Visible: push: append, move up / pop: move last to root, move down
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 7 minutes. Insert 8 into example heap; then pop 9. Only one path can violate the invariant. Worst logarithmic, peek constant.

## Slide 14 — Bottom-up heapify
Outcome: C1, C2, K4, S2
Visible: start at n//2−1 / sift down towards index zero / Θ(n) time
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 6 minutes. Trace [3,1,6,5,2,4]. Child subtrees already heaps. Explain geometric sum of node heights.

## Slide 15 — Heapsort
Outcome: C1, C2, K4, S2
Visible: build max-heap / swap root with last active item / shrink and sift
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 7 minutes. Trace [4,1,3,2]. Invariant sorted suffix, heap prefix. Worst Θ(n log n), O(1) auxiliary space, unstable.

## Slide 16 — Insertion sort
Outcome: C1, C2, K4, S2
Visible: grow sorted prefix / shift strictly larger keys / insert into gap
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 7 minutes. Trace [4,2,4,1] with labels. Explain stability, Θ(n) best and Θ(n²) worst, adaptivity to inversions.

## Slide 17 — Comparison lower bound
Outcome: C1, C2, K4, S2
Visible: n! possible orderings / ≥ n! leaves / worst Ω(n log n)
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 6 minutes. For distinct keys, each binary comparison has at most two outcomes. Not a claim about all inputs or noncomparison sorts.

## Slide 18 — Guided sorting lab
Outcome: C1, C2, K4, S2
Visible: test heaps and sorts / compare random, sorted, reverse / median of five runs
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 25 minutes. Execute notebook. Keep input copies outside timing; verify sorted output. Report measurement limitations.

## Slide 19 — Practice & exit ticket
Outcome: C1, C2, K4, S2
Visible: trace heap push/pop / compare stability / justify lower bound
Visual: editable rows; trace the displayed states on the board as appropriate.
Speaker notes: 15 minutes. Use exercises 3–4. Ask students to explain one correctness invariant and one complexity assumption. Assign independent study.