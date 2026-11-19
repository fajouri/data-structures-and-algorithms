# S05 Slide Source — Assignment 1 Studio: Symbol Tables and Benchmarking

**Deck:** 20 slides · 16:9 · editable shapes/text · native PowerPoint speaker notes. **Teaching total: 180 minutes.**
**Status:** DRAFT — teaching material, not an approved graded brief.
**Outcomes:** C1, C2, C6, S1, S6 (local approved-plan references).

## Slide 01 — Assignment 1 Studio: build, test, compare
**Time:** 5 min (minute 0–5).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** ONE CONTRACT. THREE STRUCTURES. FAIR EVIDENCE.
**Visible content:** Array-based symbol table; Linked-list symbol table; Plain BST symbol table.
**Visual specification:** hero — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Open by connecting to S03 arrays/linked lists and S04 symbol tables/BSTs. Say: Today we move from knowing separate data structures to comparing implementations of the same service. Ask learners to predict which representation might perform best at lookup when there are only five keys. Do not give the answer; the answer depends on the operation, order and assumptions. Emphasise that this is a 3-hour assignment-support studio rather than an approved graded brief. Transition: make the external contract identical first.

## Slide 02 — What you will be able to do
**Time:** 5 min (minute 5–10).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** CORRECT FIRST; FAST SECOND.
**Visible content:** Specify a shared map contract; Test boundary cases and structural invariants; Measure the same workload reproducibly; Explain trade-offs with evidence.
**Visual specification:** goals — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Ask for one learning goal from each learner. Clarify the assessed module scope: Assignment 1 involves array, linked-list and BST symbol tables plus correctness and empirical comparison. The exact due date, marking rubric, breakdown of the module's assignment component, and graded-language requirements are pending institutional confirmation. This slide does not issue them. Have pairs state why a fast program that gives wrong results must be excluded from a meaningful performance comparison. Transition into concrete API semantics.

## Slide 03 — The symbol-table contract
**Time:** 6 min (minute 10–16).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** BEHAVIOUR SHOULD NOT DEPEND ON STORAGE.
**Visible content:** put(k,v): insert or update; get(k): value or KeyError; delete(k): remove or KeyError; contains(k), len(): membership, unique-key count.
**Visual specification:** api — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Define ADT as public operations and their observable behaviour, not an internal layout. For today's teaching exercise, use comparable integer keys; stored values can include None; existing puts update a key without increasing size. Show that missing `get` raises KeyError consistently. Ask why `get(k) is not None` is not a valid membership test when None is a stored value. This is a teaching convention, not a mandated graded API. Have students record any ambiguity before code. Transition to a short trace.

## Slide 04 — Trace one operation sequence
**Time:** 6 min (minute 16–22).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** UPDATE ≠ NEW KEY.
**Visible content:** put(20, A) → size 1; put(40, B) → size 2; put(20, C) → size 2; get(20) → C; delete(40) → size 1.
**Visual specification:** trace — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Start with empty state. Invite students to predict size before revealing each state. Ask one student to track observable values and another to track logical key count. In an array, incorrect append on duplicate put creates two conflicting records; in a linked list, two matching nodes may create ambiguous searches; in a BST, duplicate comparison handling can violate uniqueness. These are correctness failures independent of benchmark speed. Ask for the outcome of get(40) after deletion: under this teaching contract, KeyError. Transition to storage details.

## Slide 05 — Representation A: array of pairs
**Time:** 6 min (minute 22–28).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** SEQUENTIAL SEARCH; CONTIGUOUS REFERENCES.
**Visible content:** Unsorted entries: [(20,C), (40,B), ...]; Key uniqueness must be enforced; Lookup and duplicate detection: worst-case Θ(n); Physical append ≠ complete put cost.
**Visual specification:** array — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Draw an unsorted array of key/value pairs and run a failed lookup from left to right. Explain that an amortized O(1) Python append does not remove the O(n) search required to enforce unique keys. Deletion may shift entries; this implementation detail affects constants. A sorted array is a different design and permits binary search but still may shift Θ(n) elements. State which variant you are analysing. Have students describe the representation invariant in one sentence. Transition to pointers and tree paths.

