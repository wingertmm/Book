# Authoring Section Implementation Plan: Chapter 02 — Wave 1

**Target Chapter & Wave**: `Chapter 02 - Wave 1: Sections 2.1–2.2 (The Physics of Relative Attributes & The Law of Weapon Eligibility in Depth)`  
**Target Milestone**: `Part I: The Master Filter (The Physics & Philosophy of Force)`  
**Status**: `GATE 1: SUBMITTED FOR REVIEW`  

---

### 1. Goal & Pedagogical Intent
Deepen the operational understanding of Distance established in Chapter 01 by examining how physical attributes (reach, height, mass, mobility) alter spatial dynamics, and how the **Law of Weapon Eligibility** functions as an active cognitive and biomechanical threat filter. Ground the analysis in the **Fighter-First, Engineer-Backed** standard: lead with coach-level decision rules, explain physical mechanisms in visceral language before introducing any models, sequester formal geometry or cognitive equations into dedicated callout blocks, and enforce the Mat Test.

---

### 2. Learning Objective & Concept Binding
- **Objective ID**: `OBJ-CH02-001`
- **Target Concepts Introduced**:
  - *The Physics of Relative Attributes*: Reach, height, mass, and center-of-gravity height are not absolute virtues; they are relative parameters with distinct biomechanical failure modes and advantages.
  - *The Reach Dilemma*: How a reach advantage creates an asymmetric spatial tax at long range, but transforms into a severe mechanical liability when crowded inside close quarters.
  - *Center of Gravity Inversion*: How greater height raises the Center of Mass (COM), making taller combatants easier to unbalance and sweep, while a compact frame provides superior base stability and low-level driving power.
  - *The Law of Weapon Eligibility (In-Depth)*: How physical distance acts as an anatomical gatekeeper, disabling strikes outside their operational envelope and pruning the threat matrix.
  - *Hick's Law Pruning ($T = b \log_2(n+1)$)*: How narrowing the adversary's eligible attacks from twenty to two collapses human reaction latency and eliminates cognitive freeze.
- **Forward Pointers**:
  - Connects directly to Chapter 02 Wave 2 (The Four Ranges in detail).
  - Connects to Chapter 03 (Timing windows and reading commitment cues).
  - Connects to Part IV (Style applications: Taekwondo long range vs. Muay Thai close range vs. Wrestling clinch).

---

