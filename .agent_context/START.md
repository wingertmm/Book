# Project Authoring Primer: .agent_context\START.md

Welcome to the **Book Authoring Workspace**. This directory holds the active, mutable state of the book.

---

## 1. Quick Navigation
- **[BOOK_OUTLINE.md](file:///c:/Book/.agent_context/BOOK_OUTLINE.md)**: Master syllabus, parts, chapters, and section targets.
- **[CONCEPT_REGISTER.md](file:///c:/Book/.agent_context/CONCEPT_REGISTER.md)**: Authoritative register of technical terms, models, and acronyms.
- **[MANUSCRIPT_REGISTER.md](file:///c:/Book/.agent_context/MANUSCRIPT_REGISTER.md)**: Real-time status register for all parts, chapters, and sections.
- **[STYLE_GUIDE.md](file:///c:/Book/.agent_context/STYLE_GUIDE.md)**: Tone, typography, code block conventions, and voice rules.
- **[CITATIONS.md](file:///c:/Book/.agent_context/CITATIONS.md)**: Verified primary sources and bibliography.
- **[GLOSSARY.md](file:///c:/Book/.agent_context/GLOSSARY.md)**: Final alphabetical index and definitions.

---

## 2. Session Protocol
1. Check `MANUSCRIPT_REGISTER.md` to see what section is currently in progress or next up.
2. Read the corresponding learning objectives in `BOOK_OUTLINE.md`.
3. Invoke `/architect` to formulate the Gate 1 Section Plan in `docs/plans/`.
4. Submit to `/editor` for Gate 1 approval.
5. Invoke `/writer` to draft prose, and `/fact_checker` to verify code examples with `Exit Code: 0`.
6. Invoke `/editor` at Gate 2 with in-line diff and evidence pack.
7. Freeze section and promote in `MANUSCRIPT_REGISTER.md`.
