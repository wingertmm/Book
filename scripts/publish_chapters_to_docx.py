#!/usr/bin/env python3
"""
Publication Export Script: Timing, Distance, and Power
Exports the manuscript to Microsoft Word (.docx) format for review and editing:
1. Individual Chapter Documents (Chapters 01 - 21) in exports/docx/chapters/
2. Front Matter Document in exports/docx/chapters/00_Front_Matter.docx
3. Back Matter Document in exports/docx/chapters/22_Back_Matter.docx
4. Complete Master Volume in exports/docx/TIME_DISTANCE_AND_POWER_MASTER_REVIEW.docx

Each document features:
- Review & Editorial Metadata Card on Page 1
- Professional typography (Calibri/Georgia, 1.2 line spacing, 1-inch margins)
- Styled Callout Boxes (quarantined math/physics/legal models in shaded boxes with thick left accent border)
- Styled Markdown Tables with shaded headers and clean borders
- Styled Monospace Blocks for ASCII diagrams preserving alignment
- Running Headers and Footers with dynamic Word page number fields
"""

import os
import re
import sys
import glob
from pathlib import Path

# Configure utf-8 stdout to avoid cp1252 charmap errors on Windows
if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

REPO_ROOT = Path("C:/Book")
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"
EXPORTS_DIR = REPO_ROOT / "exports" / "docx"
CHAPTERS_EXPORT_DIR = EXPORTS_DIR / "chapters"

# Colors
COLOR_PRIMARY_NAVY = RGBColor(26, 54, 93)     # #1A365D - Title / Heading 1
COLOR_ACCENT_BLUE   = RGBColor(43, 108, 176)   # #2B6CB0 - Section / Heading 2
COLOR_DARK_SLATE    = RGBColor(45, 55, 72)     # #2D3748 - Subsection / Heading 3
COLOR_BODY_TEXT     = RGBColor(45, 55, 72)     # #2D3748 - Normal Body
COLOR_MUTED_GRAY    = RGBColor(113, 128, 150)  # #718096 - Metadata & Footers
COLOR_CAUTION_RED   = RGBColor(197, 48, 48)    # #C53030 - Caution Callouts

HEX_CALLOUT_BG      = "F7FAFC"
HEX_CALLOUT_BORDER  = "2B6CB0"
HEX_CAUTION_BG      = "FFF5F5"
HEX_CAUTION_BORDER  = "C53030"
HEX_TABLE_HEADER_BG = "2B6CB0"
HEX_TABLE_ROW_ALT   = "F7FAFC"
HEX_TABLE_BORDER    = "CBD5E0"
HEX_CARD_BG         = "EDF2F7"
HEX_CARD_BORDER     = "A0AEC0"
HEX_CODE_BG         = "F8FAFC"
HEX_CODE_BORDER     = "E2E8F0"

PART_NAMES = {
    "part_01_foundations": "Part I: The Mechanical Engine — Foundations of Combat Biomechanics",
    "part_02_strategic_lenses": "Part II: Strategic Lenses on Violence — Military Doctrine Applied to Close Combat",
    "part_03_the_11_principles": "Part III: The 11 Unified Principles — Invariant Operational Laws",
    "part_04_discipline_applications": "Part IV: Discipline Applications Across the Ranges — Style Synthesis",
    "part_05_the_decision_engine": "Part V: The Tactical Decision Engine — High-Stress Processing",
    "part_06_training_doctrine": "Part VI: Training Doctrine & Survival Realities — Neural Conditioning & Survival",
}

