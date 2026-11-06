#!/usr/bin/env python3
"""
Publication Export Script: Three-Volume Editions
Exports:
1. Complete Volume 1: Timing, Distance, and Power — The Combat Doctrine
   -> exports/docx/TIME_DISTANCE_AND_POWER_VOL1_DOCTRINE.docx
2. Complete Volume 2: Timing, Distance, and Power — Discipline Applications
   -> exports/docx/TIME_DISTANCE_AND_POWER_VOL2_DISCIPLINE_APPLICATIONS.docx
3. Complete Volume 3: Timing, Distance, and Power — The Machine Under Load
   -> exports/docx/TIME_DISTANCE_AND_POWER_VOL3_HUMAN_FACTOR.docx
4. Volume 1 Individual Chapters in exports/docx/volume_1_chapters/
5. Volume 2 Individual Chapters in exports/docx/volume_2_chapters/
6. Volume 3 Individual Chapters in exports/docx/volume_3_chapters/
Prunes:
- Obsolete single-volume review file (TIME_DISTANCE_AND_POWER_COMPLETE_REVIEW.docx)
- Obsolete legacy chapters directory (exports/docx/chapters/)
"""

import sys
import shutil
from pathlib import Path

# Configure utf-8 stdout
if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

from publish_chapters_to_docx import (
    create_document,
    add_header_footer,
    add_metadata_card,
    set_cell_background,
    set_cell_borders,
    set_cell_margins,
    parse_markdown_to_docx,
    save_docx_safely,
    COLOR_PRIMARY_NAVY,
    COLOR_ACCENT_BLUE,
    COLOR_MUTED_GRAY,
    HEX_CARD_BG,
    HEX_CARD_BORDER,
    HEX_CALLOUT_BORDER,
)

REPO_ROOT = Path("C:/Book")
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"
EXPORTS_DIR = REPO_ROOT / "exports" / "docx"

VOL1_CHAPTERS_DIR = EXPORTS_DIR / "volume_1_chapters"
VOL2_CHAPTERS_DIR = EXPORTS_DIR / "volume_2_chapters"
VOL3_CHAPTERS_DIR = EXPORTS_DIR / "volume_3_chapters"

