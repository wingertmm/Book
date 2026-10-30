# BOOK_AGENT.md - Global Master Framework for Technical Book Authoring

This file provides persistent, cross-session instructions for any agentic authoring tool executing technical, non-fiction, or architectural book manuscripts. All outputs MUST follow these rules and the target Modular Pedagogical Architecture.

---

## 1. Core Architectural Mandate: Modular Pedagogical Architecture
- **Target Structure**: Modular, Severable, Concept-Bound Sections.
- **Core Principle**: Each chapter and section must be highly cohesive, loosely coupled, and pedagogically severable. A reader should be able to grasp a concrete mental model or implement a solution from a section without requiring circular dependencies across the book.
- **Layers (Analogous to Hexagonal Ports & Adapters)**:
  - **Core Concept Domain (Domain Layer)**: Pure foundational principles, mathematical invariants, domain definitions, and mental models. Zero dependencies on vendor-specific tooling or ephemeral library APIs.
  - **Conceptual Interfaces (Ports)**: Explicit statements of problem-solution contracts, inputs/outputs of architectural patterns, and structured evaluation criteria defined **before** descriptive text or examples.
  - **Concrete Adapters (Infrastructure & Presentation)**: Concrete case studies, real-world code snippets, platform implementations, and scenario walkthroughs. These depend strictly on the Core Concept Domain, never the reverse.
  - **Visual & Pedagogical Framing (Presentation)**: Diagrams (Mermaid, ASCII), callout blocks (`> [!NOTE]`, `> [!IMPORTANT]`), and chapter summaries.

---

