# S01 editable slide source and speaker notes

The companion `slides.pptx` is a 16:9 editable deck. Titles, labels, diagrams and pseudocode are native PowerPoint text and shapes; each slide has native speaker notes. This Markdown remains the slide-by-slide authoring source. Times indicate how to use selected slides within the 180-minute agenda in `README.md`, not 180 minutes of lecturing.

## Slide 01 — S01: reasoning about algorithms
Outcome: C2, C3, C6, K1, K2.

Visible:
- Algorithm specification
- ADT and representation
- Correctness, cost and measured time

Visual: Three editable columns labelled Contract, Proof and Cost, linked by a membership-check example.

Speaker notes: Allow 2 minutes. Introduce the catalogue-membership question: how would we answer one query against an unsorted list, and what changes if queries repeat? Say that an algorithm choice has to meet a behaviour contract before speed matters. Name the three kinds of evidence the session will use: a precise specification, an invariant argument and controlled observation. Avoid claiming that a stopwatch proves an asymptotic class. Ask students to keep one example in mind as definitions arrive. Transition to a prediction before giving costs.

## Slide 02 — Membership prediction
Outcome: C2, C6.

Visible:
- One query over 30 unsorted values
- Many queries over the same values
- What changes if values are updated?

Visual: Editable row of 30 small cells plus a repeated-query icon made from circles and labels.

Speaker notes: Allow 8 minutes including pair discussion. Ask for a choice and its assumptions, not a named data structure alone. A sequential scan has no setup cost. Repeated queries may justify building an index, but construction and updates matter. Do not present a hash table as automatically constant time. Invite one student to distinguish a query from a workload. Collect predictions without grading them; revisit after comparing bounds and observations. Transition to specifying the exact output required.

## Slide 03 — Specify the operation
Outcome: C2, C3.

Visible:
- Input: sequence A of length n; target x
- Output: first matching index or −1
- Unsorted input; equality defined

Visual: Editable indexed cells [7, 4, 7, 9] with index labels and two highlighted 7s.

Speaker notes: Allow 8 minutes. Ask which index should be returned for target 7. Emphasise that a boolean membership request has a different contract from first-index search. A duplicate example exposes an otherwise hidden specification choice. State that equality is assumed to be defined and, for the first cost model, constant time. If comparing long strings, equality cost can vary. Ask what should happen for an empty sequence. Transition to the ADT distinction.

## Slide 04 — ADT contract and representation
Outcome: K1, C2.

Visible:
- Contract: operations and observable behaviour
- Representation: how values are stored
- Algorithm: steps for one operation

Visual: Three editable labelled boxes, with `contains(x)` in Contract and array/list/tree/hash examples beneath Representation.

Speaker notes: Allow 11 minutes. A set-like ADT can offer contains, insert and remove while leaving physical storage unspecified. A dynamic array and linked list can support sequence behaviour with different indexed-access and update costs. Explain that “array” is used both informally for an indexed collection and concretely for contiguous storage, so context matters. Ask students whether the caller can observe node pointers in a normal sequence contract. Mention that later sessions develop structures named in the descriptor. Transition to operation mix.

## Slide 05 — Representation depends on workload
Outcome: C2, K1.

Visible:
- One scan avoids index construction
- Repeated queries can repay setup
- Updates and memory change the choice

Visual: Editable two-column comparison: one query versus repeated queries, with setup and per-query cost labels left symbolic.

Speaker notes: Allow 11 minutes. Work through a catalogue loaded once: a scan may be simplest for one request, while an index has an upfront cost that may be repaid over repeated lookups. A changing catalogue adds update cost. Resist presenting a numeric crossover without hardware and workload data. Ask what happens if the representation must preserve order or duplicates. Students should identify contract requirements before comparing costs. Transition to a concrete correct scan.

## Slide 06 — Linear search pseudocode
Outcome: C3, K2.

Visible:
- For i from 0 to n−1
- If A[i] equals x, return i
- After the loop, return −1

Visual: Native text pseudocode next to indexed cells [9, 4, 4, 1].

Speaker notes: Allow 5 minutes. Trace target 4 one comparison at a time and stop at index 1. Ask why the second 4 is not inspected. Make students predict the result for absent target 7 and empty input. If the loop never starts, the final return still meets the specified behaviour. Highlight that the returned index is zero based. The next slide states an invariant that explains first-index correctness for all finite inputs.

## Slide 07 — Search invariant
Outcome: C3.

Visible:
- Before index i: no earlier index matches x
- Failed comparison extends the checked prefix
- Match or exhaustion establishes the result

Visual: Editable indexed cells with a coloured checked prefix and an untested suffix; a moving i marker.

Speaker notes: Allow 12 minutes. State initialization: at i=0 the earlier prefix is empty. For maintenance, when the current element differs, the no-match prefix extends to include it. For a match, the invariant excludes any earlier match, proving the first-index promise. At exhaustion, the prefix is the entire input, proving the −1 result. Termination follows because i increases and is bounded by finite n. Ask students which part of the argument would fail if the loop skipped an index. This is a proof, separate from testing.

## Slide 08 — Search traces and edge cases
Outcome: C3, K2.

Visible:
- Empty: no comparisons
- First match at j: j+1 comparisons
- Absent: n comparisons

Visual: Three editable short rows showing empty, first-match and absent traces, with comparison counters.

Speaker notes: Allow 8 minutes. Use [7,4,7,9] for a first-position match and [9,4,4,1] for a second-position match. Ask a student to state the count for a singleton miss. The formulas are exact equality-check counts under the chosen model. Distinguish the empty input from a constant-time best case for n>0. Do not call all successful searches constant time. Transition to a second algorithm whose nested loops reveal a different growth rate.

