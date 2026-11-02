# Evidence Pack: Chapter 12 - Wave 1: Section 12.1 (Distance as Shield: Kinetic Leverage, Angular Footwork, and Long-Range Perimeter Control)

> **Archival Location**: `archives/evidence_packs/CH12_W01_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH12-W01-LONG-RANGE-TACTICS]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_04_discipline_applications/ch12_taekwondo_and_long_range/01_distance_as_shield_and_mechanics_of_the_longest_lever.md | 148 ++++++++++++++++++++
 .agent_context/MANUSCRIPT_REGISTER.md                                                                                                 |   2 +-
 2 files changed, 149 insertions(+), 1 deletion(-)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_04_discipline_applications/ch12_taekwondo_and_long_range/01_distance_as_shield_and_mechanics_of_the_longest_lever.md`: Authored Chapter 12 Wave 1 under the "Fighter-First, Engineer-Backed" standard. Launches **Part IV: Discipline Applications Across the Ranges** by examining **Chapter 12: Taekwondo & Long Range — Distance as Shield, Footwork, and Long-Range Windows**; grounds doctrine in the author's background as a Taekwondo black belt, military officer, and mechanical engineer; establishes **Distance as Shield**, contrasting the suicidal nature of close-quarters trading on asphalt with outermost standoff perimeter control ($d \approx d_{\text{kick}}$); analyzes the biomechanics of the **Longest Lever**, contrasting the fragile, low-mass arm against the multi-segment kinetic pendulum of the leg (1.5x length, 3-4x muscle mass); establishes the **Standoff Safety Delta** ($\Delta d_{\text{safety}} = L_{\text{leg}} - L_{\text{arm}} > 0$), keeping vital command centers 36–48 inches away from adversary hand strikes; proves the lethal flaw of linear backpedaling ($v_{\text{forward}} > v_{\text{backward}}$) and establishes **Angular Footwork** (45-degree angle cuts, lateral pivots, switch-steps, slide-backs); operationalizes **Refusing the Centerline** to decouple momentum, force high centripetal turning deceleration ($a_c = v^2/R \gg \mu g$), and expose the adversary's flank; isolates rotational kinetic energy ($E_k = \frac{1}{2}I\omega^2$, $I_{\text{leg}} \approx 6.75 I_{\text{arm}}$), standoff safety deltas, and centripetal turning traction demands in a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"); anchors long range to the Foundational Trinity (Principles 1, 2, and 3) under **The Master Equation: Distance $\to$ Time $\to$ Power**; and builds the operational bridge to Wave 2 (Section 12.2: *Long-Range Timing Windows, Interception, and the Fatal Traps of Sport Taekwondo*).

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | Rotational kinetic energy, standoff delta, and centripetal turning formulas strictly isolated in `> [!NOTE]` callout; main narrative stands alone in visceral combative language. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; veteran black-belt coach, engineer, and military officer voice sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (Taekwondo, Distance as Shield, Longest Lever, Angular Footwork, Refusing the Centerline, Master Equation). |
| **Lock 5: Word Count Budget** | **YES** | 1,676 words (Budget: 1,300–1,800 words; Target: 1,400–1,750 words). |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 4.21% passive voice across 95 sentences (Ceiling: 10%). |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in Taekwondo black belt credentials, mechanical engineering mechanics, and military combatives. |
| **Lock 8: Negative Blast Radius** | **YES** | 0 clinch/wrestling technique dumps (reserved for Chapters 13–15); 0 sport tournament trick-kicking catalogs. |

---

### Artifact 3: Probe Execution Command + Raw Output Tail

- **Command Run**: `pytest tests/code_examples/test_ch12_probes.py -v -s`
- **Exit Code**: `0`
- **Console Output Tail**:
```text
tests/code_examples/test_ch12_probes.py::test_ch12_w01_file_exists PASSED
tests/code_examples/test_ch12_probes.py::test_ch12_w01_word_count_within_budget 
[PROBE-CH12-W01-LONG-RANGE-TACTICS] Actual word count: 1676
PASSED
tests/code_examples/test_ch12_probes.py::test_ch12_w01_zero_banned_marketing_words PASSED
tests/code_examples/test_ch12_probes.py::test_ch12_w01_mandatory_concepts_present PASSED

============================== 4 passed in 0.02s ==============================
```

---

### Artifact 4: Negative Boundary & Integrity Confirmation
- No changes made to completed Part I, Part II, or Part III manuscripts.
- No concepts from Muay Thai clinch (Ch 13) or wrestling/grappling (Ch 14/15) leaked into this long-range striking chapter.
- No unverified physical or mathematical claims; all mechanical models derive from classical mechanics.
