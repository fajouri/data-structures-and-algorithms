# S05 — Assignment 1 Studio: Symbol Tables and Fair Benchmarking

**Module:** M12 — Data Structures and Algorithms (MSc Computer Science)  
**Duration:** 180 minutes of contact time (3 hours)  
**Suggested independent study:** 13 hours (illustrative; not a submission deadline)  
**Status:** DRAFT for lecturer review. This is an **assignment-support studio**, not a published graded brief.

## Why this session matters
The same key–value **symbol-table ADT** can be stored in an array of entries, a linked list, or an unbalanced binary search tree (BST). Students learn to keep the *interface and observable behaviour identical*, test correctness, measure performance fairly, and explain results using complexity and data-structure invariants.

## Learning outcomes
At the end of S05, students should be able to:
1. Specify a comparable `put/get/delete/contains/size` contract for unique integer keys.
2. Explain the representation invariant for array, linked-list, and BST symbol tables.
3. Build small implementations or incremental scaffolds and use contract tests to detect incorrect updates, missing keys and deletion errors.
4. Design workloads that isolate insertion, successful lookup, unsuccessful lookup and deletion; use fixed seeds, reproducible inputs and repeated measurements.
5. Relate observed scaling to worst-case/assumption-dependent theoretical costs, especially unbalanced BST height and sorted insertion order.
6. Produce an evidence-based engineering explanation that separates *correctness* from *speed*.

**Approved course-plan outcome references:** C1 (implement data structures), C2 (justify selection), C6 (empirical evaluation), S1 (BST implementation), S6 (profiling). These labels are local references to the official learning outcomes.

## Preparation and prerequisites
- **Prerequisites:** S03 dynamic arrays and linked lists; S04 BST invariants, symbol tables, search/insert/delete; S01 complexity and correctness; S02 recursion when using recursive BST operations.
- **Tools:** Python 3 / Google Colab (standard library only). Optional C++17 and VS Code for memory/benchmark extension; no C++ submission requirement is implied.
- **Before class:** read S04 lecture, review BST deletion and integer-key comparisons, open the notebook. Prepare pen-and-paper alternatives.

## Three-hour agenda
| Classroom time | Minutes | Activity | Evidence |
|---|---:|---|---|
| 00:00–00:10 | 10 | Studio orientation, assignment scope versus pending official rules | Understand what is fixed and what remains unconfirmed |
| 00:10–00:35 | 25 | Targeted review: ADT contract, representations, invariants, expected costs | Annotated contract and hand traces |
| 00:35–01:10 | 35 | Instructor-guided test design and fair benchmark demonstration | First executable tests and benchmark plan |
| 01:10–02:45 | 95 | Supervised studio: implementations, test loops, experiments, peer review | Working pieces, reproducible experimental notes |
| 02:45–03:00 | 15 | Results clinic, reflective exit ticket, individual next steps | Explain a correctness test, a performance limitation |
| **Total** | **180** | | |

**Break note:** The 95-minute block permits an instructor-managed short reset under local policy; if a formal break is required, adjust the internal practical allocation while retaining the institution's contact-time rules.

## Files in this package
- [`slides.pptx`](slides.pptx) — editable 16:9 PowerPoint with native speaker notes.
- [`slides.md`](slides.md) — slide-by-slide authoring source, notes, timing.
- [`lecture.md`](lecture.md) — the detailed lecturer script and explanations.
- [`exercises.md`](exercises.md) — student exercises, no final assignment solutions.
- [`tutorial/S05_Symbol_Table_Studio.ipynb`](tutorial/S05_Symbol_Table_Studio.ipynb) — Colab-ready *predict → run → modify → explain* lab, including testing and benchmarking guidance.
- [`tutorial/README.md`](tutorial/README.md) — how to open and teach the notebook.
- [`starter.py`](starter.py) — intentional student TODO scaffolds for three representations, not completed graded implementations.
- [`benchmark.py`](benchmark.py) — reproducible experiment harness for a built-in reference baseline; shows how to attach student-complete classes.
- [`examples/demo.py`](examples/demo.py) — standalone demonstration of contract checks and reproducible inputs.
- [`tests/test_contract.py`](tests/test_contract.py) — standard-library unit tests against a built-in baseline by default; students switch target only after implementing a class.

## How to use
```bash
cd sessions/S05
python examples/demo.py
python benchmark.py --sizes 100 500 1000 --repeats 5
python -m unittest discover -s tests -p 'test_*.py' -v
```
Open `tutorial/S05_Symbol_Table_Studio.ipynb` directly in Google Colab; **Runtime → Run all** works before students fill TODOs because incomplete student implementations are never invoked by default. After implementing the starter classes, replace the reference implementation in the tests/benchmark as explained in comments.

## Important academic boundary
The official **Assignment 1 scope** is to implement and compare *array-based, linked-list-based and BST-based symbol tables*, with correctness and empirical comparison. The designation of S05 as a **release, checkpoint, submission or due date**, per-assignment mark allocation within the official 40%, deadlines, rubric and graded language requirements are **pending institutional confirmation**. This session makes **none** of those decisions and does not offer complete assignment answers. The official exam remains a separate closed-book examination worth 60%.

**Core reading:** Cormen et al. (2022), *Introduction to Algorithms*, 4th ed.; Goodrich, Tamassia & Goldwasser (2013), *Data Structures and Algorithms in Python*; Sedgewick & Wayne (2011), *Algorithms*, 4th ed.; approved `course-plan.md`, S05 brief.