## Slide 09 — Pairwise duplicate detection
Outcome: C2, C3, K2.

Visible:
- Compare each A[i] with later A[j]
- Return true on a match
- Return false after every pair is checked

Visual: Editable triangular grid of pairs for [3, 8, 5, 8], with the matched pair highlighted.

Speaker notes: Allow 8 minutes. Trace pairs in loop order: (0,1), (0,2), (0,3), (1,2), then (1,3) matches. Explain the invariant that every earlier pair has been checked and found unequal. A match justifies immediate true; a false result requires exhaustion. For no duplicate, the pair count is n(n−1)/2. Ask what happens on empty and singleton input. Transition to separating input cases from growth notation.

## Slide 10 — Best, average and worst cases
Outcome: K2, C2.

Visible:
- Search: first, distributed first position, absent
- Duplicate check: early match or all pairs
- Average needs a stated distribution

Visual: Editable three-column table headed Best, Average model and Worst, with symbolic comparison counts.

Speaker notes: Allow 7 minutes. For a present search with a uniformly distributed first matching position, derive (n+1)/2 comparisons. State that this is a conditional teaching model and that duplicates or absent queries change it. For pairwise duplicate detection, an immediate first-pair match takes one comparison when n≥2; no duplicates take n(n−1)/2. Do not announce an average-case pair count without a distribution. Ask whether worst case means all runs are slow. Transition to formal bounds on selected cost functions.

## Slide 11 — Three asymptotic bounds
Outcome: K2.

Visible:
- O(g): eventual upper bound
- Ω(g): eventual lower bound
- Θ(g): both bounds

Visual: Editable axes with a growth curve between scaled lower and upper envelopes after n₀.

Speaker notes: Allow 10 minutes. Give the quantified definition in the lecture notes: positive constants and a threshold n₀. The functions considered are nonnegative for sufficiently large n. Big-O is an upper bound on a specified cost function, not a synonym for worst case. A worst-case cost can itself be O(n), while a best-case cost can be Θ(1). Ask whether 3n²+5n+7 is O(n³) as well as Θ(n²); explain that a loose upper bound may be true. Transition to counting loops.

## Slide 12 — Count operations before naming growth
Outcome: K2, C3.

Visible:
- Sequential loops add
- Nested pair checks sum 1+…+(n−1)
- State the unit-cost assumption

Visual: Editable row for a single scan and triangle of pair counts 3, 2, 1 for n=4.

Speaker notes: Allow 8 minutes. Derive the pair sum n(n−1)/2 and its Θ(n²) growth, keeping the exact count visible first. Two consecutive n-step scans remain Θ(n), not Θ(n²). A comparison is a unit here; if equality of two long strings costs up to L, the scan can cost O(nL). Ask what is counted by `n` in each example. Mention that recurrences are developed in S02. Transition to memory and the cost model used in practice.

## Slide 13 — Time, auxiliary space and trade-offs
Outcome: C2, K2.

Visible:
- Both scans use Θ(1) auxiliary space
- Input storage is separate
- An index can trade setup and space for queries

Visual: Editable balance diagram with query work on one side and setup/memory on the other.

Speaker notes: Allow 6 minutes. Auxiliary space excludes the given sequence; total storage includes it. The pairwise checker uses constant extra storage even though it does quadratic work on distinct values. A hash-based duplicate checker often uses linear space and expected linear time under suitable assumptions, but collisions and hashing costs matter. Do not claim a universal constant-time lookup or describe an unimplemented alternative as the lab solution. Ask what a service with frequent updates might prefer. Transition to measurement protocol.

## Slide 14 — Measuring without overclaiming
Outcome: C6, K2.

Visible:
- Deterministic inputs and target position
- Warm up; repeat; report a statistic
- Record runtime, compiler flags and hardware

Visual: Editable flow of input construction, repeated timing and interpretation, with comparison count shown separately.

Speaker notes: Allow 6 minutes. The labs use `perf_counter_ns` or `steady_clock`, one warm-up and a median of 11 calls. Input construction is outside the timed region. Ask why a small run can be dominated by timer and scheduling effects. The C++ program records its language standard; students must add compiler and hardware details. Do not compare raw Python and C++ time as if language were the only variable. Comparison counts help connect observations to a proof but do not themselves replace the proof.

## Slide 15 — Lab investigation
Outcome: C6, C2, K2.

Visible:
- Predict counts for n = 16, 64, 256, 512
- Run Python; run C++ if available
- Explain one noisy timing ratio

Visual: Editable blank table with columns n, predicted count, observed time and interpretation.

Speaker notes: Allow 40 minutes, largely away from the slide. Direct students to `lab.ipynb` or offline `lab.py`; `lab.cpp` offers a C++17 analogue. Have them write predictions before pressing Run. Confirm the examples' edge-case checks, then inspect absent search and distinct duplicate-check inputs. Ask for the environment and at least one plausible source of noise. Help with toolchain setup, but preserve the offline Python route and paper comparison-count trace. Point students to `exercises.md` after observing, without giving solutions.

## Slide 16 — Apply, explain and exit
Outcome: C2, C3, C6, K1, K2.

Visible:
- Classify five snippets with assumptions
- Justify the first-index search invariant
- One bound; one measurement limitation

Visual: Editable three-part checklist with blank spaces for student responses.

Speaker notes: Allow 30 minutes including 20 minutes of paired exercise work and a 10-minute exit ticket. Ask students to name the input size, cost model and case for each complexity claim. For the invariant, require initialization, maintenance, termination and both return paths. The exit ticket asks for one justified bound and one reason timing alone does not prove it. Collect questions for S02, which introduces recurrence relations. Avoid showing worked answers; this is student-facing practice.
