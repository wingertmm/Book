# Authoring Section Implementation Plan: Chapter 05 — Wave 2

**Target Chapter & Wave**: `Chapter 05 - Wave 2: Section 5.2 (Avoid Strength, Strike Weakness: Refusing the Centerline)`  
**Target Milestone**: `Part II: The Three Strategic Lenses (Sun Tzu, Airpower, and Ground Maneuver)`  
**Status**: `FROZEN (DONE)`  

---

### 1. Goal & Pedagogical Intent
Translate Sun Tzu’s doctrine of avoiding strength and striking weakness (*"Military disposition has no constant form, just as water has no constant shape... avoid what is strong and strike what is weak"*) into physical geometry and combative decision rules when avoidance is physically denied. Expose the deadly mechanical trap of the **Centerline Hazard**: meeting an attacker's charge along their primary sagittal vector creates a symmetric collision where superior mass, reach, and raw force prevail. Establish **Refusing the Centerline** and **Angular Flanking** as the foundational maneuver doctrine of personal defense. Explain why linear backward retreat fails (an attacker charging forward moves faster than a defender backpedaling; linear retreat ends in walls, tripping, or absorbing maximum kinetic drive). Demonstrate how a 30°–45° angular pivot exploits human **Rotational Inertia** and **Vector Decomposition**, forcing the attacker's heavy mass to decelerate and pivot while opening their unguarded flank (ribs, jawline, kidney, base of support). Deliver this under the **Fighter-First, Engineer-Backed** standard: lead every beat with coach-level decision rules, explain physical mechanisms in visceral language before introducing models, isolate vector decomposition and moment of inertia formulas in a dedicated callout block, and enforce the Mat Test.

---

### 2. Learning Objective & Concept Binding
- **Objective ID**: `OBJ-CH05-002`
- **Target Concepts Introduced**:
  - *Avoid Strength, Strike Weakness*: Sun Tzu’s core operational doctrine applied to physical geometry: never contest an adversary’s fortified mass head-on; bypass their structural strength to deliver focused force into unprotected anatomical targets.
  - *The Centerline Hazard*: The sagittal plane passing through the center of an aggressor’s body carries their maximum driving mass, forward momentum, and primary striking tools. Clashing along this line turns combat into an athletic contest of brute mass and durability.
  - *Refusing the Centerline*: The tactical decision to vacate the attacker's line of force through lateral and angular movement rather than absorbing or trading strikes along their axis of commitment.
  - *The Fallacy of Linear Retreat*: Why backing up in a straight line fails against an aggressive charge: forward locomotion is mechanically faster than backpedaling, and straight-line retreat preserves the attacker's targeting solutions until the defender hits an obstacle or trips.
  - *Angular Flanking (The 30°–45° Corridor)*: Stepping or pivoting off the primary line of attack into an oblique corridor where the defender can bear with two hands while the attacker’s weapons and balance are turned away.
  - *Rotational Inertia & Vector Decomposition*: The physical constraints that prevent a charging human body from instantly turning. To track an angular target, the attacker must apply lateral ground friction to arrest forward linear momentum and rotate their torso about their vertical axis, inducing a 200–300 ms motor delay.
- **Forward Pointers**:
  - Builds directly upon Wave 1 (Subduing Without Fighting), advancing the doctrine from pre-incident avoidance to kinetic engagement when force is forced as the residual option.
  - Connects directly to Part III (Principle 2: Security of Position, Principle 3: Maneuver to Advantage, and Principle 5: Concentration of Power).
  - Bridges to Section 5.3 (Deception, Unorthodox Force [$qi / zheng$], and Terrain Classification) when setting ambushes and shaping opponent expectations.

---

