# Evidence Pack: Chapter 13 - Wave 1: Section 13.1 (The Eight Limbs on Asphalt: Space Control, Short-Lever Kinetic Shock, and Medium-Range Angle Shifts)

> **Archival Location**: `archives/evidence_packs/CH13_W01_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH13-W01-MEDIUM-RANGE-TACTICS]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_04_discipline_applications/ch13_muay_thai_and_medium_range/01_space_control_and_short_lever_kinetic_shock.md | 134 ++++++++++++++++++++
 .agent_context/MANUSCRIPT_REGISTER.md                                                                                        |   2 +-
 2 files changed, 135 insertions(+), 1 deletion(-)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_04_discipline_applications/ch13_muay_thai_and_medium_range/01_space_control_and_short_lever_kinetic_shock.md`: Authored Chapter 13 Wave 1 under the "Fighter-First, Engineer-Backed" standard. Launches **Chapter 13: Muay Thai & Medium/Close Range — Space Control, Leverage, and Clinch Disruption**; addresses the intermediate collision zone (Medium Range $d \approx d_{\text{punch}}$ and Close Range $d \approx d_{\text{elbow}}$) when long-range kicking distance collapses; exposes **The Pocket Trap**, proving why stationary fist trading inside arm's reach leads to fractured metacarpals, mutual concussions, and defensive failure; introduces **The Science of Eight Limbs** (fists, elbows, knees, shins) to transform medium range from a fist duel into an asymmetric skeletal arsenal; establishes **Medium-Range Space Control** through the hydraulic lead push kick (*teep*) to reset range, the heavy low shin kick (*te khakha*) to destroy the femoral/peroneal nerve base, and the Long Guard stiff-arm frame; details the biomechanics of **Short-Lever Shock**, proving why swapping fragile hand bones (27 delicate bones) for dense skeletal battering rams (olecranon process and patella) produces catastrophic damage without risk of self-injury; isolates contact pressure concentration ($P = F / A \approx 10.67\ \text{MPa} \gg \sigma_{\text{yield}}$), rotational lever acceleration in compressed arcs ($\alpha_{\text{elbow}} \approx 5.44 \times \alpha_{\text{punch}}$), and low-line tibial neural stun mechanics in a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"); integrates medium-range control under **The Master Equation: Distance $\to$ Time $\to$ Power**; and constructs the operational bridge to Wave 2 (Section 13.2: *The Thai Clinch, Cervical Spine Manipulation, and Escaping the Collision Zone*).

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | Contact pressure concentration, rotational lever acceleration, and neural stun formulas strictly isolated in `> [!NOTE]` callout; main narrative stands alone in visceral combative language. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; veteran combatives coach, military officer, and engineer persona sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (Muay Thai, Eight Limbs, Short-Lever Shock, Contact Pressure Concentration, The Pocket Trap, Medium-Range Space Control, Master Equation). |
| **Lock 5: Word Count Budget** | **YES** | 1,714 words (Budget: 1,300–1,800 words; Target: 1,400–1,750 words). |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 1.25% passive voice across 80 sentences (Ceiling: 10%). |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in combatives coaching, Muay Thai striking mechanics, skeletal anatomy, and mechanical engineering. |
| **Lock 8: Negative Blast Radius** | **YES** | 0 deep-dives into full double-collar plum neck wrestling (reserved for Wave 2) or wrestling takedowns/sprawls (reserved for Chapter 14); zero ring-walk ritual trivia. |

---

### Artifact 3: Probe Execution Command + Raw Output Tail

- **Command Run**: `pytest tests/code_examples/test_ch13_probes.py -v -s`
- **Exit Code**: `0`
- **Console Output Tail**:
```text
tests/code_examples/test_ch13_probes.py::test_ch13_w01_file_exists PASSED
tests/code_examples/test_ch13_probes.py::test_ch13_w01_word_count_within_budget 
[PROBE-CH13-W01-MEDIUM-RANGE-TACTICS] Actual word count: 1714
PASSED
tests/code_examples/test_ch13_probes.py::test_ch13_w01_zero_banned_marketing_words PASSED
tests/code_examples/test_ch13_probes.py::test_ch13_w01_mandatory_concepts_present PASSED

============================== 4 passed in 0.02s ==============================
```

---

### Artifact 4: Negative Boundary & Integrity Confirmation
- No changes made to completed Part I, Part II, Part III, or Chapter 12 manuscripts.
- Clinch neck-wrestling and sweeps reserved for Chapter 13 Wave 2.
- All mechanical models derive from classical mechanics and empirical material shear-strength baselines.
