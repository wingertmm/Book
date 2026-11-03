# Master Implementation Plan: Gate 3B — Legal, Liability, and Technical Integrity Package

**Target Milestone**: `Gate 3B: External Legal & Liability Review Flag Package and Technical Inventory`  
**Scope**: High-Risk Self-Defense Sections (Chapters 20 & 21), 52 Callouts, 40 Diagrams, and Cross-Chapter References  
**Baseline Git Tag**: `GATE-3A-CONSISTENCY-AUDIT-FROZEN` (`9973add`)  
**Designated Audit Probe Suite**: `tests/code_examples/test_gate_3b_integrity_probes.py`  
**Status**: `GATE 3B: SUBMITTED FOR REVIEW`  

---

### 1. Goal & Operational Intent

With **Gate 3A** (Whole-Manuscript Consistency Audit) successfully frozen under `GATE-3A-CONSISTENCY-AUDIT-FROZEN`, the manuscript enters **Gate 3B**.

Gate 3B addresses the two highest residual risks before final production formatting:
1. **Legal & Civil Liability Risk**: Chapters 20 and 21 provide definitive tactical instructions on edged-weapon defense, multiple attackers, firearm presentation disarms, lethal force thresholds, 911 dispatch scripts, and post-incident silence. These sections carry significant liability implications for civilian defenders, instructors, and publishers. Gate 3B creates an **External Counsel Review Package** that extracts and annotates all high-risk legal passages with explicit review flags for criminal defense attorneys and use-of-force expert witnesses.
2. **Technical & Diagram Integrity**: Compiles a comprehensive inventory of all 52 formal mechanics callouts and 40 ASCII/structural diagrams across the book, confirming syntactic accuracy, rendering integrity, and cross-chapter reference alignment.

---

### 2. The 3 Core Workstreams of Gate 3B

#### Workstream 1: External Legal & Liability Review Flag Package (Chapters 20 & 21)
Compiles a dedicated review document containing complete excerpts of Chapters 20 and 21 with five prioritized legal flags:
- **Flag 1: Preemptive Physical Defense & The 21-Foot Rule (Section 20.1)**:
  - *Context*: Recommending explosive forward distance collapse or limb interception before a concealed edged weapon is fully unholstered or drawn.
  - *Counsel Question*: Does the text sufficiently protect a defender against criminal assault charges if they misperceive a drawn object, and is the Tueller 21-foot reactionary deficit properly qualified under state self-defense jurisprudence?
- **Flag 2: Lanchester's Square Law & Human Shielding (Section 20.2)**:
  - *Context*: Maneuvering multiple assailants into a single file and using an attacker as a temporary physical obstruction / barrier.
  - *Counsel Question*: Does utilizing an assailant or bystander as a physical barrier create third-party reckless endangerment liability if strikes land on them?
- **Flag 3: Firearm Contact Disarms & Out-of-Battery Clamps (Section 20.3)**:
  - *Context*: Clamping a semi-automatic slide, acknowledging that the chambered round may discharge during the struggle.
  - *Counsel Question*: In the event the chambered round discharges and strikes an unintended third party, what is the civil and criminal liability exposure for the defender?
- **Flag 4: Application of *Graham v. Connor* to Civilians (Section 21.1)**:
  - *Context*: Framing Objective Reasonableness using *Graham v. Connor* (1989), a 4th Amendment standard governing law enforcement officers.
  - *Counsel Question*: Does state statutory self-defense law in non-Stand-Your-Ground or duty-to-retreat jurisdictions impose higher burdens on private citizens than Graham's police standard?
- **Flag 5: The 24-Hour Rule, Scene Exit, and 5th Amendment Silence (Section 21.2)**:
  - *Context*: Advising defenders not to give detailed blow-by-blow statements on scene, to invoke silence, and to delay formal depositions by 24–48 hours.
  - *Counsel Question*: In jurisdictions with strict stop-and-identify or investigative detention statutes, does total silence or requesting a 24-hour delay risk arrest for obstruction of justice or tampering with evidence?

#### Workstream 2: Complete Diagram & Callout Inventory
- **Callout Master Catalog**:
  - Verification of all 52 `> [!NOTE]` callouts ("The Mechanics Behind It"): exactly 1 callout per section across all 21 chapters.
  - Verification that 100% of mathematical equations, integrals, and differential equations remain strictly quarantined within callouts.
- **Diagram & ASCII Schema Catalog**:
  - Verification of all 40 ASCII diagrams, spatial charts, and structural tables across Chapters 1–21.
  - Verification of formatting, line lengths, and mobile/eBook rendering readability.

#### Workstream 3: Cross-Chapter Reference Harmonization
- Systematic audit of all explicit chapter references (e.g., "In Chapter 1, we introduced...", "As proved in Chapter 15...", "Continuing from Chapter 20...").
- Confirming that every forward and backward chapter number, principle number, and section title exactly matches the frozen manuscript.

---

### 3. Automated Gate 3B Probe Suite Specification

A dedicated test module will be registered in `tests/code_examples/test_gate_3b_integrity_probes.py`:

| Probe ID | Verification Scope | Target Invariant |
| :--- | :--- | :--- |
| `test_gate_3b_all_52_callouts_present_and_formatted` | Scans all 52 files for `> [!NOTE]` headers | Exactly 52 callouts; 0 missing |
| `test_gate_3b_diagram_inventory_count_and_syntax` | Counts code blocks with ASCII/diagram formatting | Exactly 40 diagram/table blocks |
| `test_gate_3b_cross_chapter_reference_validity` | Regex scans all "Chapter X" mentions across text | 100% valid chapter references (1–21) |
| `test_gate_3b_legal_flags_coverage_in_ch20_ch21` | Verifies presence of all 5 legal flag topics in text | 100% coverage in Chapters 20–21 |
| `test_gate_3b_counsel_package_document_exists` | Checks `GATE_3B_LEGAL_AND_TECHNICAL_PACKAGE.md` | Document exists and exceeds 3,000 words |

---

### 4. Gate 3B Acceptance Criteria & Freeze Checklist

- [ ] **Acceptance Criterion 1**: The External Legal & Liability Review Package is authored, formatted with clear markers, and stored in `docs/walkthroughs/GATE_3B_LEGAL_AND_TECHNICAL_PACKAGE.md`.
- [ ] **Acceptance Criterion 2**: The Diagram and Callout Inventory is completely cataloged with line references.
- [ ] **Acceptance Criterion 3**: All cross-chapter references are verified with zero broken pointers.
- [ ] **Acceptance Criterion 4**: The automated probe suite (`test_gate_3b_integrity_probes.py`) passes 100% (5/5 GREEN).
- [ ] **Acceptance Criterion 5**: Cumulative test suite passes 100% (240/240 tests GREEN across 23 test suites).
- [ ] **Acceptance Criterion 6**: Gate 3B is formally reviewed and tagged under `GATE-3B-LEGAL-TECHNICAL-FROZEN`.
