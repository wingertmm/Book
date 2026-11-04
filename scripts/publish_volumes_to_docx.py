#!/usr/bin/env python3
"""
Publication Export Script: Two-Volume Editions
Exports:
1. Volume 1: Time, Distance, and Power — The Combat Doctrine -> exports/docx/TIME_DISTANCE_AND_POWER_VOL1_DOCTRINE.docx
2. Volume 2: The Machine Under Load — Stress, Conditioning, and Survival Realities -> exports/docx/TIME_DISTANCE_AND_POWER_VOL2_HUMAN_FACTOR.docx
"""

import sys
from pathlib import Path

# Configure utf-8 stdout
if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from docx.shared import Pt
from docx.enum.table import WD_TABLE_ALIGNMENT

# Import formatting infrastructure from existing publish script
from publish_chapters_to_docx import (
    create_document,
    add_header_footer,
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

def export_volume_1():
    print("\n[EXPORT] Exporting Volume 1: The Combat Doctrine (.docx)...")
    vol1_md = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_VOL1_DOCTRINE.md"
    if not vol1_md.exists():
        print("  ! Volume 1 markdown not found. Run assemble_volume_1.py first.")
        return None

    txt = vol1_md.read_text(encoding="utf-8")
    words = len(txt.split())

    doc = create_document()
    add_header_footer(doc, "Volume 1: The Combat Doctrine")

    # Header Card
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
    r1 = cp.add_run("TIME, DISTANCE, AND POWER: THE COMBAT DOCTRINE\n")
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

def export_volume_2():
    print("\n[EXPORT] Exporting Volume 2: The Machine Under Load (.docx)...")
    vol2_md = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_VOL2_HUMAN_FACTOR.md"
    if not vol2_md.exists():
        print("  ! Volume 2 markdown not found. Run assemble_volume_2.py first.")
        return None

    txt = vol2_md.read_text(encoding="utf-8")
    words = len(txt.split())

    doc = create_document()
    add_header_footer(doc, "Volume 2: The Machine Under Load")

    # Header Card
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

def main():
    v1 = export_volume_1()
    v2 = export_volume_2()

    print("\n" + "="*70)
    print("TWO-VOLUME WORD (.DOCX) EXPORT COMPLETE!")
    if v1:
        print(f"  - Volume 1: {v1.name}")
    if v2:
        print(f"  - Volume 2: {v2.name}")
    print(f"  - Destination: {EXPORTS_DIR}")
    print("="*70)

if __name__ == "__main__":
    main()
