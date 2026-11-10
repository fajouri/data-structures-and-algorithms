# S04 — Student exercises (ungraded)

Work in pairs where indicated. Show intermediate states and explain *why*, not just the final value. No instructor answer key is included.

## A. ADT contracts and traces
**1. Stack prediction.** Starting empty, apply `push(3), push(8), pop(), push(5), peek(), pop()`. Record the stack after each operation, the returned values and the result of popping an empty stack under your chosen contract. Explain LIFO.

**2. Queue prediction.** Starting empty, apply `enqueue(A), enqueue(B), dequeue(), enqueue(C), dequeue()`. Draw front/rear after each operation; explain FIFO. What goes wrong with repeatedly calling `list.pop(0)` on a large Python list?

**3. Brackets.** Hand-trace a stack for `{[()]}`, `([)]` and `((`. For each scanned character, record the stack of unmatched openings. State the invariant and O-notation bounds.

## B. Symbol tables and BST traces
**4. Symbol table contract.** Define `put/get/delete/contains`, specifying whether duplicate keys overwrite, what a missing key does, and whether values can be `None`. Explain why a value is not a reliable membership test if `None` is allowed.

**5. Construct a BST.** Insert keys `[50,30,70,20,40,60,80]` with values `'v'+str(key)`. Draw the tree after insertion of 70, 40, and 80. Trace search for 60 and missing 65, counting comparisons.

**6. Update vs duplicate.** Call `put(30,'updated')` on the BST above. Explain whether a new node is created and what `get(30)` must return.

**7. Delete a leaf, a one-child node and a two-child node.** Start from the original tree of Exercise 5 *afresh* for each deletion: delete 20, delete 30 **after deleting 20**, and delete 50 using the in-order successor. Draw all intermediate and final trees. State why each tree preserves the strict ordering invariant.

**8. Traversal.** Give in-order keys for your original tree and after deleting 50. Explain why they are ordered. What are time and auxiliary-space bounds for a recursive traversal?

## C. Implementation and interpretation
**9. Colab self-check.** Open the S04 tutorial, predict output for each demonstration before running, modify the queue workload and add one BST missing-key test. Run with an empty tree, one node, sorted insertion order and an update of an existing key. Record what each test establishes and what it does *not* prove.

**10. Compare implementations.** Build a table for unsorted array, sorted array, singly linked list and unbalanced BST. Compare lookup, insert/update and delete under fixed-size key comparisons. Explain which operations require a prior search and how worst-case BST height changes bounds.

**11. Choose for workloads.** Recommend structures for: a parser matching parentheses, a printer queue, a glossary requiring ordered key traversal, and an append-heavy list with occasional lookup. State at least one assumption and one downside for each choice.

## D. Extension (optional)
**12. Degenerate tree experiment.** Insert n ordered integer keys into a plain BST and then in shuffled order; measure comparison counts rather than asserting random expected complexity. State n, insertion orders, and observations. What does this suggest about *height* as the relevant parameter?

**13. Correctness argument.** Write a short inductive explanation of why replacing a two-child node by its in-order successor keeps the BST invariant. Include the successor's possible right child.

**Submission:** These are study exercises, *not* an assignment submission. S05 prepares for the institution-governed assignment studio.
