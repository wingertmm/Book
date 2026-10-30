---
description: Standard Operating Procedure for Technical Manuscript Authoring, Master Concept Matrix Synchronization, Code Probe Verification, and Modular Pedagogical Architecture
---

# BOOK_ENHANCED_SOP.md - Enhanced Standard Operating Procedure

**Enforcement Prompt for Antigravity** (Review at start of every session):

> "Strictly follow BOOK_ENHANCED_SOP.md exactly, including Modular Pedagogical Architecture and Dual-Gate Editor review rules. First confirm Chapter Mission and Pedagogical Objectives defined in BOOK_START.md and BOOK_OUTLINE.md, then author the Chapter/Section Plan, designate code/fact verification probes, and output only the approved next wave. Maintain full concept-to-chapter traceability."

---

## Overarching Architectural Rules (Non-Negotiable)

Before writing any chapter, section, or code snippet:

1. **Modular Pedagogical Architecture**:
   - **Domain Layer (Core Concepts)**: Foundational principles, mathematical definitions, and architectural invariants. Zero reliance on ephemeral vendor jargon or ungrounded opinions.
   - **Ports (Interfaces)**: Explicit problem statements, trade-off criteria, and input/output contracts defined *before* narrative explanations.
   - **Adapters (Implementation & Case Studies)**: Executable code examples, production scenario analyses, and benchmark figures. These must be independently executable and falsifiable.
   - **Presentation Layer**: Visual diagrams (Mermaid / ASCII), structured callout boxes, and pedagogical chapter summaries.
2. **Dual-Gate Editor Review**:
   - **Gate 1 (Plan Approval)**: No drafting begins until an explicit, falsifiable section plan is approved.
   - **Gate 2 (Prose Diff & Evidence Acceptance)**: No section is committed to the manuscript without in-line pasted diff and verified code/fact probe evidence.
3. **Reproducibility**: Every code example presented in the text must have a backing automated test file in `tests/code_examples/` that executes with `Exit Code: 0`.

---

## The 8-Phase Token-Optimized Agile Workflow

**CRITICAL TOKEN BOUNDARY RULE**: You MUST NOT attempt to monolithically draft entire chapters at once. Before writing narrative prose (Phase 5), all Conceptual Interfaces and Outline Traceability MUST be established. Context should be flushed between major execution domains (Architecture -> Prose Drafting -> Code Probe Verification).

```
Phase 1: Chapter / Section Concept Formulated
    │
    ▼
Phase 2: Pedagogical Objectives Added to Concept Matrix (CCM)  [BOOK_TECHNICAL_EDITOR]
    │
    ▼
Phase 3: Section Plan Submitted for Editor Review (Gate 1)      [BOOK_ARCHITECT]
    │    🛑 CRITIC GATE 1: PLAN APPROVAL HALT
    ▼
Phase 4: Verification Probes & Fact Checks Registered           [BOOK_FACT_CHECKER]
    │
    ▼
Phase 5: Technical Prose Drafted & Code Examples Implemented   [BOOK_WRITER]
    │
    ▼
Phase 6: Code Probes Tested, Evidence Pack Generated &
         Diff Pasted for Editor Acceptance (Gate 2)             [BOOK_FACT_CHECKER / BOOK_WRITER]
    │    🛑 CRITIC GATE 2: DIFF & EVIDENCE ACCEPTANCE
    ▼
Phase 7: Concept Architecture Updated in Master Guide           [BOOK_TECHNICAL_EDITOR]
    │
    ▼
Phase 8: Manuscript Synchronized & Chapter Freeze Tag Recorded  [BOOK_PROJECT_MANAGER]
```

### Phase 1: Chapter / Section Concept Formulated
1. Handled by the Author/Human or Orchestrator.
2. The core educational objective or technical thesis is formalized.

### Phase 2: Pedagogical Objectives Added to Concept Matrix
1. **Delegated to**: `BOOK_TECHNICAL_EDITOR`
2. Define the learning objective explicitly using `OBJ-CHxx-yyy`.
3. Extract core technical concepts into the Concept-to-Chapter Matrix (CCM).

### Phase 3: Section Plan Submitted for Editor Review (Gate 1)
1. **Delegated to**: `BOOK_ARCHITECT`
2. Confirm the planned section adheres to the Modular Pedagogical Architecture.
3. **Author Formal Plan & Dual-Register Binding**:
   - Save plan at `docs/plans/CH<XX>_W<Y>_PLAN.md` per `templates/CHAPTER_SECTION_PLAN_TEMPLATE.md`.
   - Cite the target chapter in `MANUSCRIPT_REGISTER.md` and outline milestone.
   - Detail Pedagogical Beats (Concept -> Interface -> Code Adapter -> Trade-Offs).
   - Formulate 5–10 Invariant Locks (Terminology stability, code test pass, tone, word budget).
   - Designate Code/Fact Probes (`[PROBE-CHxx-CODEyy]`) and target markdown files.
   - Declare negative boundaries (what this section will NOT cover).
   - Commit plan to git: `git add docs/plans/<PLAN>.md && git commit -m "docs(plan): initial CH<XX> W<Y> plan"`.
4. Output Mermaid `.mmd` conceptual flow diagram.
5. 🛑 **EDITOR GATE 1 (Plan Review & Direction)**:
   - Submit plan and `.mmd` diagram to `/editor`.
   - Reviewed against the **7-Point Gate 1 Plan Rubric**.
   - **EXECUTION HALTS**: No prose drafting may begin until Gate 1 is approved.

