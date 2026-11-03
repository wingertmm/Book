# Evidence Pack: Chapter 17 - Wave 2: Section 17.2 (Choose, Act & Reassess: Recognition-Primed Decision Making, Actions on Contact, and Closed-Loop Feedback under Pressure) + Chapter 17 Capstone

> **Archival Location**: `archives/evidence_packs/CH17_W02_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH17-W02-CHOOSE-ACT-REASSESS]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_05_the_decision_engine/ch17_the_4_step_cycle/02_choose_act_and_reassess.md | 118 ++++++++++++++++++++
 .agent_context/MANUSCRIPT_REGISTER.md                                                       |   2 +-
 2 files changed, 119 insertions(+), 1 deletion(-)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_05_the_decision_engine/ch17_the_4_step_cycle/02_choose_act_and_reassess.md`: Authored Chapter 17 Wave 2 under the "Fighter-First, Engineer-Backed" standard. Completes **Chapter 17: The 4-Step Cycle — Recognize, Prioritize, Choose, Act & Reassess**; resolves the temporal crisis between thought and impact under acute survival stress; operationalizes **Step 3 (Choose)** through Gary Klein’s **Recognition-Primed Decision** (RPD) model, proving why comparative decision analysis induces catastrophic motor stall and demonstrating how pattern matching to an indexed schema retrieves a satisficing action plan in $< 120\ \text{ms}$; operationalizes **Step 4 (Act)** by adapting military tactical doctrine into **Actions on Contact** (the Default High Frame Wedge and Dynamic Sprawl Frame), absorbing and deflecting incoming impulse ($J = \int F\, dt$), protecting cranial anatomy, and shattering the sensory freeze; operationalizes **Step 4 (Reassess)** through **Closed-Loop Feedback**, rejecting open-loop "fire-and-forget" striking and leveraging high-speed tactile proprioception ($90\text{--}100\ \text{ms}$) over slow visual cortical tracking ($200\text{--}250\ \text{ms}$) to continuously steer structure without halting forward drive; delivers the **Chapter 17 Capstone**, synthesizing the complete 4-Step Cycle ($\text{Recognize} \to \text{Prioritize} \to \text{Choose} \to \text{Act \& Reassess}$) in full dynamic flow; binds the cognitive loop directly to the **Master Equation** ($P = W / \Delta t$ across Distance $\to$ Time $\to$ Power); isolates RPD retrieval latency ($t_{\text{RPD}} = \alpha \log_2 M + \Delta t$), impulse redirection torque ($\vec{\tau} = \vec{r} \times \vec{F}_N$), and closed-loop control system latency in a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"); and constructs the operational bridge to Chapter 18 (*High-Stress Physiology: The Autonomic Cascade, Sensory Distortions, and Motor Degradation*).

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete combat consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | RPD retrieval latency, impulse redirection mechanics, and closed-loop control latency formulas strictly isolated in `> [!NOTE]` callout; main narrative stands alone in visceral combative language. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; veteran combatives coach, military officer, and engineer persona sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (The 4-Step Cycle, Choose, Act & Reassess, Recognition-Primed Decision, Actions on Contact, Closed-Loop Feedback, Master Equation, Chapter 17 Capstone). |
| **Lock 5: Word Count Budget** | **YES** | 1,748 words (Budget: 1,300–1,800 words; Target: 1,400–1,750 words). Chapter 17 total: 3,501 words. |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 2.25% passive voice across 89 sentences (Ceiling: 10%). |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in naturalistic decision making, OODA doctrine, impulse mechanics, control theory, and combatives coaching. |
| **Lock 8: Negative Blast Radius** | **YES** | Zero drift into hormonal endocrine cascades / autonomic failure (quarantined for Chapter 18), weapon disarms (quarantined for Chapter 20), or legal trial doctrine (quarantined for Chapter 21). |

---

### Artifact 3: Probe Execution Command + Raw Output Tail

- **Command Run**: `pytest tests/code_examples/test_ch17_probes.py -k w02 -v -s`
- **Exit Code**: `0`
- **Console Output Tail**:
```text
tests/code_examples/test_ch17_probes.py::test_ch17_w02_file_exists PASSED
tests/code_examples/test_ch17_probes.py::test_ch17_w02_word_count_within_budget 
[PROBE-CH17-W02-CHOOSE-ACT-REASSESS] Actual word count: 1748
PASSED
tests/code_examples/test_ch17_probes.py::test_ch17_w02_zero_banned_marketing_words PASSED
tests/code_examples/test_ch17_probes.py::test_ch17_w02_mandatory_concepts_present PASSED
tests/code_examples/test_ch17_probes.py::test_ch17_w02_passive_voice_under_ceiling 
[PROBE-CH17-W02-CHOOSE-ACT-REASSESS] Passive voice: 2.25% (2/89 sentences)
PASSED

======================= 5 passed, 5 deselected in 0.03s =======================
```

---

### Artifact 4: Negative Boundary & Integrity Confirmation
- No changes made to completed Part I, Part II, Part III, Part IV, or Chapter 17 Wave 1 manuscripts.
- Full regression suite across all chapters passes: 185 passed in 0.32s.
