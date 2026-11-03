# Evidence Pack: Chapter 15 - Wave 2: Section 15.2 (Sport BJJ Pitfalls on Asphalt, High-Percentage Strangleholds, and Technical Stand-Up: The Non-Negotiable Egress)

> **Archival Location**: `archives/evidence_packs/CH15_W02_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH15-W02-SPORT-BJJ-TRAPS-AND-EGRESS]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_04_discipline_applications/ch15_brazilian_jiu_jitsu_and_ground_survival/02_sport_traps_strangles_and_egress.md | 104 ++++++++++++++++++++
 .agent_context/MANUSCRIPT_REGISTER.md                                                                                           |   2 +-
 2 files changed, 105 insertions(+), 1 deletion(-)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_04_discipline_applications/ch15_brazilian_jiu_jitsu_and_ground_survival/02_sport_traps_strangles_and_egress.md`: Authored Chapter 15 Wave 2 under the "Fighter-First, Engineer-Backed" standard. Concludes **Chapter 15: Brazilian Jiu-Jitsu & Ground Survival** with Section 15.2 and the unified *Brazilian Jiu-Jitsu Capstone*. Deconstructs **The Four Sport Traps** on asphalt (guard pulling as voluntary base surrender, leg-lock/50-50 entanglements causing severe head exposure, gi-grip dependence failing under fabric shear, and prolonged closed-guard tenure inviting concussive trauma); proves why peripheral joint locks fail against stress-induced analgesia and drug intoxication (PCP, methamphetamine), prioritizing high-percentage **Vascular Strangles** (bilateral carotid occlusion inducing cortical anoxia in 6 to 9 seconds regardless of size or pain tolerance); operationalizes the **Rear Naked Choke** from back control (chest-to-back connection placing defender outside striking arcs and visual field) and the emergency guillotine; details the four biomechanical phases of the **Technical Stand-Up** (creating standoff separation, establishing the tripod base with forward structural guard shield, pelvic elevation with leg sweep beneath torso, and dynamic base recovery); isolates carotid occlusion pressure ($P_{\text{occlusion}} \ge 20\text{--}30\ \text{kPa} \implies Q \to 0, t \approx 6.0\text{--}9.0\ \text{s}$), leg-lock blind-spot exposure ($\theta_{\text{blind}} \ge 300^\circ, \Delta t_{\text{flank}} \le 1.0\ \text{s}$), and tripod stand-up work ($W \approx 550\ \text{J}$) in a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"); binds ground survival to the **Master Equation** ($P = W / \Delta t$ across Distance $\to$ Time $\to$ Power); synthesizes Part IV across all four range applications (Taekwondo, Muay Thai, Wrestling, Brazilian Jiu-Jitsu); and constructs the operational bridge into Chapter 16 (*Range Transitions & Fluid Synthesis*).

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | Carotid occlusion pressure, blind-spot angle, and stand-up work formulas strictly isolated in `> [!NOTE]` callout; main narrative stands alone in visceral combative language. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; veteran combatives coach, military officer, and engineer persona sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (Brazilian Jiu-Jitsu, The Four Sport Traps, Guard Pulling, Vascular Strangles, Rear Naked Choke, Technical Stand-Up, Ground Egress, Master Equation, Brazilian Jiu-Jitsu Capstone). |
| **Lock 5: Word Count Budget** | **YES** | 1,720 words (Budget: 1,300–1,800 words; Target: 1,400–1,750 words). Cumulative Chapter 15: 3,467 words. |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 0.00% passive voice across 96 sentences (Ceiling: 10%). |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in combatives coaching, BJJ black belt instruction, cardiovascular hemodynamics, kinematic statics, and situational threat awareness. |
| **Lock 8: Negative Blast Radius** | **YES** | Zero multi-step sport tournament leg lock variations (50/50, saddle, honey hole) beyond deconstructing them as asphalt traps; zero standing weapon disarms (reserved for Chapter 20); stand-up striking and wrestling takedown defense remain frozen in Chapters 12–14; range transitions reserved for Chapter 16. |

---

### Artifact 3: Probe Execution Command + Raw Output Tail

- **Command Run**: `pytest tests/code_examples/test_ch15_probes.py -v -s`
- **Exit Code**: `0`
- **Console Output Tail**:
```text
tests/code_examples/test_ch15_probes.py::test_ch15_w01_file_exists PASSED
tests/code_examples/test_ch15_probes.py::test_ch15_w01_word_count_within_budget 
[PROBE-CH15-W01-STRUCTURAL-FRAMING-AND-GROUND-SURVIVAL] Actual word count: 1747
PASSED
tests/code_examples/test_ch15_probes.py::test_ch15_w01_zero_banned_marketing_words PASSED
tests/code_examples/test_ch15_probes.py::test_ch15_w01_mandatory_concepts_present PASSED
tests/code_examples/test_ch15_probes.py::test_ch15_w01_passive_voice_under_ceiling 
[PROBE-CH15-W01-STRUCTURAL-FRAMING-AND-GROUND-SURVIVAL] Passive voice: 5.56% (6/108 sentences)
PASSED
tests/code_examples/test_ch15_probes.py::test_ch15_w02_file_exists PASSED
tests/code_examples/test_ch15_probes.py::test_ch15_w02_word_count_within_budget 
[PROBE-CH15-W02-SPORT-BJJ-TRAPS-AND-EGRESS] Actual word count: 1720
PASSED
tests/code_examples/test_ch15_probes.py::test_ch15_w02_zero_banned_marketing_words PASSED
tests/code_examples/test_ch15_probes.py::test_ch15_w02_mandatory_concepts_present PASSED
tests/code_examples/test_ch15_probes.py::test_ch15_w02_passive_voice_under_ceiling 
[PROBE-CH15-W02-SPORT-BJJ-TRAPS-AND-EGRESS] Passive voice: 0.00% (0/96 sentences)
PASSED

============================= 10 passed in 0.03s ==============================
```

---

### Artifact 4: Negative Boundary & Integrity Confirmation
- No changes made to completed Part I, Part II, Part III, Chapter 12, Chapter 13, or Chapter 14 manuscripts.
- Section 15.1 remains completely frozen and untouched (`CH15-W01-STRUCTURAL-FRAMING-AND-GROUND-SURVIVAL-FROZEN`).
- Range chaining and inter-discipline transitions strictly quarantined for Chapter 16.
- All mechanical models derive from classical mechanics (hemodynamics, field-of-view geometry, tripod equilibrium).
