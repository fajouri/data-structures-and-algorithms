# S06 — Balanced search trees

## Slide 01 — Why balanced trees?
Time: 10 min
Outcome: C1, C2, K6, S1
Visible: Predict the cost of inserting 1, 2, 3, 4, 5 into a plain BST.
Visual: chain
Speaker notes: A plain BST preserves ordering but not shape. Sorted insertion creates a chain. Ask students to count comparisons when searching for 5. Review S04 and distinguish node count from height. Today we preserve the ordered-map ADT while changing the representation.

## Slide 02 — The height problem
Time: 5 min
Outcome: C1, C2, K6, S1
Visible: Search follows one root-to-leaf path: O(h).
Visual: compare
Speaker notes: Define empty height 0 and leaf height 1. A chain has h=n; a perfect binary tree has h=log2(n+1). Search is O(h), best case constant at root. Recursive traversal uses O(h) stack. Ask whether every BST is logarithmic.

## Slide 03 — AVL invariant
Time: 6 min
Outcome: C1, C2, K6, S1
Visible: At every node: |height(left) − height(right)| ≤ 1.
Visual: avl
Speaker notes: Compute bottom-up heights, then balance factors BF=left minus right. The constraint applies globally, not merely at the root. With N(0)=0 and N(1)=1, minimum nodes N(h)=1+N(h−1)+N(h−2), giving exponential growth and logarithmic height. Ask students to compute N(3)=4.

## Slide 04 — A rotation preserves order
Time: 6 min
Outcome: C1, C2, K6, S1
Visible: Right rotation: promote the left child; move its right subtree.
Visual: rotate
Speaker notes: For y with left x and x.right=B, set y.left=B and x.right=y. Ordering A < x < B < y < C survives. Update y height before x. A rotation is constant time assuming stored heights. It may change the root; always return the new subtree root.

## Slide 05 — LL and RR
Time: 8 min
Outcome: C1, C2, K6, S1
Visible: LL → rotate right. RR → rotate left.
Visual: single
Speaker notes: Insert 30,20,10 for LL; 10,20,30 for RR. Both yield root 20 with children 10 and 30. Classify using the heavy child, not simply the last key. Students predict root and in-order traversal before showing the answer.

## Slide 06 — LR and RL
Time: 8 min
Outcome: C1, C2, K6, S1
Visible: LR → left child left, then root right. RL is the mirror.
Visual: double
Speaker notes: Trace 30,10,20: rotate left at 10, then right at 30. Trace 10,30,20 as mirror. The intermediate tree remains a BST but can still be unbalanced. Ask why one rotation alone is insufficient.

## Slide 07 — AVL insertion algorithm
Time: 8 min
Outcome: C1, C2, K6, S1
Visible: Insert like a BST → update height → rebalance → return root.
Visual: editable activity text
Speaker notes: Recursive insertion returns a subtree root. Equal keys are ignored for this set demonstration; maps instead update values. Induction: child insertion preserves ordering; rotations preserve ordering; local rebalance restores height constraint. Each ancestor costs constant work with cached heights. Worst case O(log n) time and stack; O(n) total storage. Deletion is an extension and may rebalance several ancestors.

## Slide 08 — Red-black trees
Time: 8 min
Outcome: C1, C2, K6, S1
Visible: Black root; black NIL leaves; no red-red edge; equal black height.
Visual: rb
Speaker notes: Explain conceptual NIL sentinels and black height. No consecutive red nodes means any path is at most twice the shortest by black-node count. Hence height ≤ 2 log2(n+1) in edges. Insertion starts red, may recolour and rotate; case details are conceptual today. Trace black 20 with red children 10,30; inserting red 5 causes red-red, recolour children black and keep root black.

