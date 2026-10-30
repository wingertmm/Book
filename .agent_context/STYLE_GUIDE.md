# Manuscript Style & Voice Guide

Authoritative rules for voice, tone, formatting, and code snippets across all manuscript chapters.

---

## 1. Authorial Voice & Tone
- **Authoritative & Stoic**: State facts and engineering trade-offs directly. Avoid conversational banter, self-referential jokes, or meta-commentary ("In this book, we will explore...").
- **Active & Direct**: Use active voice. Keep passive voice under 10% across all expository sections.
- **Show, Don't Tell**: Back every architectural virtue with an executable probe or explicit failure trace.

---

## 2. Banned Words & Anti-Patterns
The following marketing filler and vague qualifiers are strictly prohibited:
- ❌ "natively"
- ❌ "seamlessly"
- ❌ "cleanly"
- ❌ "robustly"
- ❌ "simply" / "just"
- ❌ "obviously"
- ❌ "drastically" / "massively"
- ❌ "game-changing" / "revolutionary"

---

## 3. Typography & Formatting
- **Key Terms**: Bold on first introduction (`**Triad Architecture**`).
- **Code & Identifiers**: Use backticks (`MonoSpace`) for classes, functions, file names, CLI commands, and directory paths.
- **Alert Callouts**:
  - `> [!NOTE]`: Historical context or implementation nuances.
  - `> [!IMPORTANT]`: Critical architectural constraints or mandatory invariants.
  - `> [!CAUTION]`: High-risk anti-patterns or failure modes.

---

## 4. Code Snippet Standards
- **Language Tags**: Always provide explicit language tags (`python`, `typescript`, `bash`, `mermaid`).
- **Self-Contained & Typed**: All Python code must include type annotations (`typing`). All TypeScript code must be strict-mode compliant.
- **Executable Backing**: Every code block displayed to the reader must correspond to a passing test in `tests/code_examples/`.
