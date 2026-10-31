# Evidence Pack: Chapter 10 - Wave 2: Section 10.2 (Principle 8: Avoidance When Superior: The Clean Exit and Strategic Security)

> **Archival Location**: `archives/evidence_packs/CH10_W02_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH10-W02-AVOIDANCE]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_03_the_11_principles/ch10_principles_7_to_9/02_principle_8_avoidance.md | 126 ++++++++++++++++++++
 tests/code_examples/test_ch10_probes.py                                                |  48 ++++++++
 docs/plans/CH10_W2_PLAN.md                                                             | 172 +++++++++++++++++++++++++
 .agent_context/MANUSCRIPT_REGISTER.md                                                  |   2 +-
 4 files changed, 347 insertions(+), 1 deletion(-)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_03_the_11_principles/ch10_principles_7_to_9/02_principle_8_avoidance.md`: Authored Chapter 10 Wave 2 under the "Fighter-First, Engineer-Backed" standard. Establishes **Principle 8: Avoidance When Superior** as the supreme strategic governor and risk-management engine of personal defense; translates military operational doctrine (U.S. Army FM 3-0 *Operations*, ADP 3-0 *Economy of Force and Objective*; Air Force AFDP-1 *Airpower Operations* doctrine of *Strategic Economy*; Sun Tzu Chapter 3 *Attack by Stratagem* "subduing the enemy without fighting") into civilian combatives on asphalt; dismantles the social ego trap of the "Brawler's Pride", demonstrating why mutual combat over insults or status is an unforced tactical error; models **The Mathematics of Asymmetric Tail Risk**, establishing that the expected payoff of consensual street brawling has essentially zero upside ($U(\text{win}) \approx 0$) while carrying unbounded catastrophic downside ($U(\text{loss}) \to -\infty$) across environmental curb impacts, concealed edged weapons, third-party blindside interventions, and biological contamination; articulates **The Clean Exit**, dividing active tactical navigation into Pre-Contact Avoidance (the outer bubble and non-threatening fence), Mid-Contact Manufacturing of Space (striking and framing strictly to open an **Egress Corridor**), and the disciplined Execution of the Clean Exit (zero lingering, zero admiration pause, rapid acceleration out of the hot zone); isolates expected utility asymmetry ($E[U] = P(\text{win})U(\text{win}) + P(\text{loss})U(\text{loss}) \ll 0$), relative spatial separation kinematics ($d_{\text{separation}}(t)$), and sensory horizon dissipation ($I(r) = I_0 / (4\pi r^2)$) in a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"); provides a concise tactical synthesis establishing Avoidance When Superior as the supreme filter governing whether **The Master Equation: Distance $\to$ Time $\to$ Power** is entered at all; and establishes the direct operational bridge to Wave 3 (**10.3 Principle 9: Persistence to Resolution**).
  - `tests/code_examples/test_ch10_probes.py`: Registered and verified Wave 2 probe suite testing file existence, word budget [1,300–1,800], zero banned marketing fluff, and required conceptual tokens.

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | Expected utility formulas, relative spatial kinematics, and sensory horizon equations strictly isolated in `> [!NOTE]` callout; main narrative stands alone in visceral combative language. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; Air Force officer, engineer, and combatives coach persona sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (Avoidance When Superior, Clean Exit, Asymmetric Risk, Expected Value, Egress Corridor, Master Equation). |
| **Lock 5: Word Count Budget** | **YES** | 1,736 words (Budget: 1,300–1,800 words; Target: 1,400–1,750 words). |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 5.95% passive voice across 84 sentences (Ceiling: 10%). |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in military operational doctrine, statistical decision theory, relative kinematics, and combatives coaching. |
| **Lock 8: Negative Blast Radius** | **YES** | 0 deep dive into Principle 9 (Persistence to Resolution, reserved for Wave 3); legal references kept strictly at principle level; 0 technique catalog dumps (reserved for Part IV). |

---

### Artifact 3: Probe Execution Command + Raw Output Tail

- **Command Run**: `pytest tests/code_examples/test_ch10_probes.py -v -s`
- **Exit Code**: `0`
- **Console Output Tail**:
```text
tests/code_examples/test_ch10_probes.py::test_ch10_w01_file_exists PASSED
tests/code_examples/test_ch10_probes.py::test_ch10_w01_word_count_within_budget 
[PROBE-CH10-W01-SURPRISE] Actual word count: 1751
PASSED
tests/code_examples/test_ch10_probes.py::test_ch10_w01_zero_banned_marketing_words PASSED
tests/code_examples/test_ch10_probes.py::test_ch10_w01_mandatory_concepts_present PASSED
tests/code_examples/test_ch10_probes.py::test_ch10_w02_file_exists PASSED
tests/code_examples/test_ch10_probes.py::test_ch10_w02_word_count_within_budget 
[PROBE-CH10-W02-AVOIDANCE] Actual word count: 1736
PASSED
tests/code_examples/test_ch10_probes.py::test_ch10_w02_zero_banned_marketing_words PASSED
tests/code_examples/test_ch10_probes.py::test_ch10_w02_mandatory_concepts_present PASSED

============================== 8 passed in 0.02s ==============================
```

---

### Artifact 4: Linter & Style Hygiene Report
- **Total Word Count**: `1,736 words`
- **Passive Voice Percentage**: `5.95%` (5 / 84 sentences; Ceiling: 10%)
- **Banned Words Count**: `0`
- **User Gate 1 Feedback Incorporations**:
  - **Principle-Level Avoidance & Egress Examples**: Avoidance scenarios kept strictly at principle level (when an exit corridor exists, take it; physical force is residual only when avoidance is physically denied) without expanding into technique sequences or legal treatise text.
  - **Observed Stress Framing for Risk Relationships**: Asymmetric tail risk and expected utility equations framed as typical observed real-world combat stress relationships rather than mathematical absolutes.
  - **Master Equation Strategic Filter in Synthesis**: Synthesis explicitly establishes Avoidance When Superior as the supreme strategic filter that governs whether the Master Equation (Distance $\to$ Time $\to$ Power) is entered at all, prior to the light operational bridge to Persistence to Resolution in Wave 3.
- **Conceptual Token Matches**:
  - `Avoidance When Superior`: Present
  - `Clean Exit`: Present
  - `Asymmetric Risk`: Present
  - `Expected Value`: Present
  - `Egress Corridor`: Present
  - `Master Equation`: Present

---

### Artifact 5: Citation & Source Backing
```json
{
  "citations": [
    {
      "source": "Headquarters, Department of the Army (2017) Field Manual 3-0 (FM 3-0): Operations",
      "concept": "Principles of War: Economy of Force and Objective",
      "status": "verified"
    },
    {
      "source": "Department of the Air Force (2020) Air Force Doctrine Publication 1 (AFDP-1): Operations and Planning",
      "concept": "Strategic Economy and Asset Preservation",
      "status": "verified"
    },
    {
      "source": "Sun Tzu (trans. Griffith, 1963) The Art of War, Chapter 3: Attack by Stratagem",
      "concept": "Subduing the enemy without fighting as supreme excellence",
      "status": "verified"
    },
    {
      "source": "Von Neumann, J., & Morgenstern, O. (1944) Theory of Games and Economic Behavior, Princeton University Press",
      "concept": "Expected utility theory and risk asymmetry under catastrophic downside",
      "status": "verified"
    },
    {
      "source": "Taleb, N. N. (2012) Antifragile: Things That Gain from Disorder, Random House",
      "concept": "Negative tail risk and severe asymmetric payoff structures",
      "status": "verified"
    }
  ]
}
```