## Slide 09 — Splay trees
Time: 8 min
Outcome: C1, C2, K6, S1
Visible: Move the accessed node to the root: zig, zig-zig, zig-zag.
Visual: splay
Speaker notes: Trace 30→20→10: rotate right at 30, then right at 20. A single operation can cost O(n); a sequence has amortised O(log n) per standard operation. No explicit balance or height metadata. The access lemma uses a potential based on log subtree sizes; do not mistake amortised for worst-case or average-case. Ask about frequently accessed keys.

## Slide 10 — B-trees and storage
Time: 8 min
Outcome: C1, C2, K6, S1
Visible: Many sorted keys per node → high fan-out → fewer page visits.
Visual: bt
Speaker notes: Minimum degree t≥2: nonroot nodes contain t−1 to 2t−1 keys; internal children count is keys+1; all leaves share depth. For t=2 split full [10,20,30], promote 20, leave [10] and [30]. Insert 25 into right leaf. O(log_t n) node visits; CPU comparisons depend on search within node. Root exceptions apply. Distinguish B-tree from B+ tree.

## Slide 11 — Guided Python: build the node
Time: 10 min
Outcome: C1, C2, K6, S1
Visible: Implement cached height, balance factor and rotations.
Visual: editable activity text
Speaker notes: Open notebook. Read Node fields and height helper. Work through right rotation together; students implement left rotation. Run local checks and explain why update order matters. Do not use a library balanced tree for this implementation.

## Slide 12 — Guided Python: insertion
Time: 10 min
Outcome: C1, C2, K6, S1
Visible: Rebalance on the recursive return path.
Visual: editable activity text
Speaker notes: Walk through the insertion scaffold and case conditions. Use duplicate handling consistently. Students complete TODOs. Test first with the four three-key sequences and inspect the root and in-order order.

## Slide 13 — Guided Python: validate
Time: 10 min
Outcome: C1, C2, K6, S1
Visible: Check ordering, cached heights and balance independently.
Visual: editable activity text
Speaker notes: Run invariant checker after each insertion. Test empty, singleton, duplicates, sorted and seeded shuffled keys. Explain why testing is evidence not a proof. If Colab fails, run lab.py or trace on paper.

## Slide 14 — Practice A: trace and repair
Time: 20 min
Outcome: C1, C2, K6, S1
Visible: Draw LL, RR, LR and RL; explain each pointer change.
Visual: editable activity text
Speaker notes: Pairs trace sequences from exercises. Require pre/post in-order, affected heights, and new root. Ask students to locate a stale-height bug. Allow time for debugging before moving on.

## Slide 15 — Practice B: compare workloads
Time: 20 min
Outcome: C1, C2, K6, S1
Visible: Compare plain BST and AVL heights on sorted and shuffled keys.
Visual: editable activity text
Speaker notes: Use notebook deterministic inputs. Count height and optionally time lookups separately from construction. Explain that sorted insertion is worst case for plain BST; a shuffled run is not a proof. Record n, seed, repetitions and units if timing.

## Slide 16 — Practice C: choose a tree
Time: 20 min
Outcome: C1, C2, K6, S1
Visible: Predictability, locality, and page-based storage.
Visual: editable activity text
Speaker notes: Groups choose AVL for tight lookup height, red-black for general ordered maps, splay for repeated accesses with tolerable spikes, B-tree for page-oriented indexes. Choices are conditional, not universal. Ask for one drawback and one alternative.

## Slide 17 — Exit ticket
Time: 10 min
Outcome: C1, C2, K6, S1
Visible: Trace a double rotation; explain amortised vs worst-case.
Visual: editable activity text
Speaker notes: Individually answer: classify insertion 40,10,30; state AVL invariant; choose a tree for disk pages and justify. Discuss without assigning an official grade.

## Slide 18 — Wrap-up and next session
Time: 5 min
Outcome: C1, C2, K6, S1
Visible: Invariants buy guarantees; workloads determine trade-offs.
Visual: editable activity text
Speaker notes: Review C1, C2, K6, S1. Next session covers hash tables, contrasting ordered operations with hashing. Independent study: red-black invariants, splay trace, B-tree split; full implementations are extension work.