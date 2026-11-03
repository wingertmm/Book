# Evidence Pack: Chapter 15 - Wave 1: Section 15.1 (Structural Framing, Asymmetric Limb Ratios, and the Zero-Distance Paradox: Surviving the Concrete Bottom)

> **Archival Location**: `archives/evidence_packs/CH15_W01_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH15-W01-STRUCTURAL-FRAMING-AND-GROUND-SURVIVAL]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_04_discipline_applications/ch15_brazilian_jiu_jitsu_and_ground_survival/01_structural_framing_and_ground_survival.md | 114 ++++++++++++++++++++
 .agent_context/MANUSCRIPT_REGISTER.md                                                                                                 |   2 +-
 2 files changed, 115 insertions(+), 1 deletion(-)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_04_discipline_applications/ch15_brazilian_jiu_jitsu_and_ground_survival/01_structural_framing_and_ground_survival.md`: Authored Chapter 15 Wave 1 under the "Fighter-First, Engineer-Backed" standard. Launches **Chapter 15: Brazilian Jiu-Jitsu & Ground Survival — Structural Framing, Asymmetric Limb Ratios, and the Imperative of Getting Back Up**; analyzes the brutal realities of the asphalt bottom when upright wrestling base is compromised; deconstructs **The Zero-Distance Paradox**, proving why the intermediate gap (6 to 18 inches) is a lethal striking zone where downward punches accelerate under gravity ($mg$) and impact an unyielding asphalt anvil ($k_{\text{concrete}} \to \infty$) while the pinned defender lacks rotational hip torque; establishes the two survival zones (absolute zero distance chest-to-chest clamp vs. framed structural distance); analyzes asphalt friction traps ($\mu_s \approx 0.85\text{--}1.0$) that lock the defender's hips to the street and shear skin; establishes **Structural Framing** as an architectural truss system of **Skeletal Struts** (radius, ulna, and tibia) that transmit compressive loads into the shoulder girdle and ground with near-zero ATP expenditure, contrasting it against the rapid lactic acid collapse of muscular bench-press reactions; defines the three survival functions of the minimum structural buffer ($d_{\text{min}}$: airway preservation, vascular shielding, and decoupling striking trajectories); operationalizes **Asymmetric Limb Ratios** (TRIZ Principle 6) via 2-on-1 wrist/tricep control and knee-shield integration to neutralize threat extremities with compound mechanical advantage ($MA \ge 2.5$); details the biomechanical engine of the **Hip Escape** (shrimping), proving why the defender must never push the opponent away but instead move themselves laterally to insert an impenetrable knee-shield wedge; isolates Euler column buckling ($P_{\text{cr}} = \pi^2 E I / (KL)^2 > 3,000\ \text{N}$), concrete impulse amplification ($F_{\text{avg}} = m \Delta v / \Delta t \ge 6,000\text{--}10,000\ \text{N}$), and compound mechanical advantage formulas in a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"); binds ground survival fundamentals to the **Master Equation** ($P = W / \Delta t$ across Distance $\to$ Time $\to$ Power); and constructs the operational bridge to Section 15.2 (*Sport BJJ Pitfalls on Asphalt, High-Percentage Strangleholds, and Technical Stand-Up: The Non-Negotiable Egress*).

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | Euler column buckling, impulse amplification, and compound mechanical advantage formulas strictly isolated in `> [!NOTE]` callout; main narrative stands alone in visceral combative language. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; veteran combatives coach, military officer, and engineer persona sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (Brazilian Jiu-Jitsu, Ground Survival, Zero-Distance Paradox, Structural Framing, Skeletal Struts, Asymmetric Limb Ratios, Hip Escape, Master Equation). |
| **Lock 5: Word Count Budget** | **YES** | 1,747 words (Budget: 1,300–1,800 words; Target: 1,400–1,750 words). |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 5.56% passive voice across 108 sentences (Ceiling: 10%). |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in combatives coaching, Brazilian Jiu-Jitsu mechanics, bone structural statics, impulse dynamics, and TRIZ multifunctionality. |
| **Lock 8: Negative Blast Radius** | **YES** | Zero sport guard pulling, rolling leg locks, or tournament submission point hunting (reserved for Section 15.2 sport traps analysis); zero deep-dive into standing weapon disarms (reserved for Chapter 20); standing clinch and takedown defense already completed in Chapters 13 and 14; technical stand-up reserved for Section 15.2. |

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

============================== 5 passed in 0.02s ==============================
```

---

### Artifact 4: Negative Boundary & Integrity Confirmation
- No changes made to completed Part I, Part II, Part III, Chapter 12, Chapter 13, or Chapter 14 manuscripts.
- All upright clinch, level-change, and anti-takedown mechanics remain frozen in Chapters 13 and 14.
- Sport BJJ traps, vascular strangles (RNC, guillotine), and the Technical Stand-Up reserved for Chapter 15 Wave 2.
- All mechanical models derive from classical mechanics (Euler buckling, impulse-momentum theorem, compound force couples).
