# S02 Slide Source — Recursion, recurrences, Master Theorem and binary search

**Deck status:** source drafted; editable PowerPoint export pending.  
**Format target:** 16:9, high-contrast, readable from the back of the room. Use native PowerPoint text, lines, rectangles and tables; do not flatten slides into images.  
**Audience:** MSc Computer Science, postgraduate level.  
**Teaching rule:** keep visible content concise; use speaker notes for explanation. Timings below total 180 minutes including guided activities.

## Slide 01 — Why recursion and recurrences?
**Outcome:** C2, C3, K2, K3  
**Visible:** “Program structure: recursion. Cost model: recurrence. Example: binary search halves the remaining interval.”  
**Visual:** Three linked native boxes: problem → smaller problem(s) → combine/return. Add a second row linking code structure to T(n).  
**Speaker notes:** Introduce the central distinction: recursion describes how a procedure calls itself; a recurrence models how the work changes with input size. Ask students where they have seen divide-and-conquer. Set the unit-cost RAM assumption and warn that theoretical bounds and wall-clock timing answer different questions. Ask: “Does every recursive function run in logarithmic time?” Expected discussion: no; it depends on call count, subproblem size and work per call. **Time:** 5 min. **Transition:** start from one call at a time.

## Slide 02 — Anatomy of a recursive function
**Outcome:** C3  
**Visible:** Base case; recursive case; progress measure; combination step.  
**Visual:** Four labelled editable boxes around factorial pseudocode.  
**Speaker notes:** Define each term before using it. A base case returns without another recursive call; the recursive case must move toward a base case. Trace factorial(4), distinguishing descent from return/unwinding. Ask what would happen if n were not decreased. Emphasise that an input contract is part of correctness. **Time:** 10 min. **Transition:** trace active calls.

## Slide 03 — The call stack
**Outcome:** C3  
**Visible:** factorial(4) → factorial(3) → factorial(2) → factorial(1); returns 1, 2, 6, 24.  
**Visual:** Stack of four editable frames; highlight the active frame and pending multiplication.  
**Speaker notes:** A caller remains suspended while the child executes. On return, pending operations resume in reverse call order. Explain that the stack stores control state and local values, so recursive depth contributes to auxiliary space. Ask students to identify the maximum active depth. **Time:** 8 min. **Transition:** reason about termination.

## Slide 04 — Termination is an argument
**Outcome:** C3  
**Visible:** Valid input + reachable base case + decreasing measure ⇒ termination argument.  
**Visual:** Table: input domain / measure / update / base condition. Include an intentionally flawed countdown call as a prompt, not a solution.  
**Speaker notes:** Do not claim that “it looks smaller” is a proof. Name a non-negative integer measure and show that every recursive step decreases it. Invite students to find why a missing return or unreachable base case matters. Mention runtime stack limits separately from mathematical termination. **Time:** 8 min. **Transition:** once calls are understood, count their work.

## Slide 05 — How to write a recurrence
**Outcome:** K2, K3  
**Visible:** T(n) = cost of recursive calls + non-recursive work; always state base condition.  
**Visual:** Three-column editable table: calls, subproblem sizes, combine work. Populate with a generic divide-and-conquer example.  
**Speaker notes:** T(n) denotes running time for input size n. Ask students to inspect an algorithm before writing an equation. Count how many calls are made, how large each input is, and what happens outside the calls. Distinguish a recurrence for time from the recurrence defining the mathematical answer. **Time:** 8 min. **Transition:** first pattern, a single smaller call.

## Slide 06 — Expansion: T(n) = T(n−1) + Θ(1)
**Outcome:** K2  
**Visible:** T(n) = T(n−2)+2Θ(1) = … = T(0)+nΘ(1) = Θ(n).  
**Visual:** Chain of boxes n, n−1, n−2, …, 0; annotate constant work at each node.  
**Speaker notes:** Expand only a few steps first, then generalise after k steps. The chain has linear depth and constant work per level. The base condition is essential. Ask students whether the recursion stack is constant or linear. **Time:** 8 min. **Transition:** what if the problem halves?

