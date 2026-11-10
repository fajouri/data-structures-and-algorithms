# S04 Slide Source — Stacks, queues, BSTs and symbol tables

**Deck:** 18 slides · 16:9 · editable native shapes/text with speaker notes.  **Total:** 180 minutes (including an 8-minute break).
**Audience:** MSc Computer Science · M12 · Outcome links: C1, C2, K1, S1 (local course-plan references).
**Teacher guidance:** Make students predict before revealing traces; use hand diagrams if equipment or internet fails.

## Slide 01 — Stacks, queues, maps: why access order matters
**Visible:** Same data can obey LIFO, FIFO, or key lookup; the ADT contract dictates permitted operations.
**Visual:** Three editable cards: STACK, QUEUE, MAP; tiny use-case labels.
**Speaker notes:** Ask learners for a compiler, print queue, or key lookup example. Contrast behavior with storage. Have them predict which structure suits recent-first work. Transition to LIFO.
**Time:** 8 min

## Slide 02 — Stack ADT: LIFO contract
**Visible:** push(x), pop(), peek(), is_empty(); empty pop is an error. Top is the most recent item.
**Visual:** Three vertically stacked labeled blocks A/B/C with a top arrow.
**Speaker notes:** Trace push A, B, C, pop -> C. Explain last-in-first-out and representation independence. Ask what pop returns next. Show that pop on an empty stack requires defined behavior.
**Time:** 8 min

## Slide 03 — Stack trace: delimiter matching
**Visible:** Push opening brackets; on close, match the top; accept iff empty at end.
**Visual:** Bracket string { [ ( ) ] } and stack states; mismatch ([)] highlighted.
**Speaker notes:** Have students trace balanced and crossed brackets. State prefix invariant: unmatched openings stored in order. Runtime O(n), space O(n). Ask why a matching count alone is insufficient.
**Time:** 8 min

## Slide 04 — Queue ADT: FIFO contract
**Visible:** enqueue(x), dequeue(), front(); oldest pending item leaves first.
**Visual:** Horizontal A,B,C blocks, arrow in at rear and arrow out at front.
**Speaker notes:** Trace enqueue A,B; dequeue A; enqueue C; dequeue B. Compare deque.popleft() with list.pop(0). Ask what would happen if tasks received priority rather than FIFO.
**Time:** 9 min

## Slide 05 — Pause: pair choice
**Visible:** LIFO: undo history. FIFO: printer tasks. Key lookup: dictionary.
**Visual:** Three scenario prompts; blank justification boxes.
**Speaker notes:** Pairs choose and explain one suitable structure per workload. Collect one misconception to revisit. Transition from order-based ADTs to key-based lookup.
**Time:** 8 min

## Slide 06 — Symbol-table contract
**Visible:** put(k,v), get(k), delete(k), contains(k); unique keys, duplicate put updates.
**Visual:** Editable two-column key/value table: 20↦A, 30↦B, then 20↦C.
**Speaker notes:** Explain map as ADT. Ask if setting key 20 again should increase size. Distinguish absent keys from stored None. Discuss documented KeyError missing-key semantics.
**Time:** 8 min

## Slide 07 — Representations and trade-offs
**Visible:** Unsorted list O(n) lookup; sorted array O(log n) search; BST O(h).
**Visual:** Comparison table: storage, lookup, insertion, ordering.
**Speaker notes:** Emphasize sorted array insertion still shifts Θ(n); linked-list updates after found predecessor may be O(1) but locating it costs O(n). BST operations depend on h, not automatic log n.
**Time:** 10 min

## Slide 08 — Break / quick reset
**Visible:** 8-minute reset. Then we build a search tree.
**Visual:** Single large neutral timer-style visual and next topic.
**Speaker notes:** Allow short break according to classroom arrangements. Quick return prompt: what property should each subtree satisfy to make lookup efficient?
**Time:** 8 min