CHAPTER_METADATA = [
    {
        "id": 1,
        "part_dir": "part_01_foundations",
        "chap_dir": "ch01_the_triad",
        "number_str": "Chapter 01",
        "title": "The Triad: Timing, Distance, and Power",
        "filename": "Chapter_01_The_Triad.docx",
    },
    {
        "id": 2,
        "part_dir": "part_01_foundations",
        "chap_dir": "ch02_the_four_ranges",
        "number_str": "Chapter 02",
        "title": "The Four Ranges of Combat",
        "filename": "Chapter_02_The_Four_Ranges.docx",
    },
    {
        "id": 3,
        "part_dir": "part_01_foundations",
        "chap_dir": "ch03_timing_and_windows",
        "number_str": "Chapter 03",
        "title": "Timing and Windows of Opportunity",
        "filename": "Chapter_03_Timing_and_Windows.docx",
    },
    {
        "id": 4,
        "part_dir": "part_01_foundations",
        "chap_dir": "ch04_the_command_center",
        "number_str": "Chapter 04",
        "title": "The Command Center: Neurological Reality Under Fire",
        "filename": "Chapter_04_The_Command_Center.docx",
    },
    {
        "id": 5,
        "part_dir": "part_02_strategic_lenses",
        "chap_dir": "ch05_the_sun_tzu_lens",
        "number_str": "Chapter 05",
        "title": "The Sun Tzu Lens: Asymmetric Strategy",
        "filename": "Chapter_05_The_Sun_Tzu_Lens.docx",
    },
    {
        "id": 6,
        "part_dir": "part_02_strategic_lenses",
        "chap_dir": "ch06_the_airpower_lens",
        "number_str": "Chapter 06",
        "title": "The Airpower Lens: Boyd's OODA Loop on Concrete",
        "filename": "Chapter_06_The_Airpower_Lens.docx",
    },
    {
        "id": 7,
        "part_dir": "part_02_strategic_lenses",
        "chap_dir": "ch07_the_ground_maneuver_lens",
        "number_str": "Chapter 07",
        "title": "The Ground Maneuver Lens: Armored Warfare Principles",
        "filename": "Chapter_07_The_Ground_Maneuver_Lens.docx",
    },
    {
        "id": 8,
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch08_principles_1_to_3",
        "number_str": "Chapter 08",
        "title": "Principles 1–3: Purpose, Security, and Maneuver",
        "filename": "Chapter_08_Principles_1_to_3.docx",
    },
    {
        "id": 9,
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch09_principles_4_to_6",
        "number_str": "Chapter 09",
        "title": "Principles 4–6: Initiative, Concentration, and Economy",
        "filename": "Chapter_09_Principles_4_to_6.docx",
    },
    {
        "id": 10,
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch10_principles_7_to_9",
        "number_str": "Chapter 10",
        "title": "Principles 7–9: Surprise, Avoidance, and Persistence",
        "filename": "Chapter_10_Principles_7_to_9.docx",
    },
    {
        "id": 11,
        "part_dir": "part_03_the_11_principles",
        "chap_dir": "ch11_principles_10_to_11",
        "number_str": "Chapter 11",
        "title": "Principles 10–11: Dynamic Reflexes and Situational Knowledge",
        "filename": "Chapter_11_Principles_10_to_11.docx",
    },
    {
        "id": 12,
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch12_taekwondo_and_long_range",
        "number_str": "Chapter 12",
        "title": "Taekwondo: The Long Range and Longest Lever",
        "filename": "Chapter_12_Taekwondo_and_Long_Range.docx",
    },
    {
        "id": 13,
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch13_muay_thai_and_medium_range",
        "number_str": "Chapter 13",
        "title": "Muay Thai: Medium Range, Clinch, and Short Levers",
        "filename": "Chapter_13_Muay_Thai_and_Medium_Range.docx",
    },
    {
        "id": 14,
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch14_wrestling_and_clinch_to_takedown",
        "number_str": "Chapter 14",
        "title": "Wrestling: Close Range, Tie-Ups, and Level Changes",
        "filename": "Chapter_14_Wrestling_and_Clinch_to_Takedown.docx",
    },
    {
        "id": 15,
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch15_brazilian_jiu_jitsu_and_ground_survival",
        "number_str": "Chapter 15",
        "title": "Brazilian Jiu-Jitsu: Ground Survival and Structural Framing",
        "filename": "Chapter_15_Brazilian_Jiu_Jitsu_and_Ground_Survival.docx",
    },
    {
        "id": 16,
        "part_dir": "part_04_discipline_applications",
        "chap_dir": "ch16_range_transitions_and_fluid_synthesis",
        "number_str": "Chapter 16",
        "title": "Range Transitions and Fluid Synthesis",
        "filename": "Chapter_16_Range_Transitions_and_Fluid_Synthesis.docx",
    },
    {
        "id": 17,
        "part_dir": "part_05_the_decision_engine",
        "chap_dir": "ch17_the_4_step_cycle",
        "number_str": "Chapter 17",
        "title": "The 4-Step Cycle: Recognize, Prioritize, Choose, Act",
        "filename": "Chapter_17_The_4_Step_Cycle.docx",
    },
    {
        "id": 18,
        "part_dir": "part_05_the_decision_engine",
        "chap_dir": "ch18_high_stress_physiology",
        "number_str": "Chapter 18",
        "title": "High-Stress Physiology: Surviving the Autonomic Cascade",
        "filename": "Chapter_18_High_Stress_Physiology.docx",
    },
    {
        "id": 19,
        "part_dir": "part_06_training_doctrine",
        "chap_dir": "ch19_neural_conditioning",
        "number_str": "Chapter 19",
        "title": "Train Like You Fight: The Law of Neural Conditioning",
        "filename": "Chapter_19_Neural_Conditioning.docx",
    },
    {
        "id": 20,
        "part_dir": "part_06_training_doctrine",
        "chap_dir": "ch20_asymmetric_threats",
        "number_str": "Chapter 20",
        "title": "Asymmetric Threats: Blades, Weapons, and Multiple Attackers",
        "filename": "Chapter_20_Asymmetric_Threats.docx",
    },
    {
        "id": 21,
        "part_dir": "part_06_training_doctrine",
        "chap_dir": "ch21_legal_and_ethical",
        "number_str": "Chapter 21",
        "title": "The Ethical and Legal Boundaries of Power",
        "filename": "Chapter_21_Legal_and_Ethical_Boundaries.docx",
    },
]

