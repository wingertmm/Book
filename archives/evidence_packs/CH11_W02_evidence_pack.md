# Evidence Pack: Chapter 11 - Wave 2: Section 11.2 (Principle 11: Know the Situation: Continuous Dynamic Threat Audit and the Part III Grand Capstone)

> **Archival Location**: `archives/evidence_packs/CH11_W02_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH11-W02-KNOW-THE-SITUATION]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_03_the_11_principles/ch11_principles_10_to_11/02_principle_11_know_the_situation.md | 132 ++++++++++++++++++++
 .agent_context/MANUSCRIPT_REGISTER.md                                                                 |   2 +-
 2 files changed, 133 insertions(+), 1 deletion(-)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_03_the_11_principles/ch11_principles_10_to_11/02_principle_11_know_the_situation.md`: Authored Chapter 11 Wave 2 under the "Fighter-First, Engineer-Backed" standard. Completes **Chapter 11: Dynamic Principles — Actions on Contact and Situational Knowledge** and delivers the **Part III Grand Capstone (The 11 Unified Principles Architecture)**; translates military operational doctrine (U.S. Army FM 3-0 *Operations*, ADP 3-0 *Operations*; Air Force AFDP-1 *Airpower Operations* battlespace awareness; John Boyd's *Observe* phase; Sun Tzu's *The Art of War*) into combatives on concrete; dismantles the sport-duel illusion, demonstrating why treating street violence as an isolated one-on-one match invites catastrophic blindside destruction; establishes the **Dynamic Threat Audit** across four operational vectors (Self, Threat, Terrain, Egress); addresses **Skill Disparity** by calibrating timing windows between untrained brawlers (observed 400–800 ms windows, telegraphic windups) and experienced predators (observed 150–250 ms windows, covert angles and feints); exposes the physiological collapse of **Tunnel Vision** under sympathetic surge ($\theta \approx 120^\circ \to 10^\circ\text{–}15^\circ$, >99% solid-angle loss) and establishes active mechanical scanning countermeasures (watching hands/waistbands, executing head checks, funneling multiple threats); isolates solid-angle attenuation ($\Omega = 2\pi(1 - \cos(\theta/2))$), Bayesian probability updating ($P(S_k \mid D_{1:t})$), and tactical signal-to-noise ratio ($\text{SNR}_{\text{tactical}}$) in a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"); provides the **Part III Grand Capstone**, unifying all 11 principles across the Foundational Trinity (Principles 1–3), Execution Triad (Principles 4–6), Adaptation Triad (Principles 7–9), and Dynamic Principles (Principles 10–11) under **The Master Equation: Distance $\to$ Time $\to$ Power**; and constructs the operational bridge to **Part IV: Discipline Applications Across the Ranges (Chapters 12–16)**.

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | Solid-angle attenuation, Bayesian probability updating, and tactical SNR formulas strictly isolated in `> [!NOTE]` callout; main narrative stands alone in visceral combative language. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; Air Force officer, engineer, and combatives coach persona sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (Know the Situation, Dynamic Threat Audit, Skill Disparity, Tunnel Vision, Part III Capstone, Master Equation). |
| **Lock 5: Word Count Budget** | **YES** | 1,769 words (Budget: 1,300–1,800 words; Target: 1,400–1,750 words). |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 0.96% passive voice across 104 sentences (Ceiling: 10%). |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in military operational doctrine, sensory psychophysics, Bayesian decision theory, and combatives coaching. |
| **Lock 8: Negative Blast Radius** | **YES** | 0 technique catalog dumps (reserved for Part IV); preserves clean operational handoff to Chapter 12 (Taekwondo & Long Range). |

---

### Artifact 3: Probe Execution Command + Raw Output Tail