VOL1_CHAPTERS = [
    {
        "id": 1,
        "part_name": "Part I: Foundations of Close Combat — The Master Equation",
        "part_dir": "part_01_foundations",
        "chap_dir": "ch01_the_triad",
        "number_str": "Chapter 01",
        "title": "The Triad: Timing, Distance, and Power",
        "filename": "Chapter_01_The_Triad.docx",
    },
    {
        "id": 2,
        "part_name": "Part I: Foundations of Close Combat — The Master Equation",
        "part_dir": "part_01_foundations",
        "chap_dir": "ch02_the_four_ranges",
        "number_str": "Chapter 02",
        "title": "The Four Ranges of Combat",
        "filename": "Chapter_02_The_Four_Ranges.docx",
    },
    {
        "id": 3,
        "part_name": "Part I: Foundations of Close Combat — The Master Equation",
        "part_dir": "part_01_foundations",
        "chap_dir": "ch03_timing_and_windows",
        "number_str": "Chapter 03",
        "title": "Timing and Windows of Opportunity",
        "filename": "Chapter_03_Timing_and_Windows.docx",
    },
    {
        "id": 4,
        "part_name": "Part II: The Five Strategic Lenses — Historical & Doctrinal Predecessors",
        "part_dir": "part_02_strategic_lenses",
        "chap_dir": "ch05_the_sun_tzu_lens",
        "number_str": "Chapter 04",
        "title": "The Classical Asymmetric Lens: Sun Tzu's Philosophy of Violence",
        "filename": "Chapter_04_The_Sun_Tzu_Lens.docx",
    },
    {
        "id": 5,
        "part_name": "Part II: The Five Strategic Lenses — Historical & Doctrinal Predecessors",
        "part_dir": "part_02_strategic_lenses",
        "chap_dir": "ch06_the_airpower_lens",
        "number_str": "Chapter 05",
        "title": "The Airpower Lens: Boyd's Energy-Maneuverability and OODA on Concrete",
        "filename": "Chapter_05_The_Airpower_Lens.docx",
    },
    {
        "id": 6,
        "part_name": "Part II: The Five Strategic Lenses — Historical & Doctrinal Predecessors",
        "part_dir": "part_02_strategic_lenses",
        "chap_dir": "ch07_the_ground_maneuver_lens",
        "number_str": "Chapter 06",
        "title": "The Ground Maneuver Lens: Armored Warfare, Flanking, and Structural Security",
        "filename": "Chapter_06_The_Ground_Maneuver_Lens.docx",
    },
    {
        "id": 7,
        "part_name": "Part II: The Five Strategic Lenses — Historical & Doctrinal Predecessors",
        "part_dir": "part_02_strategic_lenses",
        "chap_dir": "ch07b_the_special_operations_lens",
        "number_str": "Chapter 07",
        "title": "The Special Operations Lens: 75th Rangers, Navy SEALs, and SOCP Doctrine",
        "filename": "Chapter_07_The_Special_Operations_Lens.docx",
    },
    {
        "id": 8,
        "part_name": "Part II: The Five Strategic Lenses — Historical & Doctrinal Predecessors",
        "part_dir": "part_02_strategic_lenses",
        "chap_dir": "ch07c_the_algorithmic_combatives_lens",
        "number_str": "Chapter 08",
        "title": "The Algorithmic Combatives Lens: John Danaher & Mechanical Geometry",
        "filename": "Chapter_08_The_Algorithmic_Combatives_Lens.docx",
    },
    {
        "id": 9,
        "part_name": "Part II: The Five Strategic Lenses — Historical & Doctrinal Predecessors",
        "part_dir": "part_02_strategic_lenses",
        "chap_dir": "ch07d_the_predecessor_synthesis",
        "number_str": "Chapter 09",
        "title": "The Strategic Predecessor Synthesis: How the 11 Principles Emerge",
        "filename": "Chapter_09_The_Predecessor_Synthesis.docx",
    },
    {
        "id": 10,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch10_principle_01_purpose_first",
        "number_str": "Chapter 10",
        "title": "Principle 1: Purpose First",
        "filename": "Chapter_10_Principle_01_Purpose_First.docx",
    },
    {
        "id": 11,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch11_principle_02_security_of_position",
        "number_str": "Chapter 11",
        "title": "Principle 2: Security of Position",
        "filename": "Chapter_11_Principle_02_Security_of_Position.docx",
    },
    {
        "id": 12,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch12_principle_03_maneuver_to_advantage",
        "number_str": "Chapter 12",
        "title": "Principle 3: Maneuver to Advantage",
        "filename": "Chapter_12_Principle_03_Maneuver_to_Advantage.docx",
    },
    {
        "id": 13,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch13_principle_04_initiative",
        "number_str": "Chapter 13",
        "title": "Principle 4: Initiative",
        "filename": "Chapter_13_Principle_04_Initiative.docx",
    },
    {
        "id": 14,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch14_principle_05_concentration",
        "number_str": "Chapter 14",
        "title": "Principle 5: Concentration",
        "filename": "Chapter_14_Principle_05_Concentration.docx",
    },
    {
        "id": 15,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch15_principle_06_economy_of_force",
        "number_str": "Chapter 15",
        "title": "Principle 6: Economy of Force",
        "filename": "Chapter_15_Principle_06_Economy_of_Force.docx",
    },
    {
        "id": 16,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch16_principle_07_surprise",
        "number_str": "Chapter 16",
        "title": "Principle 7: Surprise",
        "filename": "Chapter_16_Principle_07_Surprise.docx",
    },
    {
        "id": 17,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch17_principle_08_avoidance_when_superior",
        "number_str": "Chapter 17",
        "title": "Principle 8: Avoidance When Superior",
        "filename": "Chapter_17_Principle_08_Avoidance_When_Superior.docx",
    },
    {
        "id": 18,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch18_principle_09_persistence_to_resolution",
        "number_str": "Chapter 18",
        "title": "Principle 9: Persistence to Resolution",
        "filename": "Chapter_18_Principle_09_Persistence_to_Resolution.docx",
    },
    {
        "id": 19,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch19_principle_10_actions_on_contact",
        "number_str": "Chapter 19",
        "title": "Principle 10: Actions on Contact",
        "filename": "Chapter_19_Principle_10_Actions_on_Contact.docx",
    },
    {
        "id": 20,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch20_principle_11_know_the_situation",
        "number_str": "Chapter 20",
        "title": "Principle 11: Know the Situation",
        "filename": "Chapter_20_Principle_11_Know_the_Situation.docx",
    },
]

