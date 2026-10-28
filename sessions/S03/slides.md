# S03 Slide Source — Arrays, dynamic arrays, linked lists and amortised costs

**Deck status:** editable source drafted; native PowerPoint export pending.  
**Target:** 16:9; readable, high-contrast, editable native shapes/text/tables/arrows. Do not flatten slides into images.  
**Audience:** MSc Computer Science. Timings total 180 minutes including the break and activities.

## Slide 01 — One sequence, different representations
**Outcome:** C1, C2, K1  
**Visible:** “ADT = contract. Representation = storage + invariant. Operation mix determines choice.”  
**Visual:** Three panels show the same values in a contiguous array, dynamic array with spare slots, and linked nodes.  
**Speaker notes:** Ask which structure suits frequent indexed reads versus edits after a known node. The logical sequence can be identical while operation costs differ. State the unit-cost RAM model. **Time:** 6 min. **Transition:** define the contract.

## Slide 02 — Sequence ADT and invariant
**Outcome:** C1, C3, K1  
**Visible:** length, get, set, append, insert, remove, iterate.  
**Visual:** Two columns: observable contract and concrete storage/invariant.  
**Speaker notes:** Explain that “elements occupy adjacent addresses” is a representation detail, not an ADT promise. State the dynamic-array invariant 0 ≤ size ≤ capacity and linked-list reachability invariant. **Time:** 8 min. **Transition:** array access follows from address arithmetic.

## Slide 03 — Contiguous memory
**Outcome:** C1, K2  
**Visible:** address(i) ≈ base + i × element-size; indexed access Θ(1).  
**Visual:** Native array cells labelled 0–4 with an index arrow.  
**Speaker notes:** Index calculation does not visit earlier elements. Mention cache locality as a practical advantage, not an asymptotic guarantee. Assume fixed-size elements. **Time:** 7 min. **Transition:** insertion shifts data.

## Slide 04 — Insert into the middle
**Outcome:** C1, C3, K2  
**Visible:** Insert 25 into [10,20,30,40] at index 2; shift 40, then 30, then write 25.  
**Visual:** Three array rows showing shifts and final result.  
**Speaker notes:** Shift from right to left to avoid overwriting values. Two existing values shift. Generalise to Θ(n) worst-case insertion. **Time:** 8 min. **Transition:** spare capacity motivates dynamic arrays.

## Slide 05 — Size is not capacity
**Outcome:** C1, K1, K2  
**Visible:** size = logical elements; capacity = allocated slots; 0 ≤ size ≤ capacity.  
**Visual:** Eight slots, five occupied; separate size and capacity markers.  
**Speaker notes:** Spare slots are not sequence elements. Appending writes at index size, then increments size. Ask what happens when size equals capacity. **Time:** 7 min. **Transition:** a full array must grow.

## Slide 06 — A resize is expensive
**Outcome:** C1, C6, K2  
**Visible:** Capacity 4 → allocate 8 → copy 4 elements → append. One operation Θ(n).  
**Visual:** Two arrays and arrows showing copied values.  
**Speaker notes:** One append can copy all existing values, so worst-case cost is Θ(n). This does not contradict amortised Θ(1). Diagram is not a benchmark. **Time:** 8 min. **Transition:** count copies over many appends.

## Slide 07 — Capacity trace
**Outcome:** K2, K6  
**Visible:** Capacity sequence 1, 2, 4, 8, 16; copy counts 1, 2, 4, 8.  
**Visual:** Editable table of append, size, capacity, copies.  
**Speaker notes:** Ask students to predict the ninth append. Growth factor is an implementation policy; doubling is the model for the proof. **Time:** 8 min. **Transition:** turn the pattern into a bound.

## Slide 08 — Aggregate analysis
**Outcome:** K2, K6  
**Visible:** n writes; geometric copies < 1 + 2 + 4 + … + 2ᵏ = O(n); total Θ(n); amortised Θ(1).  
**Visual:** Geometric blocks bracketed as linear total work.  
**Speaker notes:** There are n writes and O(n) copies; the writes give Ω(n). Total is Θ(n), so average cost over the sequence is Θ(1) amortised. This is not random-input average-case analysis. **Time:** 10 min. **Transition:** linked storage changes access cost.

## Slide 09 — Singly linked list anatomy
**Outcome:** C1, K1  
**Visible:** head → [10|next] → [20|next] → [30|null].  
**Visual:** Node rectangles with value/link fields and arrows; include empty state.  
**Speaker notes:** Nodes need not be contiguous. State that following links from head visits the sequence once and terminates at null. **Time:** 8 min. **Transition:** traverse to an index.

## Slide 10 — Indexed access needs traversal
**Outcome:** C1, K2  
**Visible:** To reach index 2, follow two links; worst-case Θ(n).  
**Visual:** Highlight each visited node and count steps.  
**Speaker notes:** Logical index is not physical address arithmetic. A sorted linked list is still a poor binary-search target because midpoint access is not Θ(1). **Time:** 7 min. **Transition:** insertion can be cheap if location is known.

## Slide 11 — Link updates
**Outcome:** C1, C3  
**Visible:** Insert 15 after 10: new.next = old successor; then 10.next = new.  
**Visual:** Before/after diagrams preserving the suffix.  
**Speaker notes:** Explain pointer-update order. Known predecessor means Θ(1) link updates; finding it by scan can cost Θ(n). Removal redirects predecessor.next to the successor. **Time:** 9 min. **Transition:** compare costs.

## Slide 12 — Complexity comparison
**Outcome:** C2, K2  
**Visible:** Array index Θ(1); list index Θ(n); front insert array Θ(n), list Θ(1); dynamic append Θ(n) worst-case / Θ(1) amortised.  
**Visual:** Editable comparison table with assumptions.  
**Speaker notes:** Do not say linked-list insertion is constant time without saying the location is known. Unsorted search is Θ(n) for both. Discuss memory overhead and locality. **Time:** 9 min. **Transition:** choose for a workload.

## Slide 13 — Choose for the workload
**Outcome:** C2, C6  
**Visible:** Random access → dynamic array; edits around known nodes → linked list may fit; repeated key search → consider another ADT.  
**Visual:** Three scenario cards with a blank reason line.  
**Speaker notes:** Let pairs choose before discussing. Include operation frequency, memory, and location discovery. **Time:** 8 min. **Transition:** verify in code.

## Slide 14 — Practical: mutate and test
**Outcome:** C1, C3, C6, S6  
**Visible:** Run Python self-check; compile C++17 with warnings; test empty, singleton, duplicates and repeated mutations.  
**Visual:** Checklist beside code and state table.  
**Speaker notes:** Compare logical results and invariants, not only printed output. Python list and C++ vector are dynamic-array examples; the linked-list implementation is explicit. Use paper traces if the toolchain fails. **Time:** 30 min. **Transition:** retrieve the main ideas.

## Slide 15 — Exit ticket
**Outcome:** C2, K2, K6  
**Visible:** “One worst-case cost? One amortised cost? One invariant?”  
**Visual:** Three short response prompts.  
**Speaker notes:** Students write an expensive resize example, sequence-level guarantee, and list invariant. Correct misconceptions. Preview stacks, queues and trees in S04. **Time:** 7 min.

## PowerPoint handoff

Create slides.pptx as an editable 16:9 deck using native PowerPoint shapes, text, tables and connectors. Put the full speaker notes into each slide's native Notes page. The deck remains pending until generated, opened to verify layout, and checked for native speaker notes. This source is not evidence that a PowerPoint file exists or was validated.