## Slide 06 — Representations B and C
**Time:** 7 min (minute 28–35).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** FOLLOW LINKS OR FOLLOW KEY ORDER.
**Visible content:** Linked list: head → node → node → null; Plain BST: left < node < right (globally); Linked lookup: worst-case Θ(n); BST lookup: O(h+1), up to O(n).
**Visual specification:** comparison — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Draw a chain and a small tree holding the same bindings. The linked-list invariant requires finite, acyclic links and no duplicate keys. Prepending a known-new node takes O(1), but checking key uniqueness still needs O(n) without another index. In the BST, emphasize all descendants, not just immediate children, must obey the key-order rule. Height h is maximum edges root to leaf; ordered insertion can produce a chain. Ask: Is a plain BST guaranteed logarithmic? No. Transition to checking these invariants systematically.

## Slide 07 — Three invariants to preserve
**Time:** 7 min (minute 35–42).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** INVARIANTS PROTECT CORRECTNESS.
**Visible content:** Array: every key occurs at most once; Linked list: finite chain; no duplicates; correct size; BST: strict global order; values stay with keys.
**Visual specification:** invariants — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Say an invariant is a statement intended to remain true before and after each operation. Ask learners to choose one destructive update per representation and say what can go wrong. Array put may accidentally append a duplicate. Linked delete can lose the remaining list by changing the wrong pointer. BST delete can replace a successor key but forget its associated value or right child. A loop must also make progress to terminate; for a list, current advances, for a BST, search descends. Tell students they will test observable behaviour and separately reason about invariants.

## Slide 08 — Test the edges, not just the happy path
**Time:** 7 min (minute 42–49).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** WRITE AN EXPECTED RESULT BEFORE CODE.
**Visible content:** Empty get and delete; Duplicate-key update, including value None; Delete list head and BST leaf / 1 / 2 children; Sorted insertions; absent and negative keys.
**Visual specification:** tests — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Give pairs 90 seconds to propose a bug-triggering operation sequence and expected result. Discuss how testing a single happy-path lookup misses deletion bugs, duplicate keys and size drift. Use a test matrix: input operation, expected output or exception, expected length, invariant targeted. Be precise about KeyError for absent keys under the teaching contract. Separate observed test successes from a proof for all possible sequences. Open the Colab contract-check cell next.

## Slide 09 — Differential testing with an oracle
**Time:** 7 min (minute 49–56).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** SAME OPERATIONS → SAME OBSERVABLE ANSWERS.
**Visible content:** Fresh Python dict acts as behavioural oracle; Use the same deterministic operation sequence; Compare return values, exceptions, membership and size; A matching trace is evidence, not proof.
**Visual specification:** oracle — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Run the notebook's DictReference contract check first. Explain that Python dict is a correct behavioural reference for the teaching API; it is not one of the three required Assignment 1 implementations. Students should adapt exceptions if their later institution-approved contract differs. Make a note that if internal ordering is unspecified, a student list and a dict need not iterate in the same order. Ask how a stored None value changes tests. Transition to fair performance experiments only after correctness passes.

## Slide 10 — Six rules for a fair benchmark
**Time:** 7 min (minute 56–63).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** CHANGE ONE THING AT A TIME.
**Visible content:** Same n, same keys, same operation mix; Setup separated from timed lookup; Fixed seed and stated input distribution; Warm-up, repeated runs, median + units; Check results and record environment.
**Visual specification:** fairness — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Introduce a controlled experiment: the dependent measure is time, the factor is implementation, and other relevant conditions remain fixed. Build all tables before timing lookup. Always use the same queries, including hit/miss proportions. Use a reproducible `random.Random(42)` instance but do not claim that one seed represents all random inputs. Timing noise arises from OS scheduling, caching, allocations and interpreter effects. The median of repeated runs is a robust descriptive statistic, not a proof. Explain the distinction between theoretical comparison counts and measured wall-clock time.