VOL2_CHAPTERS = [
    {
        "id": 1,
        "part_name": "Part I: Discipline Applications Across the Combat Ranges",
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch12_taekwondo_and_long_range",
        "number_str": "Chapter 01",
        "title": "Taekwondo: The Long Range and Longest Lever",
        "filename": "Chapter_01_Taekwondo_and_Long_Range.docx",
    },
    {
        "id": 2,
        "part_name": "Part I: Discipline Applications Across the Combat Ranges",
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch13_muay_thai_and_medium_range",
        "number_str": "Chapter 02",
        "title": "Muay Thai: Medium Range, Clinch, and Short Levers",
        "filename": "Chapter_02_Muay_Thai_and_Medium_Range.docx",
    },
    {
        "id": 3,
        "part_name": "Part I: Discipline Applications Across the Combat Ranges",
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch14_wrestling_and_clinch_to_takedown",
        "number_str": "Chapter 03",
        "title": "Wrestling: Close Range, Tie-Ups, and Level Changes",
        "filename": "Chapter_03_Wrestling_and_Clinch_to_Takedown.docx",
    },
    {
        "id": 4,
        "part_name": "Part I: Discipline Applications Across the Combat Ranges",
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch15_brazilian_jiu_jitsu_and_ground_survival",
        "number_str": "Chapter 04",
        "title": "Brazilian Jiu-Jitsu & SOCP: Ground Survival and Structural Framing",
        "filename": "Chapter_04_Brazilian_Jiu_Jitsu_and_Ground_Survival.docx",
    },
    {
        "id": 5,
        "part_name": "Part I: Discipline Applications Across the Combat Ranges",
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch16_range_transitions_and_fluid_synthesis",
        "number_str": "Chapter 05",
        "title": "Range Transitions and Fluid Synthesis",
        "filename": "Chapter_05_Range_Transitions_and_Fluid_Synthesis.docx",
    },
]

VOL3_CHAPTERS = [
    {
        "id": 1,
        "part_name": "Part I: The Biological Command Center — Neurological Reality Under Fire",
        "part_dir": "part_01_foundations",
        "chap_dir": "ch04_the_command_center",
        "number_str": "Chapter 01",
        "title": "The Command Center: Neurological Reality & The Dual-Brain Paradox",
        "filename": "Chapter_01_The_Command_Center.docx",
    },
    {
        "id": 2,
        "part_name": "Part I: The Biological Command Center — Neurological Reality Under Fire",
        "part_dir": "part_05_the_decision_engine",
        "chap_dir": "ch17_the_4_step_cycle",
        "number_str": "Chapter 02",
        "title": "The 4-Step Cycle: Recognize, Prioritize, Choose, and Act",
        "filename": "Chapter_02_The_4_Step_Cycle.docx",
    },
    {
        "id": 3,
        "part_name": "Part I: High-Stress Physiology — Surviving the Autonomic Cascade",
        "part_dir": "part_05_the_decision_engine",
        "chap_dir": "ch18_high_stress_physiology",
        "number_str": "Chapter 03",
        "title": "High-Stress Physiology: The Autonomic Cascade & Failure Modes",
        "filename": "Chapter_03_High_Stress_Physiology.docx",
    },
    {
        "id": 4,
        "part_name": "Part II: Training Doctrine & Survival Realities — Hardening the Operator",
        "part_dir": "part_06_training_doctrine",
        "chap_dir": "ch19_neural_conditioning",
        "number_str": "Chapter 04",
        "title": "Train Like You Fight: The Law of Neural Conditioning",
        "filename": "Chapter_04_Neural_Conditioning.docx",
    },
    {
        "id": 5,
        "part_name": "Part II: Training Doctrine & Survival Realities — Hardening the Operator",
        "part_dir": "part_06_training_doctrine",
        "chap_dir": "ch20_asymmetric_threats",
        "number_str": "Chapter 05",
        "title": "Asymmetric Threats: Blades, Weapons, and Multiple Attackers",
        "filename": "Chapter_05_Asymmetric_Threats.docx",
    },
    {
        "id": 6,
        "part_name": "Part II: Training Doctrine & Survival Realities — Hardening the Operator",
        "part_dir": "part_06_training_doctrine",
        "chap_dir": "ch21_legal_and_ethical",
        "number_str": "Chapter 06",
        "title": "The Ethical and Legal Boundaries of Power",
        "filename": "Chapter_06_Legal_and_Ethical_Boundaries.docx",
    },
]


