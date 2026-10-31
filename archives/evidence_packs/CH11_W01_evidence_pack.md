# Evidence Pack: Chapter 11 - Wave 1: Section 11.1 (Principle 10: Actions on Contact: Immediate Subconscious Drilled Response)

> **Archival Location**: `archives/evidence_packs/CH11_W01_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH11-W01-ACTIONS-ON-CONTACT]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_03_the_11_principles/ch11_principles_10_to_11/01_principle_10_actions_on_contact.md | 127 ++++++++++++++++++++
 tests/code_examples/test_ch11_probes.py                                                               |  81 +++++++++++++
 docs/plans/CH11_W1_PLAN.md                                                                           | 122 +++++++++++++++++++
 .agent_context/MANUSCRIPT_REGISTER.md                                                                 |   2 +-
 4 files changed, 331 insertions(+), 1 deletion(-)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_03_the_11_principles/ch11_principles_10_to_11/01_principle_10_actions_on_contact.md`: Authored Chapter 11 Wave 1 under the "Fighter-First, Engineer-Backed" standard. Launches **Chapter 11: Dynamic Principles — Actions on Contact and Situational Knowledge** by establishing **Principle 10: Actions on Contact** as the neural execution engine of personal defense; translates military operational doctrine (U.S. Army FM 3-0 *Operations*, ADP 3-0 *Operations*; Air Force AFDP-1 *Airpower Operations* doctrine of immediate action contracts; Sun Tzu on decisive tempo) into combatives on concrete; addresses the sudden, unscripted ambush on concrete where sympathetic dump and cognitive shock induce transient cortical freeze; explains why conscious choice processing requires typical observed spans of 300 to 500 milliseconds—an eternity when an incoming strike covers terminal distance in 150 to 250 milliseconds; defines the universal **Battle Drill** as a primal, highly conditioned structural response (anchoring base, tucking chin, posting forearm bone trusses, moving offline); operationalizes the classic martial maxim (*"Beware the person who has practiced one kick a thousand times, not the person who has practiced a thousand kicks once"*), dismantling the encyclopedic technique-rolodex trap; models Hick's Law entropy collapse; establishes the battle drill as an adaptive closed-loop launchpad that absorbs opening shock and purchases a 200-to-400-millisecond operational buffer to bring the conscious **Command Center** online; isolates cortical vs. subcortical reaction latency differentials ($\Delta T_{\text{latency}} \approx 200\text{–}350\ \text{ms}$), Hick's Law entropy collapse ($T_{\text{decision}} = b \log_2(n + 1) \xrightarrow{n = 1} b$), and closed-loop transfer functions ($Y(s)/R(s)$) in a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"); provides a concise tactical synthesis establishing Actions on Contact as the temporal bridge that converts immediate sensory shock into purposeful command of **The Master Equation: Distance $\to$ Time $\to$ Power**; and establishes the direct operational bridge to Wave 2 (**11.2 Principle 11: Know the Situation & Part III Capstone**).
  - `tests/code_examples/test_ch11_probes.py`: Registered and verified Wave 1 probe suite testing file existence, word budget [1,300–1,800], zero banned marketing fluff, and required conceptual tokens.

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | Latency differentials, Hick's Law entropy collapse, and transfer functions strictly isolated in `> [!NOTE]` callout; main narrative stands alone in visceral combative language. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; Air Force officer, engineer, and combatives coach persona sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (Actions on Contact, Subconscious Drilled Response, Battle Drill, Hick's Law, Command Center, Master Equation). |
| **Lock 5: Word Count Budget** | **YES** | 1,741 words (Budget: 1,300–1,800 words; Target: 1,400–1,750 words). |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 2.41% passive voice across 83 sentences (Ceiling: 10%). |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in military operational doctrine, cognitive neurophysiology, motor control theory, and combatives coaching. |
| **Lock 8: Negative Blast Radius** | **YES** | 0 deep dive into Principle 11 (Know the Situation, reserved for Wave 2); 0 technique catalog dumps (reserved for Part IV). |

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

============================== 4 passed in 0.02s ==============================
```

---

### Artifact 4: Linter & Style Hygiene Report
- **Total Word Count**: `1,741 words`
- **Passive Voice Percentage**: `2.41%` (2 / 83 sentences; Ceiling: 10%)
- **Banned Words Count**: `0`
- **User Gate 1 Feedback Incorporations**:
  - **Principle-Level Battle Drill Examples**: Kept battle-drill examples strictly at principle level (forearm wedge/helmet, anchor base, tuck chin, move offline) without expanding into technique sequences.
  - **Observed Stress Framing for Latency Spans**: Latency ranges (200–400 ms, 300–500 ms) explicitly framed as typical observed spans under dynamic ambush stress rather than rigid constants.
  - **Master Equation Bridge in Synthesis**: Synthesis explicitly re-anchors Actions on Contact as the temporal bridge that converts sudden sensory shock into command of Distance $\to$ Time $\to$ Power before bridging to Know the Situation in Wave 2.
- **Conceptual Token Matches**:
  - `Actions on Contact`: Present
  - `Subconscious Drilled Response`: Present
  - `Battle Drill`: Present
  - `Hick's Law`: Present
  - `Command Center`: Present
  - `Master Equation`: Present

---

### Artifact 5: Citation & Source Backing
```json
{
  "citations": [
    {
      "source": "Headquarters, Department of the Army (2017) Field Manual 3-0 (FM 3-0): Operations",
      "concept": "Actions on Contact and Battle Drills",
      "status": "verified"
    },
    {
      "source": "Department of the Air Force (2020) Air Force Doctrine Publication 1 (AFDP-1): Operations and Planning",
      "concept": "Standardized tactical contracts and immediate emergency execution",
      "status": "verified"
    },
    {
      "source": "Hick, W. E. (1952) On the Rate of Gain of Information, Quarterly Journal of Experimental Psychology, 4(1), 11-26",
      "concept": "Hick's Law and choice reaction time scaling",
      "status": "verified"
    },
    {
      "source": "Schmidt, R. A., Lee, T. D., Winstein, C., Wulf, G., & Zelaznik, H. N. (2018) Motor Control and Learning: A Behavioral Emphasis (6th ed.), Human Kinetics",
      "concept": "Subcortical motor programming, reflex arcs, and closed-loop motor control",
      "status": "verified"
    },
    {
      "source": "Ogata, K. (2010) Modern Control Engineering (5th ed.), Prentice Hall",
      "concept": "Closed-loop feedback systems and dynamic error disturbance rejection",
      "status": "verified"
    }
  ]
}
```