## Slide 11 — Live baseline: lookup experiment
**Time:** 7 min (minute 63–70).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** MEASURE LOOKUPS, NOT PRINTING.
**Visible content:** Build sample data outside timer; Run a warm-up batch; Time many identical get operations; Verify checksum; report µs per operation; This baseline is not the 3-table assignment result.
**Visual specification:** benchmark — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Open the Colab benchmark demo. The two illustrative mechanisms are linear scan of a list of pairs and built-in dict lookup; do not label this a completed A1 comparison. Explain the units: elapsed nanoseconds divided by queries then divided by 1,000 yields microseconds per operation. Ask the class to predict how time may change at n=100,500,1000, but do not announce fabricated measurements. Run live; ask students to record the environment and observed numbers. Distinguish data-generating work (outside time) from operations timed. Transition to independent studio work.

## Slide 12 — Studio phase A: define and test
**Time:** 14 min (minute 70–84).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** BUILD A TEST MATRIX BEFORE IMPLEMENTING.
**Visible content:** Specify keys, values and absent-key rules; Write 2–3 test cases for each operation; Identify the invariant each test targets; Run baseline checks before student implementation.
**Visual specification:** studioA — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Allow fourteen minutes for contract/test design. Work in pairs for peer review, but remind learners that rules for formal collaborative submissions have not been confirmed. Ask students to write at least one input sequence that would expose a duplicate-key bug and one that tests missing deletion. Show where the Colab `basic_contract_check` runs against DictReference. If students are stuck, provide a prompt: What happens when put(8,old), put(8,new), then len() is called? End this stage by collecting one unexpected edge case from the class.

## Slide 13 — Studio phase A: adversarial cases
**Time:** 14 min (minute 84–98).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** ONE TEST CAN REVEAL A STRUCTURAL BUG.
**Visible content:** Array: duplicate update and correct size; List: delete head, interior, then tail; BST: delete root with two children; All: lookup missing key, value None.
**Visual specification:** studioA2 — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Guide students through a tiny hand trace with the S04 seven-key BST [50,30,70,20,40,60,80]. They should identify the target delete case and expected remaining bindings without receiving full code. A two-child deletion must preserve the successor key AND its value. Compare the hand trace to the planned public tests. Ask each group to explain why this tests correctness rather than performance. Encourage test-first development and label unsolved operations explicitly, not as completed.

## Slide 14 — Studio phase B: array and links
**Time:** 14 min (minute 98–112).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** COMPLETE ONE METHOD; TEST; REPEAT.
**Visible content:** Array: get → put → delete → contains → size; Linked: find → update or insert → unlink; Diagram the predecessor before deleting a node; Document worst-case cost with assumptions.
**Visual specification:** studioB — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Students open starter.py or the notebook TODO cell. Explain that scaffolds are intentionally incomplete to avoid distributing finished assignment solutions. In the array, scanning to check a duplicate is logically separate from physical append. In the linked list, the head case differs from an interior removal. Ask learners to draw previous, current and next before writing pointer mutations. Each completed method should trigger a small test and a statement of the invariant. Offer hints, not entire functions. If internet fails, draw the operations and trace manually.

## Slide 15 — Studio phase B: BST integrity
**Time:** 14 min (minute 112–126).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** HEIGHT IS THE COST DRIVER.
**Visible content:** Search descends one branch at each step; Insert must preserve strict key ordering; Delete: leaf / one child / two children; Two-child case: move successor key AND value.
**Visual specification:** studioBST — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Have students draw a 7-node BST and trace search for a missing key, then the two-child deletion. Make clear that the successor cannot have a left child but may have a right child. Updating only the successor's key and not its value violates the map contract. For recursive implementations, discuss call-stack use and Python recursion limits on chain-shaped trees. Students may not complete all methods in class; they should accurately document which tests are passing. The follow-up studio phase measures only correct implementations.