def prune_legacy_exports():
    print("\n[PRUNE] Pruning obsolete single-volume exports and legacy folders...")
    legacy_files = [
        EXPORTS_DIR / "TIME_DISTANCE_AND_POWER_COMPLETE_REVIEW.docx",
        EXPORTS_DIR / "TIME_DISTANCE_AND_POWER_VOL2_HUMAN_FACTOR.docx",
    ]
    for lf in legacy_files:
        if lf.exists():
            try:
                lf.unlink()
                print(f"  [-] Removed obsolete file: {lf.name}")
            except Exception as e:
                print(f"  [!] Note on {lf.name}: {e}")

    legacy_chapters_dir = EXPORTS_DIR / "chapters"
    if legacy_chapters_dir.exists():
        for f in legacy_chapters_dir.glob("*.docx"):
            try:
                f.unlink()
            except Exception:
                pass
        try:
            legacy_chapters_dir.rmdir()
            print("  [-] Removed obsolete legacy directory: exports/docx/chapters/")
        except Exception:
            print("  [-] Emptied obsolete legacy directory: exports/docx/chapters/ (folder handle held by OS/Explorer)")

    # Prune stale chapter exports from earlier layouts
    valid_vol1 = {c["filename"] for c in VOL1_CHAPTERS} | {
        "00_Front_Matter_Vol1.docx",
        "21_Doctrinal_Coda_and_Bridge.docx",
        "22_Back_Matter_Vol1.docx",
    }
    if VOL1_CHAPTERS_DIR.exists():
        for f in VOL1_CHAPTERS_DIR.glob("*.docx"):
            if f.name not in valid_vol1:
                try:
                    f.unlink()
                    print(f"  [-] Pruned obsolete Vol 1 file: {f.name}")
                except Exception:
                    pass

    valid_vol2 = {c["filename"] for c in VOL2_CHAPTERS} | {
        "00_Front_Matter_Vol2.docx",
        "06_Doctrinal_Coda_and_Bridge.docx",
        "07_Back_Matter_Vol2.docx",
    }
    if VOL2_CHAPTERS_DIR.exists():
        for f in VOL2_CHAPTERS_DIR.glob("*.docx"):
            if f.name not in valid_vol2:
                try:
                    f.unlink()
                    print(f"  [-] Pruned obsolete Vol 2 file: {f.name}")
                except Exception:
                    pass

    valid_vol3 = {c["filename"] for c in VOL3_CHAPTERS} | {
        "00_Front_Matter_Vol3.docx",
        "07_Back_Matter_Vol3.docx",
    }
    if VOL3_CHAPTERS_DIR.exists():
        for f in VOL3_CHAPTERS_DIR.glob("*.docx"):
            if f.name not in valid_vol3:
                try:
                    f.unlink()
                    print(f"  [-] Pruned obsolete Vol 3 file: {f.name}")
                except Exception:
                    pass


def export_volume_1_complete():
    print("\n[EXPORT] Exporting Volume 1: The Combat Doctrine (.docx)...")
    vol1_md = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_VOL1_DOCTRINE.md"
    if not vol1_md.exists():
        print("  ! Volume 1 markdown not found. Run assemble_volume_1.py first.")
        return None

    txt = vol1_md.read_text(encoding="utf-8")
    words = len(txt.split())

    doc = create_document()
    add_header_footer(doc, "Volume 1: The Combat Doctrine")

    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, HEX_CARD_BG)
    set_cell_borders(
        cell,
        top={"sz": "8", "color": HEX_CARD_BORDER},
        bottom={"sz": "8", "color": HEX_CARD_BORDER},
        left={"sz": "24", "color": HEX_CALLOUT_BORDER},
        right={"sz": "8", "color": HEX_CARD_BORDER},
    )
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)

    cp = cell.paragraphs[0]
    r1 = cp.add_run("TIMING, DISTANCE, AND POWER: THE COMBAT DOCTRINE\n")
    r1.font.name = 'Calibri'
    r1.font.size = Pt(14)
    r1.bold = True
    r1.font.color.rgb = COLOR_PRIMARY_NAVY

    r2 = cp.add_run(f"Volume 1 Complete Edition — {words:,} words\n")
    r2.font.name = 'Calibri'
    r2.font.size = Pt(10)
    r2.bold = True
    r2.font.color.rgb = COLOR_ACCENT_BLUE

    r3 = cp.add_run("Foundations, Strategic Lenses, and the 11 Invariant Principles  |  Author: Michael M. Wingert")
    r3.font.name = 'Calibri'
    r3.font.size = Pt(9.0)
    r3.italic = True
    r3.font.color.rgb = COLOR_MUTED_GRAY

    parse_markdown_to_docx(doc, txt)

    out_file = EXPORTS_DIR / "TIME_DISTANCE_AND_POWER_VOL1_DOCTRINE.docx"
    saved = save_docx_safely(doc, out_file)
    size_kb = saved.stat().st_size / 1024 if saved and saved.exists() else 0
    print(f"  [OK] {saved.name} ({words:,} words, {size_kb:.1f} KB)")
    return saved


