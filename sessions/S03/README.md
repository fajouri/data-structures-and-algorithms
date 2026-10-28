# S03 — Arrays, dynamic arrays, linked lists and amortised costs

**Module:** M12 — Data Structures and Algorithms  
**Contact time:** 3 hours, face to face  
**Suggested independent study:** approximately 10 hours (illustrative, not a deadline)  
**Status:** Draft for lecturer review; ungraded teaching material.

## Learning objectives

Students should be able to:
1. Distinguish the sequence ADT contract from array and linked-list representations.
2. Explain contiguous storage, indexed access, resizing and capacity.
3. Implement basic sequence operations and a singly linked list in Python; relate them to C++17.
4. Compare time and auxiliary-space costs for access, search, insertion and deletion.
5. Explain why one append may be linear while dynamic-array append is constant amortised time under geometric growth.
6. Use an aggregate argument to justify the amortised append bound.
7. Select a representation based on operation mix, memory layout and update requirements.

## Outcome mapping

These labels are local planning references, not official outcome IDs.

| Objective | Outcome | Evidence |
|---|---|---|
| Select a representation for a workload | C1, C2, K1 | Exercises 5–7 |
| State ADT contract and representation invariant | C3, K1 | List invariant prompts |
| Analyse worst-case and amortised costs | K2, K6 | Capacity trace and proof |
| Implement and test structures | C1, C6, S6 | Python/C++ lab self-checks |

## Prerequisites and tools

Students should know functions, loops, indices, references/objects, and Big-O/Theta notation from S01. S02 recursion is useful but not required. Use Python 3 standard library and, where available, a C++17 compiler. The exercises are ungraded practice; no assignment weights or deadlines are introduced.

## 180-minute teaching plan

| Minutes | Activity | Evidence of learning |
|---:|---|---|
| 0–10 | Predict a structure for indexed reads versus front insertions | Choice plus assumptions |
| 10–30 | Sequence ADT, invariants, contiguous memory and references | Contract-versus-representation comparison |
| 30–50 | Trace array access, search, insertion and deletion | Operation count including shifts |
| 50–65 | Dynamic-array capacity and resize-copy trace | Correct size/capacity table |
| 65–75 | Break/reset according to classroom arrangements | — |
| 75–95 | Linked-list nodes, head, traversal and pointer updates | Link trace |
| 95–115 | Compare operation costs and assumptions | Qualified complexity table |
| 115–135 | Aggregate amortised analysis for append | Correct geometric-sum argument |
| 135–165 | Guided Python lab; C++17 comparison and self-checks | Test evidence and complexity note |
| 165–175 | Pair task: choose a representation for three workloads | Justified recommendation |
| 175–180 | Exit ticket: one worst-case cost, one amortised cost, one invariant | Short written explanation |

Adapt activity boundaries for required institutional breaks while retaining three contact hours. Keep paper traces available if a toolchain or internet connection fails.

## Materials

- [Lecture notes](lecture.md)
- [Student exercises](exercises.md)
- [Slide source and speaker notes](slides.md)
- [Python lab](lab.py)
- [C++17 lab](lab.cpp)
- Editable PowerPoint: slides.pptx is pending; see the handoff note in slides.md.

## Run the practical

Python 3:
~~~bash
python lab.py --self-check
python lab.py --demo
~~~

C++17:
~~~bash
g++ -std=c++17 -O2 -Wall -Wextra -pedantic lab.cpp -o lab
./lab --self-check
./lab --demo
~~~

These are instructions, not a claim that code has already been executed. On Windows, run lab.exe after compilation.

## Independent study

1. Complete exercises 1–10 with intermediate states and assumptions.
2. Explain why array insertion can be Θ(n) even if writing one element is Θ(1).
3. Re-derive dynamic-array append cost with the aggregate method.
4. Read one reference and bring a question about memory layout or amortised analysis.

## References

- Official M12 — Data Structures and Algorithms Module Descriptor, for scope and outcomes.
- Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, 4th ed. (2022), elementary data structures and amortised analysis.
- Goodrich, Tamassia and Goldwasser, Data Structures and Algorithms in Python (2013), sequence and linked structures.
- Sedgewick and Wayne, Algorithms, 4th ed. (2011), elementary data structures.
