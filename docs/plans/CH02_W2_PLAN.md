# Authoring Section Implementation Plan: Chapter 02 — Wave 2

**Target Chapter & Wave**: `Chapter 02 - Wave 2: Sections 2.3–2.6 (The Four Combat Ranges: Long, Medium, Close, and Near)`  
**Target Milestone**: `Part I: The Master Filter (The Physics & Philosophy of Force)`  
**Status**: `GATE 1: SUBMITTED FOR REVIEW`  

---

### 1. Goal & Pedagogical Intent
Provide a definitive, fighter-first operational breakdown of the **Four Combat Ranges**: Long Distance (kicks/avoidance), Medium Distance (fists/striking), Close Distance (elbows/knees/head control), and Near Distance (clinch/grappling/zero-distance jamming). Deconstruct each range through the lens of weapon eligibility, operational runway, reaction latency, and tactical failure modes. Execute under the **Fighter-First, Engineer-Backed** standard: lead with coach-level decision rules, explain physical mechanisms in visceral language before introducing any models, sequester formal mechanics into dedicated callout blocks, and enforce the Mat Test.

---

### 2. Learning Objective & Concept Binding
- **Objective ID**: `OBJ-CH02-002`
- **Target Concepts Introduced**:
  - *The Four Combat Ranges*: The distinct spatial zones governing human combat, each with unique weapon eligibility rules, cognitive loads, and survivability profiles.
  - *Range 1: Long Distance (Outside Perimeter)*: Space beyond physical contact (> 6–7 feet); the only range where escape and de-escalation are physically possible without an exchange of force; maximum reaction time.
  - *Range 2: Medium Distance (The Fist Pocket)*: Arm's length (3–5 feet); the highest-casualty zone where strikes achieve terminal velocity; the pocket where untrained combatants freeze and trade blunt-force trauma.
  - *Range 3: Close Distance (Infighting & Framing)*: Elbow and knee distance (1–2 feet); rotational leverage and short-arc impact; long punches and kicks are bio-mechanically jammed; head and neck posture control dominate.
  - *Range 4: Near Distance (The Zero-Distance Jam)*: Chest-to-chest, body-to-body contact (< 1 foot); striking runways are eliminated ($W = F \times d \to 0$); combat transitions into pure structural leverage, underhooks, base of support, and centerline control.
  - *Rotational Clearance & Operational Runway*: The physical arc required for an anatomical limb to accelerate; jamming eliminates runway.
- **Forward Pointers**:
  - Connects to Chapter 02 Wave 3 (Weapon Radius Modifiers, Zero Distance Spatial Trade-off, and The Transition Gap).
  - Connects to Part IV (Range-specific style translations: TKD for Long, Muay Thai for Close, Wrestling/BJJ for Near).

---