def export_volume_2_complete():
    print("\n[EXPORT] Exporting Volume 2: Discipline Applications (.docx)...")
    vol2_md = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_VOL2_DISCIPLINE_APPLICATIONS.md"
    if not vol2_md.exists():
        print("  ! Volume 2 markdown not found. Run assemble_volume_2.py first.")
        return None

    txt = vol2_md.read_text(encoding="utf-8")
    words = len(txt.split())

    doc = create_document()
    add_header_footer(doc, "Volume 2: Discipline Applications")

    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, HEX_CARD_BG)
    set_cell_borders(
        cell,
        top={"sz": "8", "color": HEX_CARD_BORDER},
        bottom={"sz": "8", "color": HEX_CARD_BORDER},
        left={"sz": "24", "color": HEX_CALLOUT_BORDER},
        right={"sz": "8", "color": HEX_CARD_BORDER},
    )
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)

    cp = cell.paragraphs[0]
    r1 = cp.add_run("DISCIPLINE APPLICATIONS: BIOMECHANICAL RANGE SYNTHESIS\n")
    r1.font.name = 'Calibri'
    r1.font.size = Pt(14)
    r1.bold = True
    r1.font.color.rgb = COLOR_PRIMARY_NAVY

    r2 = cp.add_run(f"Volume 2 Complete Edition — {words:,} words\n")
    r2.font.name = 'Calibri'
    r2.font.size = Pt(10)
    r2.bold = True
    r2.font.color.rgb = COLOR_ACCENT_BLUE

    r3 = cp.add_run("Biomechanical Synthesis Across the Combat Ranges  |  Author: Michael M. Wingert")
    r3.font.name = 'Calibri'
    r3.font.size = Pt(9.0)
    r3.italic = True
    r3.font.color.rgb = COLOR_MUTED_GRAY

    parse_markdown_to_docx(doc, txt)

    out_file = EXPORTS_DIR / "TIME_DISTANCE_AND_POWER_VOL2_DISCIPLINE_APPLICATIONS.docx"
    saved = save_docx_safely(doc, out_file)
    size_kb = saved.stat().st_size / 1024 if saved and saved.exists() else 0
    print(f"  [OK] {saved.name} ({words:,} words, {size_kb:.1f} KB)")
    return saved


def export_volume_3_complete():
    print("\n[EXPORT] Exporting Volume 3: The Machine Under Load (.docx)...")
    vol3_md = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_VOL3_HUMAN_FACTOR.md"
    if not vol3_md.exists():
        print("  ! Volume 3 markdown not found. Run assemble_volume_3.py first.")
        return None

    txt = vol3_md.read_text(encoding="utf-8")
    words = len(txt.split())

    doc = create_document()
    add_header_footer(doc, "Volume 3: The Machine Under Load")

    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, HEX_CARD_BG)
    set_cell_borders(
        cell,
        top={"sz": "8", "color": HEX_CARD_BORDER},
        bottom={"sz": "8", "color": HEX_CARD_BORDER},
        left={"sz": "24", "color": HEX_CALLOUT_BORDER},
        right={"sz": "8", "color": HEX_CARD_BORDER},
    )
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)

    cp = cell.paragraphs[0]
    r1 = cp.add_run("THE MACHINE UNDER LOAD: STRESS, CONDITIONING, AND SURVIVAL REALITIES\n")
    r1.font.name = 'Calibri'
    r1.font.size = Pt(14)
    r1.bold = True
    r1.font.color.rgb = COLOR_PRIMARY_NAVY

    r2 = cp.add_run(f"Volume 3 Complete Edition — {words:,} words\n")
    r2.font.name = 'Calibri'
    r2.font.size = Pt(10)
    r2.bold = True
    r2.font.color.rgb = COLOR_ACCENT_BLUE

    r3 = cp.add_run("Human Factors Engineering in Close Combat  |  Author: Michael M. Wingert")
    r3.font.name = 'Calibri'
    r3.font.size = Pt(9.0)
    r3.italic = True
    r3.font.color.rgb = COLOR_MUTED_GRAY

    parse_markdown_to_docx(doc, txt)

    out_file = EXPORTS_DIR / "TIME_DISTANCE_AND_POWER_VOL3_HUMAN_FACTOR.docx"
    saved = save_docx_safely(doc, out_file)
    size_kb = saved.stat().st_size / 1024 if saved and saved.exists() else 0
    print(f"  [OK] {saved.name} ({words:,} words, {size_kb:.1f} KB)")
    return saved


