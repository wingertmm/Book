#!/usr/bin/env python3
"""
Assemble Volume 1 Manuscript: Timing, Distance, and Power — The Combat Doctrine
Compiles:
- Volume 1 Front Matter
- Parts I through III + Doctrinal Coda (35 section files)
- Volume 1 Back Matter
into manuscript/TIME_DISTANCE_AND_POWER_VOL1_DOCTRINE.md
"""

from pathlib import Path

REPO_ROOT = Path("C:/Book")
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"
OUTPUT_FILE = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_VOL1_DOCTRINE.md"

FRONT_MATTER_FILES = [
    MANUSCRIPT_DIR / "front_matter" / "00_title_and_copyright.md",
    MANUSCRIPT_DIR / "front_matter" / "01_dedication.md",
    MANUSCRIPT_DIR / "front_matter" / "02_foreword_and_preface.md",
]

VOL1_BODY_DIRS = [
    MANUSCRIPT_DIR / "part_01_foundations" / "ch01_the_triad",
    MANUSCRIPT_DIR / "part_01_foundations" / "ch02_the_four_ranges",
    MANUSCRIPT_DIR / "part_01_foundations" / "ch03_timing_and_windows",
    MANUSCRIPT_DIR / "part_02_strategic_lenses" / "ch05_the_sun_tzu_lens",
    MANUSCRIPT_DIR / "part_02_strategic_lenses" / "ch06_the_airpower_lens",
    MANUSCRIPT_DIR / "part_02_strategic_lenses" / "ch07_the_ground_maneuver_lens",
    MANUSCRIPT_DIR / "part_02_strategic_lenses" / "ch07b_the_special_operations_lens",
    MANUSCRIPT_DIR / "part_02_strategic_lenses" / "ch07c_the_algorithmic_combatives_lens",
    MANUSCRIPT_DIR / "part_02_strategic_lenses" / "ch07d_the_predecessor_synthesis",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch10_principle_01_purpose_first",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch11_principle_02_security_of_position",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch12_principle_03_maneuver_to_advantage",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch13_principle_04_initiative",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch14_principle_05_concentration",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch15_principle_06_economy_of_force",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch16_principle_07_surprise",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch17_principle_08_avoidance_when_superior",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch18_principle_09_persistence_to_resolution",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch19_principle_10_immediate_action",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch20_principle_11_situational_awareness",
    MANUSCRIPT_DIR / "volume_1_coda",
]

BACK_MATTER_FILES = [
    MANUSCRIPT_DIR / "back_matter" / "01_glossary.md",
    MANUSCRIPT_DIR / "back_matter" / "02_concept_register.md",
    MANUSCRIPT_DIR / "back_matter" / "03_annotated_bibliography.md",
    MANUSCRIPT_DIR / "back_matter" / "04_about_the_author.md",
]


def get_section_files():
    section_files = []
    for directory in VOL1_BODY_DIRS:
        if not directory.exists():
            raise FileNotFoundError(f"Directory missing: {directory}")
        sec_files = sorted([f for f in directory.glob("*.md") if not f.name.endswith("README.md")])
        for sec_file in sec_files:
            section_files.append(sec_file)
    return section_files


