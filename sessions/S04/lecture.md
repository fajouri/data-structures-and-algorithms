# S04 Lecture — Stacks, queues, BSTs and symbol tables

## 1. Why a data structure's contract matters
A sequence says what values occur in order; a **stack** promises access to the most recently pushed item, a **queue** promises the earliest enqueued item, and a **symbol table** associates unique keys with values. These are *abstract data types (ADTs)*: behavior and error handling, not a required memory layout. Implementations may use arrays, linked nodes, or trees. State the operation mix before selecting one.

Assume a unit-cost RAM model: comparing two fixed-size keys and following a link cost O(1); allocation, Python object overhead and cache effects are not modeled in asymptotic bounds. For strings of unbounded length, key comparisons can be more expensive.

## 2. Stack ADT — last in, first out
**Contract:** `push(x)` adds on top; `pop()` removes and returns the top; `peek()` reads the top without removing; `is_empty()` checks emptiness. Define a pop on an empty stack as an error, not a fabricated value.

Trace, starting empty:
```text
push(A) -> [A]             (top is right)
push(B) -> [A, B]
push(C) -> [A, B, C]
pop()   -> C, stack [A, B]
peek()  -> B, unchanged
```
A Python list implements end-of-list push/pop with O(1) *amortized* append and O(1) pop at the end; a linked list with head as top can offer O(1) changes to links. Index-based deletion at the front of a Python list is O(n): do not implement a queue as `list.pop(0)`.

**Application — balanced delimiters.** Scan characters left-to-right. Push every opening bracket. On a closing bracket, require a nonempty stack and a matching opener. At the end the stack must be empty. Example `{a[(b+c)]}` is balanced; `([)]` is not. The invariant after each prefix: the stack holds exactly the unmatched opening brackets in encounter order. Each character is handled once: O(n) time, O(n) worst-case auxiliary space.

## 3. Queue ADT — first in, first out
**Contract:** `enqueue(x)` adds at the rear; `dequeue()` removes from the front; `front()` reads the front; empty operations should have defined behavior. A queue is suitable for incoming support requests, breadth-first search, and task dispatch.

Trace: enqueue T1; enqueue T2; dequeue gives T1; enqueue T3; dequeue gives T2. A `collections.deque` supports O(1) append and popleft at opposite ends. A circular array buffer can also support O(1) amortized operations under geometric growth; linked head/tail supports O(1) enqueue/dequeue if invariants are maintained.

**Invariant:** the front is the oldest element still pending. Do not conflate FIFO queues with priority queues: a priority queue's removal order is by priority, not arrival time.

## 4. Symbol table — a map from unique keys to values
**Contract:** `put(k,v)` inserts a new binding or updates the existing key; `get(k)` returns a value or a documented missing-key result; `delete(k)` removes a binding; `contains(k)` tests membership. Key equivalence must be consistent with ordering. In this session, keys are comparable integers and a missing lookup raises `KeyError`.

Possible representations:
| Representation | Lookup worst case | Insert/update worst case | Delete worst case |
|---|---:|---:|---:|
| Unsorted array of pairs | O(n) | O(n) for update/search; new append O(1) amortized after confirming absence | O(n) |
| Singly linked list | O(n) | O(n) when finding existing key or confirming absence | O(n) search + O(1) link changes after predecessor known |
| Sorted array | O(log n) comparison search | O(n) shifts | O(n) shifts |
| Unbalanced BST | O(h), at most O(n) | O(h) | O(h) |

The BST additionally supports ordered operations and sorted traversal. Hash-table average/expected lookup is addressed later; it is not assumed here.

## 5. BST representation and invariant
A binary search tree stores one unique key/value pair at each node, plus zero to two child pointers. **Strict invariant:** every key in the left subtree is **less** than the node key, and every key in the right subtree is **greater**. The invariant applies to *all descendants*, not only the immediate children.

Build by inserting `[50, 30, 70, 20, 40, 60, 80]`:
```text
          50
       /      \
     30        70
    /  \      /  \
   20  40    60  80
```
To search for 60: compare to 50 (go right); compare to 70 (go left); match 60. To search for 65, the path stops at a missing child, so the key is absent.

**Insertion:** compare at each node until reaching an empty link; allocate a leaf there. If the key already exists, update the value **without creating a duplicate node**. On the path down, each comparison discards one side; attaching at the correct empty link preserves the invariant.

**Cost:** a path follows at most `h` edges (height measured as max edges root-to-leaf). Search and insertion use O(h+1) time and O(1) iterative auxiliary space; a recursive implementation uses O(h+1) call-stack space. In a balanced tree, h=O(log n); in an unbalanced tree inserted in sorted order, h=n−1, making operations O(n). We do **not** assert probabilistic average-case without specifying a random-tree/input model.

## 6. Deletion — three structural cases
First search for the target key. After finding the node:
1. **Leaf:** unlink it. Example: delete 20 from the displayed tree.
2. **One child:** promote the child. Example: after deleting 20, delete 30 (whose only child is 40).
3. **Two children:** find the *in-order successor*, the minimum node of the right subtree. Copy its key/value to the target; remove the successor from its original location (it has no left child). For the original tree, deleting 50 replaces its binding with 60, then removes the original 60 node from below 70.

Deletion takes O(h+1) time. A recursive version consumes O(h+1) stack space. The successor is the smallest key greater than the target: it cannot violate the remaining left or right ordering. If `delete(k)` receives a missing key, choose and document behavior (here, raise `KeyError`).

**Trace for deleting 50:**
```text
Before:                   After:
      50                       60
    /    \                   /    \
   30     70                30     70
  / \    / \               / \      \
 20 40  60 80             20 40     80
```
Common error: moving only the successor's key but forgetting its associated value. Another error: discarding the successor's right subtree during removal.

## 7. In-order traversal
Visit left subtree, then current node, then right subtree. For a BST with the strict ordering invariant, the sequence of keys is strictly increasing. This follows by structural induction: each left key is less than the current key, and each right key greater. Traversal touches every node once: Θ(n) time, O(h+1) recursion stack space (for an empty tree, O(1)).

## 8. Practice in Google Colab
The companion notebook demonstrates stack delimiter checking, queue task dispatch and BST `put/get/delete/inorder`. Students predict each output before running, change inputs, inspect invariants, and compare with array/linked-list alternatives. Automated checks show *selected observable behavior*, not a correctness proof.

## 9. Trade-offs and S05 preview
Stacks and queues constrain access order; a symbol table selects by key, and a BST preserves order. Unbalanced BST operations can degrade to linear time on adversarial insertion order. For S05, keep identical `put/get/delete` semantics across representations and benchmark with documented workloads, seeds and hardware; do not infer a benchmark outcome in advance. Formal assignment conditions remain pending institutional confirmation.

## 10. Misconceptions to address
- LIFO is not FIFO; an operation name does not specify implementation.
- Queue removal from the front of a Python list is O(n); `deque.popleft()` is O(1).
- BST ordering is global across each subtree, not only parent/child.
- A plain BST is **not** necessarily balanced.
- Two-child deletion must preserve both the key and its associated value.
- Recursive tree algorithms use call-stack memory.
- A successful test is useful evidence, not a proof for all inputs.

**References:** CLRS (4th ed., 2022); Goodrich, Tamassia & Goldwasser (2013); Sedgewick & Wayne (2011); official course-approved S04 scope in `course-plan.md`.