def export_chapter_list(chapters, target_dir, volume_label):
    target_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n[EXPORT] Exporting {volume_label} Chapters to: {target_dir.name}...")

    count = 0
    for ch in chapters:
        chap_dir_path = MANUSCRIPT_DIR / ch["part_dir"] / ch["chap_dir"]
        section_files = sorted([f for f in chap_dir_path.glob("*.md") if not f.name.endswith("README.md")])

        total_words = 0
        section_texts = []
        for sf in section_files:
            txt = sf.read_text(encoding="utf-8")
            total_words += len(txt.split())
            section_texts.append(txt)

        doc = create_document()
        add_header_footer(doc, f"{ch['number_str']}: {ch['title']}")

        add_metadata_card(
            doc,
            chapter_num=f"{volume_label} — {ch['number_str']}",
            chapter_title=ch["title"],
            part_name=ch["part_name"],
            section_count=len(section_files),
            word_count=total_words,
        )

        for idx, sec_text in enumerate(section_texts):
            if idx > 0:
                div_p = doc.add_paragraph()
                div_p.paragraph_format.space_before = Pt(12)
                div_p.paragraph_format.space_after = Pt(12)
                drun = div_p.add_run("· · ·  SECTION TRANSITION  · · ·")
                drun.font.name = 'Calibri'
                drun.font.size = Pt(9.0)
                drun.italic = True
                drun.font.color.rgb = COLOR_MUTED_GRAY
                div_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

            parse_markdown_to_docx(doc, sec_text, is_first_section=(idx == 0))

        out_path = target_dir / ch["filename"]
        saved_path = save_docx_safely(doc, out_path)
        size_kb = saved_path.stat().st_size / 1024 if saved_path and saved_path.exists() else 0
        print(f"  [OK] {ch['number_str']}: {ch['title'][:40]:<40} -> {saved_path.name} ({total_words:,} words, {size_kb:.1f} KB)")
        count += 1

    return count


