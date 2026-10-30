# Book SOP: Technical Diagram & Schematic Standards

Visual clarity is essential for technical books. Follow these constraints when creating diagrams for chapters.

---

## 1. Primary Diagram Format: Mermaid
- All architectural and sequence diagrams must be authored as fenced GitHub-Flavored Mermaid code blocks:
  ```mermaid
  flowchart LR
    A[Core Domain] -->|Inbound Port| B[Application Service]
    B -->|Outbound Port| C[Persistence Adapter]
  ```
- Diagrams must use clean, uncluttered node hierarchies and clear directional arrows.

## 2. ASCII Fallbacks
- For CLI layouts, terminal traces, or memory layouts, use plain ASCII/Unicode box-drawing characters inside standard code blocks (`text` or `bash`):
  ```text
  +---------------------------------------------+
  |              Presentation Layer             |
  +---------------------------------------------+
                        |
                        v
  +---------------------------------------------+
  |             Application Core                |
  +---------------------------------------------+
  ```

## 3. Storage
Diagram source files must also be stored alongside the chapter under `manuscript/assets/diagrams/ch<XX>/` for publication rendering.
