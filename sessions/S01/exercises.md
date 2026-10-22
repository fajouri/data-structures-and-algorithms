# S01 student exercises — reasoning, implementation and application

These are ungraded practice prompts. Submit no instructor answer key. For every bound, identify `n`, the counted operation, case and cost-model assumptions. Work first on paper, then use the lab to test hypotheses.

## A. Understanding and tracing

### 1. Five cost classifications

For each snippet, let `A` be a sequence of length `n`. Assume indexing, integer arithmetic and a single equality comparison take constant time; say how your answer would change if element equality cost depended on element length. Give a tight asymptotic time bound and auxiliary-space bound where possible. If an average case is requested, first specify a distribution rather than inventing one.

**(a) Prefix check**

```text
if n == 0: return false
return A[0] == x
```

**(b) Full count**

```text
count = 0
for i from 0 to n - 1:
    if A[i] == x: count += 1
return count
```

**(c) Pair check**

```text
for i from 0 to n - 1:
    for j from i + 1 to n - 1:
        if A[i] == A[j]: return true
return false
```

**(d) Two separate scans**

```text
for i from 0 to n - 1: inspect(A[i])
for i from 0 to n - 1: inspect(A[i])
```

Assume `inspect` has constant cost and no early return.

**(e) Repeated halving**

```text
k = n
while k > 1:
    k = floor(k / 2)
```

Include `n = 0`, `n = 1`, a duplicate-rich input for (c), and an input with no duplicates. For (c), report an exact comparison count for a no-duplicate input of size 5 before simplifying its growth rate. Explain why a bound on worst-case cost need not describe every individual run.

### 2. Trace a first-index search

Trace the `LINEAR-SEARCH` pseudocode in `lecture.md` for these inputs: `([], 4)`, `([4], 4)`, `([4], 9)`, `([9, 4, 4, 1], 4)` and `([9, 4, 4, 1], 7)`. For each, record the indices tested, result and number of equality checks. Then state an invariant at the start of each iteration and explain initialization, maintenance, termination and the meaning of each return path. Explain why merely finding a match does not yet establish the *first-index* postcondition.

## B. Implementation

### 3. Last matching index

Implement `last_index(A, x)` in Python and, if you have a C++ toolchain, in C++17. The input is an unsorted sequence, possibly empty or containing duplicates. Return the largest matching index, or `-1` if absent. Do not call a built-in search or reverse the input. Show tests for empty, singleton, repeated target, target at the last position and missing target. Give a loop invariant and a termination argument. State best and worst comparison counts for your chosen traversal direction and its auxiliary-space cost. The supplied labs demonstrate a *first-index* search; they do not implement this task.

### 4. Duplicate experiment

Use the supplied pairwise duplicate checker as a baseline. Construct three deterministic size-`n` input families: all distinct, a duplicate in the first compared pair, and a duplicate first found late in the pair order. For `n` in `{8, 16, 32, 64}`, predict comparison counts before running code. Measure or instrument the baseline, then explain any discrepancy between counts and elapsed times. You may add instrumentation locally. Do not infer an average case from these three chosen families.

## C. Application and choice

### 5. Membership service

A small catalogue is loaded once and queried repeatedly. Consider (i) one query over 30 unsorted items, (ii) one million queries over 30 fixed items, and (iii) a catalogue that changes after every query. You may use a sequential scan, a prebuilt sorted representation, or a hash-based set. For each scenario, identify the ADT contract, relevant operations, construction/update costs, memory assumptions and a plausible choice. Describe what additional measurements or workload information would change your choice. Do not claim a universal constant-time hash lookup.

### 6. Bound or observation?

A student reports that doubling `n` changed one Python run from 0.04 ms to 0.06 ms and concludes the algorithm is `Θ(n)`. Identify what the observation establishes, what it does not establish, and a more useful repeated-run protocol. State how you would document runtime version, machine, input construction, timer, warm-up and summary statistic. No new measurements are required for this written prompt.

## D. Optional challenge

Specify a duplicate detector that uses additional memory. State the required hash/equality assumptions, what happens when many keys collide, whether the input is modified, and best/expected/worst time and auxiliary-space costs under clearly separated models. Compare its contract and practical trade-offs with the pairwise checker. Implement it only after writing the specification; do not treat passing tests as a proof.

## Reflection

In two or three sentences, distinguish an ADT from one representation of it and distinguish an asymptotic bound from an elapsed-time measurement. Bring one unresolved question to S02, where recurrences are introduced.