# Formatting Helpers
def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    tcPr = cell._tc.get_or_add_tcPr()
    borders_xml = f'<w:tcBorders {nsdecls("w")}>\n'
    for side, val in [("top", top), ("bottom", bottom), ("left", left), ("right", right)]:
        if val is None or val == "none":
            borders_xml += f'  <w:{side} w:val="none"/>\n'
        else:
            sz = val.get("sz", "12")
            color = val.get("color", "CBD5E0")
            style = val.get("style", "single")
            borders_xml += f'  <w:{side} w:val="{style}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
    borders_xml += '</w:tcBorders>'
    tcPr.append(parse_xml(borders_xml))

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def add_footer_page_number(run):
    fld = OxmlElement('w:fldSimple')
    fld.set(qn('w:instr'), 'PAGE')
    run._r.append(fld)

def parse_inlines_to_runs(p, text, default_color=COLOR_BODY_TEXT, font_size=11.0, is_callout=False):
    """
    Parses bold, italic, inline code, and inline math into docx runs.
    """
    # Tokenize inline patterns:
    # 1. ***bold italic***
    # 2. **bold**
    # 3. *italic*
    # 4. `code`
    # 5. $math$
    pattern = re.compile(
        r'(\*\*\*.*?\*\*\*|\*\*.*?\*\*|\*[^\*\n]+?\*|`.*?`|\$.*?\$)'
    )
    
    tokens = pattern.split(text)
    for token in tokens:
        if not token:
            continue
        
        run = p.add_run()
        run.font.name = 'Calibri'
        run.font.size = Pt(font_size)
        run.font.color.rgb = default_color
        
        if token.startswith('***') and token.endswith('***') and len(token) >= 6:
            inner = token[3:-3]
            run.text = inner
            run.bold = True
            run.italic = True
        elif token.startswith('**') and token.endswith('**') and len(token) >= 4:
            inner = token[2:-2]
            run.text = inner
            run.bold = True
        elif token.startswith('*') and token.endswith('*') and len(token) >= 2:
            inner = token[1:-1]
            run.text = inner
            run.italic = True
        elif token.startswith('`') and token.endswith('`') and len(token) >= 2:
            inner = token[1:-1]
            run.text = inner
            run.font.name = 'Consolas'
            run.font.size = Pt(font_size - 0.5)
            run.font.color.rgb = COLOR_PRIMARY_NAVY
        elif token.startswith('$') and token.endswith('$') and len(token) >= 2:
            inner = token[1:-1]
            # Clean common LaTeX macros for clean reading
            clean_math = inner.replace('\\text{', '').replace('}', '')
            clean_math = clean_math.replace('\\mathbf{', '').replace('\\vec{', '')
            clean_math = clean_math.replace('\\times', '×').replace('\\approx', '≈')
            clean_math = clean_math.replace('\\to', '→').replace('\\cdot', '·')
            clean_math = clean_math.replace('\\Delta', 'Δ').replace('\\tau', 'τ')
            clean_math = clean_math.replace('\\int', '∫').replace('\\frac', '')
            run.text = clean_math
            run.font.name = 'Georgia'
            run.italic = True
            run.font.color.rgb = COLOR_ACCENT_BLUE
        else:
            run.text = token

def create_document():
    doc = docx.Document()
    
    # 1-inch margins
    for sec in doc.sections:
        sec.top_margin = Inches(1.0)
        sec.bottom_margin = Inches(1.0)
        sec.left_margin = Inches(1.0)
        sec.right_margin = Inches(1.0)
        sec.header_distance = Inches(0.5)
        sec.footer_distance = Inches(0.5)
        
    return doc

def add_header_footer(doc, header_title, sub_title="Review & Editorial Draft"):
    sec = doc.sections[0]
    
    # Header
    hdr = sec.header
    hp = hdr.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run(f"Timing, Distance, and Power  |  {header_title}")
    hrun.font.name = 'Calibri'
    hrun.font.size = Pt(8.5)
    hrun.font.color.rgb = COLOR_MUTED_GRAY
    
    # Footer
    ftr = sec.footer
    fp = ftr.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    frun1 = fp.add_run("Draft for Editorial Review & Commentary (Frozen Master)                Page ")
    frun1.font.name = 'Calibri'
    frun1.font.size = Pt(8.5)
    frun1.font.color.rgb = COLOR_MUTED_GRAY
    add_footer_page_number(frun1)

