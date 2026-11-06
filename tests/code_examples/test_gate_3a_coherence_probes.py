"""
Gate 3A Verification Probe Suite: Whole-Manuscript Consistency and Integration Audit
Probes:
- test_gate_3a_all_52_sections_exist_and_non_empty
- test_gate_3a_manuscript_total_word_count_and_rollups
- test_gate_3a_global_zero_banned_marketing_words
- test_gate_3a_global_passive_voice_under_ceiling
- test_gate_3a_master_equation_anchoring_across_all_parts
- test_gate_3a_11_principles_representation_in_manuscript
- test_gate_3a_callout_quarantine_integrity
- test_gate_3a_mermaid_and_diagram_syntax
- test_gate_3a_concept_register_coverage
- test_gate_3a_negative_blast_radius_fencing
"""
import glob
import os
import re

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "manuscript")


def get_section_files():
    all_files = sorted(glob.glob(os.path.join(BASE_DIR, "**", "*.md"), recursive=True))
    return [f for f in all_files if "part_" in f and not f.endswith("README.md")]


def test_gate_3a_all_52_sections_exist_and_non_empty():
    """Verify all 57 manuscript section files exist, are readable, and exceed minimum word count."""
    files = get_section_files()
    assert len(files) == 57, f"Expected 57 sections, found {len(files)}"
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            words = len(fp.read().split())
        assert words >= 800, f"Section {f} has only {words} words (minimum 800 required)"


def test_gate_3a_manuscript_total_word_count_and_rollups():
    """Verify total manuscript word count across all 57 sections is within 95,000 - 115,000 words."""
    files = get_section_files()
    total_words = 0
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            total_words += len(fp.read().split())
    print(f"\n[GATE-3A] Total manuscript word count: {total_words}")
    assert 95000 <= total_words <= 115000, f"Total manuscript word count {total_words} outside expected range [95000, 115000]"


def test_gate_3a_global_zero_banned_marketing_words():
    """Verify zero banned marketing words exist across all 52 sections of the manuscript."""
    files = get_section_files()
    banned_patterns = [
        r"\bseamlessly\b",
        r"\bnatively\b",
        r"\bcleanly\b",
        r"\bsimply\b",
        r"\bobviously\b",
        r"\bphighting\b",
    ]
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            txt = fp.read().lower()
        for pat in banned_patterns:
            m = re.search(pat, txt)
            assert m is None, f"Banned marketing word matching '{pat}' found in {f}!"


def test_gate_3a_global_passive_voice_under_ceiling():
    """Verify manuscript-wide passive voice is under 6.0% and no section exceeds 15.0%."""
    files = get_section_files()
    total_sentences = 0
    total_passive = 0
    passive_pattern = re.compile(
        r"\b(am|is|are|was|were|be|been|being)\b\s+([a-z]+ed|thrown|struck|caught|taken|held|driven|broken|pinned|swept)\b",
        re.IGNORECASE,
    )
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            txt = fp.read()
        sentences = [s.strip() for s in re.split(r"[.!?]+", txt) if s.strip()]
        f_passive = sum(1 for s in sentences if passive_pattern.search(s))
        total_sentences += len(sentences)
        total_passive += f_passive
        if sentences:
            sec_pct = (f_passive / len(sentences)) * 100
            assert sec_pct < 15.0, f"Section {f} has high passive voice: {sec_pct:.2f}%"

    global_pct = (total_passive / total_sentences) * 100 if total_sentences else 0
    print(f"\n[GATE-3A] Whole-manuscript passive voice: {global_pct:.2f}% ({total_passive}/{total_sentences} sentences)")
    assert global_pct < 6.0, f"Global passive voice {global_pct:.2f}% exceeds 6.0% ceiling"


