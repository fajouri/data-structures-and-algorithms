# S04 — Stacks, queues, binary search trees and symbol tables

**Module:** M12 — Data Structures and Algorithms  
**Contact:** 3 hours / 180 minutes, face to face  
**Suggested independent study:** approximately 10 hours (illustrative, not a deadline)  
**Status:** DRAFT — for lecturer review; exercises are **ungraded**.

## Learning outcomes
Students will:
1. Specify the stack (LIFO) and queue (FIFO) ADT contracts and choose suitable implementations.
2. Trace stacks for delimiter matching and queues for task dispatch.
3. Define a key/value symbol table, with duplicate-key updates and missing-key behavior.
4. Explain and preserve the strict BST ordering invariant; trace search, insertion, deletion (0/1/2 children), and in-order traversal.
5. Derive BST time costs in terms of tree height h and compare balanced with degenerate cases.
6. Implement and test a minimal Python symbol table and prepare an **ungraded** comparison for S05.

**Planned course-outcome links:** C1, C2, K1, S1, following the approved S04 course-plan entry; they are local planning labels and do not change the official module descriptor.

## Prerequisites and resources
S02 recursion and binary search; S03 arrays, linked lists, invariants and cost models. Google Colab (no third-party libraries) or Python 3.9+; optional paper-based tracing. C++17 analogies are optional, not required for the practical.

## Three-hour teaching sequence
| Time | Activity | Evidence |
|---|---|---|
| 00–24 | LIFO/FIFO, stack and queue contracts, predict output | Stack/queue traces |
| 24–41 | Delimiter matching and queue scheduling walkthroughs | Explain invariant |
| 41–57 | Symbol table interface; map operation to representation | API and cost table |
| 57–65 | Break/reset | — |
| 65–101 | BST structure, invariant, search and insertion, height | Correct search/insert traces |
| 101–132 | BST deletion: 0, 1, 2 children | Trace with successor |
| 132–147 | In-order traversal, correctness, costs | Sorted output and h bound |
| 147–165 | Guided Colab lab and student self-checks | Run examples, change input |
| 165–180 | Compare representations; S05 handoff and exit ticket | Justified trade-offs |

For detailed per-slide timings, see [slide source](slides.md); the total is exactly 180 minutes. Adjust activities for local break rules without changing total contact time.

## Deliverables
- [Lecture notes](lecture.md)
- [18-slide source and detailed speaker notes](slides.md)
- [Practice worksheet](exercises.md)
- [Runnable Python lab](lab.py)
- [Colab tutorial](tutorial/S04_Stacks_Queues_BST_Symbol_Tables.ipynb)
- [Editable slide deck with native speaker notes](slides.pptx) (18 slides; PowerPoint opening/rendering has not been independently tested)

The editable slide source remains the source of truth if the presentation must be regenerated. Do not treat draft materials as lecturer-approved or graded.

## Running locally
```bash
python sessions/S04/lab.py --self-check
python sessions/S04/lab.py --demo
```

Open the notebook from the repository in Google Colab and choose **Runtime → Run all**; Python standard library only.

## Academic notes
Deletion uses the **in-order successor** for the two-child case. Comparisons assume ordered, unique keys; inserting an existing key replaces its value. Unbalanced BST operations depend on height, not just the number of nodes. S05 is an assignment studio, but assessment instructions, weights and deadlines are **not** introduced here.

**References:** Cormen et al., *Introduction to Algorithms*, 4th ed. (2022), elementary data structures and binary search trees; Goodrich et al., *Data Structures and Algorithms in Python* (2013), stacks, queues and trees; Sedgewick & Wayne, *Algorithms*, 4th ed. (2011), symbol tables and BSTs.