## Slide 16 — Studio phase C: identical input datasets
**Time:** 14 min (minute 126–140).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** SORTED AND SHUFFLED ARE DIFFERENT EXPERIMENTS.
**Visible content:** Use n = 100, 500, 1000 for teaching trials; Create shuffled keys with seed 42; Include ascending-order insertion; Keep hits, misses, updates and deletes separate.
**Visual specification:** workloads — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Students generate immutable key lists once, then pass copies to each implementation. Explain why sorted input can make a plain BST linear in height whereas shuffled insertion often produces a shorter tree in a particular run. We do not claim a universally balanced random tree. Ask what n means: number of unique bindings, not number of total operations unless specified. Students who cannot finish implementations can inspect the notebook's comparison-count shape demo as meaningful practice, but should not present it as full symbol-table benchmark data.

## Slide 17 — Studio phase C: repeat and record
**Time:** 13 min (minute 140–153).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** NO TIMINGS BEFORE CONTRACT TESTS PASS.
**Visible content:** perf_counter_ns for timing; One warm-up, ≥5 repeated runs for practice; Median µs/op; state n and operation count; Document runtime, OS, seed and distribution; Do not invent values for unfinished implementations.
**Visual specification:** measure — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Have learners fill the blank experiment table in Colab. Remind them that a benchmark should isolate the cost being studied: for hit lookup, build the structure outside the timed loop and check a result checksum. For insert timing, include the building operations deliberately and disclose what exactly was measured. If one implementation fails public tests, mark it not measured. Students with very fast operations should increase batch size instead of recording timer-resolution artefacts. Discuss that memory overhead and cache locality may affect real results but are not captured fully by asymptotic notation.

## Slide 18 — Studio phase D: peer review and report
**Time:** 12 min (minute 153–165).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** DEFEND A CLAIM WITH CONDITIONS.
**Visible content:** Peer checks one contract test and one invariant; Report: n, workload, structure, median and repeats; Explain predicted complexity + observed limitations; Describe a decision for a concrete workload.
**Visual specification:** report — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Pair-review one line of code or one small trace, not full solutions. Peer checks for hidden differences in semantics and workload. Ask students to write a two-sentence engineering decision: For workload X with input distribution Y, choose Z because..., provided..., and with limitation.... If there is noisy or inconclusive timing, it is valid to say so. Encourage result tables where blank means unmeasured rather than copying sample or invented numbers. Identify one potential confounder in every report. Transition to whole-class reflection.

## Slide 19 — Exit ticket: show your reasoning
**Time:** 7 min (minute 165–172).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** INVARIANT · EDGE CASE · FAIRNESS.
**Visible content:** 1. State a representation invariant; 2. Describe one bug-catching test; 3. Name one benchmark confounder.
**Visual specification:** exit — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Ask individuals to write their responses before discussion. A good invariant might say no duplicate keys, or global BST ordering. A strong test might delete a BST node with two children and verify both key and value of the successor. Fairness confounders include unequal input order, measuring setup in one implementation only, different operations, timing print statements, or differing environment. Stress that correctness tests and asymptotic proofs answer different questions. Do not convert these answers into an unapproved formal grade.

## Slide 20 — Next steps and academic boundary
**Time:** 8 min (minute 172–180).
**Outcome:** C1, C2, C6, S1, S6
**Visible takeaway:** KEEP THE EVIDENCE. CHECK THE OFFICIAL BRIEF.
**Visible content:** Finish implementations from starter TODOs; Retest every representation under one contract; Run reproducible sorted/shuffled experiments; Use institution-approved A1 release, rubric and dates.
**Visual specification:** finish — editable PowerPoint native shapes/text; no flattened figure.
**Speaker notes:** Summarise the thread: ADT contract, invariant, tests, fair measurement, cautious interpretation. Preview S06 balanced trees, explaining why guaranteed logarithmic height requires maintenance rather than wishful thinking. Tell students the official descriptor specifies Assignment 1's three table types and empirical correctness comparison, but the interpretation of S05 as release/checkpoint/submission, deadlines, per-assignment weighting, rubric and graded implementation languages are pending institutional confirmation. Ask what one thing they will improve before the next teaching session. Thank them and close at 180 minutes.

## PowerPoint handoff
The corresponding `slides.pptx` contains actual native speaker notes, editable text boxes and shape diagrams. Recreate or revise it using this source. Never add unconfirmed official grades, deadlines or answer keys.