def generate_vol1_toc():
    return """# TABLE OF CONTENTS — VOLUME 1: THE COMBAT DOCTRINE

### FRONT MATTER
- **Title, Copyright & Disclaimers**
- **Dedication**
- **Foreword & Preface**

---

### PART I: FOUNDATIONS OF CLOSE COMBAT — The Master Equation
- **Chapter 01: The Triad: Timing, Distance, and Power**
- **Chapter 02: The Four Ranges of Combat**
- **Chapter 03: Timing and Windows of Opportunity**

---

### PART II: THE FIVE STRATEGIC LENSES — Historical & Doctrinal Predecessors
- **Chapter 04: The Classical Asymmetric Lens: Sun Tzu's Philosophy of Violence**
- **Chapter 05: The Airpower Lens: Boyd's Energy-Maneuverability and OODA on Concrete**
- **Chapter 06: The Ground Maneuver Lens: Armored Warfare, Flanking, and Structural Security**
- **Chapter 07: The Special Operations Lens: 75th Rangers, Navy SEALs, and SOCP Doctrine**
- **Chapter 08: The Algorithmic Combatives Lens: John Danaher & Mechanical Geometry**
- **Chapter 09: The Strategic Predecessor Synthesis: How the 11 Principles Emerge**

---

### PART III: THE 11 UNIFIED PRINCIPLES — Invariant Operational Laws
- **Chapter 10: Principle 1: Purpose First**
- **Chapter 11: Principle 2: Security of Position**
- **Chapter 12: Principle 3: Maneuver to Advantage**
- **Chapter 13: Principle 4: Initiative**
- **Chapter 14: Principle 5: Concentration**
- **Chapter 15: Principle 6: Economy of Force**
- **Chapter 16: Principle 7: Surprise**
- **Chapter 17: Principle 8: Avoidance When Superior**
- **Chapter 18: Principle 9: Persistence to Resolution**
- **Chapter 19: Principle 10: Immediate Action**
- **Chapter 20: Principle 11: Situational Awareness**

---

### DOCTRINAL CODA & TRILOGY BRIDGE
- **The Invariant Principles and the Trilogy Road Ahead**
- **Bridge to Volume 2 (Discipline Applications) and Volume 3 (The Machine Under Load)**

---

### BACK MATTER
- **Master Glossary of Combatives Engineering**
- **Concept Register & Cross-Index**
- **Annotated Military Bibliography**
- **About the Author**
"""


def assemble():
    section_files = get_section_files()
    print(f"[VOL 1] Discovered {len(section_files)} body section files.")
    assert len(section_files) == 35, f"Expected 35 section files, found {len(section_files)}"

    for f in FRONT_MATTER_FILES:
        assert f.exists(), f"Missing front matter: {f}"
    for f in BACK_MATTER_FILES:
        assert f.exists(), f"Missing back matter: {f}"

    parts_content = []

    # Front Matter Header
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- VOLUME 1: FRONT MATTER                     -->\n")
    parts_content.append("<!-- ========================================== -->\n\n")

    for f in FRONT_MATTER_FILES:
        content = f.read_text(encoding="utf-8").strip()
        parts_content.append(content)
        parts_content.append("\n\n---\n\n")

    # Volume 1 TOC
    parts_content.append(generate_vol1_toc())
    parts_content.append("\n\n---\n\n")

    # Body Sections
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- VOLUME 1: MANUSCRIPT BODY (PARTS I - III)  -->\n")
    parts_content.append("<!-- ========================================== -->\n\n")
    for f in section_files:
        content = f.read_text(encoding="utf-8").strip()
        parts_content.append(content)
        parts_content.append("\n\n---\n\n")

    # Back Matter
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- VOLUME 1: BACK MATTER                      -->\n")
    parts_content.append("<!-- ========================================== -->\n\n")
    for f in BACK_MATTER_FILES:
        content = f.read_text(encoding="utf-8").strip()
        parts_content.append(content)
        parts_content.append("\n\n---\n\n")

    full_text = "".join(parts_content)
    OUTPUT_FILE.write_text(full_text, encoding="utf-8")
    print(f"Successfully compiled Volume 1 to: {OUTPUT_FILE}")

    words = len(full_text.split())
    lines = len(full_text.splitlines())
    bytes_count = len(full_text.encode("utf-8"))

    print(f"Volume 1 Metrics:")
    print(f"  - Words: {words:,}")
    print(f"  - Lines: {lines:,}")
    print(f"  - Bytes: {bytes_count:,}")
    print(f"  - Section Files: {len(section_files)}")


if __name__ == "__main__":
    assemble()