def add_metadata_card(doc, chapter_num, chapter_title, part_name, section_count, word_count):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, HEX_CARD_BG)
    set_cell_borders(cell, 
                     top={"sz": "8", "color": HEX_CARD_BORDER},
                     bottom={"sz": "8", "color": HEX_CARD_BORDER},
                     left={"sz": "24", "color": HEX_CALLOUT_BORDER},
                     right={"sz": "8", "color": HEX_CARD_BORDER})
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    cp = cell.paragraphs[0]
    cp.paragraph_format.space_before = Pt(0)
    cp.paragraph_format.space_after = Pt(4)
    cp.paragraph_format.line_spacing = 1.15
    
    r1 = cp.add_run(f"MANUSCRIPT REVIEW EDITION — {chapter_num.upper()}\n")
    r1.font.name = 'Calibri'
    r1.font.size = Pt(9.5)
    r1.bold = True
    r1.font.color.rgb = COLOR_PRIMARY_NAVY
    
    r2 = cp.add_run(f"{chapter_title}\n")
    r2.font.name = 'Calibri'
    r2.font.size = Pt(14)
    r2.bold = True
    r2.font.color.rgb = COLOR_PRIMARY_NAVY
    
    r3 = cp.add_run(f"{part_name}\n")
    r3.font.name = 'Calibri'
    r3.font.size = Pt(9.5)
    r3.italic = True
    r3.font.color.rgb = COLOR_MUTED_GRAY
    
    r4 = cp.add_run(f"Metrics: {word_count:,} words  |  {section_count} Sections  |  Status: Frozen (Gate 3C Complete)\n")
    r4.font.name = 'Calibri'
    r4.font.size = Pt(9.0)
    r4.bold = True
    r4.font.color.rgb = COLOR_DARK_SLATE
    
    r5 = cp.add_run("Editorial Notes: This chapter is formatted for manuscript review and line-editing. Margins (1.0 in) and line spacing (1.2) provide space for Track Changes, margin comments, and queries. Callout boxes isolate formal engineering and legal models.")
    r5.font.name = 'Calibri'
    r5.font.size = Pt(8.5)
    r5.italic = True
    r5.font.color.rgb = COLOR_MUTED_GRAY

    # Add space after card
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(6)

def render_callout_box(doc, callout_type, lines):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    
    is_caution = "CAUTION" in callout_type or "WARNING" in callout_type
    bg_color = HEX_CAUTION_BG if is_caution else HEX_CALLOUT_BG
    border_color = HEX_CAUTION_BORDER if is_caution else HEX_CALLOUT_BORDER
    title_color = COLOR_CAUTION_RED if is_caution else COLOR_ACCENT_BLUE
    
    set_cell_background(cell, bg_color)
    set_cell_borders(cell, left={"sz": "24", "color": border_color})
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    # Process lines inside callout
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    
    for idx, line in enumerate(lines):
        if idx > 0:
            p = cell.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.15
            
        parse_inlines_to_runs(p, line, default_color=COLOR_DARK_SLATE, font_size=10.0, is_callout=True)

def render_table(doc, table_lines):
    # Parse table lines
    rows = []
    for l in table_lines:
        clean = l.strip().strip('|')
        if not clean:
            continue
        # Check if separator row
        if re.match(r'^[\s\:\-\|]+$', clean):
            continue
        cells = [c.strip() for c in clean.split('|')]
        rows.append(cells)
        
    if not rows:
        return
        
    cols_count = max(len(r) for r in rows)
    tbl = doc.add_table(rows=len(rows), cols=cols_count)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    for row_idx, row_cells in enumerate(rows):
        is_header = (row_idx == 0)
        tr = tbl.rows[row_idx]
        
        for col_idx in range(cols_count):
            cell = tr.cells[col_idx]
            val = row_cells[col_idx] if col_idx < len(row_cells) else ""
            
            # Styling
            if is_header:
                set_cell_background(cell, HEX_TABLE_HEADER_BG)
                set_cell_borders(cell, 
                                 top={"sz": "10", "color": HEX_TABLE_HEADER_BG},
                                 bottom={"sz": "16", "color": HEX_PRIMARY_BORDER if "HEX_PRIMARY_BORDER" in locals() else "1A365D"},
                                 left={"sz": "4", "color": "4299E1"},
                                 right={"sz": "4", "color": "4299E1"})
            else:
                bg = HEX_TABLE_ROW_ALT if (row_idx % 2 == 1) else "FFFFFF"
                set_cell_background(cell, bg)
                set_cell_borders(cell, 
                                 top={"sz": "4", "color": HEX_TABLE_BORDER},
                                 bottom={"sz": "4", "color": HEX_TABLE_BORDER},
                                 left={"sz": "4", "color": HEX_TABLE_BORDER},
                                 right={"sz": "4", "color": HEX_TABLE_BORDER})
                                 
            set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
            
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            
            if is_header:
                run = p.add_run(val)
                run.font.name = 'Calibri'
                run.font.size = Pt(9.5)
                run.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
            else:
                parse_inlines_to_runs(p, val, default_color=COLOR_DARK_SLATE, font_size=9.5)

