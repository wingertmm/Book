# Authoring Section Implementation Plan: Chapter 07 — Wave 3

**Target Chapter & Wave**: `Chapter 07 - Wave 3: Section 7.3 (Economy of Force and Terrain Navigation: Walls, Curbs, and Corridors)`  
**Target Milestone**: `Part II: The Three Strategic Lenses (Sun Tzu, Airpower, and Ground Maneuver) — COMPLETE`  
**Status**: `GATE 1: SUBMITTED FOR REVIEW`  

---

### 1. Goal & Pedagogical Intent
Complete **The Ground Maneuver Lens** and conclude **Part II: The Three Strategic Lenses** by translating military infantry doctrine on terrain appreciation, restrictive corridors, and the Principle of War—**Economy of Force** (codified in U.S. Army FM 3-0 *Operations*, TC 3-25.150 *Combatives*) into personal survival on urban concrete. Demonstrate how an experienced combatives practitioner actively weaponizes urban architectural features—masonry walls, curb ledges, parked vehicles, and narrow corridors—rather than viewing them as accidental hazards.

Analyze the tactical mechanics of **Terrain Navigation**:
1. **The Wall as Weapon and Structural Anchor**: Contrast the catastrophic hazard of getting pinned with your back to a wall against the dominant tactic of pinning an adversary against masonry ($F_N \to \infty$) to eliminate their translational degrees of freedom and nullify rotational power.
2. **Micro-Terrain and Curb Dynamics**: Detail the mechanics of curb ledges, showing how backward steps over a six-inch drop cause sudden postural perturbation, and how an offline step weaponizes the curb behind an opponent into a rotational tipping fulcrum.
3. **Urban Fatal Funnels and Corridor Navigation**: Apply small-unit infantry movement doctrine to narrow alleys and hallways, using environmental bottlenecks to funnel multiple threats into sequential single-file engagements.
4. **Economy of Force & The Asymmetric Limb Ratio (TRIZ Principle 6)**: Define Economy of Force as metabolic resource conservation. Introduce Altshuller's TRIZ Principle 6 (*Universality / Multifunctionality*) to combat geometry: using a single structural skeletal frame or wall post to simultaneously control multiple degrees of freedom, achieving an **Asymmetric Limb Ratio** (1-on-2 or 1-on-3 control) that preserves free tools for striking or disengagement.
5. **Part II Capstone**: Unify the Three Strategic Lenses—Sun Tzu’s Classical Deception, Boyd’s Airpower Energy-Maneuverability, and Terrestrial Ground Maneuver—under the **Master Equation: Distance $\to$ Time $\to$ Power**, establishing the launchpad for **Part III: The 11 Unified Principles**.

Deliver this under the **Fighter-First, Engineer-Backed** standard: lead every beat with coach-level decision rules, explain physical mechanisms in visceral language before introducing models, isolate obstacle mechanics, degrees of freedom constraints, and normal reaction forces in a dedicated callout block, and enforce the Mat Test.

---

### 2. Learning Objective & Concept Binding
- **Objective ID**: `OBJ-CH07-003`
- **Target Concepts Introduced**:
  - *Economy of Force*: Principle 6 of the 11 Unified Principles; conserving metabolic reserves and structural energy on secondary threats to ensure decisive force is available for the primary objective or exit.
  - *Terrain Navigation*: Actively reading and exploiting micro-terrain, vertical drops, environmental barriers, and structural geometry in close-quarters combat.
  - *The Asymmetric Limb Ratio*: The tactical mathematics of limb commitment wherein one defensive limb or skeletal anchor immobilizes two or more of an opponent's limbs or movement axes (TRIZ Principle 6).
  - *Urban Fatal Funnel*: Restricting engagement geography through narrow corridors, doorways, or obstacles to stack multiple attackers into sequential 1-on-1 fights.
  - *Degrees of Freedom (DOF) Constraint*: Using unyielding environmental structures (masonry walls, ground) to reduce an opponent's translational and rotational movement axes from six down to near zero.
  - *Part II Capstone & The Strategic Triad*: The unified synthesis of Sun Tzu (Strategic Philosophy), Boyd (Cognitive & Aerial Tempo), and Ground Maneuver (Terrestrial Anchoring).