### 3. Invariant Locks (Mandatory Constraints)
- [ ] **Lock 1 (Fighter-First Delivery)**: Every major subsection must open with a direct, usable tactical rule and concrete consequence before introducing any physical or anatomical mechanics. [Yes]
- [ ] **Lock 2 (Action Precedes Math)**: All mechanical formulas (kinetic energy arcs, impulse, moment arms $\tau = r \times F$) must reside in dedicated `> [!NOTE]` callouts ("The Mechanics Behind It") or concise parentheticals—never in the primary prose narrative. [Yes]
- [ ] **Lock 3 (The Mat Test Compliance)**: The prose must pass the Mat Test: read like a seasoned coach explaining realities between rounds, avoiding dry academic or classroom pedantry. [Yes]
- [ ] **Lock 4 (Terminology Fidelity)**: All technical terms (Long Distance, Medium Distance, Close Distance, Near Distance, Jamming, Rotational Clearance, Base of Support) must match [CONCEPT_REGISTER.md](file:///c:/Book/.agent_context/CONCEPT_REGISTER.md) and [GLOSSARY.md](file:///c:/Book/.agent_context/GLOSSARY.md) exactly. [Yes]
- [ ] **Lock 5 (Word Count Budget)**: Target is 1,400 – 1,700 words (hard ceiling: 1,900 words). [Yes]
- [ ] **Lock 6 (Linguistic Hygiene)**: Zero banned marketing words ("seamlessly", "natively", "cleanly", "simply", "obviously", "phighting"); passive voice strictly under 10%. [Yes]
- [ ] **Lock 7 (Authorial Credibility)**: Grounded in the author's background as an Air Force officer, mechanical engineer, and multi-discipline martial artist without displaying credentials as an academic lectern. [Yes]
- [ ] **Lock 8 (Negative Blast Radius)**: Zero impact weapon modifier analysis (reserved for Wave 3); zero detailed ground grappling submission mechanics (reserved for Chapter 15). [Yes]

---

### 3.1 Updated Style Guide Compliance Matrix (Fighter-First Mandates)
| Requirement | Implementation in Chapter 02 Wave 2 | Verification Method |
| :--- | :--- | :--- |
| **1. Lead sentence states usable rule** | Each subsection opens with an unequivocal tactical rule (e.g., *"Long distance is the only range where you can escape without exchanging blood; surrender it only if you have a decisive reason to close."*). | Code review of opening sentences in Beats 1–4. |
| **2. Plain-language mechanism first** | The spatial tax of standing in the pocket, head control breaking spinal alignment in the clinch, and chest-to-chest underhook battles are explained with visceral mat metaphors before any technical abstraction. | Pre-draft beat outline audit. |
| **3. Formal physics in callouts/parentheticals** | Kinetic arc acceleration and torque mechanics isolated entirely inside a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"). | Automated grep / AST scan ensuring 0 equations in main prose flow. |
| **4. Explicit Mat Test check** | Voice must pass the Mat Test: *Would a coach say this to a fighter between rounds?* If a line sounds like a classroom lecture, it must be rewritten into physical action cues. | Post-draft Mat Test audit prior to Gate 2 submission. |

---

### 4. Target Files
- **File to Create**:
  - `manuscript/part_01_foundations/ch02_the_four_ranges/02_the_four_combat_ranges.md`
- **Harness & Verification Files to Update**:
  - `tests/code_examples/test_ch02_probes.py` (Add Wave 2 probe suite for word count, banned words, passive voice, and conceptual invariants)
  - `.agent_context/MANUSCRIPT_REGISTER.md` (Update Chapter 02 Wave 2 tracking)

---

### 5. Pedagogical Beats Breakdown

#### Beat 1: Range 1 — Long Distance (The Avoidance & Reaction Zone)
- *Lead Rule*: Long distance is the only range where you can escape without exchanging blood; surrender it only if you have a decisive reason to close.
- *Tactical Reality*: Outside physical contact (> 6–7 feet). Why this is the safest range: reaction time is maximized, cognitive panic drops, and escape paths remain open.
- *Mechanism*: An attacker must cross open space to strike, converting an ambush into an observable closing trajectory that can be intercepted or evaded.

#### Beat 2: Range 2 — Medium Distance (The High-Casualty Pocket)
- *Lead Rule*: Medium distance is where people take the most damage; never stand toe-to-toe in the pocket unless you possess the angle and the initiative.
- *Tactical Reality*: Arm's length (3–5 feet). The classic boxing and brawling range where straight punches and hooks reach maximum acceleration. Why untrained fighters freeze here.
- *Mechanism*: This range maximizes kinetic energy transfer ($E_k = \frac{1}{2}mv^2$) because limbs reach peak velocity right at the point of impact. The defender must not linger: either expand back to Long Distance or crash forward into Range 4.
- *Callout Block*: `> [!NOTE]` — *The Mechanics Behind It: Kinetic Arc Acceleration and the High-Casualty Zone*.

#### Beat 3: Range 3 — Close Distance (Infighting & Neck Control)
- *Lead Rule*: When space collapses to elbow range, posture control replaces punching speed; whoever controls the head and neck controls the fight.
- *Tactical Reality*: 1–2 feet away. Long punches and kicks are bio-mechanically disabled because limbs run out of extension runway. Elbows, inside knees, and collar ties dominate.
- *Mechanism*: Cervical spine manipulation. Pulling the head down bends the spine, breaking the adversary's base and destroying their ability to generate rotational power.

#### Beat 4: Range 4 — Near Distance (The Zero-Distance Jam & Clinch)
- *Lead Rule*: At chest-to-chest range, strikes lose their runway; you do not trade blows, you fight for underhooks, base, and balance.
- *Tactical Reality*: Body-to-body contact (< 1 foot). The grappling, clinch, and takedown domain. All strikes are smothered into muffled bumps.
- *Mechanism*: Jamming rotational clearance. Without distance, kinetic work drops to zero. Control depends on pummeling for underhooks, establishing a dominant head position, and driving hips below the opponent's Center of Mass.

#### Tactical Synthesis: The Spatial Dial & Dynamic Transitions
- *Lead Rule*: Combat mastery is knowing where you stand on the spatial dial and forcing the adversary into the range where their tools become useless.
- *Synthesis*: Maps the Four Ranges into an interconnected progression, setting up Wave 3's analysis of impact weapons and the Transition Gap.

---

### 6. Verification Probes & Fact Checks
- **Designated Probe ID**: `[PROBE-CH02-W02-FOUR-RANGES]`
- **Verification Harness**: `tests/code_examples/test_ch02_probes.py`
  - Automated & Editorial assertions:
    1. Word count in bounds [1,300 – 1,900 words].
    2. Zero occurrences of banned words list (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`).
    3. Passive voice $< 10\%$.
    4. Required conceptual tokens present (`Long Distance`, `Medium Distance`, `Close Distance`, `Near Distance`, `Jamming`, `Rotational Clearance`).
    5. **Mat Test Protocol**: Full prose read-aloud audit verifying that no paragraph reads like a whiteboard physics lecture; all mechanics grounded in coach-to-fighter cues before draft acceptance.
- **Citation Anchors**:
  - *Lee (1975)*: The four ranges of combat in martial systems.
  - *Thalken (2015)*: Kinetic energy and impulse across striking arcs.
  - *FM 3-0 / Boyd (1987)*: Spatial compression and tempo control.

---

### 7. Out of Scope (Negative Blast Radius)
- Will NOT analyze impact weapon modifiers (bats, clubs, blades) or weapon perimeters—reserved strictly for Wave 3.
- Will NOT detail the Spatial Trade-Off or Transition Gap mechanics—reserved strictly for Wave 3.
- Will NOT catalog specific style-by-style range techniques (TKD vs. Muay Thai vs. BJJ)—reserved for Part IV.

---

### 8. Rollback Strategy
- Deterministic rollback command:
  ```powershell
  git checkout -- manuscript/part_01_foundations/ch02_the_four_ranges/02_the_four_combat_ranges.md
  ```

---

### 🛑 EDITOR GATE 1 SUBMISSION
> **CRITICAL POLICY NOTICE**:  
> This plan is hereby submitted for Editor Review prior to drafting any narrative prose.  
> **NO PROSE DRAFTING PERMITTED BEFORE EDITOR GATE 1 APPROVAL.**