def get_matching_figure(code_lines):
    combined = "".join(code_lines)
    # Figure 1.1: The Triad & Efficiency
    if ("EFFICIENCY" in combined and "TIMING" in combined and "POWER" in combined) or ("[ POWER ]" in combined and "[ TIMING ]" in combined):
        fig_path = REPO_ROOT / "exports" / "figures" / "fig_01_the_triad.png"
        if fig_path.exists():
            return fig_path, "Figure 1.1: The Mechanical Triad of Combatives (Timing, Distance, and Power Converging on Peak Efficiency)"
            
    # Figure 1.2: The Master Equation
    if "THE MASTER EQUATION" in combined and ("reactionary gap" in combined.lower() or "stage 01" in combined.lower() or "creates the reactionary" in combined.lower()):
        fig_path = REPO_ROOT / "exports" / "figures" / "fig_02_master_equation.png"
        if fig_path.exists():
            return fig_path, "Figure 1.2: The Master Equation Kinetic Cascade (Sequential Causal Pipeline from Spatial Buffer to Terminal Power)"

    # Figure 12.1: The Range Matrix
    if "THE RANGE MATRIX" in combined or ("STANDOFF DEFENSE VS. CHAOS ZONE" in combined):
        fig_path = REPO_ROOT / "exports" / "figures" / "fig_12_01_range_matrix.png"
        if fig_path.exists():
            return fig_path, "Figure 12.1: The Range Matrix: Standoff Defense vs. Chaos Zone"

    return None, None

def render_code_diagram(doc, code_lines):
    if not code_lines:
        return
        
    fig_path, caption = get_matching_figure(code_lines)
    if fig_path and fig_path.exists():
        # Render high-resolution figure with caption
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(2)
        run_img = p_img.add_run()
        run_img.add_picture(str(fig_path), width=Inches(6.2))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(12)
        run_cap = p_cap.add_run(caption)
        run_cap.font.name = 'Calibri'
        run_cap.font.size = Pt(9.0)
        run_cap.font.italic = True
        run_cap.font.color.rgb = COLOR_DARK_SLATE
        return
        
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    
    set_cell_background(cell, HEX_CODE_BG)
    set_cell_borders(cell, 
                     top={"sz": "6", "color": HEX_CODE_BORDER},
                     bottom={"sz": "6", "color": HEX_CODE_BORDER},
                     left={"sz": "18", "color": "718096"},
                     right={"sz": "6", "color": HEX_CODE_BORDER})
    set_cell_margins(cell, top=100, bottom=100, left=160, right=160)
    
    # Render line-by-line in Consolas to preserve exact vertical ASCII alignment in Word
    for idx, line in enumerate(code_lines):
        line_clean = line.rstrip('\r\n')
        cp = cell.paragraphs[0] if idx == 0 else cell.add_paragraph()
        cp.paragraph_format.space_before = Pt(0)
        cp.paragraph_format.space_after = Pt(0)
        cp.paragraph_format.line_spacing = 1.0
        
        run = cp.add_run(line_clean if line_clean else " ")
        run.font.name = 'Consolas'
        run.font.size = Pt(8.5)
        run.font.color.rgb = COLOR_DARK_SLATE

def clean_latex_math(text):
    t = text.strip('$').strip()
    # Replace \mathbf{...}, \text{...}, \mathit{...}
    t = re.sub(r'\\(mathbf|text|mathit|mathrm)\{([^}]+)\}', r'\2', t)
    # Replace arrows
    t = re.sub(r'\\(longrightarrow|rightarrow|to)\b', ' ➔ ', t)
    # Replace \frac{A}{B} with (A / B)
    t = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1 / \2)', t)
    # Replace \vec{F} with F
    t = re.sub(r'\\vec\{([^}]+)\}', r'\1', t)
    # Replace \cdot with ·
    t = re.sub(r'\\cdot\b', '·', t)
    # Greek letters
    t = t.replace(r'\Delta', 'Δ').replace(r'\eta', 'η').replace(r'\tau', 'τ')
    t = t.replace(r'\alpha', 'α').replace(r'\beta', 'β').replace(r'\sigma', 'σ')
    # Math symbols
    t = t.replace(r'\approx', '≈').replace(r'\times', '×')
    t = t.replace(r'\le', '≤').replace(r'\ge', '≥')
    # Remove stray backslashes before words
    t = re.sub(r'\\([a-zA-Z]+)', r'\1', t)
    # Clean up double spaces
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def render_equation_block(doc, raw_text):
    text = raw_text.strip('$').strip()
    norm = text.lower()
    
    # 1. Check for graphical banner matching
    if "distance" in norm and "time" in norm and "timing" in norm and "power" in norm:
        banner = REPO_ROOT / "exports" / "figures" / "banner_master_equation.png"
        if banner.exists():
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(8)
            r = p_img.add_run()
            r.add_picture(str(banner), width=Inches(6.2))
            return True
            
    if "distance" in norm and "time" in norm and "power" in norm and "timing" not in norm:
        banner = REPO_ROOT / "exports" / "figures" / "banner_triad_principles.png"
        if banner.exists():
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(8)
            r = p_img.add_run()
            r.add_picture(str(banner), width=Inches(5.6))
            return True

    if "recognize" in norm and "prioritize" in norm and "choose" in norm:
        banner = REPO_ROOT / "exports" / "figures" / "banner_4_step_cycle.png"
        if banner.exists():
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(8)
            r = p_img.add_run()
            r.add_picture(str(banner), width=Inches(6.2))
            return True

    # 2. Render as clean, centered formula card
    clean_eq = clean_latex_math(text)
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F8FAFC")
    set_cell_borders(cell, 
                     top={"sz": "4", "color": "E2E8F0"},
                     bottom={"sz": "4", "color": "E2E8F0"},
                     left={"sz": "18", "color": "2B6CB0"},
                     right={"sz": "4", "color": "E2E8F0"})
    set_cell_margins(cell, top=70, bottom=70, left=140, right=140)
    
    cp = cell.paragraphs[0]
    cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp.paragraph_format.space_before = Pt(2)
    cp.paragraph_format.space_after = Pt(2)
    
    run = cp.add_run(clean_eq)
    run.font.name = 'Georgia'
    run.font.size = Pt(11.5)
    run.font.italic = True
    run.font.color.rgb = COLOR_PRIMARY_NAVY
    
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(4)
    return True

