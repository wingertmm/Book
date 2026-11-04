#!/usr/bin/env python3
"""
Assemble Volume 1 Manuscript: Time, Distance, and Power — The Combat Doctrine
Compiles:
- Volume 1 Front Matter
- Parts I through IV + Doctrinal Coda (32 section files)
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
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch08_principles_1_to_3",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch09_principles_4_to_6",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch10_principles_7_to_9",
    MANUSCRIPT_DIR / "part_03_the_11_principles" / "ch11_principles_10_to_11",
    MANUSCRIPT_DIR / "part_04_discipline_applications" / "ch12_taekwondo_and_long_range",
    MANUSCRIPT_DIR / "part_04_discipline_applications" / "ch13_muay_thai_and_medium_range",
    MANUSCRIPT_DIR / "part_04_discipline_applications" / "ch14_wrestling_and_clinch_to_takedown",
    MANUSCRIPT_DIR / "part_04_discipline_applications" / "ch15_brazilian_jiu_jitsu_and_ground_survival",
    MANUSCRIPT_DIR / "part_04_discipline_applications" / "ch16_range_transitions_and_fluid_synthesis",
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

---

### FRONT MATTER
- **Title Page & Copyright Notice**
- **Safety, Medical, and Legal Disclaimers**
- **Dedication**
- **Preface: The Genesis of the Martial Engineer**

---

### PART I: THE MECHANICAL ENGINE — Foundations of Combat Biomechanics
- **Chapter 01: The Triad: Time, Distance, and Power**
- **Chapter 02: The Four Ranges of Combat**
- **Chapter 03: Timing and Windows of Opportunity**

---

### PART II: STRATEGIC LENSES ON VIOLENCE — Military Doctrine Applied to Close Combat
- **Chapter 04: The Sun Tzu Lens: Asymmetric Strategy**
- **Chapter 05: The Airpower Lens: Boyd's OODA Loop on Concrete**
- **Chapter 06: The Ground Maneuver Lens: Armored Warfare Principles**

---

### PART III: THE 11 UNIFIED PRINCIPLES — Invariant Operational Laws
- **Chapter 07: Principles 1–3: Purpose, Security, and Maneuver**
- **Chapter 08: Principles 4–6: Initiative, Concentration, and Economy**
- **Chapter 09: Principles 7–9: Surprise, Avoidance, and Persistence**
- **Chapter 10: Principles 10–11: Dynamic Reflexes and Situational Knowledge**

---

### PART IV: DISCIPLINE APPLICATIONS ACROSS THE RANGES — Style Synthesis
- **Chapter 11: Taekwondo: The Long Range and Longest Lever**
- **Chapter 12: Muay Thai: Medium Range, Clinch, and Short Levers**
- **Chapter 13: Wrestling: Close Range, Tie-Ups, and Level Changes**
- **Chapter 14: Brazilian Jiu-Jitsu: Ground Survival and Structural Framing**
- **Chapter 15: Range Transitions and Fluid Synthesis**

---

### DOCTRINAL CODA & BRIDGE
- **The Invariant Principles and the Human Operator: The Five Invariant Laws**
- **Bridge to Volume 2: The Machine Under Load**

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
    assert len(section_files) == 40, f"Expected 40 section files, found {len(section_files)}"

    for f in FRONT_MATTER_FILES:
        assert f.exists(), f"Missing front matter: {f}"
    for f in BACK_MATTER_FILES:
        assert f.exists(), f"Missing back matter: {f}"

    parts_content = []

    # Front Matter Header
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- VOLUME 1: FRONT MATTER                     -->\n")
    parts_content.append("<!-- ========================================== -->\n\n")

    # Title & Legal
    for f in FRONT_MATTER_FILES:
        content = f.read_text(encoding="utf-8").strip()
        parts_content.append(content)
        parts_content.append("\n\n---\n\n")

    # Volume 1 TOC
    parts_content.append(generate_vol1_toc())
    parts_content.append("\n\n---\n\n")

    # Body Sections
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- VOLUME 1: MANUSCRIPT BODY (PARTS I - IV)   -->\n")
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
