# Authoring Section Implementation Plan: Chapter 07 — Wave 2

**Target Chapter & Wave**: `Chapter 07 - Wave 2: Section 7.2 (Security of Position: Never Ceding Structural Advantage for a Cheap Strike)`  
**Target Milestone**: `Part II: The Three Strategic Lenses (Sun Tzu, Airpower, and Ground Maneuver)`  
**Status**: `GATE 1: SUBMITTED FOR REVIEW`  

---

### 1. Goal & Pedagogical Intent
Deepen the Ground Maneuver Lens by translating the foundational military Principle of War—**Security** (codified in U.S. Army FM 3-0 *Operations* and ADP 3-0)—into physical self-defense and biomechanics on concrete. Establish **Security of Position** as the unyielding anchor of terrestrial survival: never sacrifice a sound base, balanced posture, dominant angle, or safe distance to chase a speculative, low-percentage strike or high-risk takedown. Contrast the adrenaline-driven temptation of the "cheap strike" (over-reaching, lunging, pitching the center of mass forward, bending the cervical spine) against structural integrity. 

Introduce **Convex Tactics** through the lens of Decision Theory and asymmetric risk-reward, analyzing the stark contrast between the **Double Leg Failure Trap** (high investment, catastrophic downside on concrete—cracked patellas, flattened under a 200-lb sprawl, neck trapped in a guillotine, head vulnerable to third-party strikes) and the **Ankle Pick Advantage** (negligible downside, head stays above hips, posture remains vertical, failure simply resets to a collar-tie frame on two feet with zero penalty). 

Articulate the **Three Structural Columns** (head over hips, hips over base, elbows inside the ribcage) that preserve equilibrium against sudden shocks. Deliver this under the **Fighter-First, Engineer-Backed** standard: lead every beat with coach-level decision rules, explain physical mechanisms in visceral language before introducing models, isolate center-of-mass tipping moments, cervical lever torque, and asymmetric expected value equations in a dedicated callout block, and enforce the Mat Test.

---

### 2. Learning Objective & Concept Binding
- **Objective ID**: `OBJ-CH07-002`
- **Target Concepts Introduced**:
  - *Security of Position*: Principle 2 of the 11 Unified Principles; the operational doctrine that you must never surrender structural integrity, balance, or geometric leverage to chase an unvetted offensive opening.
  - *Structural Advantage*: Maintaining alignment between the skeletal frame, center of mass, and ground reaction forces so external force is absorbed into the earth rather than collapsing muscle tissue.
  - *Convex Tactics (Asymmetric Tactical ROI)*: Selecting combat techniques where the downside cost of failure is bounded and negligible, while the upside of success is decisive ($\mathbb{E}[V] = P(S)U(S) - P(F)C(F)$ with $C(F) \approx 0$).
  - *The Double Leg Failure Trap*: The catastrophic risk profile of deep, level-dropping takedown shots on asphalt or pavement against unvetted threats.
  - *The Ankle Pick Advantage*: The biomechanical model of a convex technique that attacks an opponent's base while preserving the defender's upright spinal column and escape options.
  - *Center of Mass & Polygon of Support*: The physical foundation of balance, restoring moments ($M_{\text{restoring}} = m g d$), and tipping vulnerabilities under combat load.
- **Forward Pointers**:
  - Direct bridge to Part III (Principle 2: Security of Position, Principle 6: Economy of Force, Principle 10: Actions on Contact).
  - Connects to Part IV (Chapter 14: Wrestling Clinch and Takedown Selection; Chapter 15: Ground Survival and Base Recovery).
  - Prepares the foundation for Wave 3 (Section 7.3: *Economy of Force and Terrain Navigation: Walls, Curbs, and Corridors*).

---

