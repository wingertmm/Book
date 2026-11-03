# Evidence Pack: Chapter 18 - Wave 1: Section 18.1 (The Autonomic Cascade and Sensory Distortions under Threat: Sympathetic Arousal, Tunnel Vision, Auditory Exclusion, and Tachypsychia)

> **Archival Location**: `archives/evidence_packs/CH18_W01_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH18-W01-AUTONOMIC-CASCADE]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_05_the_decision_engine/ch18_high_stress_physiology/01_the_autonomic_cascade_and_sensory_distortions.md | 124 ++++++++++++++++++++
 .agent_context/MANUSCRIPT_REGISTER.md                                                                                   |   2 +-
 2 files changed, 125 insertions(+), 1 deletion(-)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_05_the_decision_engine/ch18_high_stress_physiology/01_the_autonomic_cascade_and_sensory_distortions.md`: Authored Chapter 18 Wave 1 under the "Fighter-First, Engineer-Backed" standard. Opens **Chapter 18: High-Stress Physiology — The Biological Cost of Combat**; establishes the biological hardware reality upon which the cognitive decision engine runs; details the **Sympathetic Surge** triggered by the sympathoadrenal axis, flooding the vascular system with epinephrine, norepinephrine, and cortisol, causing immediate peripheral vasoconstriction and shunting blood to major muscle groups; models **Heart Rate Performance Zones** (Siddle's framework: Baseline $60\text{--}80\ \text{BPM}$, Zone 1 $115\text{--}145\ \text{BPM}$ optimal combative zone, Zone 2 $145\text{--}175\ \text{BPM}$ motor degradation threshold, Zone 3 $> 175\ \text{BPM}$ prefrontal hypofrontality and cognitive collapse); analyzes **Sensory Distortions under Threat**, detailing **Tunnel Vision** (ciliary muscle spasm and vasoconstriction collapsing visual fields to a $5^\circ\text{--}10^\circ$ focal cone), **Auditory Exclusion** (acoustic suppression via the reticular activating system filtering speech and sirens), and **Tachypsychia** (subjective temporal dilation caused by high-frequency amygdala memory encoding vs. objective clock time); establishes physical, non-visual countermeasures (mechanical head sweeps across the $180^\circ$ forward arc, proprioceptive and tactile indexing over visual confirmation, and gross skeletal frame reliance); isolates physiological mathematical models (Siddle-Yerkes-Dodson arousal function $P(HR)$, visual field attenuation $\theta_{\text{FOV}}$, and tachypsychic time dilation ratio $\Delta t_{\text{perceived}} / \Delta t_{\text{clock}}$) in a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"); anchors physiological response to the Master Equation ($P = W / \Delta t$ across Distance $\to$ Time $\to$ Power); and constructs the operational bridge to Wave 2 (Section 18.2: Motor Skill Degradation, the "Plan A" Trap, Autonomic Recovery / Tactical Breathing, and Chapter 18 Capstone).

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete combat consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | Siddle-Yerkes-Dodson arousal curves, visual field attenuation angle, and tachypsychia dilation ratios strictly isolated in `> [!NOTE]` callout; main narrative stands alone in visceral combative language. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; veteran combatives coach, military officer, and engineer persona sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (Autonomic Cascade, Sympathetic Surge, Heart Rate Performance Zones, Tunnel Vision, Auditory Exclusion, Tachypsychia, Master Equation). |
| **Lock 5: Word Count Budget** | **YES** | 1,700 words (Budget: 1,300–1,800 words; Target: 1,400–1,750 words). |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 1.92% passive voice across 104 sentences (Ceiling: 10%). |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in human stress physiology, Siddle's combative arousal models, neurobiology, and real-world high-threat engagement tactics. |
| **Lock 8: Negative Blast Radius** | **YES** | Zero drift into motor skill classification (fine/complex/gross motor breakdown quarantined for Wave 2), "Plan A" fixations (quarantined for Wave 2), somatic reset / box breathing protocols (quarantined for Wave 2), weapon disarms (quarantined for Chapter 20), or legal trial doctrine (quarantined for Chapter 21). |

---

### Artifact 3: Probe Execution Command + Raw Output Tail

- **Command Run**: `pytest tests/code_examples/test_ch18_probes.py -k w01 -v -s`
- **Exit Code**: `0`
- **Console Output Tail**:
```text
tests/code_examples/test_ch18_probes.py::test_ch18_w01_file_exists PASSED
tests/code_examples/test_ch18_probes.py::test_ch18_w01_word_count_within_budget 
[PROBE-CH18-W01-AUTONOMIC-CASCADE] Actual word count: 1700
PASSED
tests/code_examples/test_ch18_probes.py::test_ch18_w01_zero_banned_marketing_words PASSED
tests/code_examples/test_ch18_probes.py::test_ch18_w01_mandatory_concepts_present PASSED
tests/code_examples/test_ch18_probes.py::test_ch18_w01_passive_voice_under_ceiling 
[PROBE-CH18-W01-AUTONOMIC-CASCADE] Passive voice: 1.92% (2/104 sentences)
PASSED

======================= 5 passed, 5 deselected in 0.02s =======================
```

---

### Artifact 4: Negative Boundary & Integrity Confirmation
- No changes made to completed Part I, Part II, Part III, Part IV, or Chapter 17 manuscripts.
- Full regression suite across all chapters passes: 190 passed (and 5 Wave 2 tests pending in RED).
