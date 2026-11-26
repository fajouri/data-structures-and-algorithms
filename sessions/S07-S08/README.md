# M12 — S07 + S08 | Hash tables, heaps and sorting

Ascencia Malta · MSc Computer Science · Lecturer review draft

Combined delivery: **180 minutes**, 90 per topic. This is a condensed teaching arrangement requested by the lecturer, not a change to the approved official contact-hour total. The approved plan allocates 180 minutes to each original session; the remaining 180 minutes of contact teaching must be reconciled separately. Independent study supports but does not automatically replace contact hours.

Prerequisites: symbol-table ADT, arrays, BSTs, asymptotic analysis and amortisation (S01, S03–S04). S07 outcomes: C1, C2, K1, S1. S08: C1, C2, K4, S2. Students should implement both hash collision strategies, justify performance assumptions, maintain a binary heap, trace heapsort, and explain comparison-sorting lower bounds.

## Agenda
| Minutes | Activity |
|---|---|
| 0–10 | Retrieve symbol-table operations; predict collisions |
| 10–35 | Hashing, load factor, separate chaining |
| 35–55 | Linear probing, deletion, tombstones, resizing |
| 55–75 | Guided Python demo and tests |
| 75–90 | Paired exercise and comparison with BSTs |
| 90–100 | Priority queue ADT and array representation |
| 100–120 | Sift operations, heapify, trace |
| 120–140 | Heapsort, insertion sort, lower bound |
| 140–165 | Guided coding and timing experiment |
| 165–180 | Practice and exit ticket |

If a break is required, adapt activities while respecting institutional rules. No graded assessment requirements are introduced.

## Materials
- [Slide source and speaker notes](slides.md) — editable PowerPoint prepared locally, binary upload pending.
- [Lecture notes](lecture.md)
- [Student exercises](exercises.md)
- [Colab tutorial](tutorial/S07_S08_Hashing_Heaps_Sorting.ipynb): upload notebook to Google Colab, then Run all. No external dependencies.
- [Offline Python lab](lab.py): `python lab.py` (Python 3).

Suggested follow-up (10 h per original session in approved plan): S07 implement both maps independently and compare probe counts across load factors; S08 implement heap operations and compare sort performance across input distributions. Read the corresponding chapters of CLRS (4th ed.) and Goodrich et al. (2013). No assignment solutions or new deadlines are included.
