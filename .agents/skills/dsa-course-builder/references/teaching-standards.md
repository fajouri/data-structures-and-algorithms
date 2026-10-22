# DSA teaching and quality checks

Read when planning, building, or reviewing a session, not for repository administration.

## Source fidelity

- Map each session objective to the exact relevant official learning outcome(s). The Module Descriptor governs requirements; an approved `course-plan.md` allocates them to sessions.
- Keep approved assessment scope unchanged. Explicitly link exercises to the planned knowledge/skills but do not turn practice into unapproved graded work.
- Use accessible postgraduate English; define terms before using them. Attribute textbook/reference material and write original figures and examples.

## Academic correctness

- State ADT contract, concrete representation, supported operations and invariants separately.
- Provide an executable or hand-checkable trace with initial state, intermediate states, final result, and edge cases (empty, singleton, duplicates, missing keys, disconnected graphs, negative weights, etc., as relevant).
- Describe preconditions and correctness by invariant, induction or appropriate argument; specify termination and failure cases.
- Give time and auxiliary-space bounds with explicit model and assumptions: input sizes, average-case assumptions, recursion stack, amortised vs worst-case, hashing/collision assumptions, and comparisons vs allocations/cache effects where relevant.
- Avoid unsupported benchmarks or performance claims. If empirical results are included, document hardware/versions, input generation, seeds, repeats, measurement method and limitations.

## Three-hour live teaching design

- Assign realistic minutes to explanation, visual trace, prediction/poll, live code, paired exercise, recap and questions. Allow room for debugging and different student starting levels.
- For every new algorithm: motivating problem → small trace/diagram → pseudocode → correctness idea → complexity → implementation/testing → choice/trade-off question.
- Show purposeful editable diagrams: arrays/index positions, nodes/links, recursion trees/stacks, tree rotations, sorting stages, DP tables and graph traversal as relevant. Validate every intermediate state.
- Include a brief low-tech fallback for a failed internet connection or demonstration.

## Slide source and speaker notes

Keep `slides.md` even when a PowerPoint exists. For each slide, record:

```text
## Slide 07 — Descriptive title
Outcome: <official outcome reference>
Visible: concise visual or pseudocode plus one takeaway
Visual: editable native shapes/steps/labels and expected state
Speaker notes: concept explanation; worked example; misconception;
  one student question; time estimate; transition
```

Use 16:9 and readable projection typography. One conceptual step per slide; diagrams, progressive worked examples and practice prompts are preferred to walls of text. Ensure `slides.pptx` has actual editable elements and non-empty native speaker notes (not only speaker notes in Markdown). If slide generation is unavailable, document exact creation instructions and speaker notes in `slides.md`; do not claim the `.pptx` exists.

## Student/instructor separation

Student packages contain prompts, starter code, self-checks and expected *behaviour*, not hidden solutions. Keep full solutions and answer keys in a separate private location (outside a public repository), and never accidentally commit them. Before delivering, check that notebook outputs do not disclose solutions.
