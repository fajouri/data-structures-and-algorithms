# S02 — Recursion, recurrences, Master Theorem and binary search

**Module:** M12 — Data Structures and Algorithms  
**Contact time:** 3 hours, face to face  
**Suggested independent study:** approximately 10 hours (illustrative allocation, not an assessment deadline)  
**Package status:** Draft for lecturer review; not a graded assignment.

## Learning objectives

By the end of this session, students should be able to:

1. Trace recursive execution, identify base and recursive cases, and explain how calls use the call stack.
2. Formulate a recurrence that reflects an algorithm's subproblem sizes and non-recursive work.
3. Use expansion, a recursion-tree argument, or substitution to reason about simple recurrences.
4. Apply the Master Theorem only when its form and regularity conditions are satisfied.
5. Implement and test iterative and recursive binary search on sorted sequences, including boundary cases.
6. Justify binary search correctness and state time and auxiliary-space costs with assumptions.

## Outcome mapping

The course plan maps S02 to the official/local outcome labels below. The descriptor and approved course plan remain authoritative.

| Objective | Outcome label | Evidence |
|---|---|---|
| Choose an appropriate search strategy and state its preconditions | C2 | Exercise 5 and lab |
| Analyse correctness using invariants and recurrence relations | C3 | Recursion traces, binary-search invariant |
| Apply asymptotic notation to recursive algorithms | K2 | Recurrence classification exercises |
| Describe and apply the Master Theorem | K3 | Recurrence worksheet and exit ticket |

## Prerequisites and preparation

- Variables, functions, loops, conditionals and elementary algebra.
- S01 asymptotic notation, input size, and the distinction between worst-case and average-case analysis.
- Basic use of Python 3; C++17 is provided as an equivalent optional implementation path.
- Review logarithms and powers. Bring paper for call-stack and recursion-tree traces.

## 180-minute agenda

| Time | Activity | Evidence of learning |
|---:|---|---|
| 0–10 | Retrieval warm-up: predict what happens when a recursive function has no reachable base case | Students name termination conditions |
| 10–30 | Call stack, base case, recursive case; trace factorial and a deliberately flawed example | Annotated stack frames and corrected termination condition |
| 30–50 | Recurrence modelling: identify number/size of subproblems and combine work | Students translate code structure into a recurrence |
| 50–70 | Expansion and recursion trees; compare linear, logarithmic and n log n work | Small-tree calculation with level costs |
| 70–80 | Break / reset, according to classroom arrangements | — |
| 80–105 | Master Theorem: form, cases, conditions and counterexamples | Students classify supported recurrences and flag unsupported ones |
| 105–130 | Binary search: half-open interval, invariant, trace and off-by-one defects | Students explain each boundary update |
| 130–160 | Guided practical: run tests, add edge cases, compare recursive and iterative versions | Passing self-checks plus a short complexity note |
| 160–173 | Pair exercises: recurrence choice and search failure diagnosis | Written justification, not just a final answer |
| 173–180 | Exit ticket and preview of arrays/lists in S03 | One recurrence, one binary-search invariant |

If a break is institutionally required, place it within the three-hour contact window and adjust activity minutes without increasing total contact time. Keep a paper-based trace ready if the live coding environment is unavailable.

## Materials

- [Lecture notes](lecture.md)
- [Student exercises](exercises.md)
- [Slide source and speaker notes](slides.md)
- [Python practical](lab.py)
- [C++17 practical](lab.cpp)

The PowerPoint export is **pending**; `slides.md` is the editable source and includes per-slide visual specifications and speaker notes. No instructor solutions are included in this public student package.

## Lab commands

Python 3:
```bash
python lab.py --self-check
python lab.py --demo
```

C++17:
```bash
g++ -std=c++17 -O2 -Wall -Wextra -pedantic lab.cpp -o lab
./lab --self-check
./lab --demo
```

On Windows, run `lab.exe` after compilation. The examples are designed to run offline. These commands are instructions; they are not a claim that the code has been executed in this environment.

## Independent study

1. Complete the recurrence and binary-search prompts in `exercises.md`.
2. Explain in your own words why the Master Theorem does not automatically apply to every recurrence.
3. Compare the stack-space cost of recursive and iterative binary search.
4. Read the references below and bring one question about a recurrence proof.

## References

- Official *M12 — Data Structures and Algorithms Module Descriptor*, for module outcomes and scope.
- Cormen, Leiserson, Rivest and Stein, *Introduction to Algorithms*, 4th ed. (2022), sections on recurrence relations, divide-and-conquer and binary search.
- Sedgewick and Wayne, *Algorithms*, 4th ed. (2011), discussion of binary search and recursive algorithms.
