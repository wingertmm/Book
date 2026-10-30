# Book SOP: Git Branching & Freeze Tag Workflow

All changes to the book manuscript, code examples, and architectural plans must follow strict version control hygiene.

---

## 1. Branching Strategy
- `main`: Authoritative master manuscript. Direct pushes to `main` are strictly prohibited.
- `dev`: Active integration branch for complete, accepted chapters.
- `chapter/ch<XX>-<topic>`: Feature branch for drafting and testing a specific chapter.

## 2. Commit Standards
Use semantic commit prefixes:
- `docs(plan)`: Authoring or updating a Gate 1 section plan.
- `docs(draft)`: Adding initial raw prose following an approved plan.
- `feat(code)`: Adding or updating executable code examples in `tests/code_examples/`.
- `test(probe)`: Adding verification probes for code or facts.
- `docs(freeze)`: Freezing an accepted section/chapter after Gate 2 approval.

## 3. Freeze Tag Discipline
Upon Gate 2 acceptance, the commit MUST be formally tagged:
- Format: `v<Major>.<Chapter>.<Wave>` or `CH<XX>-SEC<YY>-FROZEN`
- *Example*: `git tag -a CH02-SEC01-FROZEN -m "freeze: Chapter 2 Section 1 Domain Ports accepted at Gate 2"`