def parse_markdown_to_docx(doc, md_text, is_first_section=True):
    lines = md_text.splitlines(keepends=True)
    
    in_code_block = False
    code_lines = []
    
    in_callout = False
    callout_type = ""
    callout_lines = []
    
    in_table = False
    table_lines = []
    
    for l in lines:
        stripped = l.strip()
        
        # Display Math / Equation handling
        if stripped.startswith("$$") and stripped.endswith("$$") and len(stripped) >= 4:
            render_equation_block(doc, stripped)
            continue
        
        # Fenced code block handling
        if stripped.startswith("```"):
            if not in_code_block:
                in_code_block = True
                code_lines = []
            else:
                in_code_block = False
                render_code_diagram(doc, code_lines)
                code_lines = []
            continue
            
        if in_code_block:
            code_lines.append(l)
            continue
            
        # Callout handling
        if stripped.startswith(">"):
            inner = stripped[1:].strip()
            if not in_callout:
                in_callout = True
                callout_lines = []
                # Check for callout tag
                m = re.match(r'^\[\!(NOTE|CAUTION|WARNING|IMPORTANT|TIP)\]', inner)
                if m:
                    callout_type = m.group(1)
                    # Next part of inner if any
                    rest = inner[m.end():].strip()
                    if rest:
                        callout_lines.append(rest)
                else:
                    callout_type = "NOTE"
                    callout_lines.append(inner)
            else:
                m = re.match(r'^\[\!(NOTE|CAUTION|WARNING|IMPORTANT|TIP)\]', inner)
                if m:
                    callout_type = m.group(1)
                else:
                    callout_lines.append(inner)
            continue
        elif in_callout:
            # End of callout
            in_callout = False
            render_callout_box(doc, callout_type, callout_lines)
            callout_lines = []
            
        # Markdown table handling
        if stripped.startswith("|") and stripped.endswith("|"):
            if not in_table:
                in_table = True
                table_lines = [stripped]
            else:
                table_lines.append(stripped)
            continue
        elif in_table:
            in_table = False
            render_table(doc, table_lines)
            table_lines = []
            
        # Empty lines
        if not stripped:
            continue
            
        # Horizontal rules
        if stripped in ["---", "===", "***"]:
            # Insert subtle paragraph space or divider
            hp = doc.add_paragraph()
            hp.paragraph_format.space_before = Pt(4)
            hp.paragraph_format.space_after = Pt(4)
            continue
            
        # Headings
        if stripped.startswith("#"):
            hm = re.match(r'^(#{1,4})\s+(.*)$', stripped)
            if hm:
                level = len(hm.group(1))
                htext = hm.group(2).strip()
                
                # If Heading 1 in subsequent sections, demote or keep clean
                hp = doc.add_paragraph()
                
                if level == 1:
                    hp.paragraph_format.space_before = Pt(14)
                    hp.paragraph_format.space_after = Pt(6)
                    hp.paragraph_format.line_spacing = 1.15
                    run = hp.add_run(htext)
                    run.font.name = 'Calibri'
                    run.font.size = Pt(18)
                    run.bold = True
                    run.font.color.rgb = COLOR_PRIMARY_NAVY
                elif level == 2:
                    hp.paragraph_format.space_before = Pt(12)
                    hp.paragraph_format.space_after = Pt(4)
                    hp.paragraph_format.line_spacing = 1.15
                    run = hp.add_run(htext)
                    run.font.name = 'Calibri'
                    run.font.size = Pt(14)
                    run.bold = True
                    run.font.color.rgb = COLOR_ACCENT_BLUE
                elif level == 3:
                    hp.paragraph_format.space_before = Pt(8)
                    hp.paragraph_format.space_after = Pt(2)
                    hp.paragraph_format.line_spacing = 1.15
                    run = hp.add_run(htext)
                    run.font.name = 'Calibri'
                    run.font.size = Pt(12)
                    run.bold = True
                    run.font.color.rgb = COLOR_DARK_SLATE
                else: # level 4
                    hp.paragraph_format.space_before = Pt(6)
                    hp.paragraph_format.space_after = Pt(2)
                    hp.paragraph_format.line_spacing = 1.15
                    run = hp.add_run(htext)
                    run.font.name = 'Calibri'
                    run.font.size = Pt(11)
                    run.bold = True
                    run.italic = True
                    run.font.color.rgb = COLOR_DARK_SLATE
                continue
                
        # Lists
        if stripped.startswith(("- ", "* ", "+ ")):
            lp = doc.add_paragraph(style='List Bullet')
            lp.paragraph_format.space_before = Pt(1)
            lp.paragraph_format.space_after = Pt(3)
            lp.paragraph_format.line_spacing = 1.2
            parse_inlines_to_runs(lp, stripped[2:].strip(), default_color=COLOR_BODY_TEXT, font_size=11.0)
            continue
            
        num_m = re.match(r'^(\d+)\.\s+(.*)$', stripped)
        if num_m:
            lp = doc.add_paragraph()
            lp.paragraph_format.left_indent = Inches(0.3)
            lp.paragraph_format.first_line_indent = Inches(-0.3)
            lp.paragraph_format.space_before = Pt(1)
            lp.paragraph_format.space_after = Pt(3)
            lp.paragraph_format.line_spacing = 1.2
            prefix_run = lp.add_run(f"{num_m.group(1)}.  ")
            prefix_run.font.name = 'Calibri'
            prefix_run.font.size = Pt(11.0)
            prefix_run.font.color.rgb = COLOR_BODY_TEXT
            prefix_run.bold = True
            parse_inlines_to_runs(lp, num_m.group(2).strip(), default_color=COLOR_BODY_TEXT, font_size=11.0)
            continue
            
        # Regular paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.2
        parse_inlines_to_runs(p, stripped, default_color=COLOR_BODY_TEXT, font_size=11.0)

    # Flush any dangling callout or table
    if in_callout:
        render_callout_box(doc, callout_type, callout_lines)
    if in_table:
        render_table(doc, table_lines)
    if in_code_block:
        render_code_diagram(doc, code_lines)