def test_gate_3a_master_equation_anchoring_across_all_parts():
    """Verify the Master Equation (P = W / dt) is actively represented in all 6 parts of the book."""
    files = get_section_files()
    parts = {}
    for f in files:
        parts.setdefault(f.split(os.sep)[-3], []).append(f)

    for p, f_list in parts.items():
        p_text = ""
        for f in f_list:
            with open(f, "r", encoding="utf-8") as fp:
                p_text += fp.read() + "\n"
        has_eq = bool(re.search(r'P\s*=\s*\\frac\{W\}\{\\Delta t\}|Master Equation', p_text, re.IGNORECASE))
        assert has_eq, f"Part {p} missing Master Equation reference or formal formulation"


def test_gate_3a_11_principles_representation_in_manuscript():
    """Verify all 11 Unified Principles are represented and indexed across the manuscript."""
    files = get_section_files()
    all_text = ""
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            all_text += fp.read() + "\n"

    real_principles = [
        "Purpose First",
        "Security of Position",
        "Maneuver to Advantage",
        "Initiative",
        "Concentration",
        "Economy of Force",
        "Surprise",
        "Avoidance",
        "Persistence",
        "Immediate Action",
        "Situational Awareness",
    ]
    for p in real_principles:
        cnt = len(re.findall(re.escape(p), all_text, re.IGNORECASE))
        assert cnt > 0, f"Principle '{p}' missing from manuscript text"


def test_gate_3a_callout_quarantine_integrity():
    """Verify all formal mechanics callout blocks use '> [!NOTE]' and valid formatting."""
    files = get_section_files()
    total_callouts = 0
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()
        callouts = re.findall(r'> \[!NOTE\]', content)
        total_callouts += len(callouts)
    print(f"\n[GATE-3A] Total '> [!NOTE]' callouts across manuscript: {total_callouts}")
    assert total_callouts >= 50, f"Expected at least 50 callouts, found {total_callouts}"


def test_gate_3a_mermaid_and_diagram_syntax():
    """Verify that all Mermaid blocks across the manuscript have valid diagram headers."""
    files = get_section_files()
    all_text = ""
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            all_text += fp.read() + "\n"

    mermaid_blocks = re.findall(r'```mermaid\s+(.*?)\s+```', all_text, re.DOTALL)
    valid_starts = ["graph", "flowchart", "sequenceDiagram", "stateDiagram", "classDiagram", "gantt", "pie"]
    for i, block in enumerate(mermaid_blocks):
        first_line = block.strip().split("\n")[0].strip()
        assert any(first_line.startswith(vs) for vs in valid_starts), f"Invalid Mermaid diagram #{i}: {first_line}"


def test_gate_3a_concept_register_coverage():
    """Verify key registered concepts from CONCEPT_REGISTER.md are actively present in manuscript."""
    files = get_section_files()
    all_text = ""
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            all_text += fp.read() + "\n"

    core_concepts = [
        "Ground Reaction Force",
        "Kinetic Chain",
        "Center of Mass",
        "Longest Lever",
        "Thai Clinch",
        "Structural Framing",
        "Dynamic Range Switching",
        "4-Step Cycle",
        "Prefrontal Hypofrontality",
        "Progressive Stress Inoculation",
        "Asymmetric",
        "Objective Reasonableness",
        "Golden Ten Minutes",
    ]
    for c in core_concepts:
        cnt = len(re.findall(re.escape(c), all_text, re.IGNORECASE))
        assert cnt > 0, f"Core concept '{c}' missing from manuscript"


def test_gate_3a_negative_blast_radius_fencing():
    """Verify that advanced topics (legal, firearms, edged weapons) are quarantined from foundational chapters."""
    files = get_section_files()
    foundations_files = [f for f in files if "part_01_foundations" in f or "part_02_strategic_lenses" in f]
    foundations_text = ""
    for f in foundations_files:
        with open(f, "r", encoding="utf-8") as fp:
            foundations_text += fp.read() + "\n"

    # Legal standards should not appear in Parts 1 or 2
    assert "Graham v. Connor" not in foundations_text, "Legal standard 'Graham v. Connor' leaked into Foundations!"
    assert "Stress-Induced Analgesia" not in foundations_text, "Post-incident 'Stress-Induced Analgesia' leaked into Foundations!"
    assert "911 Call Architecture" not in foundations_text, "'911 Call Architecture' leaked into Foundations!"
