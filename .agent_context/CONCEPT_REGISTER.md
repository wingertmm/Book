# Concept Register & Terminology Lexicon

Master source of truth for technical terminology, conceptual models, and architectural boundaries in this book.

---

## 1. Core Architectural Concepts
| Term | Formal Definition | Scope / Layer | Invariant Constraint |
| :--- | :--- | :--- | :--- |
| **Triad Architecture** | 3-tier organizational model: Global Governance Engine, Thin Personas, and Decentralized Context. | Architectural Governance | Personas must remain < 80 lines. |
| **Dual-Gate Critic Lifecycle** | Formal 2-step verification loop: Gate 1 approves the Plan before execution; Gate 2 accepts the Diff and Evidence before merging. | Process / Governance | Zero code/prose modifications permitted before Gate 1 approval. |
| **Invariant Lock** | A deterministic, falsifiable constraint evaluated via automated check or exact invariant inspection. | Verification | Must evaluate strictly to Yes/No. |
| **Falsification Probe** | An automated executable test suite or physical harness designed to falsify a technical claim. | Testing / QA | Must output authentic `Exit Code: 0` console tail. |
| **Single Front Door Invariant** | Architectural constraint mandating exactly one user-facing interactive supervisor per system. | Swarm Architecture | Specialists run headlessly; never exposed in UI chat dropdowns. |
| **In-Line Diff Primacy** | The standard requiring verbatim `git diff --stat` and unified hunks pasted directly into the review thread. | Review Process | Diffs are primary; narrative summaries without diffs fail Gate 2. |
| **Modular Pedagogical Architecture** | Modular structuring of knowledge into Domain Core, Abstract Interfaces (Ports), and Concrete Adapters. | Technical Writing | Sections must be severable and independently teachable. |

---

## 2. Acronyms & Abbreviations
- **CCM**: Concept-to-Chapter Matrix
- **MOSA**: Modular Open Systems Approach
- **SOP**: Standard Operating Procedure
- **SRP**: Single Responsibility Principle
- **VCRM**: Verification Cross-Reference Matrix
- **DTE**: Developmental Test & Evaluation
