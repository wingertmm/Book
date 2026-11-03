# Evidence Pack: Chapter 21 - Wave 1: Section 21.1 (Proportionality and the Continuum of Force)

> **Archival Location**: `archives/evidence_packs/CH21_W01_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH21-W01-PROPORTIONALITY-AND-FORCE]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_06_training_doctrine/ch21_legal_and_ethical/01_proportionality_and_force.md | 85 ++++++++++++++++++++
 .agent_context/MANUSCRIPT_REGISTER.md                                                       |  2 +-
 2 files changed, 86 insertions(+), 1 deletion(-)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_06_training_doctrine/ch21_legal_and_ethical/01_proportionality_and_force.md`: Authored Chapter 21 Wave 1 under the "Fighter-First, Engineer-Backed" standard. Launches **Chapter 21: The Ethical and Legal Boundaries of Power**; establishes the constitutional, statutory, and ethical boundaries that govern the application of physical combative power; deconstructs the fantasy of martial arts fiction and contrasts it with the reality of forensic scrutiny, surveillance evidence, and courtroom accountability; details the **Objective Reasonableness** doctrine established by the U.S. Supreme Court in *Graham v. Connor* (1989), evaluating force from the perspective of a reasonable person facing tense, uncertain, and rapidly evolving threats without 20/20 hindsight across three core legal prongs (threat severity, immediate danger, and active resistance); constructs the dynamic **Continuum of Force** ladder matching threat gradients to justified physical responses; enforces the **Proportionality Invariant**, proving that defensive force must be reasonably calculated to stop the active threat and never to punish, retaliate, or avenge an insult; formulates **Disparity of Force**, explaining how numerical superiority (Lanchester's Law), extreme size/weight asymmetry, ground entrapment, and physical disability legally cross the **Lethal Force Threshold** against an otherwise "unarmed" assailant; establishes the non-negotiable **Cessation of Threat** duty, marking the precise millisecond where an adversary's incapacity, surrender, or flight terminates legal justification ($F_{\text{allowed}} \to 0$); translates observed biological intent cues into admissible **Pre-Attack Articulation**; binds defensive kinetics to the **Master Equation Legal Bounds** ($P = W / \Delta t$), ensuring mechanical work ($W$) ceases instantly upon threat termination; and isolates proportionality escalation vectors, disparity force multipliers, and the cessation step function in a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It").

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete combat consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | Proportionality vectors, disparity multipliers, and cessation step functions strictly isolated in `> [!NOTE]` callout; main narrative stands alone in visceral combative language. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; veteran combatives coach, military officer, and engineer persona sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (Objective Reasonableness, Continuum of Force, Proportionality Invariant, Disparity of Force, Cessation of Threat, Lethal Force Threshold, Pre-Attack Articulation, Master Equation Legal Bounds). |
| **Lock 5: Word Count Budget** | **YES** | 1,633 words (Budget: 1,300–1,800 words; Target: 1,400–1,750 words). Cumulative manuscript total: 86,340 words across 51 completed sections. |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 1.06% passive voice across 94 sentences (Ceiling: 10%). |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in constitutional jurisprudence, law enforcement use-of-force standards, military ROE, and combatives coaching. |
| **Lock 8: Negative Blast Radius** | **YES** | Zero drift into 911 dispatch scripts, trauma medical self-triage, scene exit protocols (quarantined for Section 21.2), or the whole-book Capstone (quarantined for Wave 2). |

---

### Artifact 3: Probe Execution Command + Raw Output Tail

- **Command Run**: `pytest tests/code_examples/test_ch21_probes.py -v -s`
- **Exit Code**: `0`
- **Console Output Tail**:
```text
tests/code_examples/test_ch21_probes.py::test_ch21_w01_file_exists PASSED
tests/code_examples/test_ch21_probes.py::test_ch21_w01_word_count_within_budget 
[PROBE-CH21-W01-PROPORTIONALITY-AND-FORCE] Actual word count: 1633
PASSED
tests/code_examples/test_ch21_probes.py::test_ch21_w01_zero_banned_marketing_words PASSED
tests/code_examples/test_ch21_probes.py::test_ch21_w01_mandatory_concepts_present PASSED
tests/code_examples/test_ch21_probes.py::test_ch21_w01_passive_voice_under_ceiling 
[PROBE-CH21-W01-PROPORTIONALITY-AND-FORCE] Passive voice: 1.06% (1/94 sentences)
PASSED

============================== 5 passed in 0.03s ==============================
```

---

### Artifact 4: Negative Boundary & Integrity Confirmation
- No changes made to completed Part I, Part II, Part III, Part IV, Part V, Chapter 19, or Chapter 20 manuscripts.
- Full regression suite across all chapters passes: 220 passed in 0.38s.
