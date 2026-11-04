#!/usr/bin/env python3
"""
Assemble Volume 2 Manuscript: The Machine Under Load — Stress, Conditioning, and Survival Realities
Compiles:
- Volume 2 Front Matter (Title, Copyright, Preface, TOC)
- Parts I through IV (13 section files across human systems, decision engine, training doctrine, weapons, law)
- Volume 2 Back Matter
into manuscript/TIME_DISTANCE_AND_POWER_VOL2_HUMAN_FACTOR.md
"""

from pathlib import Path

REPO_ROOT = Path("C:/Book")
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"
OUTPUT_FILE = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_VOL2_HUMAN_FACTOR.md"

FRONT_MATTER_FILES = [
    MANUSCRIPT_DIR / "front_matter_volume_2" / "00_title_and_copyright_vol2.md",
    MANUSCRIPT_DIR / "front_matter_volume_2" / "01_preface_volume_2.md",
]

VOL2_BODY_DIRS = [
    MANUSCRIPT_DIR / "part_01_foundations" / "ch04_the_command_center",
    MANUSCRIPT_DIR / "part_05_the_decision_engine" / "ch17_the_4_step_cycle",
    MANUSCRIPT_DIR / "part_05_the_decision_engine" / "ch18_high_stress_physiology",
    MANUSCRIPT_DIR / "part_06_training_doctrine" / "ch19_neural_conditioning",
    MANUSCRIPT_DIR / "part_06_training_doctrine" / "ch20_asymmetric_threats",
    MANUSCRIPT_DIR / "part_06_training_doctrine" / "ch21_legal_and_ethical",
]

BACK_MATTER_FILES = [
    MANUSCRIPT_DIR / "back_matter" / "01_glossary.md",
    MANUSCRIPT_DIR / "back_matter" / "03_annotated_bibliography.md",
    MANUSCRIPT_DIR / "back_matter" / "04_about_the_author.md",
]

def get_section_files():
    section_files = []
    for directory in VOL2_BODY_DIRS:
        if not directory.exists():
            raise FileNotFoundError(f"Directory missing: {directory}")
        sec_files = sorted([f for f in directory.glob("*.md") if not f.name.endswith("README.md")])
        for sec_file in sec_files:
            section_files.append(sec_file)
    return section_files

def generate_vol2_toc():
    return """# TABLE OF CONTENTS — VOLUME 2: THE MACHINE UNDER LOAD

---

### FRONT MATTER
- **Title Page & Copyright Notice**
- **Safety, Medical, and Legal Disclaimers**
- **Preface: The Meat and the Machine — Why Flawless Tactics Collapse in Chaos**

---

### PART I: THE BIOLOGICAL COMMAND CENTER — Neurological Reality Under Fire
- **Chapter 01: The Command Center: Neurological Reality Under Fire**
  - *1.1 The Mind as Primary Weapon and the Dual-Brain Paradox*
  - *1.2 Offloading to the Lizard Brain: Developing Subconscious Reflexes*
  - *1.3 The Iron Law: Decision Quality Under Severe Physical Stress*
- **Chapter 02: The 4-Step Cycle: Recognize, Prioritize, Choose, Act**
  - *2.1 Recognize and Prioritize: Threat Classification Under Pressure*
  - *2.2 Choose, Act, and Reassess: Executing Inside the Opponent's Loop*

---

### PART II: HIGH-STRESS PHYSIOLOGY — Surviving the Autonomic Surge
- **Chapter 03: High-Stress Physiology: Surviving the Autonomic Cascade**
  - *3.1 The Autonomic Cascade and Sensory Distortions*
  - *3.2 Motor Degradation, Recovery Protocols, and Part II Capstone*

---

### PART III: THE SCIENCE OF NEURAL CONDITIONING — Training Doctrine
- **Chapter 04: Train Like You Fight: The Law of Neural Conditioning**
  - *4.1 Neural Conditioning, Myelination, and the Law of Permanence*
  - *4.2 Progressive Stress Inoculation, Decision Drilling, and Chapter 4 Capstone*

---

### PART IV: SURVIVAL REALITIES & ASYMMETRIC THREATS — Weapons, Blades, and Law
- **Chapter 05: Asymmetric Threats: Blades, Weapons, and Multiple Attackers**
  - *5.1 Edged Weapons, Reactionary Deficits, and Flanking*
  - *5.2 Immediate Action Drills on Weapon Presentation and Survival Capstone*
- **Chapter 06: The Ethical and Legal Boundaries of Power**
  - *6.1 Proportionality, Objective Reasonableness, and the Continuum of Force*
  - *6.2 Post-Incident Procedures: Medical, Exit, Legal Preservations, and Complete Capstone*

---

### BACK MATTER
- **Master Glossary of Combatives & Human Performance Engineering**
- **Annotated Scientific & Legal Bibliography**
- **About the Author**
"""

def assemble():
    section_files = get_section_files()
    print(f"[VOL 2] Discovered {len(section_files)} body section files.")
    assert len(section_files) == 13, f"Expected 13 section files, found {len(section_files)}"

    for f in FRONT_MATTER_FILES:
        assert f.exists(), f"Missing front matter: {f}"
    for f in BACK_MATTER_FILES:
        assert f.exists(), f"Missing back matter: {f}"

    parts_content = []

    # Front Matter Header
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- VOLUME 2: FRONT MATTER                     -->\n")
    parts_content.append("<!-- ========================================== -->\n\n")

    for f in FRONT_MATTER_FILES:
        content = f.read_text(encoding="utf-8").strip()
        parts_content.append(content)
        parts_content.append("\n\n---\n\n")

    # Volume 2 TOC
    parts_content.append(generate_vol2_toc())
    parts_content.append("\n\n---\n\n")

    # Body Sections
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- VOLUME 2: MANUSCRIPT BODY (PARTS I - IV)   -->\n")
    parts_content.append("<!-- ========================================== -->\n\n")
    for f in section_files:
        content = f.read_text(encoding="utf-8").strip()
        parts_content.append(content)
        parts_content.append("\n\n---\n\n")

    # Back Matter
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- VOLUME 2: BACK MATTER                      -->\n")
    parts_content.append("<!-- ========================================== -->\n\n")
    for f in BACK_MATTER_FILES:
        content = f.read_text(encoding="utf-8").strip()
        parts_content.append(content)
        parts_content.append("\n\n---\n\n")

    full_text = "".join(parts_content)
    OUTPUT_FILE.write_text(full_text, encoding="utf-8")
    print(f"Successfully compiled Volume 2 to: {OUTPUT_FILE}")

    words = len(full_text.split())
    lines = len(full_text.splitlines())
    bytes_count = len(full_text.encode("utf-8"))

    print(f"Volume 2 Metrics:")
    print(f"  - Words: {words:,}")
    print(f"  - Lines: {lines:,}")
    print(f"  - Bytes: {bytes_count:,}")
    print(f"  - Section Files: {len(section_files)}")

if __name__ == "__main__":
    assemble()
