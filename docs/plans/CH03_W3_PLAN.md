# Authoring Section Implementation Plan: Chapter 03 — Wave 3

**Target Chapter & Wave**: `Chapter 03 - Wave 3: Section 3.3 (Setups, Predictive Funneling, and the Engineered Opening: Collapsing Opponent Attack Vectors)`  
**Target Milestone**: `Part I: The Master Filter (The Physics & Philosophy of Force)`  
**Status**: `GATE 1: SUBMITTED FOR REVIEW`  

---

### 1. Goal & Pedagogical Intent
Conclude Chapter 03 by elevating timing from passive reaction to active engineering. Dispel the myth that counter-fighters must wait for an adversary to offer an opening; establish how a disciplined practitioner deliberately manufactures the opportunity window through **Predictive Funneling** and **The Engineered Opening**. Demonstrate mathematically and biomechanically how dangling calculated bait collapses the adversary's choice architecture (**Hick's Law Inversion**), reducing reaction latency from a lagging 250–400 ms to zero. Ground this in a concrete biomechanical case study (the lead-leg bait to cervical spine crossface and momentum redirection). Deliver this under the **Fighter-First, Engineer-Backed** standard: lead every beat with coach-level decision rules, explain physical mechanisms in visceral language before introducing models, isolate Hick's Law ($T = b \cdot \log_2(n + 1)$) in a dedicated callout block, and enforce the Mat Test.

---

### 2. Learning Objective & Concept Binding
- **Objective ID**: `OBJ-CH03-003`
- **Target Concepts Introduced**:
  - *The Engineered Opening*: Deliberately creating an apparent physical vulnerability to provoke a specific, pre-calculated attack.
  - *Predictive Funneling*: Restricting the adversary's perceived options so that an unconstrained multi-vector environment collapses into a single deterministic attack lane.
  - *Hick's Law Inversion ($n \to 1$)*: Decision latency increases with the number of choices ($T = b \cdot \log_2(n + 1)$). By presenting an irresistible high-value target, the defender reduces the attacker's options to $n = 1$, eliminating defender cognitive latency and enabling zero-latency counter-execution.
  - *Baiting*: Displaying an intentional positional or spatial opening to lure the opponent into committing their Center of Mass past their Base of Support.
  - *Cervical Spine Torque (Crossface)*: Applying rotational leverage across the head/jaw; because spinal alignment follows the cervical spine, turning the skull perpendicular breaks forward kinetic drive.
  - *Momentum Redirection*: Converting linear forward momentum into rotational torque to topple an over-committed attacker with minimal muscular energy.
- **Forward Pointers**:
  - Completes Chapter 03 and locks the second pillar (Timing) of Part I.
  - Bridges directly into Chapter 04: *The Command Center — Fighting as a Contest of Minds* (the neurological engine executing these strategic decisions).
  - Connects to Part III (Principle 4: Initiative, Principle 7: Deception, and Principle 8: Exploitation).

---