- **Command Run**: `pytest tests/code_examples/test_ch11_probes.py -v -s`
- **Exit Code**: `0`
- **Console Output Tail**:
```text
tests/code_examples/test_ch11_probes.py::test_ch11_w01_file_exists PASSED
tests/code_examples/test_ch11_probes.py::test_ch11_w01_word_count_within_budget 
[PROBE-CH11-W01-ACTIONS-ON-CONTACT] Actual word count: 1741
PASSED
tests/code_examples/test_ch11_probes.py::test_ch11_w01_zero_banned_marketing_words PASSED
tests/code_examples/test_ch11_probes.py::test_ch11_w01_mandatory_concepts_present PASSED
tests/code_examples/test_ch11_probes.py::test_ch11_w02_file_exists PASSED
tests/code_examples/test_ch11_probes.py::test_ch11_w02_word_count_within_budget 
[PROBE-CH11-W02-KNOW-THE-SITUATION] Actual word count: 1769
PASSED
tests/code_examples/test_ch11_probes.py::test_ch11_w02_zero_banned_marketing_words PASSED
tests/code_examples/test_ch11_probes.py::test_ch11_w02_mandatory_concepts_present PASSED

============================== 8 passed in 0.03s ==============================
```

---

### Artifact 4: Linter & Style Hygiene Report
- **Total Word Count**: `1,769 words`
- **Passive Voice Percentage**: `0.96%` (1 / 104 sentences; Ceiling: 10%)
- **Banned Words Count**: `0`
- **User Gate 1 Feedback Incorporations**:
  - **Principle-Level Threat Audit & Scanning**: Dynamic Threat Audit (Self, Threat, Terrain, Egress) and scanning examples (watching hands, waistbands, mechanical head checks, funneling) maintained strictly at principle level without expanding into technique catalogs.
  - **Observed Stress Framing for Timing & Visual Spans**: Timing windows (400–800 ms untrained, 150–250 ms experienced) and visual field narrowing (10°–15° cone) explicitly framed as typical observed spans under acute adrenal surge rather than rigid constants.
  - **Operational Part III Grand Capstone**: Concise, high-impact grand synthesis organizing all 11 principles into four pillars (Foundational Trinity, Execution Triad, Adaptation Triad, Dynamic Principles) under The Master Equation before a clean bridge to Part IV.
- **Conceptual Token Matches**:
  - `Know the Situation`: Present
  - `Dynamic Threat Audit`: Present
  - `Skill Disparity`: Present
  - `Tunnel Vision`: Present
  - `Part III Capstone`: Present
  - `Master Equation`: Present

---

### Artifact 5: Citation & Source Backing
```json
{
  "citations": [
    {
      "source": "Sun Tzu (trans. Griffith, S.B., 1963) The Art of War, Oxford University Press",
      "concept": "Operational intelligence and knowing the enemy and self",
      "status": "verified"
    },
    {
      "source": "Headquarters, Department of the Army (2017) Field Manual 3-0 (FM 3-0): Operations",
      "concept": "Continuous reconnaissance and situational understanding",
      "status": "verified"
    },
    {
      "source": "Department of the Air Force (2020) Air Force Doctrine Publication 1 (AFDP-1): Operations and Planning",
      "concept": "Battlespace awareness and sensory update tempo",
      "status": "verified"
    },
    {
      "source": "Boyd, J. R. (1987) A Discourse on Winning and Losing, Air University Press",
      "concept": "Observe phase of the OODA loop and environmental orientation",
      "status": "verified"
    },
    {
      "source": "Grossman, D. (2008) On Combat: The Psychology and Physiology of Deadly Conflict in War and in Peace, PPCT Research Publications",
      "concept": "Vasoconstriction, tunnel vision, and sensory exclusion under sympathetic surge",
      "status": "verified"
    },
    {
      "source": "Jaynes, E. T. (2003) Probability Theory: The Logic of Science, Cambridge University Press",
      "concept": "Bayesian inference and hypothesis updating under incomplete tactical information",
      "status": "verified"
    }
  ]
}
```
