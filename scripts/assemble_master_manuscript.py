#!/usr/bin/env python3
"""
Assemble Master Manuscript Script for Timing, Distance, and Power
Compiles:
- 4 Front Matter files
- 52 Section files across 6 Parts (in canonical order)
- 4 Back Matter files
into manuscript/TIME_DISTANCE_AND_POWER_MASTER.md
"""

import os
from pathlib import Path

REPO_ROOT = Path("C:/Book")
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"
OUTPUT_FILE = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_MASTER.md"

FRONT_MATTER_FILES = [
    MANUSCRIPT_DIR / "front_matter" / "00_title_and_copyright.md",
    MANUSCRIPT_DIR / "front_matter" / "01_dedication.md",
    MANUSCRIPT_DIR / "front_matter" / "02_foreword_and_preface.md",
    MANUSCRIPT_DIR / "front_matter" / "03_table_of_contents.md",
]

BACK_MATTER_FILES = [
    MANUSCRIPT_DIR / "back_matter" / "01_glossary.md",
    MANUSCRIPT_DIR / "back_matter" / "02_concept_register.md",
    MANUSCRIPT_DIR / "back_matter" / "03_annotated_bibliography.md",
    MANUSCRIPT_DIR / "back_matter" / "04_about_the_author.md",
]

PART_DIRS = [
    MANUSCRIPT_DIR / "part_01_foundations",
    MANUSCRIPT_DIR / "part_02_strategic_lenses",
    MANUSCRIPT_DIR / "part_03_the_11_principles",
    MANUSCRIPT_DIR / "part_04_discipline_applications",
    MANUSCRIPT_DIR / "part_05_the_decision_engine",
    MANUSCRIPT_DIR / "part_06_training_doctrine",
]

def get_section_files():
    section_files = []
    for part_dir in PART_DIRS:
        if not part_dir.exists():
            raise FileNotFoundError(f"Part directory missing: {part_dir}")
        chapter_dirs = sorted([d for d in part_dir.iterdir() if d.is_dir()])
        for chap_dir in chapter_dirs:
            sec_files = sorted([f for f in chap_dir.glob("*.md") if not f.name.endswith("README.md")])
            for sec_file in sec_files:
                section_files.append(sec_file)
    return section_files

def assemble():
    section_files = get_section_files()
    print(f"Discovered {len(section_files)} section files.")
    assert len(section_files) == 57, f"Expected 57 section files, found {len(section_files)}"

    for f in FRONT_MATTER_FILES:
        assert f.exists(), f"Missing front matter: {f}"
    for f in BACK_MATTER_FILES:
        assert f.exists(), f"Missing back matter: {f}"

    total_files = len(FRONT_MATTER_FILES) + len(section_files) + len(BACK_MATTER_FILES)
    print(f"Total compilation units: {total_files}")

    parts_content = []

    # Front Matter
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- FRONT MATTER                               -->\n")
    parts_content.append("<!-- ========================================== -->\n\n")
    for f in FRONT_MATTER_FILES:
        content = f.read_text(encoding="utf-8").strip()
        parts_content.append(content)
        parts_content.append("\n\n---\n\n")

    # Body Sections
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- MANUSCRIPT BODY (PARTS I - VI)             -->\n")
    parts_content.append("<!-- ========================================== -->\n\n")
    for idx, f in enumerate(section_files, start=1):
        content = f.read_text(encoding="utf-8").strip()
        parts_content.append(content)
        parts_content.append("\n\n---\n\n")

    # Back Matter
    parts_content.append("<!-- ========================================== -->\n")
    parts_content.append("<!-- BACK MATTER                                -->\n")
    parts_content.append("<!-- ========================================== -->\n\n")
    for f in BACK_MATTER_FILES:
        content = f.read_text(encoding="utf-8").strip()
        parts_content.append(content)
        parts_content.append("\n\n---\n\n")

    full_text = "".join(parts_content)

    OUTPUT_FILE.write_text(full_text, encoding="utf-8")
    print(f"Successfully compiled master manuscript to: {OUTPUT_FILE}")

    words = len(full_text.split())
    lines = len(full_text.splitlines())
    bytes_count = len(full_text.encode("utf-8"))

    print(f"Master Manuscript Metrics:")
    print(f"  - Words: {words:,}")
    print(f"  - Lines: {lines:,}")
    print(f"  - Bytes: {bytes_count:,}")
    print(f"  - Total Files Merged: {total_files}")

if __name__ == "__main__":
    assemble()
