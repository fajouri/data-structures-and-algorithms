# S01 — Algorithmic thinking, ADTs and asymptotic analysis

**Contact:** 3 hours, face to face. The course plan proposes about 10 hours of independent study for this session; that allocation is illustrative, not an assessment deadline.

## What you should be able to do

| Session objective | Descriptor outcome (local plan label) |
|---|---|
| Specify an algorithm's inputs, outputs and assumptions, then justify a suitable membership-check approach. | C2: Select appropriate data structures and algorithms for a given problem, justifying the choice analytically. |
| Trace a search loop and explain why its invariant proves the result on termination. | C3: Analyse algorithm correctness using loop invariants and recurrence relations. This session introduces invariants; recurrences follow in S02. |
| Count work and compare cautious timing observations with predicted growth. | C6: Measure and compare empirical performance of algorithms against theoretical predictions. |
| Separate an ADT's operations and contract from a concrete representation. | K1: Define arrays, linked lists, stacks, queues, trees, heaps, hash tables, and graphs as abstract data types. This session introduces the distinction and examples; later sessions develop each structure. |
| Use Big-O, Big-Omega and Big-Theta with a stated input size and cost model. | K2: Recall Big-O, Big-Omega, Big-Theta notation and apply them to classify algorithm complexity. |

## Before class

You should be comfortable with variables, `for` loops, functions and elementary algebra. Review logarithms and the difference between a mathematical bound and a measured time. No formal institutional entry prerequisite is asserted here.

Bring a laptop if available. The Python notebook runs in Google Colab or a local Jupyter environment. `lab.py` runs offline with Python 3. A C++17 compiler and Visual Studio Code are useful for `lab.cpp`; the Python route remains usable without them. Paper traces remain possible if devices or internet access fail.

## 180-minute teaching plan

| Minutes | Activity | Evidence of learning |
|---:|---|---|
| 0–10 | Prediction: which membership check would you choose for one query and for many queries? State assumptions. | Individual prediction, then brief pair discussion. |
| 10–40 | Explain algorithm specification, input size, ADT contract and concrete representation, using a membership service as the running example. | Students name operations and distinguish contract from storage. |
| 40–65 | Trace linear search, including empty and missing cases; build a loop invariant together. | Students annotate states and challenge the termination argument. |
| 65–110 | Trace a duplicate check; count comparisons; derive best, worst and conditional average cases and time/space bounds. | Paired count and whole-class reconciliation. |
| 110–150 | Guided lab: run the Python examples, alter input size/order, inspect repeated timings; compile and run the C++ analogue when a toolchain is available. Allow setup/debugging time. | Small trace table and a measurement note with environment and limitations. |
| 150–170 | Work on the five classification prompts and the search-invariant exercise in `exercises.md`; discuss algorithm choice under changed assumptions. | Short written justifications, not only complexity labels. |
| 170–180 | Exit ticket: state one justified bound and one reason a timing observation cannot prove it. Preview recurrences in S02. | Two-sentence response. |

The 30-minute opening explanation, portions of the traces, and the notation discussion provide roughly 65–75 minutes of direct theory. The rest is prediction, demonstration, practice and feedback. Adapt the clock for institutionally required breaks without changing the three contact hours.

## Materials and commands

- [Lecture notes](lecture.md) explain the definitions, traces, proof and complexity assumptions.
- [Exercises](exercises.md) are ungraded student practice and contain no worked answers.
- [Editable slide source](slides.md) and [PowerPoint deck](slides.pptx) provide classroom prompts and detailed speaker notes.
- [Colab notebook](lab.ipynb), [offline Python](lab.py) and [C++17 source](lab.cpp) contain runnable demonstrations and self-checks.

From this directory:

```text
python lab.py --self-check
python lab.py --benchmark
g++ -std=c++17 -O2 -Wall -Wextra -pedantic lab.cpp -o lab
./lab --self-check
./lab --benchmark
```

On Windows, run `lab.exe` after compiling. In Colab, upload/open `lab.ipynb` and run its cells in order. Use the notebook's stated measurements only as observations from your own machine.

## Independent study

Review logarithms and growth functions; complete the remaining complexity and invariant prompts in `exercises.md`; explain in writing how the empty input changes a search proof. Use the reading list below for a deeper account of asymptotic notation and ADTs. The plan's 10 hours are an illustrative share of the module's 212 self-study hours.

## References

- Official *M12 Data Structures and Algorithms Module Descriptor*, pp. 1–3, for learning outcomes and module scope.
- Cormen, Leiserson, Rivest and Stein, *Introduction to Algorithms*, 4th ed. (2022), chapters 1–3 for algorithm analysis and asymptotic notation.
- Goodrich, Tamassia and Goldwasser, *Data Structures and Algorithms in Python* (2013), introductory chapters on Python, algorithms and data structures.
