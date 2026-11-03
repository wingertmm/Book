"""
Gate 3B Verification Probe Suite: Legal, Liability, and Technical Integrity Audit
Probes:
- test_gate_3b_all_52_callouts_present_and_formatted
- test_gate_3b_diagram_inventory_count_and_syntax
- test_gate_3b_cross_chapter_reference_validity
- test_gate_3b_legal_flags_coverage_in_ch20_ch21
- test_gate_3b_counsel_package_document_exists
"""
import glob
import os
import re

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "manuscript")
DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "docs")


def get_section_files():
    all_files = sorted(glob.glob(os.path.join(BASE_DIR, "**", "*.md"), recursive=True))
    return [f for f in all_files if not f.endswith("README.md")]


def test_gate_3b_all_52_callouts_present_and_formatted():
    """Verify that all 52 sections contain exactly one properly formatted '> [!NOTE]' callout block."""
    files = get_section_files()
    total_callouts = 0
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()
        callouts = re.findall(r"^> \[!NOTE\]", content, re.MULTILINE)
        assert len(callouts) == 1, f"Section {f} has {len(callouts)} callouts (expected exactly 1)"
        total_callouts += len(callouts)
    print(f"\n[GATE-3B] Total callouts verified: {total_callouts}")
    assert total_callouts == 52, f"Expected exactly 52 callouts, found {total_callouts}"


def test_gate_3b_diagram_inventory_count_and_syntax():
    """Verify that exactly 40 diagram/table code blocks exist across the manuscript."""
    files = get_section_files()
    diagram_count = 0
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            lines = fp.readlines()

        in_code_block = False
        code_lang = ""
        code_lines = []

        for l in lines:
            if l.strip().startswith("```"):
                if not in_code_block:
                    in_code_block = True
                    code_lang = l.strip()[3:].strip()
                    code_lines = []
                else:
                    in_code_block = False
                    if code_lang in ["text", "ascii", "mermaid", ""]:
                        block = "".join(code_lines)
                        if any(c in block for c in ["-->", "|", "+--", "===", "---", "[", "]"]):
                            diagram_count += 1
            elif in_code_block:
                code_lines.append(l)

    print(f"\n[GATE-3B] Total diagram and table blocks verified: {diagram_count}")
    assert diagram_count == 40, f"Expected 40 diagram/table blocks, found {diagram_count}"


def test_gate_3b_cross_chapter_reference_validity():
    """Verify that all 'Chapter X' references point to valid chapter numbers between 1 and 21."""
    files = get_section_files()
    total_refs = 0
    pattern = re.compile(r"\bChapter\s+(\d+)\b", re.IGNORECASE)

    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()
        matches = pattern.findall(content)
        for m in matches:
            ch_num = int(m)
            assert 1 <= ch_num <= 21, f"Invalid Chapter reference 'Chapter {ch_num}' in {f}!"
            total_refs += 1

    print(f"\n[GATE-3B] Total cross-chapter references audited: {total_refs}")
    assert total_refs >= 40, f"Expected at least 40 cross-chapter references, found {total_refs}"


def test_gate_3b_legal_flags_coverage_in_ch20_ch21():
    """Verify that all 5 legal flag topics are represented in Chapters 20 and 21."""
    files = get_section_files()
    ch20_ch21_files = [f for f in files if "ch20" in f or "ch21" in f]
    combined_text = ""
    for f in ch20_ch21_files:
        with open(f, "r", encoding="utf-8") as fp:
            combined_text += fp.read() + "\n"

    # Flag 1: 21-foot rule / reactionary deficit
    assert re.search(r"reactionary|21[- ]foot", combined_text, re.IGNORECASE), "Flag 1 concept missing"
    # Flag 2: Lanchester / multiple attackers
    assert re.search(r"Lanchester", combined_text, re.IGNORECASE), "Flag 2 concept missing"
    # Flag 3: Out-of-battery / slide clamp
    assert re.search(r"Out-of-Battery|slide", combined_text, re.IGNORECASE), "Flag 3 concept missing"
    # Flag 4: Graham v. Connor / objective reasonableness
    assert re.search(r"Graham v\. Connor|Objective Reasonableness", combined_text, re.IGNORECASE), "Flag 4 concept missing"
    # Flag 5: 24-Hour Rule / cognitive preservation / silence
    assert re.search(r"24-Hour Rule|Cognitive Preservation|silence", combined_text, re.IGNORECASE), "Flag 5 concept missing"


def test_gate_3b_counsel_package_document_exists():
    """Verify that the Gate 3B Legal & Technical Review Package exists and is comprehensive."""
    pkg_path = os.path.join(DOCS_DIR, "walkthroughs", "GATE_3B_LEGAL_AND_TECHNICAL_PACKAGE.md")
    assert os.path.exists(pkg_path), f"Package document missing: {pkg_path}"
    with open(pkg_path, "r", encoding="utf-8") as fp:
        word_count = len(fp.read().split())
    print(f"\n[GATE-3B] Legal & Technical Review Package word count: {word_count}")
    assert word_count >= 2500, f"Package word count {word_count} is less than 2,500 words"
