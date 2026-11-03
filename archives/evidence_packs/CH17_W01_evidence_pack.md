# Evidence Pack: Chapter 17 - Wave 1: Section 17.1 (Recognize and Prioritize: Perceptual Audits, Intent Cues, and Locking Strategic Purpose)

> **Archival Location**: `archives/evidence_packs/CH17_W01_evidence_pack.md`  
> **Status**: `SUBMITTED FOR EDITOR GATE 2 REVIEW`  
> **Designated Probe ID**: `[PROBE-CH17-W01-RECOGNIZE-AND-PRIORITIZE]`

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)

```text
 manuscript/part_05_the_decision_engine/ch17_the_4_step_cycle/01_recognize_and_prioritize.md | 124 ++++++++++++++++++++
 .agent_context/MANUSCRIPT_REGISTER.md                                                       |   2 +-
 2 files changed, 125 insertions(+), 1 deletion(-)
```

- **Targeted Unified Diff Hunk Summary**:
  - `manuscript/part_05_the_decision_engine/ch17_the_4_step_cycle/01_recognize_and_prioritize.md`: Authored Chapter 17 Wave 1 under the "Fighter-First, Engineer-Backed" standard. Opens **Chapter 17: The 4-Step Cycle — Recognize, Prioritize, Choose, Act & Reassess** and launches **Part V: The Decision Engine**; establishes the primacy of the cognitive Command Center under acute threat, explaining why cognitive speed ($150\text{--}250\ \text{ms}$ in primed practitioners vs. $600\text{--}1,000\ \text{ms}$ in unprimed individuals) dominates muscular contraction speed ($7\text{--}10\ \text{m/s}$ straight punch, $0.2\text{--}0.3\ \text{s}$ sprawl); operationalizes **Step 1 (Recognize)** through an active, continuous **Perceptual Audit** across Self (base, posture, frame readiness), Threat (hands, gaze, orientation, closing velocity), and Environment (terrain, lighting, choke points, escape corridors); catalogs the five universal **Intent Cues** (target fixation & predator scan, weight transfer & hip coiling, blade step, weapon indexing, verbal agitation with spatial compression); analyzes the **Reactionary Gap** in milliseconds ($200\text{--}300\ \text{ms}$ attack initiation vs. $450\text{--}600\ \text{ms}$ defensive latency) and proves why action beats reaction unless pre-attack cues are intercepted; operationalizes **Step 2 (Prioritize)** through military Mission Command (Clear Purpose + Flexible Method), establishing the absolute strategic dichotomy between Priority A (Immediate Egress / Exit) and Priority B (Definitive Mechanical Control); proves that locking strategic purpose prunes $90\%$ of tactical options from working memory, reducing cognitive decision latency from $> 735\ \text{ms}$ to $\approx 285\ \text{ms}$; isolates Shannon information-theoretic threat entropy ($H(X) = -\sum P \log_2 P$), reactionary deficit kinematics ($\Delta d_{\text{deficit}} = v \times \Delta t_{\text{total}}$), and Hick's Law cognitive option pruning ($T = b \log_2(n+1)$) in a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"); anchors the cognitive engine to the Master Equation ($P = W / \Delta t$ across Distance $\to$ Time $\to$ Power); and constructs the operational bridge to Wave 2 (Section 17.2: Step 3 [Choose], Step 4 [Act & Reassess], and Chapter 17 Capstone).

---

### Artifact 2: Master Invariant Checklist (Locks)

| Safety Invariant / Lock | Status | Verification Method |
| :--- | :---: | :--- |
| **Lock 1: Fighter-First Delivery** | **YES** | Every subsection opens with a direct, usable tactical rule and concrete combat consequence. |
| **Lock 2: Action Precedes Science / Math** | **YES** | Shannon entropy, reactionary deficit kinematics, and Hick's Law pruning formulas strictly isolated in `> [!NOTE]` callout; main narrative stands alone in visceral combative language. |
| **Lock 3: The Mat Test Compliance** | **YES** | Coach-to-fighter corner voice maintained throughout; veteran combatives coach, military officer, and engineer persona sounds authentic between rounds. |
| **Lock 4: Terminology Fidelity** | **YES** | Aligns with `CONCEPT_REGISTER.md` and `GLOSSARY.md` (The 4-Step Cycle, Recognize, Prioritize, Perceptual Audit, Intent Cues, Strategic Purpose, Reactionary Gap, Master Equation). |
| **Lock 5: Word Count Budget** | **YES** | 1,753 words (Budget: 1,300–1,800 words; Target: 1,400–1,750 words). |
| **Lock 6: Linguistic Hygiene** | **YES** | 0 banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`); 0.97% passive voice across 103 sentences (Ceiling: 10%). |
| **Lock 7: Authorial Credibility** | **YES** | Grounded in OODA/Mission Command military doctrine, cognitive neuroscience, reactionary deficit kinematics, information theory, and street combatives coaching. |
| **Lock 8: Negative Blast Radius** | **YES** | Zero drift into Step 3/Step 4 (quarantined for Wave 2), high-stress autonomic failure (quarantined for Chapter 18), weapon disarms (quarantined for Chapter 20), or legal trial doctrine (quarantined for Chapter 21). |

---

### Artifact 3: Probe Execution Command + Raw Output Tail

- **Command Run**: `pytest tests/code_examples/test_ch17_probes.py -k w01 -v -s`
- **Exit Code**: `0`
- **Console Output Tail**:
```text
tests/code_examples/test_ch17_probes.py::test_ch17_w01_file_exists PASSED
tests/code_examples/test_ch17_probes.py::test_ch17_w01_word_count_within_budget 
[PROBE-CH17-W01-RECOGCOGNIZE-AND-PRIORITIZE] Actual word count: 1753
PASSED
tests/code_examples/test_ch17_probes.py::test_ch17_w01_zero_banned_marketing_words PASSED
tests/code_examples/test_ch17_probes.py::test_ch17_w01_mandatory_concepts_present PASSED
tests/code_examples/test_ch17_probes.py::test_ch17_w01_passive_voice_under_ceiling 
[PROBE-CH17-W01-RECOGNIZE-AND-PRIORITIZE] Passive voice: 0.97% (1/103 sentences)
PASSED

======================= 5 passed, 5 deselected in 0.03s =======================
```

---

### Artifact 4: Negative Boundary & Integrity Confirmation
- No changes made to completed Part I, Part II, Part III, or Part IV (Chapters 12–16) manuscripts.
- Full regression suite across all chapters passes: 175 passed in 0.32s.
