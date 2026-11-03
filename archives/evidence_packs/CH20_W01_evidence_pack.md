# Evidence Pack: Chapter 20 - Wave 1: Sections 20.1 & 20.2 (Edged Weapons and Flanking/Funneling Multiple Attackers)

> **Archival Location**: `archives/evidence_packs/CH20_W01_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH20-W01-EDGED-WEAPONS-AND-FLANKING]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_06_training_doctrine/ch20_asymmetric_threats/01_edged_weapons_and_flanking.md | 85 ++++++++++++++++++++
 .agent_context/MANUSCRIPT_REGISTER.md                                                         |  2 +-
 2 files changed, 86 insertions(+), 1 deletion(-)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_06_training_doctrine/ch20_asymmetric_threats/01_edged_weapons_and_flanking.md`: Authored Chapter 20 Wave 1 under the "Fighter-First, Engineer-Backed" standard. Launches **Chapter 20: Weapon Surprises, Asymmetric Threats, and Multiple Attackers**; resolves severe survival asymmetries where single-opponent sport assumptions become fatal; deconstructs traditional martial arts knife myths (flashy wrist locks, mid-air catches, static parries) and establishes real-world **Edged Weapon Realities**; exposes the forensic reality of the **Sewing-Machine Attack** (cyclic piston-like stabs at 3–5 Hz executed while clinching or grabbing); proves why **Tactile Recognition** must supersede visual detection due to adrenaline-induced tunnel vision and tachypsychia; formulates the reactionary gap deficit under Tueller dynamics, proving that linear backpedaling is fatal because backward human movement velocity ($\approx 3.2\ \text{m/s}$) is half of forward sprint speed ($> 7.0\ \text{m/s}$); establishes gross-motor **2-on-1 Limb Control** (bilateral clamping and cervical disruption) to eliminate weapon leverage ($\tau = 0$) while accepting forearm lacerations to protect vital arteries; models multiple-opponent violence through **Lanchester's Law** (Square Law), proving that group fighting efficacy scales quadratically ($P \propto N^2$) in unconstrained combat; deconstructs **The Encirclement Trap** and resolves it through **Geometric Funneling** and aggressive **Angular Flanking** to convert a 2-on-1 assault into sequential 1-on-1 engagements via the Human Shield principle; operationalizes environmental bottlenecks (parked cars, narrow doorways, urban obstacles) to enforce the Thermopylae dynamic; establishes the non-negotiable absolute refusal of the ground in multi-adversary confrontations; and isolates reciprocating stab kinematics, Lanchester differential equations, and line-of-sight occlusion angle geometry in a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It").

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete combat consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | Piston stab kinematics, Lanchester differential equations, and occlusion angle formulas strictly isolated in `> [!NOTE]` callout; main narrative stands alone in visceral combative language. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; veteran combatives coach, military officer, and engineer persona sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (Edged Weapon Realities, Sewing-Machine Attack, Tactile Recognition, 2-on-1 Limb Control, Lanchester's Law, Geometric Funneling, Angular Flanking, The Encirclement Trap). |
| **Lock 5: Word Count Budget** | **YES** | 1,710 words (Budget: 1,300–1,800 words; Target: 1,400–1,750 words). |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 4.31% passive voice across 116 sentences (Ceiling: 10%). |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in forensic assault data, Tueller/Blair reactionary gap research, Lanchester military combat modeling, and high-threat combatives coaching. |
| **Lock 8: Negative Blast Radius** | **YES** | Zero drift into firearm disarms or weapon retention (quarantined for Section 20.3), Chapter 20 Capstone (quarantined for Wave 2), or legal trial testimony (quarantined for Chapter 21). |

---

### Artifact 3: Probe Execution Command + Raw Output Tail

- **Command Run**: `pytest tests/code_examples/test_ch20_probes.py -v -s`
- **Exit Code**: `0`
- **Console Output Tail**:
```text
tests/code_examples/test_ch20_probes.py::test_ch20_w01_file_exists PASSED
tests/code_examples/test_ch20_probes.py::test_ch20_w01_word_count_within_budget 
[PROBE-CH20-W01-EDGED-WEAPONS-AND-FLANKING] Actual word count: 1710
PASSED
tests/code_examples/test_ch20_probes.py::test_ch20_w01_zero_banned_marketing_words PASSED
tests/code_examples/test_ch20_probes.py::test_ch20_w01_mandatory_concepts_present PASSED
tests/code_examples/test_ch20_probes.py::test_ch20_w01_passive_voice_under_ceiling 
[PROBE-CH20-W01-EDGED-WEAPONS-AND-FLANKING] Passive voice: 4.31% (5/116 sentences)
PASSED

============================== 5 passed in 0.03s ==============================
```

---

### Artifact 4: Negative Boundary & Integrity Confirmation
- No changes made to completed Part I, Part II, Part III, Part IV, Part V, or Chapter 19 manuscripts.
- Full regression suite across all chapters passes: 210 passed in 0.40s.