- **Forward Pointers**:
  - Completes Part II: The Three Strategic Lenses.
  - Direct bridge to Part III: The 11 Unified Principles (Chapter 08: Principles 1–3: Purpose First, Security of Position, Maneuver to Advantage).
  - Connects to Part IV (Chapter 16: Range Transitions in Confined Terrain) and Part VI (Chapter 20: Environmental Weapons and Asymmetric Tactics).

---

### 3. Invariant Locks (Mandatory Constraints)
- [ ] **Lock 1 (Fighter-First Delivery)**: Every major subsection must open with a direct, usable tactical rule and concrete consequence before introducing infantry doctrine or physics.
- [ ] **Lock 2 (Action Precedes Math / Physics)**: Normal reaction forces ($F_N$), degrees of freedom state matrices ($\Delta \text{DOF}$), curb tipping torques ($\tau_{\text{curb}} = m g d + m a h$), and metabolic power burn rates must reside in dedicated `> [!NOTE]` callouts ("The Mechanics Behind It")—never in the primary narrative flow.
- [ ] **Lock 3 (The Mat Test Compliance)**: The prose must pass the Mat Test: read like a seasoned coach instructing a fighter between rounds, avoiding academic lectures or detached tactical manual recitations.
- [ ] **Lock 4 (Terminology Fidelity)**: All technical terms (Economy of Force, Terrain Navigation, Asymmetric Limb Ratio, Urban Fatal Funnel, Degrees of Freedom, The Three Strategic Lenses, Master Equation) must match [CONCEPT_REGISTER.md](file:///c:/Book/.agent_context/CONCEPT_REGISTER.md) and [GLOSSARY.md](file:///c:/Book/.agent_context/GLOSSARY.md) exactly.
- [ ] **Lock 5 (Word Count Budget)**: Target is 1,400 – 1,750 words (hard ceiling: 1,800 words).
- [ ] **Lock 6 (Linguistic Hygiene)**: Zero banned marketing words ("seamlessly", "natively", "cleanly", "simply", "obviously", "phighting"); passive voice strictly under 10%.
- [ ] **Lock 7: Authorial Credibility**: Grounded in the author's background as an Air Force officer, engineer, and combatives coach without turning into an infantry field manual.
- [ ] **Lock 8: Negative Blast Radius**: Zero deep dive into Part III principles (Purpose First, Initiative, Concentration, Surprise, Avoidance, Persistence) beyond Principle 2, 3, and 6; zero style-specific move catalogs (reserved for Part IV).

---

### 3.1 Style Guide Compliance Matrix (Fighter-First Mandates)
| Requirement | Implementation in Chapter 07 Wave 3 | Verification Method |
| :--- | :--- | :--- |
| **1. Lead sentence states usable rule** | Each subsection opens with an unequivocal tactical rule (e.g., *"Never fight in an environmental vacuum; use masonry and obstacles to do the structural work your muscles cannot sustain."*). | Code review of opening sentences in Beats 1–6. |
| **2. Plain-language mechanism first** | Walls, curb drops, narrow alleys, limb trapping, and metabolic fatigue explained through visceral street realities before formulas. | Pre-draft beat outline audit. |
| **3. Formal physics in callouts** | Normal reaction forces ($F_N$), curb rotational torque ($\tau_{\text{curb}}$), and DOF constraint matrices isolated entirely in `> [!NOTE]` callout block ("The Mechanics Behind It"). | Automated grep / AST scan ensuring 0 equations in main prose flow. |
| **4. Explicit Mat Test check** | Voice must pass the Mat Test: *Would a coach say this to a fighter between rounds?* If a line sounds like an academic paper, it must be rewritten into physical coaching cues. | Post-draft Mat Test audit prior to Gate 2 submission. |

---

### 4. Target Files
- **File to Create**:
  - `manuscript/part_02_strategic_lenses/ch07_the_ground_maneuver_lens/03_economy_of_force_and_terrain.md`
- **Harness & Verification Files to Create / Update**:
  - `tests/code_examples/test_ch07_probes.py` (Add Wave 3 probe suite for word count, banned words, passive voice, and conceptual invariants)
  - `.agent_context/MANUSCRIPT_REGISTER.md` (Update Chapter 07 Wave 3 tracking)

---

### 5. Detailed Beat Outline (Section 7.3)

#### Beat 1: Terrain Appreciation: Concrete Is Not a Canvas
- **Lead Rule**: Never fight as if you are on an empty mat; the physical environment dictates your survival options before the first punch flies.
- **Narrative**:
  - Military infantry doctrine on terrain appreciation (OCOKA: Observation, Cover, Obstacles, Key Terrain, Avenues of Approach).
  - Combat reality on concrete: Studio martial artists train on open, flat, padded canvas with zero boundaries. Street violence unfolds in restricted geometries: between parked cars, against brick walls, across fractured curbs, and down narrow corridors. 
  - The fighter who ignores terrain gets pinned, tripped, or cornered. The fighter who reads terrain uses the environment to multiply force and conserve energy.

#### Beat 2: Obstacle Weaponization: Walls, Curbs, and Corridors
- **Lead Rule**: Never let an obstacle sit at your back; maneuver to put the barrier behind the attacker.
- **Narrative**:
  - The Wall Hazard vs. Wall Weapon: Getting driven backward into a wall eliminates your reactionary buffer and pins your head. But driving the adversary into a wall forces an inelastic impact, robs them of retreating space, and immobilizes their hips.
  - Micro-Terrain and Curbs: Backpedaling over a curb ledge drops your heel six inches, pitching your center of mass backward into an unrecoverable fall. Stepping offline positions that same curb behind the charging attacker, weaponizing urban geometry into a tripwire.
  - Urban Fatal Funnels: How narrow alleys, parked cars, or doorways funnel multiple attackers into sequential single-file engagements, preventing lateral envelopment.

#### Beat 3: Economy of Force: The Asymmetric Limb Ratio (TRIZ Principle 6)
- **Lead Rule**: Never commit two limbs to control one of the attacker's; use structural wedges to achieve an asymmetric surplus in free weapons.
- **Narrative**:
  - Principle 6: Economy of Force. In combat, muscular exertion burns finite anaerobic glycogen. Prolonged wrestling or flailing drains your cardiovascular reservoir.
  - TRIZ Principle 6 (Universality / Multifunctionality): In engineering, make one component perform multiple functions. In combat, make one skeletal frame or environmental pin control multiple degrees of freedom.
  - The Limb Economy: Committing both hands to control an attacker's wrist leaves you at a 2-vs-3 deficit. Using a forearm wedge against their jaw while pinning their shoulder to a wall achieves 1-on-2 or 1-on-3 dominance, leaving your secondary arm free to deliver force or manipulate exit doors.

#### Beat 4: Callout Block: Obstacle Mechanics, Degrees of Freedom, and Normal Reaction Forces
- **Mechanical & Mathematical Details** (`> [!NOTE]` callout):
  1. *Normal Reaction Forces on Inelastic Barriers*: Normal reaction force $F_N \le \infty$ from rigid masonry absorbs kinetic energy ($\Delta E_k = \frac{1}{2} m v^2$), enforcing boundary condition $x_{\text{barrier}} = 0$.
  2. *Constraint of Degrees of Freedom*: A free body possesses 6 DOF (3 translational, 3 rotational). Contact with an orthogonal corner reduces DOF to zero ($DOF = 6 - 6 = 0$), completely immobilizing the adversary without ongoing muscular energy.
  3. *Curb Tipping Torque*: Rotational overturning moment over curb edge height $h_{\text{curb}}$: $\tau_{\text{curb}} = m g d + m a_{\text{linear}} h_{\text{curb}}$. Tipping acceleration $\alpha = \frac{\tau_{\text{curb}}}{I_z}$ creates rapid postural collapse.
  4. *Metabolic Power of Skeletal Framing*: Metabolic power expenditure $P_{\text{metabolic}} = \sigma \cdot v$. For bone-to-barrier skeletal frames, strain velocity $v \approx 0$, yielding near-zero metabolic consumption compared to active isometric muscular clamping.

#### Beat 5: Part II Capstone: The Triad of Strategic Lenses
- **Lead Rule**: Combine ancient wisdom, aerospace energy, and terrestrial maneuver into a single operating system; no single lens solves the total fight.
- **Narrative**:
  - The Synthesis of Part II:
    1. *The Sun Tzu Lens (Chapter 05)*: The strategic foundation—purpose over ego, pre-calculation, winning before striking, refusing the centerline, and deceptive shaping.
    2. *The Airpower Lens (Chapter 06)*: The tempo engine—Boyd's Energy-Maneuverability, fast transients, orientation disruption in microseconds, and vertical 3D warfare.
    3. *The Ground Maneuver Lens (Chapter 07)*: The physical anchor—offline angular footwork, flanking envelopment, security of position, convex tactics, and terrain navigation.
  - Unifying the Three Lenses under the Master Equation (**Distance $\to$ Time $\to$ Power**).

#### Beat 6: Transition to Part III: The 11 Unified Principles
- **Lead Rule**: Theory without operational principles is useless; operational principles without biomechanical execution are dead.
- **Narrative**:
  - Having established the Master Filter (Part I) and the Strategic Lenses (Part II), the combatant requires actionable decision rules for the chaotic instant of contact.
  - Direct bridge to **Part III: The 11 Unified Principles of Personal Defense** (Chapter 08: Principles 1–3: Purpose First, Security of Position, and Maneuver to Advantage).

---

### 6. Verification Probes & Fact Checks
- **Designated Code Probe ID**: `[PROBE-CH07-W03-ECONOMY-TERRAIN]`
- **Probe Test Location**: `tests/code_examples/test_ch07_probes.py`
- **Probe Test Suite**:
  1. `test_ch07_w03_file_exists`: Validates existence of manuscript file.
  2. `test_ch07_w03_word_count_within_budget`: Asserts word count is between 1,300 and 1,800 words.
  3. `test_ch07_w03_zero_banned_marketing_words`: Asserts 0 occurrences of banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`).
  4. `test_ch07_w03_mandatory_concepts_present`: Validates presence of:
     - `Economy of Force`
     - `Terrain Navigation`
     - `Asymmetric Limb Ratio`
     - `Degrees of Freedom` (or `Normal Force`)
     - `Part II Capstone` (or `The Three Strategic Lenses`)
     - `Master Equation`
- **Primary Source / Fact Check Index**:
  - Headquarters, Department of the Army (2017) *Field Manual 3-0 (FM 3-0): Operations*.
  - Headquarters, Department of the Army (2012) *Training Circular 3-25.150 (TC 3-25.150): Combatives*.
  - Altshuller, G. (1984) *Creativity as an Exact Science: The Theory of the Solution of Inventive Problems (TRIZ)*, Gordon and Breach.
  - Hall, S. J. (2018) *Basic Biomechanics*, McGraw-Hill.
  - Morris, M. (1993) *The Science of Striking and Maneuver in Martial Combatives*.

---

### 7. Out of Scope (Negative Blast Radius)
- **Strictly Excluded from this Wave**:
  - *Part III Material*: Detailed exploration of Principle 1 (Purpose First), Principle 4 (Initiative), Principle 5 (Concentration), Principle 7 (Surprise), Principle 8 (Avoidance), Principle 9 (Persistence), Principle 10 (Actions on Contact), and Principle 11 (Proportionality) — strictly reserved for Chapters 08–11.
  - *Part IV Material*: Style-specific combo execution (specific wrestling pins, judo throws, or BJJ submissions).

---

### 8. Rollback Strategy
- Deterministic rollback command:
  ```bash
  git checkout -- manuscript/part_02_strategic_lenses/ch07_the_ground_maneuver_lens/03_economy_of_force_and_terrain.md
  git checkout -- tests/code_examples/test_ch07_probes.py
  ```

---

### 🛑 EDITOR GATE 1 SUBMISSION
> **CRITICAL POLICY NOTICE**:  
> This plan is hereby submitted for Editor Review prior to drafting any narrative prose or publishing any text.  
> **NO PROSE DRAFTING PERMITTED BEFORE EDITOR GATE 1 APPROVAL.**
