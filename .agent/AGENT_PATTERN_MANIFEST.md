# Book Triad Architecture Manifest

This manifest documents the architectural standard for AI Agents governing the creation of this technical/non-fiction book.

## The Triad Architecture
To prevent LLM context-window exhaustion, cognitive dilution, hallucinated drift, and style inconsistencies, this workspace strictly enforces a 3-tier architecture for all authoring agent deployments:

### 1. Global Governance Engine
- **Location**: `C:\Book\.agent\BOOK_AGENT\BOOK_AGENT.md`
- **Role**: The absolute universal law. It dictates structural writing rules (e.g., modular concept encapsulation, section word limits, technical clarity, banned marketing fluff, and citation rigor) for *all* agents to prevent duplicating these rules across individual sessions or personas.

### 2. Thin Personas
- **Location**: `C:\Book\.agent\BOOK_AGENT\` (e.g., `BOOK_EDITOR.md`, `BOOK_ARCHITECT.md`, `BOOK_WRITER.md`)
- **Role**: Agents are not parallel brains; they are narrow specializations (Personas) that hook into the Master Governance Engine. They are strictly focused under ~80 lines on specific execution domains (e.g., structural outlining, technical prose authoring, citation verification, or code snippet validation).

### 3. Decentralized Context
- **Location**: `C:\Book\.agent_context\START.md`
- **Role**: Never pollute global framework rules with manuscript-specific drafts, working outlines, or subject-matter research. The AI must always route to `.agent_context\` to locate the active `BOOK_OUTLINE.md`, `CONCEPT_REGISTER.md`, `STYLE_GUIDE.md`, and `MANUSCRIPT_REGISTER.md`.

## How to Add a New Authoring Persona
Run or duplicate `C:\Book\.agent\BOOK_AGENT\templates\persona_template.md` into `BOOK_AGENT\`. Ensure it never re-defines global governance or bypasses the Dual-Gate Critic review process.

## Workflow & Governance
All AI Agents must strictly adhere to the Standard Operating Procedures (SOPs) located in `.agent\book_sops\`.
- **Git Branching Strategy**: Agents MUST read and comply with `SOP_Git_Workflow.md`. Direct modification of the `main` branch is strictly prohibited. All drafting and editing occur on feature/chapter branches.
- **Single Authorial Front Door**: One primary orchestrator persona interfaces with the author/user; specialized sub-agents (researcher, style linter, fact-checker) run headlessly or on demand.