## Slide 09 — BST invariant: global order
**Visible:** All keys in left subtree < node < all keys in right subtree; recursively.
**Visual:** Editable seven-node tree with root 50, children 30 and 70.
**Speaker notes:** Draw tree from insertion [50,30,70,20,40,60,80]. Verify descendants, not only direct children. Ask if key 55 can be placed anywhere in left subtree. Transition to search.
**Time:** 10 min

## Slide 10 — BST search: compare and descend
**Visible:** Search 60: 50→70→60; missing 65 stops at null.
**Visual:** Editable tree with bold path and null branch; complexity O(h+1).
**Speaker notes:** Count comparisons and distinguish successful from missing search. At each step one subtree is eliminated by invariant. Ask what happens to height after sorted insertions.
**Time:** 9 min

## Slide 11 — BST insertion and updates
**Visible:** Insert at first missing child; existing key updates its associated value.
**Visual:** Tree with new 65 under 60-right; annotate no-duplicate update of 30.
**Speaker notes:** Walk insertion for 65 and overwrite value at key 30. Emphasize key and value travel together. Show why comparisons preserve global order, and ask for corner cases empty root and duplicate key.
**Time:** 10 min

## Slide 12 — BST height is the cost driver
**Visible:** Balanced height O(log n); ascending-order insertion can make h=n−1.
**Visual:** Side-by-side editable balanced tree and 5-node right chain.
**Speaker notes:** Compare shapes for same n. Distinguish strict O(h+1) bound from unsupported expected-time claims. Have students trace largest key in chain. S06 introduces balanced trees.
**Time:** 12 min

## Slide 13 — BST delete: leaf and one child
**Visible:** Leaf: unlink. One child: promote child; preserve descendants.
**Visual:** Before/after trees for deleting 20, then 30 with sole child 40.
**Speaker notes:** Trace mutations with students. If deleting root with one child, child becomes new root. Ask about a leaf and empty tree. Transition to two-child deletion.
**Time:** 10 min

## Slide 14 — BST delete: two children
**Visible:** Replace by in-order successor = minimum of right subtree; remove successor original.
**Visual:** Tree 50 root with 60 successor, after root becomes 60.
**Speaker notes:** Step through deleting 50 in 7-node BST. Explain successor has no left child, may have a right child. Remind to copy value as well as key and reattach successor's child.
**Time:** 10 min

## Slide 15 — In-order traversal and correctness
**Visible:** Left → node → right returns sorted keys. Θ(n) time; O(h+1) call stack.
**Visual:** Editable traversal callout and sorted key strip 20,30,40,50,60,70,80.
**Speaker notes:** Prove order with subtree invariant. Ask learners to produce output after delete 50. Note recursion stack is nonzero auxiliary memory. Contrast traversal with point lookup.
**Time:** 15 min

## Slide 16 — Colab lab: predict, run, change
**Visible:** Run stack checker, FIFO deque, BST put/get/delete/inorder in Colab.
**Visual:** Four-step checklist and test table for empty, duplicate, missing, two-child.
**Speaker notes:** Open notebook and predict outputs before execution. Students change workloads and add a missing-key test. If offline, draw stack/queue/tree transitions on paper. Do not treat passing tests as proof.
**Time:** 12 min

## Slide 17 — Application: choose and justify
**Visible:** Stacks for parsers; queues for dispatch; BST for ordered map—with height caveat.
**Visual:** Three workload cards plus fourth blank choose-for-your-app prompt.
**Speaker notes:** Small groups choose representation and state time/space assumptions. Contrast unsorted, sorted and tree-backed maps. Have them defend one trade-off rather than merely naming a structure.
**Time:** 10 min

## Slide 18 — Exit ticket and S05 handoff
**Visible:** One invariant; one deletion trace; one cost claim. Next: fair symbol-table comparisons.
**Visual:** Three short exit prompts; S05 ungraded preparation arrows.
**Speaker notes:** Ask: Why does in-order successor preserve keys? What is BST search cost with height h? Which workload needs FIFO? Explain S05 prepares testing and benchmarks, but do not assign weights or deadlines.
**Time:** 15 min