## Slide 07 — Halving gives logarithmic depth
**Outcome:** K2, K3  
**Visible:** n → n/2 → n/4 → … → 1; solve n/2ᵏ ≤ 1 ⇒ k ≥ log₂ n.  
**Visual:** Editable decreasing-width bars labelled with subproblem sizes.  
**Speaker notes:** The number of halvings, not the final interval size, determines the number of levels. State n≥1 and ignore floor/ceiling for asymptotic intuition. Connect this to binary search's one recursive branch. Ask students to predict depth for n=64. **Time:** 8 min. **Transition:** multiple branches create a tree.

## Slide 08 — Recursion tree: two halves plus linear combine
**Outcome:** K2, K3  
**Visible:** T(n)=2T(n/2)+Θ(n); each internal level costs Θ(n); Θ(log n) levels.  
**Visual:** Native shapes for the first three levels. Annotate level totals: cn, 2·c(n/2), 4·c(n/4).  
**Speaker notes:** Show that each level's total combine work is proportional to n. There are logarithmically many internal levels and linear total leaf work, so the total is Θ(n log n). State the simplifying power-of-two assumption and explain why rounding does not alter the result. Ask why simply counting leaves is not enough. **Time:** 12 min. **Transition:** generalise with a theorem, but retain conditions.

## Slide 09 — Master Theorem: shape and comparison
**Outcome:** K3  
**Visible:** T(n)=aT(n/b)+f(n); p=log_b a; compare f(n) with nᵖ.  
**Visual:** Three editable columns labelled recursive-dominated / balanced / non-recursive-dominated.  
**Speaker notes:** Define a, b and f(n). Emphasise that the theorem has a required recurrence shape and case conditions; it is not a lookup slogan. Ask students to compute p before selecting a case. **Time:** 10 min. **Transition:** work one case at a time.

## Slide 10 — Case 1: recursive work dominates
**Outcome:** K3  
**Visible:** If f(n)=O(nᵖ⁻ᵋ), then T(n)=Θ(nᵖ). Example: 4T(n/2)+Θ(n)=Θ(n²).  
**Visual:** Native comparison bars for n versus n².  
**Speaker notes:** Here p=log₂4=2. The recursive leaves dominate the lower-order combine work. The ε margin matters: it must be a positive constant. Have students explain why Θ(n) is polynomially smaller than n². **Time:** 7 min. **Transition:** balanced work.

## Slide 11 — Case 2: balanced work
**Outcome:** K3  
**Visible:** If f(n)=Θ(nᵖ logᵏ n), then T(n)=Θ(nᵖ logᵏ⁺¹ n) in the standard case.  
**Visual:** Recursion tree with equal total work per internal level.  
**Speaker notes:** For merge sort, a=2, b=2, p=1, f(n)=Θ(n), so T(n)=Θ(n log n). Explain why one logarithmic factor appears: the tree has logarithmically many levels, each with linear work. **Time:** 8 min. **Transition:** when combine work dominates.

## Slide 12 — Case 3 and regularity
**Outcome:** K3  
**Visible:** If f(n)=Ω(nᵖ⁺ᵋ) and a f(n/b)≤c f(n), c<1, then T(n)=Θ(f(n)).  
**Visual:** A large top-level combine-work bar and smaller descendant bars.  
**Speaker notes:** State the regularity condition explicitly; do not silently omit it. For 2T(n/2)+Θ(n²), p=1 and quadratic f(n) dominates, satisfying the condition for the usual quadratic cost. Ask students why “f is bigger” alone is not the complete theorem statement. **Time:** 8 min. **Transition:** identify cases outside this theorem.

## Slide 13 — When the basic theorem does not fit
**Outcome:** K3  
**Visible:** T(n)=T(n/2)+T(n/3)+n is not aT(n/b)+f(n) with equal subproblem sizes.  
**Visual:** Two branches with different widths, n/2 and n/3.  
**Speaker notes:** The theorem is powerful because its assumptions are specific. Unequal subproblems can need a recursion tree, substitution, or a more general theorem. Ask students to identify the exact mismatch rather than merely saying “it is complicated.” **Time:** 7 min. **Transition:** apply recurrence thinking to binary search.