## 2. Project Context & Routing
- The `.agent/` directory is strictly for global framework rules.
- **CRITICAL**: Before executing any drafting or editing work, you must identify your active volume or chapter folder and read `c:\Book\.agent_context\START.md`. All working outlines, concept registers, style guides, and manuscript registers live in `.agent_context\`.

---

## 3. Workflow & Verification: The Dual-Gate Critic Lifecycle
- Follow `BOOK_ENHANCED_SOP.md` exactly for execution phases and the **Dual-Gate Falsifiable Slice Lifecycle**.
- **Non-Negotiable Policy**: Zero prose or code modifications may occur without prior Editor plan approval (**Gate 1**). Zero prose or code modifications may be committed or merged into the manuscript without subsequent Editor diff & evidence acceptance (**Gate 2**).
- **Iterative Execution & Wave Decomposition**:
  - Every chapter is executed iteratively through discrete sections or "waves".
  - Large or multi-faceted chapters MUST be decomposed into discrete, falsifiable **Waves** (e.g., Wave 1: Core Definitions & Mental Model, Wave 2: Architectural Patterns & Code Implementation, Wave 3: Case Study & Chapter Exercises).
  - Each Wave executes the full 6-step Dual-Gate Critic cycle independently.

### The 6-Step Dual-Gate Evidence Loop
1. **Plan Formulation & Automated Git Upload**: Author section plan per [templates/CHAPTER_SECTION_PLAN_TEMPLATE.md](file:///c:/Book/.agent/BOOK_AGENT/templates/CHAPTER_SECTION_PLAN_TEMPLATE.md) at `docs/plans/<CHAPTER>_<WAVE>_PLAN.md`. Detail Objective, Pedagogical Beats, 5–10 Invariant Locks, designated Fact/Code Probes, target files, negative blast radius bounds, and rollback commands. **Immediately commit this plan to git** (`git add docs/plans/<PLAN>.md && git commit -m "docs(plan): initial <CHAPTER> <WAVE> plan"`).
2. **Editor Gate 1 (Plan Review & Direction)**: Submit the plan for Editor Review. The Editor evaluates against the *Gate 1 Plan Review Rubric*. Work halts until the plan is approved, corrected, or directed. **NO PROSE DRAFTING PERMITTED BEFORE GATE 1 APPROVAL.**
3. **Drafting & Probe Execution**:
   - Draft conceptual interfaces and core principles first, followed by concrete case studies and code adapters.
   - Execute designated verification probes: run all code snippets in an isolated test harness (`exit code 0`), verify primary citations, run style and readability linters.
   - Confirm negative blast radius (no unrelated chapters touched, no retroactive canon drift).
4. **Diff & Evidence Pack Compilation**:
   - Capture exact `git diff --stat` and targeted unified prose/code diff hunks (`--unified=3`) on modified markdown files per [templates/EVIDENCE_PACK_TEMPLATE.md](file:///c:/Book/.agent/BOOK_AGENT/templates/EVIDENCE_PACK_TEMPLATE.md).
   - Include raw probe console tails (compiler output, linter stats) and citation verification logs.
   - Draft the 1/2-page Walkthrough Cover Letter per [templates/WALKTHROUGH_TEMPLATE.md](file:///c:/Book/.agent/BOOK_AGENT/templates/WALKTHROUGH_TEMPLATE.md).
5. **Editor Gate 2 (In-Line Pasted Diff & Evidence Acceptance)**:
   - **Mandatory In-Line Diff Primacy**: Paste the incremental diffstat and unified hunks directly into the review thread alongside the Walkthrough Cover Letter. The pasted diff is the primary evaluation surface.
   - The Editor evaluates against the *Gate 2 Code Diff & Evidence Rubric* (Pedagogical clarity, terminology consistency, Invariant preservation, code probe passing, zero collateral bleed).
   - Acceptance promotes the section/wave; rejection triggers directed remediation or rollback.
6. **Freeze Tag, Plan Finalization & Register Promotion**:
   - Update the plan status to `COMPLETED` and commit to git.
   - Formalize freeze tag name (e.g., `CH02-W1-CONCEPTS-FROZEN`) and update section status from `Open` to `Done` in `MANUSCRIPT_REGISTER.md`.

---

## 4. Scale Check (Section Sizing Standard)
- Individual markdown files for sections should remain under **~300 to 500 lines** (or ~1,500–2,500 words) for cognitive clarity and Single Responsibility Principle (SRP).
- Print a `[Scale Check]` thought block before expanding a file beyond 500 lines to assess if it should be split into a subsequent subsection.

---

## 5. Banned Anti-Patterns (Zero-Tolerance)
- ❌ **Filler Adverb & Buzzword Chains**: Never use filler adverbs ("seamlessly", "natively", "cleanly", "robustly", "drastically", "obviously").
- ❌ **Unverified Code Mocks**: Never publish code snippets in the manuscript that have not been physically executed through a test harness.
- ❌ **Recycled Synopsis Filler**: Never restate the entire history of previous chapters as filler intro paragraphs.
- ❌ **Monolithic Unreviewed Dumps**: Never dump an entire 10,000-word chapter at once without pre-approved section plans.
- ❌ **Ungrounded Claims**: Every technical assertion, metric, or benchmark must cite a primary source, standard (ISO/IEEE/RFC), or reproducible test harness.

---

## 6. Authoring Personas
Load specific personas from `C:\Book\.agent\BOOK_AGENT\` as needed:
- `BOOK_EDITOR.md`: Gate 1 Plan approval and Gate 2 Diff acceptance.
- `BOOK_ARCHITECT.md`: High-level table of contents, pedagogical progression, and Mermaid architecture diagrams.
- `BOOK_WRITER.md`: High-clarity technical exposition, case studies, and practical implementations.
- `BOOK_RESEARCHER.md`: Primary source validation, citation indexing, and academic cross-references.
- `BOOK_TECHNICAL_EDITOR.md`: Concept-to-Chapter Matrix (CCM), Terminology Lexicon, and Glossary maintenance.
- `BOOK_FACT_CHECKER.md`: Technical fact-checking, code example probe validation, and mathematical sanity checks.
- `BOOK_STYLE_LINTER.md`: Passive voice budget, rhythm analysis, and anti-pattern linting.
- `BOOK_PROJECT_MANAGER.md`: Word count burndown, sprint cadence, and manuscript register tracking.