def export_vol1_coda_and_matters():
    # 1. Vol 1 Coda
    coda_file = MANUSCRIPT_DIR / "volume_1_coda" / "01_the_five_invariant_laws_of_the_human_operator.md"
    if coda_file.exists():
        doc = create_document()
        add_header_footer(doc, "Doctrinal Coda: The Invariant Principles & Trilogy Bridge")
        txt = coda_file.read_text(encoding="utf-8")
        words = len(txt.split())
        parse_markdown_to_docx(doc, txt)
        out_path = VOL1_CHAPTERS_DIR / "21_Doctrinal_Coda_and_Bridge.docx"
        saved = save_docx_safely(doc, out_path)
        size_kb = saved.stat().st_size / 1024 if saved and saved.exists() else 0
        print(f"  [OK] Volume 1 Coda -> {saved.name} ({words:,} words, {size_kb:.1f} KB)")

    # 2. Vol 1 Front Matter
    from assemble_volume_1 import generate_vol1_toc
    doc_fm = create_document()
    add_header_footer(doc_fm, "Volume 1: Front Matter & TOC")
    fm_texts = [
        (MANUSCRIPT_DIR / "front_matter" / "00_title_and_copyright.md").read_text(encoding="utf-8"),
        (MANUSCRIPT_DIR / "front_matter" / "01_dedication.md").read_text(encoding="utf-8"),
        (MANUSCRIPT_DIR / "front_matter" / "02_foreword_and_preface.md").read_text(encoding="utf-8"),
        generate_vol1_toc(),
    ]
    words_fm = sum(len(t.split()) for t in fm_texts)
    parse_markdown_to_docx(doc_fm, "\n\n---\n\n".join(fm_texts))
    out_fm = VOL1_CHAPTERS_DIR / "00_Front_Matter_Vol1.docx"
    saved_fm = save_docx_safely(doc_fm, out_fm)
    size_fm = saved_fm.stat().st_size / 1024 if saved_fm and saved_fm.exists() else 0
    print(f"  [OK] Volume 1 Front Matter -> {saved_fm.name} ({words_fm:,} words, {size_fm:.1f} KB)")

    # 3. Vol 1 Back Matter
    doc_bm = create_document()
    add_header_footer(doc_bm, "Volume 1: Back Matter & Glossary")
    bm_files = [
        MANUSCRIPT_DIR / "back_matter" / "01_glossary.md",
        MANUSCRIPT_DIR / "back_matter" / "02_concept_register.md",
        MANUSCRIPT_DIR / "back_matter" / "03_annotated_bibliography.md",
        MANUSCRIPT_DIR / "back_matter" / "04_about_the_author.md",
    ]
    bm_texts = [f.read_text(encoding="utf-8") for f in bm_files if f.exists()]
    words_bm = sum(len(t.split()) for t in bm_texts)
    parse_markdown_to_docx(doc_bm, "\n\n---\n\n".join(bm_texts))
    out_bm = VOL1_CHAPTERS_DIR / "22_Back_Matter_Vol1.docx"
    saved_bm = save_docx_safely(doc_bm, out_bm)
    size_bm = saved_bm.stat().st_size / 1024 if saved_bm and saved_bm.exists() else 0
    print(f"  [OK] Volume 1 Back Matter -> {saved_bm.name} ({words_bm:,} words, {size_bm:.1f} KB)")


def export_vol2_coda_and_matters():
    # 1. Vol 2 Coda
    coda_file = MANUSCRIPT_DIR / "volume_2_coda" / "01_the_five_invariant_laws_of_the_human_operator.md"
    if coda_file.exists():
        doc = create_document()
        add_header_footer(doc, "Doctrinal Coda: The Five Invariant Laws")
        txt = coda_file.read_text(encoding="utf-8")
        words = len(txt.split())
        parse_markdown_to_docx(doc, txt)
        out_path = VOL2_CHAPTERS_DIR / "06_Doctrinal_Coda_and_Bridge.docx"
        saved = save_docx_safely(doc, out_path)
        size_kb = saved.stat().st_size / 1024 if saved and saved.exists() else 0
        print(f"  [OK] Volume 2 Coda -> {saved.name} ({words:,} words, {size_kb:.1f} KB)")

    # 2. Vol 2 Front Matter
    from assemble_volume_2 import generate_vol2_toc
    doc_fm = create_document()
    add_header_footer(doc_fm, "Volume 2: Front Matter & TOC")
    fm_texts = [
        (MANUSCRIPT_DIR / "front_matter_volume_2" / "00_title_and_copyright_vol2.md").read_text(encoding="utf-8"),
        (MANUSCRIPT_DIR / "front_matter_volume_2" / "01_preface_volume_2.md").read_text(encoding="utf-8"),
        generate_vol2_toc(),
    ]
    words_fm = sum(len(t.split()) for t in fm_texts)
    parse_markdown_to_docx(doc_fm, "\n\n---\n\n".join(fm_texts))
    out_fm = VOL2_CHAPTERS_DIR / "00_Front_Matter_Vol2.docx"
    saved_fm = save_docx_safely(doc_fm, out_fm)
    size_fm = saved_fm.stat().st_size / 1024 if saved_fm and saved_fm.exists() else 0
    print(f"  [OK] Volume 2 Front Matter -> {saved_fm.name} ({words_fm:,} words, {size_fm:.1f} KB)")

    # 3. Vol 2 Back Matter
    doc_bm = create_document()
    add_header_footer(doc_bm, "Volume 2: Back Matter & Glossary")
    bm_files = [
        MANUSCRIPT_DIR / "back_matter" / "01_glossary.md",
        MANUSCRIPT_DIR / "back_matter" / "02_concept_register.md",
        MANUSCRIPT_DIR / "back_matter" / "03_annotated_bibliography.md",
        MANUSCRIPT_DIR / "back_matter" / "04_about_the_author.md",
    ]
    bm_texts = [f.read_text(encoding="utf-8") for f in bm_files if f.exists()]
    words_bm = sum(len(t.split()) for t in bm_texts)
    parse_markdown_to_docx(doc_bm, "\n\n---\n\n".join(bm_texts))
    out_bm = VOL2_CHAPTERS_DIR / "07_Back_Matter_Vol2.docx"
    saved_bm = save_docx_safely(doc_bm, out_bm)
    size_bm = saved_bm.stat().st_size / 1024 if saved_bm and saved_bm.exists() else 0
    print(f"  [OK] Volume 2 Back Matter -> {saved_bm.name} ({words_bm:,} words, {size_bm:.1f} KB)")


