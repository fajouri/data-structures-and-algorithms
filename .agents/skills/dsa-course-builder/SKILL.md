---
name: dsa-course-builder
description: Build, revise, or validate one university Data Structures and Algorithms (DSA) teaching session, including lecture notes, editable slides, exercises, practical code, and course status. Use for S01–S20 only after the official Module Descriptor has been reviewed and the lecturer has approved course-plan.md; do not use to invent requirements or publish materials automatically.
---

# DSA course builder

## Before creating anything

1. Inspect the repository and read the **official Module Descriptor** (normally `module-descriptor/original-descriptor.pdf`), `course-plan.md`, `COURSE_STATUS.md`, and any existing files for the requested session.
2. Treat the descriptor as the authority for academic requirements; the **lecturer-approved** course plan determines session coverage and order. Respect already approved session materials. If they conflict, report the conflict; do not silently resolve it.
3. **Gate:** do not generate a session unless the descriptor has been analysed and the course plan has explicit lecturer approval (recorded in the plan or unmistakably supplied by the lecturer). File existence or a draft plan is not approval. If the gate is unmet, perform only analysis, planning, or skill/validator maintenance and state the blocker.
4. Preserve all official learning outcomes, contact hours, languages, assessment methods and weights. Do not silently change the four assignment milestones or exam rules described in the descriptor.

## Build or revise one session at a time

Use `sessions/SXX/` and the matching approved session entry in `course-plan.md`. Write student-facing materials in clear academic English.

- `README.md`: objectives/outcome mapping, prerequisites, tools, **timed 3-hour agenda where the approved plan specifies 3 hours**, teaching activities, preparation and links.
- `lecture.md`: substantial explanations; definitions, motivation, real-world analogy and example, pseudocode, step-by-step traces, correctness argument, best/average/worst time and space costs **with assumptions**, trade-offs, edge cases, misconceptions and references. Distinguish ADTs from implementations.
- `exercises.md`: scaffolded understanding → implementation → application → optional challenge; specify inputs, outputs, constraints, examples, edge cases and reasoning requested. Never include instructor answers.
- Practical source or notebook **when appropriate**: use the course's approved Python/C++ approach; include executable examples, tests or self-checks, and commands to run them. For Python notebooks, prefer a portable `.ipynb` compatible with Colab. Never claim code was run unless it was.
- `slides.md`: editable slide-by-slide authoring source, with slide title, key visible content, technical visual/pseudocode specification, and **substantial speaker notes** for each slide (explanation, worked example, pitfalls, questions, timing, transition). Create `slides.pptx` with editable native shapes/text and actual PowerPoint notes if supported; otherwise retain `slides.md` with explicit PowerPoint handoff steps and note that PPTX is pending. Do not substitute an image of slides for an editable deck.

Use the detailed quality guidance only when preparing/reviewing materials: [Teaching and quality checks](references/teaching-standards.md). Build active learning into the agenda; do not make three hours of bullet slides. Keep instructor solutions **out of the public student repository**; deliver them separately through a private lecturer-controlled channel when requested.

## Verify and update

1. Cross-check each concept against the descriptor, approved plan and learning outcomes. Verify algorithm invariants, termination, pseudocode, complexity bounds and assumptions; compare traces/edge cases with implementations. Do not infer proofs from passing tests.
2. Run the local validator from the repository root:
   `python .agents/skills/dsa-course-builder/scripts/validate_session.py --session S01`
   Use `--execute` only in a trusted environment to run available examples/tests/notebooks. Report what passed, failed or was **not run**; fix findings rather than declaring success prematurely.
3. Update **only** `COURSE_STATUS.md` with actual progress, using `NOT STARTED`, `DRAFT`, `REVIEW`, `APPROVED`. Never mark lecturer approval yourself.
4. Show the lecturer the deliverables, coverage and unresolved decisions. **No commit, push, publication or overwrite of approved academic content without explicit authorisation.** When authorised, commit to the repository's single existing default branch only; no branches, PRs, Issues, board, hashes, additional status systems or multi-agent orchestration.
