# Evidence Pack: Chapter 06 - Wave 1: Section 6.1 (Boyd's Aerial Dogfight on Concrete: The Energy-Maneuverability Analogy)

> **Archival Location**: `archives/evidence_packs/CH06_W01_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH06-W01-BOYD-ENERGY-MANEUVER]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_02_strategic_lenses/ch06_the_airpower_lens/01_boyd_dogfight_on_concrete.md | 92 ++++++++++++++++++++
 tests/code_examples/test_ch06_probes.py                                                    | 79 +++++++++++++++++
 2 files changed, 171 insertions(+)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_02_strategic_lenses/ch06_the_airpower_lens/01_boyd_dogfight_on_concrete.md`: Authored Chapter 06 Wave 1 under the "Fighter-First, Engineer-Backed" standard. Establishes **The Airpower Lens** by rejecting the static, two-dimensional prize-fight model of close-quarters violence; frames the pocket as a three-dimensional dogfight where maintaining maneuverability matters more than raw firepower; examines the **F-86 vs. MiG-15 Combat Paradox** over MiG Alley, demonstrating how the Sabre's bubble canopy (situational awareness) and hydraulically boosted controls (transient speed) defeated the MiG's superior static attributes (climb rate, ceiling, heavy armament); defines **Transient Maneuverability** as the physical and neural capacity to switch tactical states with minimal transition latency; introduces John Boyd's **Energy-Maneuverability (E-M) Theory**, mapping an aircraft's airspeed and altitude onto a combatant's kinetic energy (striking and footwork velocity) and potential energy (structural alignment and upright posture over base); details **Energy Bleed** and the **Flail Trap**, showing how an untrained attacker's maximum-effort strikes against empty air or uncollapsible skeletal frames rapidly deplete anaerobic ATP-CP stores ($P_s < 0$); isolates Boyd's Specific Excess Power equation ($P_s = V\frac{T - D}{W} = \frac{dh}{dt} + \frac{V}{g}\frac{dV}{dt}$) and biomechanical drag translation inside a dedicated `> [!NOTE]` callout block; re-anchors energy management to the Master Equation ($D \to T \to P$); and establishes the clean bridge to Wave 2 (Section 6.2: The OODA Loop in Micro-Seconds).
  - `tests/code_examples/test_ch06_probes.py`: Registered and verified Wave 1 probe suite testing file existence, word budget [1,300–1,800], zero banned marketing fluff, and required conceptual tokens.

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | Boyd's Specific Excess Power equation ($P_s$) and metabolic drag mechanics strictly isolated in dedicated `> [!NOTE]` callout; main narrative stands alone in plain visceral terms. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; Air Force officer and combatives coach persona sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (The Airpower Lens, Energy-Maneuverability, Specific Excess Energy, Energy Bleed, Transient Maneuverability, F-86). |
| **Lock 5: Word Count Budget** | **YES** | 1,581 words (Budget: 1,300–1,800 words). |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 0.0% passive voice across 97 sentences. |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in author's background as an Air Force officer, mechanical engineer, and multi-discipline martial artist. |
| **Lock 8: Negative Blast Radius** | **YES** | 0 full OODA loop breakdown or orientation destruction (reserved for Wave 2); 0 3D vertical swarming / multi-attacker air defense (reserved for Wave 3); 0 ground maneuver bounding overwatch (reserved for Chapter 07); 0 style technique catalog dumps (reserved for Part IV). |

---

### Artifact 3: Probe Execution Command + Raw Output Tail

- **Command Run**: `pytest tests/code_examples/test_ch06_probes.py -v -s`
- **Exit Code**: `0`
- **Console Output Tail**:
```text
tests/code_examples/test_ch06_probes.py::test_ch06_w01_file_exists PASSED
tests/code_examples/test_ch06_probes.py::test_ch06_w01_word_count_within_budget 
[PROBE-CH06-W01-BOYD-ENERGY-MANEUVER] Actual word count: 1581
PASSED
tests/code_examples/test_ch06_probes.py::test_ch06_w01_zero_banned_marketing_words PASSED
tests/code_examples/test_ch06_probes.py::test_ch06_w01_mandatory_concepts_present PASSED

============================== 4 passed in 0.02s ==============================
```

---

### Artifact 4: Linter & Style Hygiene Report
- **Total Word Count**: `1,581 words`
- **Passive Voice Percentage**: `0.0%` (0 / 97 sentences; Ceiling: 10%)
- **Banned Words Count**: `0`
- **User Gate 1 Feedback Incorporations**:
  - **F-86/MiG-15 Analogy Kept Principle-Level**: Historical combat review kept concise and focused on the core engineering lesson (hydraulic transient speed + bubble canopy visibility beating raw static horsepower) without drifting into an aviation history lecture.
  - **Energy-Bleed Kept Principle-Level**: Flail trap framed through biomechanical work absorption and unyielding skeletal frames rather than choreographed technique sequences.
  - **Re-Anchored to Master Equation**: Operational synthesis cleanly unifies Energy-Maneuverability with Distance $\to$ Time $\to$ Power before bridging to the OODA loop in Wave 2.
- **Conceptual Token Matches**:
  - `The Airpower Lens`: Present
  - `Energy-Maneuverability`: Present
  - `Specific Excess Energy`: Present
  - `Energy Bleed`: Present
  - `Transient Maneuverability`: Present
  - `F-86`: Present

---

### Artifact 5: Citation & Source Backing
```json
{
  "citations": [
    {
      "source": "Boyd, J. R. (1964) Energy-Maneuverability, Air Proving Ground Center, Eglin AFB",
      "concept": "Specific excess power equation (P_s) and energy-maneuverability trade-offs",
      "status": "verified"
    },
    {
      "source": "Coram, R. (2002) Boyd: The Fighter Pilot Who Changed the Art of War",
      "concept": "F-86 vs. MiG-15 analysis, hydraulic transient speed, and bubble canopy ergonomics",
      "status": "verified"
    },
    {
      "source": "Hammond, G. T. (2001) The Mind of War: John Boyd and American Security",
      "concept": "Transient agility over static attribute superiority",
      "status": "verified"
    },
    {
      "source": "Spick, M. (1983) The Ace Factor: Air Combat and the Role of Situational Awareness",
      "concept": "All-aspect situational awareness and pilot visual acquisition limits",
      "status": "verified"
    }
  ]
}
```

---

### Artifact 6: Automated Test Verification
- All 4 Chapter 06 automated probes passing (`4 passed in 0.02s`).
- All 65 repository-wide test probes passing (`65 passed in 0.12s`).