## Slide 14 — Binary search contract
**Outcome:** C2, C3  
**Visible:** Input must be sorted; interval [lo, hi); return matching index or −1.  
**Visual:** Editable array cells with indices; colour candidate interval and mark hi as excluded.  
**Speaker notes:** Explain that sortedness is a precondition, not an implementation detail. The half-open interval includes lo and excludes hi. It handles an empty array naturally because [0,0) is empty. Ask why a linked list is a poor fit for repeated midpoint access. **Time:** 8 min. **Transition:** trace one successful search.

## Slide 15 — Trace a successful search
**Outcome:** C3  
**Visible:** [2,4,7,9,13,18,21], target 13; states: [0,7) → [4,7) → [4,5) → found at 4.  
**Visual:** Editable row of array cells and a state table with lo, hi, mid and comparison.  
**Speaker notes:** Recompute each midpoint as lo+(hi−lo)//2. First 9 is too small, so exclude indices through mid; then 18 is too large, so exclude mid and above. The next midpoint is 13. Ask students to predict the next state before revealing each row. **Time:** 8 min. **Transition:** turn the trace into a proof.

## Slide 16 — The loop invariant
**Outcome:** C3  
**Visible:** If target occurs in the original array, an occurrence remains inside [lo, hi).  
**Visual:** Three stages: initialise, preserve after comparison, terminate with empty interval or return a match.  
**Speaker notes:** Prove initialization from [0,n). For the smaller-than branch, sortedness means every index ≤ mid is too small; for the larger-than branch, every index ≥ mid is too large. On termination, lo=hi means the interval is empty. The invariant then implies the target is absent if no match was returned. State the progress measure hi−lo. **Time:** 10 min. **Transition:** debug a common boundary error.

## Slide 17 — Off-by-one defect
**Outcome:** C3  
**Visible:** If values[mid] < target, use lo=mid+1, not lo=mid.  
**Visual:** Two-element interval with lo=0, hi=2, mid=1 and a callout showing a non-shrinking interval risk.  
**Speaker notes:** Boundary conventions must be consistent. With a half-open interval, the midpoint has been ruled out, so the next interval begins at mid+1. If lo remains mid, an interval can fail to shrink and the loop can repeat forever. Ask students for a minimal failing case. **Time:** 7 min. **Transition:** compare recursive and iterative implementations.

## Slide 18 — Time and auxiliary space
**Outcome:** C2, K2  
**Visible:** Linear search Θ(n); iterative binary search Θ(log n), Θ(1) extra space; recursive binary search Θ(log n) stack space.  
**Visual:** Editable comparison table.  
**Speaker notes:** State that binary search assumes sorted random-access data. Best-case time is Θ(1) when the first midpoint matches; worst-case is Θ(log n). Recursive stack frames contribute auxiliary space. Preprocessing to sort can cost Θ(n log n), so number of queries and update frequency affect the choice. **Time:** 8 min. **Transition:** students test assumptions in code.

## Slide 19 — Practical: test boundaries
**Outcome:** C2, C3, K2  
**Visible:** Test empty, singleton, first/last, missing below/between/above, duplicates.  
**Visual:** Checklist beside code editor; no hidden solution shown.  
**Speaker notes:** Ask students to run the provided Python self-check, then add one case. Compile the C++ version if the toolchain is available. Encourage test-first debugging: minimise a failing input, record lo/hi/mid, and locate the invariant violation. Paper trace is the offline fallback. **Time:** 20 min. **Transition:** return to reasoning.

## Slide 20 — Exit ticket
**Outcome:** C3, K2, K3  
**Visible:** 1) Solve one supported recurrence. 2) State binary-search invariant. 3) Name one Master-Theorem limitation.  
**Visual:** Three numbered prompts with space for short responses.  
**Speaker notes:** Give students three minutes to answer individually and the remaining time for a quick synthesis. Look for explicit assumptions and reasoning, not just a final bound. Preview S03: arrays, dynamic arrays, linked lists and amortised costs. **Time:** 7 min.

## Export checklist for the lecturer

1. Create a 16:9 PowerPoint deck using the slide titles and visible content above.
2. Build diagrams from native editable PowerPoint shapes and tables.
3. Add each slide's speaker notes as actual PowerPoint notes, not just in this Markdown file.
4. Check font size, contrast, slide order, equation rendering, and boundary values in all diagrams.
5. Keep instructor solutions out of the public repository.