def save_docx_safely(doc, target_path: Path) -> Path:
    """Save docx file, falling back to an _updated variant if the file is locked by Word."""
    try:
        doc.save(target_path)
        return target_path
    except PermissionError:
        alt_path = target_path.with_name(f"{target_path.stem}_updated{target_path.suffix}")
        try:
            doc.save(alt_path)
            print(f"  [NOTE] {target_path.name} is currently open in Word. Saved update to: {alt_path.name}")
            return alt_path
        except Exception as e:
            print(f"  [WARNING] Could not save {target_path.name} or fallback {alt_path.name}: {e}")
            return target_path

def export_individual_chapters():
    CHAPTERS_EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    generated_files = []
    
    print("\n[EXPORT] Commencing Chapter-by-Chapter Word (.docx) Export...")
    
    for ch in CHAPTER_METADATA:
        chap_dir_path = MANUSCRIPT_DIR / ch["part_dir"] / ch["chap_dir"]
        section_files = sorted([f for f in chap_dir_path.glob("*.md") if not f.name.endswith("README.md")])
        
        # Calculate word count
        total_words = 0
        section_texts = []
        for sf in section_files:
            txt = sf.read_text(encoding="utf-8")
            total_words += len(txt.split())
            section_texts.append(txt)
            
        doc = create_document()
        part_name = PART_NAMES.get(ch["part_dir"], ch["part_dir"])
        add_header_footer(doc, f"{ch['number_str']}: {ch['title']}")
        
        # Add Chapter Review Header Card
        add_metadata_card(doc, 
                          chapter_num=ch["number_str"],
                          chapter_title=ch["title"],
                          part_name=part_name,
                          section_count=len(section_files),
                          word_count=total_words)
                          
        # Render Sections
        for idx, sec_text in enumerate(section_texts):
            if idx > 0:
                # Add a clean section divider
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
            
        out_path = CHAPTERS_EXPORT_DIR / ch["filename"]
        saved_path = save_docx_safely(doc, out_path)
        file_size_kb = saved_path.stat().st_size / 1024 if saved_path and saved_path.exists() else 0
        print(f"  [OK] {ch['number_str']}: {ch['title'][:40]:<40} -> {saved_path.name} ({total_words:,} words, {file_size_kb:.1f} KB)")
        generated_files.append((saved_path, total_words))
        
    return generated_files

