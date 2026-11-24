# S06 — Practice (ungraded)

1. Trace insertion sequences [30,20,10], [10,20,30], [30,10,20], [10,30,20]. For each show balance factors, new root and in-order traversal.
2. Implement left rotation in the notebook; preserve the transferred middle subtree. Test empty and singleton input via insertion, and duplicate keys (set semantics).
3. Complete AVL insertion and validate after every operation; test 100 ascending keys and 100 shuffled keys. Explain the complexity.
4. Compare BST and AVL height for n=20,100,500 with seed 42. Report measured heights, not invented results. Explain the input distribution.
5. Trace splay access of 10 in the tree 30→20→10. Explain single-operation versus amortised cost.
6. For minimum degree 2, insert 25 after splitting full root [10,20,30]. Draw nodes and check key ranges.
7. Choose a tree for a latency-sensitive ordered map, repeated hot-key accesses and an on-disk index. Justify assumptions and alternatives.
8. Extension: explain why AVL deletion can require rebalancing multiple ancestors; design edge-case tests.
