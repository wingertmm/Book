# Evidence Pack: Chapter 08 - Wave 1: Section 8.1 (Principle 1: Purpose First: The Strategic Compass and Mission Command on Concrete)

> **Archival Location**: `archives/evidence_packs/CH08_W01_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH08-W01-PURPOSE-FIRST]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_03_the_11_principles/ch08_principles_1_to_3/01_principle_1_purpose_first.md | 85 ++++++++++++++++++++
 tests/code_examples/test_ch08_probes.py                                                    | 82 ++++++++++++++++++++
 2 files changed, 167 insertions(+)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_03_the_11_principles/ch08_principles_1_to_3/01_principle_1_purpose_first.md`: Authored Chapter 08 Wave 1 under the "Fighter-First, Engineer-Backed" standard. Launches **Part III: The 11 Unified Principles of Personal Defense** by establishing **Principle 1: Purpose First** as the master operational governor of every physical combat choice; translates military doctrine (U.S. Army FM 3-0 *Operations* Principle of the *Objective*) and Air Force operational doctrine into combatives on concrete; contrasts consensual sporting fights (pre-packaged objectives, rounds, referee) with unscripted violence on pavement; identifies the unconditioned default to ego-driven brawling under adrenaline dumps ($>175\ \text{bpm}$); introduces **Clear Purpose + Flexible Method**, defining the locked end-state (creating safety, securing an exit, protecting a dependent) while treating tactical methods (framing, stepping offline, disrupting structure) as fluid and disposable; exposes the catastrophic operational, physical (multi-attacker exposure, hidden weapons, pavement trauma), and legal costs of secondary ego goals; establishes **The Exit Filter**, requiring every action to create an exit corridor or neutralize an immediate threat and mandating immediate disengagement the instant an exit corridor opens; aligns the Master Triad (**Distance, Time, and Power**) under Purpose First; isolates outcome utility value functions ($V(a) = w_{\text{safety}} U_{\text{safety}}(a) + w_{\text{legal}} U_{\text{legal}}(a) - w_{\text{ego}} C_{\text{regret}}(a)$) and Hick-Hyman information entropy decision tree pruning ($T_{\text{reaction}} = b \log_2(N + 1)$) into a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"); provides a concise tactical synthesis re-anchoring Purpose First as the directional vector for **The Master Equation: Distance $\to$ Time $\to$ Power**; and bridges smoothly to Wave 2 (**8.2 Principle 2: Security of Position: Defending the Anchor Under Pressure**).
  - `tests/code_examples/test_ch08_probes.py`: Registered and verified Wave 1 probe suite testing file existence, word budget [1,300–1,800], zero banned marketing fluff, and required conceptual tokens.

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | Expected utility, regret penalties, Hick-Hyman reaction latency, and decision-tree pruning equations strictly isolated in `> [!NOTE]` callout; main narrative stands alone in visceral combative language. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; Air Force officer, engineer, and combatives coach persona sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (Purpose First, Clear Purpose + Flexible Method, Exit Filter, Primary Objective, Decision Tree Pruning, Master Triad, Master Equation). Preferred framing strictly maintained ("Clear Purpose + Flexible Method" / "locked end-state + adaptive methods"; avoided elevating "commander's intent"). |
| **Lock 5: Word Count Budget** | **YES** | 1,756 words (Budget: 1,300–1,800 words). |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 3.9% passive voice across 77 sentences (Ceiling: 10%). |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in military operational doctrine, decision theory, cognitive psychology, and combatives coaching. |
| **Lock 8: Negative Blast Radius** | **YES** | 0 deep dive into Principle 2 (Security of Position, reserved for Wave 2) or Principle 3 (Maneuver to Advantage, reserved for Wave 3); 0 style technique catalog dumps (reserved for Part IV). |

---

### Artifact 3: Probe Execution Command + Raw Output Tail

- **Command Run**: `pytest tests/code_examples/test_ch08_probes.py -v -s`
- **Exit Code**: `0`
- **Console Output Tail**:
```text
tests/code_examples/test_ch08_probes.py::test_ch08_w01_file_exists PASSED
tests/code_examples/test_ch08_probes.py::test_ch08_w01_word_count_within_budget 
[PROBE-CH08-W01-PURPOSE-FIRST] Actual word count: 1756
PASSED
tests/code_examples/test_ch08_probes.py::test_ch08_w01_zero_banned_marketing_words PASSED
tests/code_examples/test_ch08_probes.py::test_ch08_w01_mandatory_concepts_present PASSED

============================== 4 passed in 0.02s ==============================
```

---

### Artifact 4: Linter & Style Hygiene Report
- **Total Word Count**: `1,756 words`
- **Passive Voice Percentage**: `3.9%` (3 / 77 sentences; Ceiling: 10%)
- **Banned Words Count**: `0`
- **User Gate 1 Feedback Incorporations**:
  - **Preferred Framing Maintained**: Framed throughout as "Clear Purpose + Flexible Method" and "locked end-state + adaptive methods"; completely avoided elevating "commander's intent" as primary terminology.
  - **Principle-Level Exit Filter**: Kept Exit Filter examples strictly principle-level (any action must create an exit corridor or neutralize an immediate threat; disengage the moment exit is viable) without prescribing style-specific sequences.
  - **Re-Anchored Master Equation in Synthesis**: Tactical synthesis explicitly re-anchors Purpose First as the directional vector for The Master Equation ($\text{Distance} \to \text{Time} \to \text{Power}$) before the light bridge to Security of Position in Wave 2.
- **Conceptual Token Matches**:
  - `Purpose First`: Present
  - `Clear Purpose + Flexible Method`: Present
  - `Exit Filter`: Present
  - `Primary Objective`: Present
  - `Decision Tree Pruning`: Present
  - `Master Equation`: Present

---

### Artifact 5: Citation & Source Backing
```json
{
  "citations": [
    {
      "source": "Headquarters, Department of the Army (2017) Field Manual 3-0 (FM 3-0): Operations",
      "concept": "Principles of War: Principle of the Objective",
      "status": "verified"
    },
    {
      "source": "Department of the Air Force (2020) Air Force Doctrine Publication 1 (AFDP-1): Mission Command",
      "concept": "Clear Purpose + Flexible Method: centralized intent with decentralized execution",
      "status": "verified"
    },
    {
      "source": "Sun Tzu (c. 5th century BC) The Art of War",
      "concept": "Calculations and single-minded strategic focus",
      "status": "verified"
    },
    {
      "source": "Hick, W. E. (1952) On the rate of gain of information, Quarterly Journal of Experimental Psychology, 4(1), 11-26",
      "concept": "Hick-Hyman law of choice reaction latency and information entropy",
      "status": "verified"
    },
    {
      "source": "Von Neumann, J. and Morgenstern, O. (1944) Theory of Games and Economic Behavior, Princeton University Press",
      "concept": "Expected utility and objective value functions under uncertainty",
      "status": "verified"
    }
  ]
}
```

---

### Artifact 6: Automated Test Verification
- All 4 Chapter 08 automated probes passing (`4 passed in 0.02s`).
- All 89 repository-wide test probes passing (`89 passed in 0.16s`).