### 3. Invariant Locks (Mandatory Constraints)
- [ ] **Lock 1 (Fighter-First Delivery)**: Every major subsection must open with a direct, usable tactical rule and concrete consequence before introducing physics or military strategy.
- [ ] **Lock 2 (Action Precedes Math / Physics)**: All vector decomposition equations ($\vec{p} = m \vec{v}$, $F_{\text{lateral}} = m \frac{d\vec{v}_{\perp}}{dt}$) and rotational inertia formulations ($I = \sum m_i r_i^2$, $\tau = I \alpha$) must reside in dedicated `> [!NOTE]` callouts ("The Mechanics Behind It")—never in the primary narrative flow.
- [ ] **Lock 3 (The Mat Test Compliance)**: The prose must pass the Mat Test: read like a seasoned coach instructing a fighter between rounds, avoiding academic geometry lecturing or style-specific move lists.
- [ ] **Lock 4 (Terminology Fidelity)**: All technical terms (Avoid Strength Strike Weakness, The Centerline, Refusing the Centerline, Angular Flanking, Linear Retreat, Rotational Inertia, Vector Decomposition) must match [CONCEPT_REGISTER.md](file:///c:/Book/.agent_context/CONCEPT_REGISTER.md) and [GLOSSARY.md](file:///c:/Book/.agent_context/GLOSSARY.md) exactly.
- [ ] **Lock 5 (Word Count Budget)**: Target is 1,400 – 1,700 words (hard ceiling: 1,800 words).
- [ ] **Lock 6 (Linguistic Hygiene)**: Zero banned marketing words ("seamlessly", "natively", "cleanly", "simply", "obviously", "phighting"); passive voice strictly under 10%.
- [ ] **Lock 7 (Authorial Credibility)**: Grounded in the author's background as an Air Force officer, engineer, wrestling coach, and multi-discipline martial artist without converting the text into an abstract historical treatise.
- [ ] **Lock 8 (Negative Blast Radius)**: Zero discussion of orthodox vs. unorthodox force ($qi / zheng$) or deceptive ambush/Nine Terrains taxonomy (reserved for Wave 3, Section 5.3); zero Airpower doctrine or Boyd EM theory (reserved for Chapter 06); zero style-specific technique catalogs (reserved for Part IV).

---

### 3.1 Style Guide Compliance Matrix (Fighter-First Mandates)
| Requirement | Implementation in Chapter 05 Wave 2 | Verification Method |
| :--- | :--- | :--- |
| **1. Lead sentence states usable rule** | Each subsection opens with an unequivocal tactical rule (e.g., *"Never contest an attacker's force along their line of commitment; step off the centerline to nullify their mass and strike their unguarded flank."*). | Code review of opening sentences in Beats 1–5. |
| **2. Plain-language mechanism first** | Head-on collisions, backpedaling failure, angular pivots, and exposed ribs/jawline explained with visceral realities before any physics equations. | Pre-draft beat outline audit. |
| **3. Formal physics in callouts** | Vector decomposition and moment of inertia formulas isolated entirely inside a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"). | Automated grep / AST scan ensuring 0 equations in main prose flow. |
| **4. Explicit Mat Test check** | Voice must pass the Mat Test: *Would a coach say this to a fighter between rounds?* If a line sounds like a math lecture or kata textbook, it must be rewritten into physical coaching cues. | Post-draft Mat Test audit prior to Gate 2 submission. |

---

### 4. Target Files
- **File to Create**:
  - `manuscript/part_02_strategic_lenses/ch05_the_sun_tzu_lens/02_avoid_strength_strike_weakness.md`
- **Harness & Verification Files to Update**:
  - `tests/code_examples/test_ch05_probes.py` (Register Wave 2 probe suite for word count, banned words, passive voice, and conceptual invariants)
  - `.agent_context/MANUSCRIPT_REGISTER.md` (Update Chapter 05 Wave 2 tracking)

---

### 5. Pedagogical Beats Breakdown

#### Beat 1: The Centerline Hazard (Why Head-On Collisions Favor the Predator)
- **Lead Rule**: *Never contest an attacker along their line of commitment; meeting force with force turns combat into a coin toss where the heavier mass wins.*
- **Core Narrative**:
  - Dissecting the catastrophic instinct of squaring up and trading blows along the centerline.
  - The anatomy of the centerline: It is the sagittal plane containing the adversary's primary mass (chest, pelvis, hips), driving legs, and forward momentum.
  - Why predators charge along the centerline: Aggressors rely on superior weight, forward aggression, and raw kinetic output. When a defender stands on that line, they validate the attacker's physical advantages.
  - Symmetrical collisions: In a head-on collision, kinetic force transfers proportionally to mass. If you weigh 160 pounds and contest a 220-pound attacker head-on, you enter an exchange where their structural momentum overpowers your resistance, even if your technical form is sound.

#### Beat 2: The Fallacy of Linear Retreat (The Backpedal Trap)
- **Lead Rule**: *Do not backpedal in a straight line to escape an incoming charge; human biomechanics make forward sprinting faster than backward retreat.*
- **Core Narrative**:
  - The instinctive human fear reaction: When an attacker rushes, the untrained defender steps straight backward.
  - Locomotion mechanics: Forward locomotion engages the powerful posterior chain (glutes, hamstrings, gastrocnemius) in extension with full visual tracking. Backward locomotion relies on awkward quadricep pushes and toe-reaching, cutting speed by nearly 40%.
  - The environmental trap: Backpedaling on pavement leads to disaster: curbs, parking blocks, furniture, curbside garbage, or walls. The moment your heels contact an obstacle, your center of mass continues backward, resulting in an unbraced fall.
  - Preserving the attacker's targeting solution: By retreating in a straight line, you keep yourself squarely inside their crosshairs, allowing them to accelerate into maximum punch power at full arm extension.

#### Beat 3: Refusing the Centerline & Angular Flanking
- **Lead Rule**: *Step off the line of fire at a sharp angle; forcing an attacker to turn their hips neutralizes their forward power and exposes their vulnerabilities.*
- **Core Narrative**:
  - Translating Sun Tzu’s water metaphor into footwork: *"Water shapes its course according to the nature of the ground over which it flows; the soldier works out his victory in relation to the foe whom he is facing."*
  - The mechanics of the angular slip and pivot: Instead of absorbing or backpedaling, the defender plants the lead foot slightly outside the attacker's lead foot and pivots at a 30° to 45° angle.
  - Breaking the attacker's alignment: The attacker's forward drive continues into empty air. To re-acquire the target, they must arrest their forward linear momentum, rotate their torso, and reset their feet.
  - The tactical jackpot of the flank: You occupy an asymmetric positional advantage. You stand outside their primary weapon arcs (their rear cross cannot bear without total body rotation; their lead shoulder blocks their own hook). Meanwhile, their jaw, carotid artery, floating ribs, and rear kidney are completely exposed along your centerline. You strike "emptiness" while bypassing their strength.

#### Beat 4: Physics & Biomechanical Modeling (The Mechanics Behind It)
- **Isolated Callout (`> [!NOTE]`)**:
  - *Title*: `The Mechanics Behind It: Vector Decomposition, Linear Momentum, and Rotational Inertia in Angular Maneuver`
  - *Content*:
    - **Vector Decomposition of Forward Momentum**:
      An attacker charging forward carries linear momentum:
      $$\vec{p} = m \cdot \vec{v}$$
      When you step offline at an angle $\theta$ (typically $30^\circ \le \theta \le 45^\circ$), their kinetic energy continues along the original trajectory vector $\vec{v}_{\parallel}$. To redirect toward you, their cleats/shoes must generate lateral friction force against the pavement:
      $$F_{\text{lateral}} = m \frac{d\vec{v}_{\perp}}{dt} \le \mu \cdot m \cdot g$$
      If lateral force exceeds the frictional limit ($\mu \cdot m \cdot g$), the attacker slips or stumbles.
    - **Rotational Inertia About the Vertical Axis**:
      The resistance of the human body to sudden axial rotation is governed by moment of inertia:
      $$I_z = \sum_{i=1}^{n} m_i r_i^2$$
      With committed forward stride and arms extended, $I_z$ is maximized. Turning requires applying torque:
      $$\tau = I_z \cdot \alpha$$
      Because human muscular actuators cannot produce infinite torque instantly, changing direction incurs a rotational delay of $200\text{--}300\text{ ms}$—creating an uncontested opportunity window for the defender.

#### Beat 5: Tactical Synthesis & Bridge to Wave 3
- **Lead Rule**: *Never trade blow for blow with an adversary's strength; flow around their committed mass and strike where their defenses cannot reach.*
- **Core Narrative**:
  - Synthesis of refusing the centerline: In personal defense, maneuver is not an aesthetic display; it is structural survival. Bypassing the attacker's primary vector ensures you never rely on superior size or chin durability.
  - Re-anchoring to the Master Equation: Angular flanking simultaneously manages Distance (collapses or expands relative range), Time (forces a 250 ms rotational penalty on the attacker), and Power (delivers whole-body mass into unguarded targets).
  - Bridge to Wave 3 (Section 5.3: Deception, Unorthodox Force [$qi / zheng$], and Terrain Classification): How Sun Tzu combines physical angular flanking with cognitive misdirection, baiting, and terrain exploitation to make the attacker's every assumption catastrophically wrong.

---

### 6. Verification Probes & Fact Checks
- **Designated Code Probe ID**: `[PROBE-CH05-W02-REFUSING-CENTERLINE]`
- **Probe Test Location**: `tests/code_examples/test_ch05_probes.py`
- **Probe Test Suite**:
  1. `test_ch05_w02_file_exists`: Validates existence of manuscript file.
  2. `test_ch05_w02_word_count_within_budget`: Asserts word count is between 1,300 and 1,800 words.
  3. `test_ch05_w02_zero_banned_marketing_words`: Asserts 0 occurrences of banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`).
  4. `test_ch05_w02_mandatory_concepts_present`: Validates presence of:
     - `Avoid Strength, Strike Weakness` (or `Avoid Strength and Strike Weakness`)
     - `The Centerline`
     - `Refusing the Centerline` (or `Refuse the Centerline`)
     - `Angular Flanking`
     - `Rotational Inertia` (or `Vector Decomposition`)
     - `Linear Momentum` (or `Momentum`)
- **Primary Source / Fact Check Index**:
  - Sun Tzu (c. 5th Century BC) *The Art of War*, trans. Lionel Giles (Chapter 6: Weak Points and Strong; Chapter 11: The Nine Situations).
  - Beer, F. P., & Johnston, E. R. *Vector Mechanics for Engineers: Statics and Dynamics* (linear momentum and moment of inertia).
  - Morris, M. (1993) *The Science of Striking and Maneuver in Martial Combatives*.
  - Winter, D. A. (2009) *Biomechanics and Motor Control of Human Movement* (locomotion differences between forward and backward gait).

---

### 7. Out of Scope (Negative Blast Radius)
- **Strictly Excluded from this Wave**:
  - *Wave 3 Material (Section 5.3)*: Deception doctrine, orthodox vs. unorthodox force ($qi / zheng$), and the Nine Terrains classification taxonomy.
  - *Chapter 06 Material*: Airpower doctrine, Boyd's energy-maneuverability theory, and multi-domain operations.
  - *Chapter 07 Material*: Ground maneuver, bounding overwatch, and tactical egress corridors.
  - *Part IV Material*: Style-specific combo execution (specific TKD roundhouses, Muay Thai sweeps, or wrestling throws).

---

### 8. Rollback Strategy
- Deterministic rollback command:
  ```bash
  git checkout -- manuscript/part_02_strategic_lenses/ch05_the_sun_tzu_lens/02_avoid_strength_strike_weakness.md
  git checkout -- tests/code_examples/test_ch05_probes.py
  ```

---

### 🛑 EDITOR GATE 1 SUBMISSION
> **CRITICAL POLICY NOTICE**:  
> This plan is hereby submitted for Editor Review prior to drafting any narrative prose or publishing any text.  
> **NO PROSE DRAFTING PERMITTED BEFORE EDITOR GATE 1 APPROVAL.**
