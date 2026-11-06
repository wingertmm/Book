#!/usr/bin/env python3
"""
Assemble Volume 2 Manuscript: Timing, Distance, and Power — Discipline Applications
Compiles:
- Volume 2 Front Matter
- Part IV (Discipline Applications Across the Ranges) + Doctrinal Coda (11 section files)
- Volume 2 Back Matter
into manuscript/TIME_DISTANCE_AND_POWER_VOL2_DISCIPLINE_APPLICATIONS.md
"""

from pathlib import Path

REPO_ROOT = Path("C:/Book")
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"
OUTPUT_FILE = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_VOL2_DISCIPLINE_APPLICATIONS.md"

FRONT_MATTER_FILES = [
    MANUSCRIPT_DIR / "front_matter_volume_2" / "00_title_and_copyright_vol2.md",
    MANUSCRIPT_DIR / "front_matter_volume_2" / "01_preface_volume_2.md",
]

VOL2_BODY_DIRS = [
    MANUSCRIPT_DIR / "part_04_discipline_applications" / "ch12_taekwondo_and_long_range",
    MANUSCRIPT_DIR / "part_04_discipline_applications" / "ch13_muay_thai_and_medium_range",
    MANUSCRIPT_DIR / "part_04_discipline_applications" / "ch14_wrestling_and_clinch_to_takedown",
    MANUSCRIPT_DIR / "part_04_discipline_applications" / "ch15_brazilian_jiu_jitsu_and_ground_survival",
    MANUSCRIPT_DIR / "part_04_discipline_applications" / "ch16_range_transitions_and_fluid_synthesis",
    MANUSCRIPT_DIR / "volume_2_coda",
]

BACK_MATTER_FILES = [
    MANUSCRIPT_DIR / "back_matter" / "01_glossary.md",
    MANUSCRIPT_DIR / "back_matter" / "02_concept_register.md",
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
    return """# TABLE OF CONTENTS — VOLUME 2: DISCIPLINE APPLICATIONS

### FRONT MATTER
- **Title, Copyright & Disclaimers**
- **Preface: The Crucible of Physical Application**

---

### PART I: DISCIPLINE APPLICATIONS ACROSS THE COMBAT RANGES
- **Chapter 01: Taekwondo: The Long Range and Longest Lever**
  - 1.1 Distance as Active Shield and Mechanics of the Longest Lever
  - 1.2 Timing Windows, Interception, and Sport Traps on Concrete
- **Chapter 02: Muay Thai: Medium Range, Clinch, and Short Levers**
  - 2.1 Space Control, Framing, and Short-Lever Kinetic Shock
  - 2.2 The Thai Clinch, Cervical Manipulation, and Disengagement
- **Chapter 03: Wrestling: Close Range, Tie-Ups, and Level Changes**
  - 3.1 Posture, Dynamic Base, and Anti-Takedown Sprawl Architecture
  - 3.2 Upper-Body Tie-Ups, Pummeling, and Sport Traps
- **Chapter 04: Brazilian Jiu-Jitsu & SOCP: Ground Survival and Structural Framing**
  - 4.1 Structural Framing, Asymmetric Limb Control, and Danaher's Algorithm
  - 4.2 Beyond Blind Flight: Knee on Belly, Standing Joint Breaks, and SOCP Weapon Auditing
- **Chapter 05: Range Transitions and Fluid Synthesis**
  - 5.1 Range Chaining, Dynamic Bridges, and Penetration Flanks
  - 5.2 Dynamic Switching and Discipline Synthesis Capstone

---

### DOCTRINAL CODA & BRIDGE
- **The Invariant Principles and the Human Operator: The Five Invariant Laws**
- **Bridge to Volume 3: The Machine Under Load**

---

### BACK MATTER
- **Master Glossary of Combatives Engineering**
- **Concept Register & Cross-Index**
- **Annotated Military Bibliography**
- **About the Author**
"""


def assemble():
    section_files = get_section_files()
    print(f"[VOL 2] Discovered {len(section_files)} body section files.")
    assert len(section_files) == 11, f"Expected 11 section files, found {len(section_files)}"

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
    parts_content.append("<!-- VOLUME 2: MANUSCRIPT BODY (PART IV)        -->\n")
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