### 3. Invariant Locks (Mandatory Constraints)
- [ ] **Lock 1 (Fighter-First Delivery)**: Every major subsection must open with a direct, usable tactical rule and concrete consequence before introducing any physical or anatomical mechanics. [Yes]
- [ ] **Lock 2 (Action Precedes Math)**: All mathematical formulas (Hick's Law $T = b \log_2(n+1)$, reach arc radiuses $r$, moment arms $\tau = r \times F$) must reside in dedicated `> [!NOTE]` callouts ("The Mechanics Behind It") or concise parentheticals—never in the primary prose narrative. [Yes]
- [ ] **Lock 3 (The Mat Test Compliance)**: The prose must pass the Mat Test: read like a seasoned coach explaining realities between rounds, avoiding dry academic or classroom pedantry. [Yes]
- [ ] **Lock 4 (Terminology Fidelity)**: All technical terms (Relative Attributes, Reach Advantage, Law of Weapon Eligibility, Base of Support, Center of Mass) must match [CONCEPT_REGISTER.md](file:///c:/Book/.agent_context/CONCEPT_REGISTER.md) and [GLOSSARY.md](file:///c:/Book/.agent_context/GLOSSARY.md) exactly. [Yes]
- [ ] **Lock 5 (Word Count Budget)**: Target is 1,200 – 1,500 words (hard ceiling: 1,700 words). [Yes]
- [ ] **Lock 6 (Linguistic Hygiene)**: Zero banned marketing words ("seamlessly", "natively", "cleanly", "simply", "obviously", "phighting"); passive voice strictly under 10%. [Yes]
- [ ] **Lock 7 (Authorial Credibility)**: Grounded in the author's background as an Air Force officer, mechanical engineer, and multi-discipline martial artist without displaying credentials as an academic lectern. [Yes]
- [ ] **Lock 8 (Negative Blast Radius)**: Zero detailed taxonomy of the Four Ranges (Long, Medium, Close, Near reserved for Wave 2); zero weapon radius modifier analysis (reserved for Wave 3). [Yes]

---

### 3.1 Updated Style Guide Compliance Matrix (Fighter-First Mandates)
| Requirement | Implementation in Chapter 02 Wave 1 | Verification Method |
| :--- | :--- | :--- |
| **1. Lead sentence states usable rule** | Each subsection opens with an unequivocal tactical rule (e.g., *"Reach is only an advantage if you control the distance; inside an opponent's reach, long limbs become liabilities."*). | Code review of opening sentences in Beats 1–4. |
| **2. Plain-language mechanism first** | The spatial tax of long reach, the leverage vulnerability of tall frames, and the physical impossibility of throwing an elbow from four feet are explained with visceral mat metaphors before any technical abstraction. | Pre-draft beat outline audit. |
| **3. Formal physics in callouts/parentheticals** | Reach arc geometry and Hick's Law ($T = b \log_2(n+1)$) isolated entirely inside a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"). | Automated grep / AST scan ensuring 0 equations in main prose flow. |
| **4. Explicit Mat Test check** | Voice must pass the Mat Test: *Would a coach say this to a fighter between rounds?* If a line sounds like a classroom lecture, it must be rewritten into physical action cues. | Post-draft Mat Test audit prior to Gate 2 submission. |

---

### 4. Target Files
- **File to Create**:
  - `manuscript/part_01_foundations/ch02_the_four_ranges/01_relative_attributes_and_weapon_eligibility.md`
- **Harness & Verification Files to Update**:
  - `tests/code_examples/test_ch02_probes.py` (Create Section 2.1–2.2 probe suite for word count, banned words, passive voice, and conceptual invariants)
  - `.agent_context/MANUSCRIPT_REGISTER.md` (Update Chapter 02 status to `Gate 1 In Review`)

---

### 5. Pedagogical Beats Breakdown

#### Beat 1: The Myth of Absolute Attributes (The Reach Illusion)
- *Lead Rule*: Reach is only an advantage if you control the distance; inside your opponent's reach, long limbs become liabilities.
- *Tactical Reality*: The reach tax. A fighter with a 76-inch wingspan can hit from outside a 68-inch wingspan opponent's perimeter. But if the shorter fighter slips inside, the tall fighter's long levers cannot fold tightly enough to generate power, and their exposed ribs and jawline become open targets.
- *Mechanism*: Rotational clearance and joint articulation. Long limbs require expansive arcs to accelerate; crowding eliminates their operational runway.

#### Beat 2: Height, Mass, and Center-of-Gravity Inversion
- *Lead Rule*: A tall opponent owns the air; a grounded opponent owns the floor.
- *Tactical Reality*: Taller adversaries have elevated Centers of Mass (COM), making them top-heavy and vulnerable to trips, level changes, and sweeps. A compact fighter has a lower center of gravity, a tighter base of support, and natural leverage when driving under the hips.
- *Mechanism*: Inverted pendulum physics and moment arm length. The higher the mass, the longer the lever arm to topple it.

#### Beat 3: The Law of Weapon Eligibility in Action (Pruning the Threat Matrix)
- *Lead Rule*: You do not defend against every strike in the martial arts; you defend only against the weapons eligible at the current distance.
- *Tactical Reality*: How physical distance operates as an anatomical gatekeeper. At eight feet, you cannot be punched, elbowed, or knee-struck; the only eligible threats are lunging kicks or tackles. At one foot, roundhouse kicks and long straights are physically disabled.
- *Mechanism*: Anatomical joint envelopes and reach radii. Distance determines weapon eligibility before intent is expressed.

#### Beat 4: Hick's Law Inversion: Collapsing Reaction Latency
- *Lead Rule*: Control the distance to shrink your opponent's options, and your brain responds twice as fast.
- *Tactical Reality*: Untrained defenders freeze because they try to process fifty potential attacks simultaneously. By enforcing a specific distance, the defender prunes the threat matrix down to two or three eligible attacks, dramatically dropping cognitive processing time.
- *Callout Block*: `> [!NOTE]` — *The Mechanics Behind It: Anatomical Reach Envelopes and Hick's Law ($T = b \log_2(n+1)$)*.

#### Tactical Synthesis: The Rule of Relative Engagement
- *Lead Rule*: Never fight an opponent at their optimal range. Enforce your distance, prune their weapons, and force them to fight where their attributes become handicaps.
- *Synthesis*: Bridges relative attributes and threat filtering into the detailed range breakdown coming in Wave 2 (Long, Medium, Close, Near).

---

### 6. Verification Probes & Fact Checks
- **Designated Probe ID**: `[PROBE-CH02-W01-ATTRIBUTES-ELIGIBILITY]`
- **Verification Harness**: `tests/code_examples/test_ch02_probes.py`
  - Automated & Editorial assertions:
    1. Word count in bounds [1,100 – 1,700 words].
    2. Zero occurrences of banned words list (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`).
    3. Passive voice $< 10\%$.
    4. Required conceptual tokens present (`Relative Attributes`, `Reach Advantage`, `Law of Weapon Eligibility`, `Base of Support`, `Center of Mass`).
    5. **Mat Test Protocol**: Full prose read-aloud audit verifying that no paragraph reads like a whiteboard physics lecture; all mechanics grounded in coach-to-fighter cues before draft acceptance.
- **Citation Anchors**:
  - *Thalken (2015)*: Reach geometry, leverage, and center-of-mass mechanics in combat sports.
  - *Hick (1952) / Hyman (1953)*: Decision latency as a function of choice set size ($n$).
  - *Blair et al. (2011)*: Reaction time under threat stimulus.

---

### 7. Out of Scope (Negative Blast Radius)
- Will NOT detail the four specific combat ranges (Long, Medium, Close, Near) in depth—reserved strictly for Wave 2.
- Will NOT analyze impact weapon modifiers (bats, clubs, blades) or the Zero Distance spatial trade-off—reserved for Wave 3.
- Will NOT introduce grappling submissions or takedown finishes—reserved for Part IV.

---

### 8. Rollback Strategy
- Deterministic rollback command:
  ```powershell
  git checkout -- manuscript/part_01_foundations/ch02_the_four_ranges/01_relative_attributes_and_weapon_eligibility.md
  ```

---

### 🛑 EDITOR GATE 1 SUBMISSION
> **CRITICAL POLICY NOTICE**:  
> This plan is hereby submitted for Editor Review prior to drafting any narrative prose.  
> **NO PROSE DRAFTING PERMITTED BEFORE EDITOR GATE 1 APPROVAL.**