### 3. Invariant Locks (Mandatory Constraints)
- [ ] **Lock 1 (Fighter-First Delivery)**: Every major subsection must open with a direct, usable tactical rule and concrete consequence before introducing any physical or cognitive mechanics.
- [ ] **Lock 2 (Action Precedes Math)**: All cognitive and kinematic formulas (Hick's Law $T = b \cdot \log_2(n + 1)$, rotational torque $\tau = r \times F$, linear momentum $p = mv$) must reside in dedicated `> [!NOTE]` callouts ("The Mechanics Behind It") or concise parentheticals—never in the primary narrative flow.
- [ ] **Lock 3 (The Mat Test Compliance)**: The prose must pass the Mat Test: read like a seasoned coach explaining realities between rounds, avoiding dry academic or classroom pedantry.
- [ ] **Lock 4 (Terminology Fidelity)**: All technical terms (Engineered Opening, Predictive Funneling, Hick's Law Inversion, Baiting, Cervical Spine Torque, Momentum Redirection) must match [CONCEPT_REGISTER.md](file:///c:/Book/.agent_context/CONCEPT_REGISTER.md) and [GLOSSARY.md](file:///c:/Book/.agent_context/GLOSSARY.md) exactly.
- [ ] **Lock 5 (Word Count Budget)**: Target is 1,300 – 1,600 words (hard ceiling: 1,800 words).
- [ ] **Lock 6 (Linguistic Hygiene)**: Zero banned marketing words ("seamlessly", "natively", "cleanly", "simply", "obviously", "phighting"); passive voice strictly under 10%.
- [ ] **Lock 7 (Authorial Credibility)**: Grounded in the author's background as an Air Force officer, mechanical engineer, and multi-discipline martial artist without displaying credentials as an academic lectern.
- [ ] **Lock 8 (Negative Blast Radius)**: Zero dual-brain cortical vs. lizard brain neuroanatomy (reserved for Chapter 04); zero Sun Tzu deception doctrine (reserved for Chapter 05); zero style-by-style wrestling or BJJ catalogs (reserved for Part IV).

---

### 3.1 Style Guide Compliance Matrix (Fighter-First Mandates)
| Requirement | Implementation in Chapter 03 Wave 3 | Verification Method |
| :--- | :--- | :--- |
| **1. Lead sentence states usable rule** | Each subsection opens with an unequivocal tactical rule (e.g., *"Do not wait for an elite fighter to give you an opening; give them a target they cannot resist, and destroy them on the way in."*). | Code review of opening sentences in Beats 1–4. |
| **2. Plain-language mechanism first** | The trap of dangling a lead leg, snapping the crossface across the jaw to kill drive, and tilting momentum onto the ceiling are explained with visceral mat realities before any mathematical modeling. | Pre-draft beat outline audit. |
| **3. Formal physics in callouts/parentheticals** | Hick's Law decision equation ($T = b \cdot \log_2(n + 1)$) and torque mechanics isolated entirely inside a dedicated `> [!NOTE]` callout block ("The Mechanics Behind It"). | Automated grep / AST scan ensuring 0 equations in main prose flow. |
| **4. Explicit Mat Test check** | Voice must pass the Mat Test: *Would a coach say this to a fighter between rounds?* If a line sounds like a classroom lecture, it must be rewritten into physical action cues. | Post-draft Mat Test audit prior to Gate 2 submission. |

---

### 4. Target Files
- **File to Create**:
  - `manuscript/part_01_foundations/ch03_timing_and_windows/03_setups_predictive_funneling_and_engineered_openings.md`
- **Harness & Verification Files to Update**:
  - `tests/code_examples/test_ch03_probes.py` (Add Wave 3 probe suite for word count, banned words, passive voice, and conceptual invariants)
  - `.agent_context/MANUSCRIPT_REGISTER.md` (Update Chapter 03 Wave 3 tracking)

---

### 5. Pedagogical Beats Breakdown

#### Beat 1: The Trap of Passive Countering (Why Waiting Gets You Killed)
- *Lead Rule*: If you wait for a disciplined opponent to make an unforced error, you surrender the initiative and let them choose the moment of your destruction.
- *Tactical Reality*: Novices think counter-fighting means standing still with hands high, waiting for an opponent to make a mistake. Against an elite fighter, this passive posture is suicidal. Advanced fighters do not make unforced errors; they use feints, probes, and tempo shifts to dismantle a stationary guard.
- *Mechanism*: Taking the initiative does not mean charging forward blindly. It means actively dictating the terms of engagement by creating engineered conditions that force the opponent to move on your schedule.

#### Beat 2: Predictive Funneling & Hick's Law Inversion ($n \to 1$)
- *Lead Rule*: Do not try to defend against every possible strike; offer an irresistible bait that forces the attacker down a single, predictable lane.
- *Tactical Reality*: The cognitive mechanics of Predictive Funneling. When an opponent has full freedom of choice ($n = 10\text{--}15$ eligible weapons), human reaction time lags.
- *Mechanism*: You deliberately show an apparent structural vulnerability—a heavy lead leg, a slightly lowered rear hand, or an open angle. By offering high-value bait, you collapse the opponent's decision architecture down to a single deterministic action ($n = 1$). Because *you* chose the attack vector, your counter-program is already loaded into muscle memory. Reaction latency drops from 250–400 ms to zero.
- *Callout Block*: `> [!NOTE]` — *The Mechanics Behind It: Hick's Law Inversion ($T = b \cdot \log_2(n + 1)$) and Deterministic Threat Collapsing*.

#### Beat 3: Biomechanical Case Study (The Lead-Leg Bait $\to$ Crossface & Momentum Redirection)
- *Lead Rule*: When an attacker bites on your bait, do not absorb their charge; break their spine alignment and redirect their kinetic drive into the floor.
- *Tactical Reality*: Concrete mat-level case study of an engineered opening in action.
- *Mechanism*:
  1. *The Bait*: Exposing the lead leg in a slightly heavy stance, inviting an aggressive opponent to shoot for a low single or double leg.
  2. *Cervical Spine Torque (The Crossface)*: As the opponent shoots forward, the defender sprawls their hip back and drives a rigid forearm across the opponent's jaw/philtrum. Human anatomy mandates that where the head turns, the spine must follow. Turning the head ninety degrees perpendicular to the spine neutralizes forward driving force.
  3. *Momentum Redirection*: Catching the far armpit or lat and rolling their chest toward the ceiling converts forward linear momentum into rotational torque, flipping the attacker onto their back with minimal effort.

#### Beat 4: Chapter 03 Synthesis: Unifying Timing into the Master Triad
- *Lead Rule*: Space creates the runway, but timing pulls the trigger; master the geometry, calibrate to the window, and engineer the collision.
- *Synthesis*: Unifies Chapter 03 across its three waves:
  - Wave 1: The Geometry of Mistakes reveals that openings are structural bankruptcies.
  - Wave 2: Skill Disparity defines how the Opportunity Window shrinks from seconds to milliseconds.
  - Wave 3: Predictive Funneling and Hick's Law Inversion empower you to manufacture the window at will.
- *Bridge to Chapter 04*: All physical tactics—distance control, skeletal framing, and engineered timing—rely on a central command engine. Fighting is fundamentally a contest of minds. This bridges directly into Chapter 04: *The Command Center — Fighting as a Contest of Minds* (the neurological engine executing strategy under high-stress adrenal load).

---

### 6. Verification Probes & Fact Checks
- **Designated Probe ID**: `[PROBE-CH03-W03-ENGINEERED-OPENINGS]`
- **Verification Harness**: `tests/code_examples/test_ch03_probes.py`
  - Automated assertions:
    1. Target file `03_setups_predictive_funneling_and_engineered_openings.md` exists.
    2. Word count in bounds [1,300 – 1,800 words].
    3. Zero occurrences of banned words list (`seamlessly`, `natively`, `cleanly`, `simply`, `obviously`, `phighting`).
    4. Passive voice $< 10\%$.
    5. Required conceptual tokens present (`Engineered Opening`, `Predictive Funneling`, `Hick's Law Inversion`, `Baiting`, `Cervical Spine Torque`, `Momentum Redirection`).
    6. **Mat Test Protocol**: Full prose read-aloud audit verifying coach-to-fighter corner instruction before Gate 2 submission.
- **Citation Anchors**:
  - *Hick (1952) / Hyman (1953)*: Logarithmic choice reaction time in cognitive tasks.
  - *Boyd (1987) / Patterns of Conflict*: Fast transients, entrapping adversary decisions, and tempo dominance.
  - *USA Wrestling / National Coaching Manual*: Cervical spine control (crossface), head position, and momentum redirection.

---

### 7. Out of Scope (Negative Blast Radius)
- Will NOT detail cortical vs. lizard brain neuroanatomy or subconscious offloading (reserved for Chapter 04).
- Will NOT detail Sun Tzu deception doctrine or indirect maneuver (reserved for Chapter 05).
- Will NOT catalog style-specific wrestling or BJJ finishes (reserved for Part IV).

---

### 8. Rollback Strategy
- Deterministic rollback command:
  ```powershell
  git checkout -- manuscript/part_01_foundations/ch03_timing_and_windows/03_setups_predictive_funneling_and_engineered_openings.md
  ```

---

### 🛑 EDITOR GATE 1 SUBMISSION
> **CRITICAL POLICY NOTICE**:  
> This plan is hereby submitted for Editor Review prior to drafting any narrative prose.  
> **NO PROSE DRAFTING PERMITTED BEFORE EDITOR GATE 1 APPROVAL.**
