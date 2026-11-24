# S06 lecture notes

## Why balanced trees?

Predict the cost of inserting 1, 2, 3, 4, 5 into a plain BST.

A plain BST preserves ordering but not shape. Sorted insertion creates a chain. Ask students to count comparisons when searching for 5. Review S04 and distinguish node count from height. Today we preserve the ordered-map ADT while changing the representation.

## The height problem

Search follows one root-to-leaf path: O(h).

Define empty height 0 and leaf height 1. A chain has h=n; a perfect binary tree has h=log2(n+1). Search is O(h), best case constant at root. Recursive traversal uses O(h) stack. Ask whether every BST is logarithmic.

## AVL invariant

At every node: |height(left) − height(right)| ≤ 1.

Compute bottom-up heights, then balance factors BF=left minus right. The constraint applies globally, not merely at the root. With N(0)=0 and N(1)=1, minimum nodes N(h)=1+N(h−1)+N(h−2), giving exponential growth and logarithmic height. Ask students to compute N(3)=4.

## A rotation preserves order

Right rotation: promote the left child; move its right subtree.

For y with left x and x.right=B, set y.left=B and x.right=y. Ordering A < x < B < y < C survives. Update y height before x. A rotation is constant time assuming stored heights. It may change the root; always return the new subtree root.

## LL and RR

LL → rotate right. RR → rotate left.

Insert 30,20,10 for LL; 10,20,30 for RR. Both yield root 20 with children 10 and 30. Classify using the heavy child, not simply the last key. Students predict root and in-order traversal before showing the answer.

## LR and RL

LR → left child left, then root right. RL is the mirror.

Trace 30,10,20: rotate left at 10, then right at 30. Trace 10,30,20 as mirror. The intermediate tree remains a BST but can still be unbalanced. Ask why one rotation alone is insufficient.

## AVL insertion algorithm

Insert like a BST → update height → rebalance → return root.

Recursive insertion returns a subtree root. Equal keys are ignored for this set demonstration; maps instead update values. Induction: child insertion preserves ordering; rotations preserve ordering; local rebalance restores height constraint. Each ancestor costs constant work with cached heights. Worst case O(log n) time and stack; O(n) total storage. Deletion is an extension and may rebalance several ancestors.

## Red-black trees

Black root; black NIL leaves; no red-red edge; equal black height.

Explain conceptual NIL sentinels and black height. No consecutive red nodes means any path is at most twice the shortest by black-node count. Hence height ≤ 2 log2(n+1) in edges. Insertion starts red, may recolour and rotate; case details are conceptual today. Trace black 20 with red children 10,30; inserting red 5 causes red-red, recolour children black and keep root black.

## Splay trees

Move the accessed node to the root: zig, zig-zig, zig-zag.

Trace 30→20→10: rotate right at 30, then right at 20. A single operation can cost O(n); a sequence has amortised O(log n) per standard operation. No explicit balance or height metadata. The access lemma uses a potential based on log subtree sizes; do not mistake amortised for worst-case or average-case. Ask about frequently accessed keys.

## B-trees and storage

Many sorted keys per node → high fan-out → fewer page visits.

Minimum degree t≥2: nonroot nodes contain t−1 to 2t−1 keys; internal children count is keys+1; all leaves share depth. For t=2 split full [10,20,30], promote 20, leave [10] and [30]. Insert 25 into right leaf. O(log_t n) node visits; CPU comparisons depend on search within node. Root exceptions apply. Distinguish B-tree from B+ tree.

## Guided Python: build the node

Implement cached height, balance factor and rotations.

Open notebook. Read Node fields and height helper. Work through right rotation together; students implement left rotation. Run local checks and explain why update order matters. Do not use a library balanced tree for this implementation.

## Guided Python: insertion

Rebalance on the recursive return path.

Walk through the insertion scaffold and case conditions. Use duplicate handling consistently. Students complete TODOs. Test first with the four three-key sequences and inspect the root and in-order order.

## Guided Python: validate

Check ordering, cached heights and balance independently.

Run invariant checker after each insertion. Test empty, singleton, duplicates, sorted and seeded shuffled keys. Explain why testing is evidence not a proof. If Colab fails, run lab.py or trace on paper.

## Practice A: trace and repair

Draw LL, RR, LR and RL; explain each pointer change.

Pairs trace sequences from exercises. Require pre/post in-order, affected heights, and new root. Ask students to locate a stale-height bug. Allow time for debugging before moving on.

## Practice B: compare workloads

Compare plain BST and AVL heights on sorted and shuffled keys.

Use notebook deterministic inputs. Count height and optionally time lookups separately from construction. Explain that sorted insertion is worst case for plain BST; a shuffled run is not a proof. Record n, seed, repetitions and units if timing.

## Practice C: choose a tree

Predictability, locality, and page-based storage.

Groups choose AVL for tight lookup height, red-black for general ordered maps, splay for repeated accesses with tolerable spikes, B-tree for page-oriented indexes. Choices are conditional, not universal. Ask for one drawback and one alternative.

## Exit ticket

Trace a double rotation; explain amortised vs worst-case.

Individually answer: classify insertion 40,10,30; state AVL invariant; choose a tree for disk pages and justify. Discuss without assigning an official grade.

## Wrap-up and next session

Invariants buy guarantees; workloads determine trade-offs.

Review C1, C2, K6, S1. Next session covers hash tables, contrasting ordered operations with hashing. Independent study: red-black invariants, splay trace, B-tree split; full implementations are extension work.

## Comparison

| Structure | Search/update | Main cost |
|---|---|---|
| Plain BST | O(n) worst | shape |
| AVL | O(log n) worst | cached heights, rotations |
| Red-black | O(log n) worst | colour and fix-up |
| Splay | O(log n) amortised, O(n) single operation | access restructuring |
| B-tree | O(log_t n) page visits | within-node search and split |

All store O(n) keys. Recursive AVL insertion uses O(log n) stack. B-tree bounds assume fixed minimum degree t and a page per node; root exceptions apply.

## Reading
CLRS, Introduction to Algorithms, 4th ed., chapters on red-black trees and B-trees; Goodrich et al., Data Structures and Algorithms in Python, search trees; Sleator and Tarjan (1985), Self-Adjusting Binary Search Trees.
