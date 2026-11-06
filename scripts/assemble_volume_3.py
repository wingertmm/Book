#!/usr/bin/env python3
"""
Assemble Volume 3 Manuscript: Timing, Distance, and Power — The Machine Under Load
Compiles:
- Volume 3 Front Matter
- Parts V and VI (The Decision Engine & Training Doctrine) (13 section files)
- Volume 3 Back Matter
into manuscript/TIME_DISTANCE_AND_POWER_VOL3_HUMAN_FACTOR.md
"""

from pathlib import Path

REPO_ROOT = Path("C:/Book")
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"
OUTPUT_FILE = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_VOL3_HUMAN_FACTOR.md"

FRONT_MATTER_FILES = [
    MANUSCRIPT_DIR / "front_matter_volume_3" / "00_title_and_copyright_vol3.md",
    MANUSCRIPT_DIR / "front_matter_volume_3" / "01_preface_volume_3.md",
]

VOL3_BODY_DIRS = [
    MANUSCRIPT_DIR / "part_01_foundations" / "ch04_the_command_center",
    MANUSCRIPT_DIR / "part_05_the_decision_engine" / "ch17_the_4_step_cycle",
    MANUSCRIPT_DIR / "part_05_the_decision_engine" / "ch18_high_stress_physiology",
    MANUSCRIPT_DIR / "part_06_training_doctrine" / "ch19_neural_conditioning",
    MANUSCRIPT_DIR / "part_06_training_doctrine" / "ch20_asymmetric_threats",
    MANUSCRIPT_DIR / "part_06_training_doctrine" / "ch21_legal_and_ethical",
]

BACK_MATTER_FILES = [
    MANUSCRIPT_DIR / "back_matter" / "01_glossary.md",
    MANUSCRIPT_DIR / "back_matter" / "02_concept_register.md",
    MANUSCRIPT_DIR / "back_matter" / "03_annotated_bibliography.md",
    MANUSCRIPT_DIR / "back_matter" / "04_about_the_author.md",
]


def get_section_files():
    section_files = []
    for directory in VOL3_BODY_DIRS:
        if not directory.exists():
            raise FileNotFoundError(f"Directory missing: {directory}")
        sec_files = sorted([f for f in directory.glob("*.md") if not f.name.endswith("README.md")])
        for sec_file in sec_files:
            section_files.append(sec_file)
    return section_files


def generate_vol3_toc():
    return """# TABLE OF CONTENTS — VOLUME 3: THE MACHINE UNDER LOAD

### FRONT MATTER
- **Title, Copyright & Disclaimers**
- **Preface: The Meat and the Machine**

---

### PART I: THE DECISION ENGINE — Cognitive Processing under Lethal Threat
- **Chapter 01: The Command Center: Neurological Reality & The Dual-Brain Paradox**
  - 1.1 The Mind as Primary Weapon and the Dual-Brain Paradox
  - 1.2 Offloading to the Lizard Brain and Controlled Chaos
  - 1.3 The Iron Law and the Quality Constraint
- **Chapter 02: The 4-Step Cycle: Recognize, Prioritize, Choose, and Act**
  - 2.1 Recognize and Prioritize: Threat Classification under Stress
  - 2.2 Choose, Act, and Reassess: Closed-Loop Execution in Microseconds
- **Chapter 03: High-Stress Physiology: Surviving the Autonomic Cascade**
  - 3.1 The Sympathetic Surge: Tunnel Vision, Auditory Exclusion, and Tachypsychia
  - 3.2 Motor Degradation, The "Plan A" Trap, and Navy SEAL Arousal Inoculation

---

### PART II: TRAINING DOCTRINE & SURVIVAL REALITIES — Hardening the Operator
- **Chapter 04: Train Like You Fight: The Law of Neural Conditioning**
  - 4.1 Neural Conditioning and Permanence: Myelination and Motor Engrams
  - 4.2 The Stress Inoculation Ladder: From Slow Precision to Controlled Chaos
- **Chapter 05: Asymmetric Threats: Blades, Weapons, and Multiple Attackers**
  - 5.1 Edged Weapon Realities: Tactile Recognition and 2-on-1 Limb Control
  - 5.2 Flanking Multiple Opponents, Lanchester's Law, and CQB Fatal Funnels
- **Chapter 06: The Ethical and Legal Boundaries of Power**
  - 6.1 Proportionality, Objective Reasonableness, and Force Justification
  - 6.2 The Post-Incident Architecture and Master Book Capstone

---

### BACK MATTER
- **Master Glossary of Combatives Engineering**
- **Concept Register & Cross-Index**
- **Annotated Military Bibliography**
- **About the Author**
"""


def assemble():
    section_files = get_section_files()
    print(f"[VOL 3] Discovered {len(section_files)} body section files.")
    assert len(section_files) == 13, f"Expected 13 section files, found {len(section_files)}"

    for f in FRONT_MATTER_FILES:
        assert f.exists(), f"Missing front matter: {f}"
    for f in BACK_MATTER_FILES:
        assert f.exists(), f"Missing back matter: {f}"

    parts_content = []

    # Front Matter Header
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- VOLUME 3: FRONT MATTER                     -->\n")
    parts_content.append("<!-- ========================================== -->\n\n")

    for f in FRONT_MATTER_FILES:
        content = f.read_text(encoding="utf-8").strip()
        parts_content.append(content)
        parts_content.append("\n\n---\n\n")

    # Volume 3 TOC
    parts_content.append(generate_vol3_toc())
    parts_content.append("\n\n---\n\n")

    # Body Sections
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- VOLUME 3: MANUSCRIPT BODY (PARTS V - VI)   -->\n")
    parts_content.append("<!-- ========================================== -->\n\n")
    for f in section_files:
        content = f.read_text(encoding="utf-8").strip()
        parts_content.append(content)
        parts_content.append("\n\n---\n\n")

    # Back Matter
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- VOLUME 3: BACK MATTER                      -->\n")
    parts_content.append("<!-- ========================================== -->\n\n")
    for f in BACK_MATTER_FILES:
        content = f.read_text(encoding="utf-8").strip()
        parts_content.append(content)
        parts_content.append("\n\n---\n\n")

    full_text = "".join(parts_content)
    OUTPUT_FILE.write_text(full_text, encoding="utf-8")
    print(f"Successfully compiled Volume 3 to: {OUTPUT_FILE}")

    words = len(full_text.split())
    lines = len(full_text.splitlines())
    bytes_count = len(full_text.encode("utf-8"))

    print(f"Volume 3 Metrics:")
    print(f"  - Words: {words:,}")
    print(f"  - Lines: {lines:,}")
    print(f"  - Bytes: {bytes_count:,}")
    print(f"  - Section Files: {len(section_files)}")


if __name__ == "__main__":
    assemble()
