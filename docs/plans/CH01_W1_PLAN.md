# Authoring Section Implementation Plan

**Target Chapter & Wave**: `Chapter 01 - Wave 1: Why Single-Attribute Tactics Fail & The Master Equation`  
**Target Milestone**: `Part I: The Master Filter (The Physics & Philosophy of Force)`  
**Status**: `PENDING EDITOR GATE 1 APPROVAL`  

---

### 1. Goal & Pedagogical Intent
Establish the foundational thesis of the entire book: personal combat is not a collection of arbitrary moves, but an operational discipline governed by the immutable physics of **Time, Distance, and Power**. Demonstrate why single-attribute reliance (raw strength without timing, or distance management without striking velocity) fails under real-world pressure, and introduce the Master Equation: **Distance buys Time, and Time directs Power**.

### 2. Learning Objective & Concept Binding
- **Objective ID**: `OBJ-CH01-001`
- **Target Concepts Introduced**:
  - The Triad of Force: Time, Distance, and Power as an integrated system.
  - The Single-Attribute Fallacy (the "Bigger/Stronger" or "Faster" trap).
  - The Master Equation: $\text{Distance} \longrightarrow \text{Time} \longrightarrow \text{Power}$.
  - The Hard Target Concept: Correct structural position and fundamentals over elaborate techniques.
- **Forward Pointers**: Brief structural previews of Chapter 2 (The 4 Ranges) and Chapter 3 (Timing & Windows) without premature duplication.

### 3. Invariant Locks (Yes/No)
- [ ] **Lock 1 (Terminology Fidelity)**: All terms match [CONCEPT_REGISTER.md](file:///c:/Book/.agent_context/CONCEPT_REGISTER.md) exactly. [Yes]
- [ ] **Lock 2 (No Scope Bleed)**: Does NOT catalog specific martial arts techniques or deep ground submissions (reserved for Part IV). [Yes]
- [ ] **Lock 3 (Forward Pointer Restraint)**: Distance ranges and millisecond OODA calculations are introduced only as concepts, not fully unpacked (avoiding Ch 2/3 overlap). [Yes]
- [ ] **Lock 4 (Word Count Ceiling)**: Section target is 1,200 – 1,500 words (hard ceiling: 1,800). [Yes]
- [ ] **Lock 5 (Linguistic Hygiene)**: Zero banned marketing words ("seamlessly", "natively", "cleanly", "simply", "obviously", "phighting"); passive voice strictly under 10%. [Yes]
- [ ] **Lock 6 (Authorial Voice)**: Written in the pragmatic, analytical tone of a military officer and multi-discipline combat coach. [Yes]
- [ ] **Lock 7 (Falsifiable Assertion)**: Includes a concrete physical/bio-mechanical example illustrating the failure of power without position. [Yes]

### 4. Target Files
- Files to create:
  - `manuscript/part_01_foundations/ch01_the_triad/01_why_single_attribute_tactics_fail.md`
- Tracking / verification files to update:
  - `manuscript/part_01_foundations/ch01_the_triad/README.md`
  - `tests/code_examples/test_sanity.py` (Asserts structural file existence and word count bounds)

### 5. Pedagogical Beats Breakdown
- **Beat 1: The Illusion of the Technique Catalog**
  - Why memorizing 100 self-defense moves creates catastrophic cognitive failure under adrenaline.
  - The difference between choreography on a clean mat and physics in an alley.
- **Beat 2: The Three Failures of Single-Attribute Reliance**
  - *Power without Timing*: The heavyweight haymaker that hits air and creates fatal over-extension.
  - *Distance without Velocity/Offense*: The defender who retreats in a straight line until pinned against a wall.
  - *Timing without Power/Structure*: The precise strike with broken wrist alignment that shatters the puncher's hand.
- **Beat 3: The Master Equation**
  - How physical separation (Distance) creates the sensory and cognitive window (Time) to recognize intent, select an entry, and concentrate kinetic force (Power).
- **Beat 4: The Law of the Hard Target**
  - Why correct base, posture, and alignment prevent errors before contact occurs.
  - Fundamentals as the shield that allows the strategic mind to operate.

### 6. Verification Probes & Fact Checks
- **Designated Probe ID**: `[PROBE-CH01-TRIAD-PHYSICS]`
- **Verification Method**: Automated python text probe checking:
  1. Section word count within range [1,000, 1,800].
  2. Zero occurrences of banned words list.
  3. Passive voice ratio $< 10\%$.
- **Citation Anchors**:
  - Bruce Lee (*Tao of Jeet Kune Do*): Economy of motion and directness.
  - AFDP 1 / John Boyd: Time as the decisive competitive medium.

### 7. Out of Scope (Negative Blast Radius)
- Will NOT discuss legal justification or post-incident aftermath (reserved for Ch 21).
- Will NOT provide step-by-step instructions for takedowns, submissions, or kicks (reserved for Part IV).
- Will NOT unpack the 4 distinct combat ranges in detail (reserved for Ch 02).

### 8. Rollback Strategy
- Deterministic rollback command:
  ```powershell
  git checkout -- manuscript/part_01_foundations/ch01_the_triad/01_why_single_attribute_tactics_fail.md
  ```

---

### 🛑 EDITOR GATE 1 SUBMISSION
> **CRITICAL POLICY NOTICE**:  
> This plan is hereby submitted for Editor Review prior to drafting any narrative prose.  
> **NO PROSE DRAFTING PERMITTED BEFORE EDITOR GATE 1 APPROVAL.**