### Phase 4: Verification Probes & Fact Checks Registered
1. **Delegated to**: `BOOK_FACT_CHECKER`
2. Pre-register test cases for code snippets in `tests/code_examples/test_ch<xx>_<topic>.py` (or language of choice).
3. Pre-register primary citation claims in the verification matrix.

### Phase 5: Technical Prose Drafted & Code Examples Implemented
1. **Delegated to**: `BOOK_WRITER`
2. **Execute only after Gate 1 Approval**:
   - Write clear, concise prose following the approved beats.
   - Keep code snippets self-contained, typed, and idiomatic.
   - Adhere to the `[Scale Check]`: Keep individual sections under ~500 lines / ~2,500 words.
3. Commit 1: Write test harness asserting expected behavior of the code example (Test Red).
4. Commit 2: Implement code and prose satisfying the test (Test Green).

### Phase 6: Code Probes Tested, Evidence Pack Generated & Diff Pasted for Gate 2
1. **Delegated to**: `BOOK_FACT_CHECKER` / `BOOK_WRITER`
2. Execute code probes: run pytest/runner asserting `Exit Code: 0`.
3. Run style linter: verify zero banned adverbs and passive voice budget < 10%.
4. Publish **Evidence Pack** per `templates/EVIDENCE_PACK_TEMPLATE.md` at `archives/evidence_packs/`.
5. Publish 1/2-page **Walkthrough Cover Letter** per `templates/WALKTHROUGH_TEMPLATE.md`.
6. 🛑 **EDITOR GATE 2 (Diff & Evidence Acceptance - In-Line Diff Primacy)**:
   - **Paste the complete `git diff --stat` and targeted unified diff hunks (`-U3`) directly into the review thread.**
   - The Editor evaluates against the **6-Point Gate 2 Code Diff & Evidence Rubric**.
   - **Acceptance Gate**: Slices without the in-line pasted diff and verified test evidence are rejected immediately.
7. **Freeze Tag & Register Promotion**:
   - Update plan status to `[GATE 2: ACCEPTED]`.
   - Record freeze tag name (e.g., `CH01-SEC02-FROZEN`), tag commit, promote status in `MANUSCRIPT_REGISTER.md`.

### Phase 7: Concept Architecture Updated in Master Guide
1. **Delegated to**: `BOOK_TECHNICAL_EDITOR`
2. Update the master book compendium, glossary, and concept definitions to reflect final verified terminology.

### Phase 8: Manuscript Synchronized & Chapter Exercises Published
1. **Delegated to**: `BOOK_TECHNICAL_EDITOR` / `BOOK_PROJECT_MANAGER`
2. Finalize chapter review questions, exercises, and compile the unified chapter into the manuscript build.

---

## Chapter-to-Wave Decomposition Standard

To prevent cognitive overload, runaway prose drift, and unreviewable monolithic drafts:

1. **Iterative Section Execution**:
   - Chapters are never written in a single massive prompt.
   - Each major section is a discrete **Wave**:
     - **Wave 1 (Foundations & Mental Models)**: Terminology, core principles, problem framing, architectural diagram.
     - **Wave 2 (Patterns & Executable Code)**: Concrete implementation, code walk-throughs, executed test probes.
     - **Wave 3 (Production Trade-Offs, Case Studies & Exercises)**: Failure modes, edge cases, benchmark analysis, review questions.
2. **Autonomous Wave Loop**:
   - Each Wave executes the full 6-step Dual-Gate cycle independently.

---

## Mandatory Diff Presentation Standard

At Editor Gate 2, the authoring agent MUST physically paste the diff directly into the review thread:
1. **Diffstat (`git diff --stat`)**: Verbatim file change overview.
2. **Targeted Unified Diff Hunks (`git diff -U3 <target_files>`)**: Full text of added/modified prose and code.
3. **Probe Execution Evidence**: Exact test command, `Exit Code: 0`, and raw console output tail (last 20 lines).

---

## Two-Stage Reviewer Rubrics

### Rubric 1: Gate 1 Plan Review Rubric (Pre-Drafting)
1. **Educational Goal & Scope**: Is the objective clear, focused, and mapped to a single section/wave?
2. **Wave Sizing**: Is the content broken down so it does not exceed ~2,000 words per wave?
3. **Pedagogical Invariant Locks**: Are 5–10 falsifiable Yes/No constraints explicitly declared (e.g., terminology, code execution, tone)?
4. **Designated Probes**: Are specific code probe IDs (`[PROBE-...]`) and exact verification commands defined?
5. **Blast Radius Bounds**: Are negative boundaries declared ("What this section will NOT cover or alter")?
6. **Diagram Plan**: Is a visual schematic or flowchart planned to anchor complex concepts?
7. **Rollback Strategy**: Is a deterministic git revert command provided?
*Verdict*: **APPROVE** | **DIRECT CORRECTIONS** | **REJECT**.

### Rubric 2: Gate 2 Prose Diff & Evidence Rubric (Post-Drafting)
1. **Diff Hygiene**: Does the pasted diffstat match approved target files with zero drive-by edits to unrelated chapters?
2. **Conceptual Decoupling**: Are foundational concepts explained without circular dependencies on unintroduced material?
3. **Code Verification**: Did all code examples execute cleanly in the test harness with `Exit Code: 0`?
4. **Style & Linguistic Hygiene**: Zero banned adverbs ("seamlessly", "natively", "cleanly"), passive voice under 10%, concrete tone.
5. **Invariant Preservation**: Did all 5–10 declared locks hold?
6. **Source Rigor**: Are all statistics, claims, and quotes cited from authoritative primary sources?
*Verdict*: **ACCEPT** (freeze section & promote) | **FIX** | **REJECT**.