def export_front_and_back_matter():
    print("\n[EXPORT] Exporting Front Matter and Back Matter Word (.docx)...")
    
    # 1. Front Matter
    fm_files = [
        MANUSCRIPT_DIR / "front_matter" / "00_title_and_copyright.md",
        MANUSCRIPT_DIR / "front_matter" / "01_dedication.md",
        MANUSCRIPT_DIR / "front_matter" / "02_foreword_and_preface.md",
        MANUSCRIPT_DIR / "front_matter" / "03_table_of_contents.md",
    ]
    doc_fm = create_document()
    add_header_footer(doc_fm, "Front Matter: Title, Preface & Table of Contents")
    
    fm_words = 0
    for idx, f in enumerate(fm_files):
        if not f.exists():
            continue
        txt = f.read_text(encoding="utf-8")
        fm_words += len(txt.split())
        parse_markdown_to_docx(doc_fm, txt)
        if idx < len(fm_files) - 1:
            doc_fm.add_page_break()
            
    out_fm = CHAPTERS_EXPORT_DIR / "00_Front_Matter.docx"
    saved_fm = save_docx_safely(doc_fm, out_fm)
    file_size_kb = saved_fm.stat().st_size / 1024 if saved_fm and saved_fm.exists() else 0
    print(f"  [OK] {saved_fm.name} ({fm_words:,} words, {file_size_kb:.1f} KB)")
    
    # 2. Back Matter
    bm_files = [
        MANUSCRIPT_DIR / "back_matter" / "01_glossary.md",
        MANUSCRIPT_DIR / "back_matter" / "02_concept_register.md",
        MANUSCRIPT_DIR / "back_matter" / "03_annotated_bibliography.md",
        MANUSCRIPT_DIR / "back_matter" / "04_about_the_author.md",
    ]
    doc_bm = create_document()
    add_header_footer(doc_bm, "Back Matter: Glossary, Concepts & Citations")
    
    bm_words = 0
    for idx, f in enumerate(bm_files):
        if not f.exists():
            continue
        txt = f.read_text(encoding="utf-8")
        bm_words += len(txt.split())
        parse_markdown_to_docx(doc_bm, txt)
        if idx < len(bm_files) - 1:
            doc_bm.add_page_break()
            
    out_bm = CHAPTERS_EXPORT_DIR / "22_Back_Matter.docx"
    saved_bm = save_docx_safely(doc_bm, out_bm)
    file_size_kb = saved_bm.stat().st_size / 1024 if saved_bm and saved_bm.exists() else 0
    print(f"  [OK] {saved_bm.name} ({bm_words:,} words, {file_size_kb:.1f} KB)")
    
    return saved_fm, saved_bm

def export_complete_master_volume():
    print("\n[EXPORT] Exporting Complete Single-Volume Review Manuscript (.docx)...")
    master_md = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_MASTER.md"
    if not master_md.exists():
        print("  ! Master markdown not found, skipping single-volume export.")
        return None
        
    txt = master_md.read_text(encoding="utf-8")
    words = len(txt.split())
    
    doc = create_document()
    add_header_footer(doc, "Complete Manuscript Review Edition")
    
    # Top Master Card
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, HEX_CARD_BG)
    set_cell_borders(cell, 
                     top={"sz": "8", "color": HEX_CARD_BORDER},
                     bottom={"sz": "8", "color": HEX_CARD_BORDER},
                     left={"sz": "24", "color": HEX_CALLOUT_BORDER},
                     right={"sz": "8", "color": HEX_CARD_BORDER})
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    cp = cell.paragraphs[0]
    r1 = cp.add_run("TIMING, DISTANCE, AND POWER: THE MECHANICAL FOUNDATIONS OF FIGHTING\n")
    r1.font.name = 'Calibri'
    r1.font.size = Pt(14)
    r1.bold = True
    r1.font.color.rgb = COLOR_PRIMARY_NAVY
    
    r2 = cp.add_run(f"Complete Master Manuscript Review Draft — {words:,} words\n")
    r2.font.name = 'Calibri'
    r2.font.size = Pt(10)
    r2.bold = True
    r2.font.color.rgb = COLOR_ACCENT_BLUE
    
    r3 = cp.add_run("6 Parts  |  21 Chapters  |  52 Sections  |  Front & Back Matter Included  |  Frozen Master Edition")
    r3.font.name = 'Calibri'
    r3.font.size = Pt(9.0)
    r3.italic = True
    r3.font.color.rgb = COLOR_MUTED_GRAY
    
    parse_markdown_to_docx(doc, txt)
    
    out_master = EXPORTS_DIR / "TIME_DISTANCE_AND_POWER_COMPLETE_REVIEW.docx"
    saved_master = save_docx_safely(doc, out_master)
    file_size_kb = saved_master.stat().st_size / 1024 if saved_master and saved_master.exists() else 0
    print(f"  [OK] {saved_master.name} ({words:,} words, {file_size_kb:.1f} KB)")
    return saved_master

def main():
    chap_files = export_individual_chapters()
    fm_file, bm_file = export_front_and_back_matter()
    master_file = export_complete_master_volume()
    
    print("\n" + "="*70)
    print("PUBLICATION WORD EXPORT COMPLETE!")
    print(f"  - Total Individual Chapter Documents: {len(chap_files)}")
    print(f"  - Front & Back Matter Documents:     2")
    if master_file:
        print(f"  - Single-Volume Complete Document:   1")
    print(f"  - Output Directory: {CHAPTERS_EXPORT_DIR}")
    print("="*70)

if __name__ == "__main__":
    main()
