#!/usr/bin/env python3
"""
Publication Export Script: Two-Volume Editions
Exports:
1. Complete Volume 1: Timing, Distance, and Power — The Combat Doctrine -> exports/docx/TIME_DISTANCE_AND_POWER_VOL1_DOCTRINE.docx
2. Complete Volume 2: The Machine Under Load — Stress, Conditioning, and Survival Realities -> exports/docx/TIME_DISTANCE_AND_POWER_VOL2_HUMAN_FACTOR.docx
3. Volume 1 Individual Chapters in exports/docx/volume_1_chapters/
4. Volume 2 Individual Chapters in exports/docx/volume_2_chapters/
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

# Import formatting infrastructure from existing publish script
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

VOL1_CHAPTERS = [
    {
        "id": 1,
        "part_name": "Part I: The Mechanical Engine — Foundations of Combat Biomechanics",
        "part_dir": "part_01_foundations",
        "chap_dir": "ch01_the_triad",
        "number_str": "Chapter 01",
        "title": "The Triad: Timing, Distance, and Power",
        "filename": "Chapter_01_The_Triad.docx",
    },
    {
        "id": 2,
        "part_name": "Part I: The Mechanical Engine — Foundations of Combat Biomechanics",
        "part_dir": "part_01_foundations",
        "chap_dir": "ch02_the_four_ranges",
        "number_str": "Chapter 02",
        "title": "The Four Ranges of Combat",
        "filename": "Chapter_02_The_Four_Ranges.docx",
    },
    {
        "id": 3,
        "part_name": "Part I: The Mechanical Engine — Foundations of Combat Biomechanics",
        "part_dir": "part_01_foundations",
        "chap_dir": "ch03_timing_and_windows",
        "number_str": "Chapter 03",
        "title": "Timing and Windows of Opportunity",
        "filename": "Chapter_03_Timing_and_Windows.docx",
    },
    {
        "id": 4,
        "part_name": "Part II: Strategic Lenses on Violence — Military Doctrine Applied to Close Combat",
        "part_dir": "part_02_strategic_lenses",
        "chap_dir": "ch05_the_sun_tzu_lens",
        "number_str": "Chapter 04",
        "title": "The Sun Tzu Lens: Asymmetric Strategy",
        "filename": "Chapter_04_The_Sun_Tzu_Lens.docx",
    },
    {
        "id": 5,
        "part_name": "Part II: Strategic Lenses on Violence — Military Doctrine Applied to Close Combat",
        "part_dir": "part_02_strategic_lenses",
        "chap_dir": "ch06_the_airpower_lens",
        "number_str": "Chapter 05",
        "title": "The Airpower Lens: Boyd's OODA Loop on Concrete",
        "filename": "Chapter_05_The_Airpower_Lens.docx",
    },
    {
        "id": 6,
        "part_name": "Part II: Strategic Lenses on Violence — Military Doctrine Applied to Close Combat",
        "part_dir": "part_02_strategic_lenses",
        "chap_dir": "ch07_the_ground_maneuver_lens",
        "number_str": "Chapter 06",
        "title": "The Ground Maneuver Lens: Armored Warfare Principles",
        "filename": "Chapter_06_The_Ground_Maneuver_Lens.docx",
    },
    {
        "id": 7,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch08_principles_1_to_3",
        "number_str": "Chapter 07",
        "title": "Principles 1–3: Purpose, Security, and Maneuver",
        "filename": "Chapter_07_Principles_1_to_3.docx",
    },
    {
        "id": 8,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch09_principles_4_to_6",
        "number_str": "Chapter 08",
        "title": "Principles 4–6: Initiative, Concentration, and Economy",
        "filename": "Chapter_08_Principles_4_to_6.docx",
    },
    {
        "id": 9,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch10_principles_7_to_9",
        "number_str": "Chapter 09",
        "title": "Principles 7–9: Surprise, Avoidance, and Persistence",
        "filename": "Chapter_09_Principles_7_to_9.docx",
    },
    {
        "id": 10,
        "part_name": "Part III: The 11 Unified Principles — Invariant Operational Laws",
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch11_principles_10_to_11",
        "number_str": "Chapter 10",
        "title": "Principles 10–11: Dynamic Reflexes and Situational Knowledge",
        "filename": "Chapter_10_Principles_10_to_11.docx",
    },
    {
        "id": 11,
        "part_name": "Part IV: Discipline Applications Across the Ranges — Style Synthesis",
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch12_taekwondo_and_long_range",
        "number_str": "Chapter 11",
        "title": "Taekwondo: The Long Range and Longest Lever",
        "filename": "Chapter_11_Taekwondo_and_Long_Range.docx",
    },
    {
        "id": 12,
        "part_name": "Part IV: Discipline Applications Across the Ranges — Style Synthesis",
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch13_muay_thai_and_medium_range",
        "number_str": "Chapter 12",
        "title": "Muay Thai: Medium Range, Clinch, and Short Levers",
        "filename": "Chapter_12_Muay_Thai_and_Medium_Range.docx",
    },
    {
        "id": 13,
        "part_name": "Part IV: Discipline Applications Across the Ranges — Style Synthesis",
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch14_wrestling_and_clinch_to_takedown",
        "number_str": "Chapter 13",
        "title": "Wrestling: Close Range, Tie-Ups, and Level Changes",
        "filename": "Chapter_13_Wrestling_and_Clinch_to_Takedown.docx",
    },
    {
        "id": 14,
        "part_name": "Part IV: Discipline Applications Across the Ranges — Style Synthesis",
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch15_brazilian_jiu_jitsu_and_ground_survival",
        "number_str": "Chapter 14",
        "title": "Brazilian Jiu-Jitsu: Ground Survival and Structural Framing",
        "filename": "Chapter_14_Brazilian_Jiu_Jitsu_and_Ground_Survival.docx",
    },
    {
        "id": 15,
        "part_name": "Part IV: Discipline Applications Across the Ranges — Style Synthesis",
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch16_range_transitions_and_fluid_synthesis",
        "number_str": "Chapter 15",
        "title": "Range Transitions and Fluid Synthesis",
        "filename": "Chapter_15_Range_Transitions_and_Fluid_Synthesis.docx",
    },
]

VOL2_CHAPTERS = [
    {
        "id": 1,
        "part_name": "Part I: The Biological Command Center — Neurological Reality Under Fire",
        "part_dir": "part_01_foundations",
        "chap_dir": "ch04_the_command_center",
        "number_str": "Chapter 01",
        "title": "The Command Center: Neurological Reality Under Fire",
        "filename": "Chapter_01_The_Command_Center.docx",
    },
    {
        "id": 2,
        "part_name": "Part I: The Biological Command Center — Neurological Reality Under Fire",
        "part_dir": "part_05_the_decision_engine",
        "chap_dir": "ch17_the_4_step_cycle",
        "number_str": "Chapter 02",
        "title": "The 4-Step Cycle: Recognize, Prioritize, Choose, Act",
        "filename": "Chapter_02_The_4_Step_Cycle.docx",
    },
    {
        "id": 3,
        "part_name": "Part II: High-Stress Physiology — Surviving the Autonomic Surge",
        "part_dir": "part_05_the_decision_engine",
        "chap_dir": "ch18_high_stress_physiology",
        "number_str": "Chapter 03",
        "title": "High-Stress Physiology: Surviving the Autonomic Cascade",
        "filename": "Chapter_03_High_Stress_Physiology.docx",
    },
    {
        "id": 4,
        "part_name": "Part III: The Science of Neural Conditioning — Training Doctrine",
        "part_dir": "part_06_training_doctrine",
        "chap_dir": "ch19_neural_conditioning",
        "number_str": "Chapter 04",
        "title": "Train Like You Fight: The Law of Neural Conditioning",
        "filename": "Chapter_04_Neural_Conditioning.docx",
    },
    {
        "id": 5,
        "part_name": "Part IV: Survival Realities & Asymmetric Threats — Weapons, Blades, and Law",
        "part_dir": "part_06_training_doctrine",
        "chap_dir": "ch20_asymmetric_threats",
        "number_str": "Chapter 05",
        "title": "Asymmetric Threats: Blades, Weapons, and Multiple Attackers",
        "filename": "Chapter_05_Asymmetric_Threats.docx",
    },
    {
        "id": 6,
        "part_name": "Part IV: Survival Realities & Asymmetric Threats — Weapons, Blades, and Law",
        "part_dir": "part_06_training_doctrine",
        "chap_dir": "ch21_legal_and_ethical",
        "number_str": "Chapter 06",
        "title": "The Ethical and Legal Boundaries of Power",
        "filename": "Chapter_06_Legal_and_Ethical_Boundaries.docx",
    },
]

def prune_legacy_exports():
    print("\n[PRUNE] Pruning obsolete single-volume exports and legacy folders...")
    legacy_file = EXPORTS_DIR / "TIME_DISTANCE_AND_POWER_COMPLETE_REVIEW.docx"
    if legacy_file.exists():
        try:
            legacy_file.unlink()
            print(f"  [-] Removed obsolete single-volume file: {legacy_file.name}")
        except Exception as e:
            print(f"  [!] Note on {legacy_file.name}: {e}")

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

    r2 = cp.add_run(f"Volume 1 Review Edition — {words:,} words\n")
    r2.font.name = 'Calibri'
    r2.font.size = Pt(10)
    r2.bold = True
    r2.font.color.rgb = COLOR_ACCENT_BLUE

    r3 = cp.add_run("Principles, Strategy, and Mechanics  |  Parts I – IV & Doctrinal Coda  |  Author: Michael M. Wingert")
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
    print("\n[EXPORT] Exporting Volume 2: The Machine Under Load (.docx)...")
    vol2_md = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_VOL2_HUMAN_FACTOR.md"
    if not vol2_md.exists():
        print("  ! Volume 2 markdown not found. Run assemble_volume_2.py first.")
        return None

    txt = vol2_md.read_text(encoding="utf-8")
    words = len(txt.split())

    doc = create_document()
    add_header_footer(doc, "Volume 2: The Machine Under Load")

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

    r2 = cp.add_run(f"Volume 2 Review Edition — {words:,} words\n")
    r2.font.name = 'Calibri'
    r2.font.size = Pt(10)
    r2.bold = True
    r2.font.color.rgb = COLOR_ACCENT_BLUE

    r3 = cp.add_run("Human Systems Engineering in Close Combat  |  Parts I – IV  |  Author: Michael M. Wingert")
    r3.font.name = 'Calibri'
    r3.font.size = Pt(9.0)
    r3.italic = True
    r3.font.color.rgb = COLOR_MUTED_GRAY

    parse_markdown_to_docx(doc, txt)

    out_file = EXPORTS_DIR / "TIME_DISTANCE_AND_POWER_VOL2_HUMAN_FACTOR.docx"
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
        add_header_footer(doc, "Doctrinal Coda: The Five Invariant Laws")
        txt = coda_file.read_text(encoding="utf-8")
        words = len(txt.split())
        parse_markdown_to_docx(doc, txt)
        out_path = VOL1_CHAPTERS_DIR / "16_Doctrinal_Coda_and_Bridge.docx"
        saved = save_docx_safely(doc, out_path)
        size_kb = saved.stat().st_size / 1024 if saved and saved.exists() else 0
        print(f"  [OK] Doctrinal Coda -> {saved.name} ({words:,} words, {size_kb:.1f} KB)")

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
    for idx, t in enumerate(fm_texts):
        parse_markdown_to_docx(doc_fm, t)
        if idx < len(fm_texts) - 1:
            doc_fm.add_page_break()
    out_fm = VOL1_CHAPTERS_DIR / "00_Front_Matter_Vol1.docx"
    saved_fm = save_docx_safely(doc_fm, out_fm)
    print(f"  [OK] Volume 1 Front Matter -> {saved_fm.name}")

    # 3. Vol 1 Back Matter
    doc_bm = create_document()
    add_header_footer(doc_bm, "Volume 1: Back Matter")
    bm_files = [
        MANUSCRIPT_DIR / "back_matter" / "01_glossary.md",
        MANUSCRIPT_DIR / "back_matter" / "02_concept_register.md",
        MANUSCRIPT_DIR / "back_matter" / "03_annotated_bibliography.md",
        MANUSCRIPT_DIR / "back_matter" / "04_about_the_author.md",
    ]
    for idx, f in enumerate(bm_files):
        parse_markdown_to_docx(doc_bm, f.read_text(encoding="utf-8"))
        if idx < len(bm_files) - 1:
            doc_bm.add_page_break()
    out_bm = VOL1_CHAPTERS_DIR / "17_Back_Matter_Vol1.docx"
    saved_bm = save_docx_safely(doc_bm, out_bm)
    print(f"  [OK] Volume 1 Back Matter -> {saved_bm.name}")

def export_vol2_matters():
    # Vol 2 Front Matter
    from assemble_volume_2 import generate_vol2_toc
    doc_fm = create_document()
    add_header_footer(doc_fm, "Volume 2: Front Matter & TOC")
    fm_texts = [
        (MANUSCRIPT_DIR / "front_matter_volume_2" / "00_title_and_copyright_vol2.md").read_text(encoding="utf-8"),
        (MANUSCRIPT_DIR / "front_matter_volume_2" / "01_preface_volume_2.md").read_text(encoding="utf-8"),
        generate_vol2_toc(),
    ]
    for idx, t in enumerate(fm_texts):
        parse_markdown_to_docx(doc_fm, t)
        if idx < len(fm_texts) - 1:
            doc_fm.add_page_break()
    out_fm = VOL2_CHAPTERS_DIR / "00_Front_Matter_Vol2.docx"
    saved_fm = save_docx_safely(doc_fm, out_fm)
    print(f"  [OK] Volume 2 Front Matter -> {saved_fm.name}")

    # Vol 2 Back Matter
    doc_bm = create_document()
    add_header_footer(doc_bm, "Volume 2: Back Matter")
    bm_files = [
        MANUSCRIPT_DIR / "back_matter" / "01_glossary.md",
        MANUSCRIPT_DIR / "back_matter" / "03_annotated_bibliography.md",
        MANUSCRIPT_DIR / "back_matter" / "04_about_the_author.md",
    ]
    for idx, f in enumerate(bm_files):
        parse_markdown_to_docx(doc_bm, f.read_text(encoding="utf-8"))
        if idx < len(bm_files) - 1:
            doc_bm.add_page_break()
    out_bm = VOL2_CHAPTERS_DIR / "07_Back_Matter_Vol2.docx"
    saved_bm = save_docx_safely(doc_bm, out_bm)
    print(f"  [OK] Volume 2 Back Matter -> {saved_bm.name}")

def main():
    prune_legacy_exports()

    v1 = export_volume_1_complete()
    v2 = export_volume_2_complete()

    c1 = export_chapter_list(VOL1_CHAPTERS, VOL1_CHAPTERS_DIR, "Vol 1")
    export_vol1_coda_and_matters()

    c2 = export_chapter_list(VOL2_CHAPTERS, VOL2_CHAPTERS_DIR, "Vol 2")
    export_vol2_matters()

    print("\n" + "="*70)
    print("TWO-VOLUME PUBLICATION EXPORT & PRUNING COMPLETE!")
    print(f"  - Complete Volumes:  2 documents in {EXPORTS_DIR}")
    print(f"  - Volume 1 Chapters: {c1 + 3} documents in {VOL1_CHAPTERS_DIR.name}")
    print(f"  - Volume 2 Chapters: {c2 + 2} documents in {VOL2_CHAPTERS_DIR.name}")
    print("="*70)

if __name__ == "__main__":
    main()