def export_vol3_matters():
    from assemble_volume_3 import generate_vol3_toc

    # 1. Vol 3 Front Matter
    doc_fm = create_document()
    add_header_footer(doc_fm, "Volume 3: Front Matter & TOC")
    fm_texts = [
        (MANUSCRIPT_DIR / "front_matter_volume_3" / "00_title_and_copyright_vol3.md").read_text(encoding="utf-8"),
        (MANUSCRIPT_DIR / "front_matter_volume_3" / "01_preface_volume_3.md").read_text(encoding="utf-8"),
        generate_vol3_toc(),
    ]
    words_fm = sum(len(t.split()) for t in fm_texts)
    parse_markdown_to_docx(doc_fm, "\n\n---\n\n".join(fm_texts))
    out_fm = VOL3_CHAPTERS_DIR / "00_Front_Matter_Vol3.docx"
    saved_fm = save_docx_safely(doc_fm, out_fm)
    size_fm = saved_fm.stat().st_size / 1024 if saved_fm and saved_fm.exists() else 0
    print(f"  [OK] Volume 3 Front Matter -> {saved_fm.name} ({words_fm:,} words, {size_fm:.1f} KB)")

    # 2. Vol 3 Back Matter
    doc_bm = create_document()
    add_header_footer(doc_bm, "Volume 3: Back Matter & Glossary")
    bm_files = [
        MANUSCRIPT_DIR / "back_matter" / "01_glossary.md",
        MANUSCRIPT_DIR / "back_matter" / "02_concept_register.md",
        MANUSCRIPT_DIR / "back_matter" / "03_annotated_bibliography.md",
        MANUSCRIPT_DIR / "back_matter" / "04_about_the_author.md",
    ]
    bm_texts = [f.read_text(encoding="utf-8") for f in bm_files if f.exists()]
    words_bm = sum(len(t.split()) for t in bm_texts)
    parse_markdown_to_docx(doc_bm, "\n\n---\n\n".join(bm_texts))
    out_bm = VOL3_CHAPTERS_DIR / "07_Back_Matter_Vol3.docx"
    saved_bm = save_docx_safely(doc_bm, out_bm)
    size_bm = saved_bm.stat().st_size / 1024 if saved_bm and saved_bm.exists() else 0
    print(f"  [OK] Volume 3 Back Matter -> {saved_bm.name} ({words_bm:,} words, {size_bm:.1f} KB)")


def main():
    prune_legacy_exports()

    # Complete Volume Exports
    export_volume_1_complete()
    export_volume_2_complete()
    export_volume_3_complete()

    # Individual Chapter Exports
    export_chapter_list(VOL1_CHAPTERS, VOL1_CHAPTERS_DIR, "Volume 1")
    export_vol1_coda_and_matters()

    export_chapter_list(VOL2_CHAPTERS, VOL2_CHAPTERS_DIR, "Volume 2")
    export_vol2_coda_and_matters()

    export_chapter_list(VOL3_CHAPTERS, VOL3_CHAPTERS_DIR, "Volume 3")
    export_vol3_matters()

    print("\n" + "=" * 70)
    print("THREE-VOLUME PUBLICATION EXPORT COMPLETE!")
    print(f"  - Complete Volumes:  3 documents in {EXPORTS_DIR}")
    print(f"  - Volume 1 Chapters: 23 documents in {VOL1_CHAPTERS_DIR.name}")
    print(f"  - Volume 2 Chapters: 8 documents in {VOL2_CHAPTERS_DIR.name}")
    print(f"  - Volume 3 Chapters: 8 documents in {VOL3_CHAPTERS_DIR.name}")
    print("=" * 70)


if __name__ == "__main__":
    main()
