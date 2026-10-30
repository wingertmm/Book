# Slash Commands & Workflow Cheatsheet

Quick reference for orchestrating authoring sessions, switching personas, and running authoring workflows in `c:\Book`.

## 1. Persona Directives
Invoke these personas to restrict and sharpen LLM behavior during focused authoring tasks:

| Command | Persona File | Primary Function |
| :--- | :--- | :--- |
| `/editor` | `BOOK_EDITOR.md` | **Gatekeeper**: Evaluates Gate 1 Chapter Plans and Gate 2 Prose Diffs against strict rubrics. |
| `/architect` | `BOOK_ARCHITECT.md` | **Narrative & Concept Architect**: Designs chapter outlines, pedagogical frameworks, and Mermaid diagrams. |
| `/writer` | `BOOK_WRITER.md` | **Prose Author**: Drafts concise, rigorous technical sections and case studies based *only* on approved Gate 1 plans. |
| `/researcher` | `BOOK_RESEARCHER.md` | **Research & Citations**: Locates primary sources, validates quotes, and compiles verified citations. |
| `/technical_editor` | `BOOK_TECHNICAL_EDITOR.md` | **Traceability & Glossary**: Manages Concept-to-Chapter Matrix (CCM), Terminology Lexicon, and Index. |
| `/fact_checker` | `BOOK_FACT_CHECKER.md` | **QA & Code Probes**: Executes code snippets, verifies technical claims, checks equations, asserts test pass. |
| `/style_linter` | `BOOK_STYLE_LINTER.md` | **Copy & Voice Linter**: Strips filler adverbs, asserts passive-voice budget, checks readability scores. |
| `/project_manager` | `BOOK_PROJECT_MANAGER.md` | **Cadence & Backlog**: Tracks word count budgets, chapter milestones, and promotes manuscript status. |

---

## 2. Core Operational Workflows

### `/plan_chapter` (Phase 3 -> Gate 1)
- Authors a formal chapter/section plan using `templates/CHAPTER_SECTION_PLAN_TEMPLATE.md`.
- Formulates 5–10 Invariant Locks, designates fact/code verification probes, defines negative boundaries.
- Halts execution until approved by `/editor` at **Gate 1**.

### `/draft_section` (Phase 5)
- Executes strictly after Gate 1 approval.
- Writes focused prose following the approved pedagogical beats (target: 300–800 words per section).
- Proves code snippets pass or technical claims cite verified sources.

### `/review_diff` (Phase 6 -> Gate 2)
- Formulates `git diff --stat` and targeted unified hunks (`git diff -U3`).
- Compiles the **Evidence Pack** and 1/2-page **Walkthrough Cover Letter**.
- Pastes the diff directly into review thread for `/editor` evaluation.

### `/freeze_chapter` (Phase 6 Stage 4)
- Upon Gate 2 acceptance, records the freeze tag (e.g., `CH01-V1-FROZEN`), promotes chapter status in `MANUSCRIPT_REGISTER.md`, and commits to git.

### `/audit_manuscript` (Phase 4 / Phase 7)
- Verifies that every concept defined in `CONCEPT_REGISTER.md` is covered across the outline, draft, and glossary with zero orphaned ideas.