### 3. Invariant Locks (Mandatory Constraints)
- [ ] **Lock 1 (Fighter-First Delivery)**: Every major subsection must open with a direct, usable tactical rule and concrete consequence before introducing infantry doctrine or physics.
- [ ] **Lock 2 (Action Precedes Math / Physics)**: Restoring moment formulas ($M_{\text{restoring}} = m g d$), tipping moments ($\tau = F \cdot h$), cervical spine lever mechanics ($\tau = F_{\text{sprawl}} \cdot r_{\text{head}}$), and convex expected-value equations must reside in dedicated `> [!NOTE]` callouts ("The Mechanics Behind It")—never in the primary narrative flow.
- [ ] **Lock 3 (The Mat Test Compliance)**: The prose must pass the Mat Test: read like a seasoned coach instructing a fighter between rounds, avoiding academic lectures or detached tactical manual recitations.
- [ ] **Lock 4 (Terminology Fidelity)**: All technical terms (Security of Position, Structural Advantage, Convex Tactics, Ankle Pick, Double Leg, Center of Mass, Polygon of Support) must match [CONCEPT_REGISTER.md](file:///c:/Book/.agent_context/CONCEPT_REGISTER.md) and [GLOSSARY.md](file:///c:/Book/.agent_context/GLOSSARY.md) exactly.
- [ ] **Lock 5 (Word Count Budget)**: Target is 1,400 – 1,750 words (hard ceiling: 1,800 words).
- [ ] **Lock 6 (Linguistic Hygiene)**: Zero banned marketing words ("seamlessly", "natively", "cleanly", "simply", "obviously", "phighting"); passive voice strictly under 10%.
- [ ] **Lock 7: Authorial Credibility**: Grounded in the author's background as an Air Force officer, engineer, wrestling coach, and martial artist without turning into sport-grappling dogma.
- [ ] **Lock 8: Negative Blast Radius**: Zero deep dive into Economy of Force, wall-pinning mechanics, curb tripping, or multi-attacker escape corridor preservation (strictly reserved for Wave 3, Section 7.3); zero style-specific move catalogs (reserved for Part IV).

---

### 3.1 Style Guide Compliance Matrix (Fighter-First Mandates)
| Requirement | Implementation in Chapter 07 Wave 2 | Verification Method |
| :--- | :--- | :--- |
| **1. Lead sentence states usable rule** | Each subsection opens with an unequivocal tactical rule (e.g., *"Never sacrifice your base or posture to reach for a strike; an unanchored hit buys you nothing if you lose your feet."*). | Code review of opening sentences in Beats 1–6. |
| **2. Plain-language mechanism first** | Balance, overextension, cervical bending, sprawl impact, and asphalt friction explained through visceral street realities before equations. | Pre-draft beat outline audit. |
| **3. Formal physics in callouts** | Center of mass tipping moments, cervical lever torque, and asymmetric expected value equations isolated entirely in `> [!NOTE]` callout block ("The Mechanics Behind It"). | Automated grep / AST scan ensuring 0 equations in main prose flow. |
| **4. Explicit Mat Test check** | Voice must pass the Mat Test: *Would a coach say this to a fighter between rounds?* If a line sounds like an engineering textbook, it must be rewritten into physical coaching cues. | Post-draft Mat Test audit prior to Gate 2 submission. |

---

### 4. Target Files
- **File to Create**:
  - `manuscript/part_02_strategic_lenses/ch07_the_ground_maneuver_lens/02_security_of_position.md`
- **Harness & Verification Files to Create / Update**:
  - `tests/code_examples/test_ch07_probes.py` (Add Wave 2 probe suite for word count, banned words, passive voice, and conceptual invariants)
  - `.agent_context/MANUSCRIPT_REGISTER.md` (Update Chapter 07 Wave 2 tracking)

---

### 5. Detailed Beat Outline (Section 7.2)

#### Beat 1: The Tactical Anchor: Security in Infantry and Combatives
- **Lead Rule**: Never sacrifice posture, balance, or defensive integrity to reach for an unvetted offensive strike; position is your survival insurance.
- **Narrative**:
  - Grounding in military doctrine: In infantry tactics (FM 3-0), Security protects the force from unexpected enemy advantage. A squad holding dominant terrain never abandons its defensive anchor to chase a fleeing scout.
  - Combatives reality on concrete: An upright, balanced frame with aligned spine and active base protects you against sudden punches, headbutts, and takedowns. The moment you surrender your structural anchor to chase a cheap shot, you trade guaranteed security for an uncertain gamble.

#### Beat 2: The Siren Song of the Cheap Strike: Why Fighters Compromise Their Base
- **Lead Rule**: A strike thrown from a broken base generates minimal damage while multiplying your own vulnerability.
- **Narrative**:
  - Analyze the psychological trap: In the heat of combat, the adrenaline-driven urge to "hit" causes untrained fighters to reach, lunge, overextend their lead shoulder, and lean forward off their hips.
  - Biomechanical consequence: Reaching shifts the center of mass outside the base of support. The cervical spine bends forward, removing the head's structural shock absorption. An alert attacker does not even need a clean strike to defeat you; a simple clubbing counter or collar drag redirects your own overextended mass directly into the concrete.

#### Beat 3: Convex Tactics: Asymmetric Risk-Reward on the Ground (The Ankle Pick vs. The Double Leg)
- **Lead Rule**: In real-world violence, select techniques with negligible cost of failure and decisive upside; never choose high-downside gambles.
- **Narrative**:
  - Case Study: The Double Leg vs. The Ankle Pick under the lens of Decision Theory and ground combat.
  - The Double Leg Failure Trap: A classic wrestling blast double is devastating on a spring-loaded canvas mat, but on street concrete it carries catastrophic downside. Shooting on concrete risks shattering knees on asphalt; if the attacker sprawls with 200 pounds of downward mass, your neck is trapped in a front headlock or guillotine, your hands are committed to their thighs, and you are immobilized against third-party threats.
  - The Ankle Pick Advantage (Convexity): By contrast, an ankle pick (or snapdown frame) allows you to attack the opponent's base while your own head remains above your hips, your knees stay off the pavement, and your posture stays upright. If the ankle grip slips or fails, the cost of failure is near zero: you release the ankle, retract behind your collar frame, and remain on your feet with structural security intact.

#### Beat 4: Positional Anchoring: The Three Structural Columns
- **Lead Rule**: Anchor your structure through three aligned columns—head over hips, hips over base, and elbows inside the ribcage.
- **Narrative**:
  - Detail the physical mechanism of positional security:
    - Column 1: Head over hips (Spinal verticality prevents cervical levering).
    - Column 2: Hips over base (Center of mass maintained inside the polygon of support).
    - Column 3: Elbows inside ribcage (Framing wedges protect vital organs and prevent arm isolation).
  - Maintaining these three columns ensures that any force delivered by the attacker is absorbed through the entire skeletal frame into the ground, rather than collapsing a lone muscle group.

#### Beat 5: Callout Block: Biomechanical Stability, Center of Pressure, and Convex Payoff Matrices
- **Mechanical & Mathematical Details** (`> [!NOTE]` callout):
  1. *Static and Dynamic Equilibrium*: Restoring moment $M_{\text{restoring}} = m g d$, where $d$ is horizontal distance from COM projection to the tipping pivot edge. As $d \to 0$ (overextension), critical tipping force $F_{\text{crit}} = \frac{m g d}{h} \to 0$.
  2. *Cervical Lever Mechanics*: Cervical spine flexion under external load. When the head extends forward by distance $r_{\text{head}}$, torque on the cervical spine is $\tau = F_{\text{sprawl}} \cdot r_{\text{head}}$.
  3. *Convex Decision Theory in Combat*: Asymmetric payoff function $\mathbb{E}[V] = P(S) \cdot U(S) - P(F) \cdot C(F)$. Comparing double leg ($C(F) \gg 0$, catastrophic downside on concrete) vs. ankle pick ($C(F) \approx 0$).

#### Beat 6: Tactical Synthesis: Position Before Submission, Structure Before Strike
- **Lead Rule**: Secure your platform first; let the strike be a dividend of superior structure, not an overdraft on your balance.
- **Narrative**:
  - Re-anchoring to the Master Equation (**Distance $\to$ Time $\to$ Power**):
    - *Distance*: Security of position maintains the critical defensive buffer.
    - *Time*: An anchored base eliminates recovery latency; you never waste time scrambling to regain your feet.
    - *Power*: Power is only real if backed by an unyielding base; a strike from a sound anchor delivers structural ground-reaction mass.
  - Bridge to Wave 3 (Section 7.3: *Economy of Force and Terrain Navigation: Walls, Curbs, and Corridors*).

---

### 6. Verification Probes & Fact Checks
- **Designated Code Probe ID**: `[PROBE-CH07-W02-SECURITY-POSITION]`
- **Probe Test Location**: `tests/code_examples/test_ch07_probes.py`
- **Probe Test Suite**:
  1. `test_ch07_w02_file_exists`: Validates existence of manuscript file.
  2. `test_ch07_w02_word_count_within_budget`: Asserts word count is between 1,300 and 1,800 words.
  3. `test_ch07_w02_zero_banned_marketing_words`: Asserts 0 occurrences of banned words (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`).
  4. `test_ch07_w02_mandatory_concepts_present`: Validates presence of:
     - `Security of Position`
     - `Structural Advantage`
     - `Convex Tactics` (or `Convexity`)
     - `Ankle Pick`
     - `Double Leg`
     - `Center of Mass` (or `Polygon of Support`)
- **Primary Source / Fact Check Index**:
  - Headquarters, Department of the Army (2017) *Field Manual 3-0 (FM 3-0): Operations*.
  - Headquarters, Department of the Army (2019) *Army Doctrine Publication 3-0 (ADP 3-0): Operations*.
  - Taleb, N. N. (2012) *Antifragile: Things That Gain from Disorder* (Convexity and asymmetric payoffs).
  - Hall, S. J. (2018) *Basic Biomechanics*, McGraw-Hill (Equilibrium, center of gravity, and base of support).
  - Morris, M. (1993) *The Science of Striking and Maneuver in Martial Combatives*.

---

### 7. Out of Scope (Negative Blast Radius)
- **Strictly Excluded from this Wave**:
  - *Wave 3 Material (Section 7.3)*: Economy of force, terrain navigation, wall pinning, obstacle bridging, escape corridor preservation, and chapter capstone.
  - *Part IV Material*: Style-specific combo execution (specific wrestling pins, judo throws, or BJJ submissions).

---

### 8. Rollback Strategy
- Deterministic rollback command:
  ```bash
  git checkout -- manuscript/part_02_strategic_lenses/ch07_the_ground_maneuver_lens/02_security_of_position.md
  git checkout -- tests/code_examples/test_ch07_probes.py
  ```

---

### 🛑 EDITOR GATE 1 SUBMISSION
> **CRITICAL POLICY NOTICE**:  
> This plan is hereby submitted for Editor Review prior to drafting any narrative prose or publishing any text.  
> **NO PROSE DRAFTING PERMITTED BEFORE EDITOR GATE 1 APPROVAL.**
