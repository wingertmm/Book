"""
Verification probe suite for Chapter 16: Range Transitions & Fluid Synthesis — Inter-Discipline Bridges, The Fluidity Paradox, and Dynamic Range Switching
Probe IDs:
- [PROBE-CH16-W01-RANGE-CHAINING-AND-BRIDGES]
- [PROBE-CH16-W02-DYNAMIC-SWITCHING-AND-CAPSTONE]
"""
import os
import re

BANNED_WORDS = [
    r"\bseamlessly\b",
    r"\bnatively\b",
    r"\bcleanly\b",
    r"\bsimply\b",
    r"\bobviously\b",
    r"\bphighting\b",
]

# ---------------------------------------------------------------------------
# Wave 1 Probe Suite: Section 16.1 (Range Chaining, Inter-Discipline Bridges, and the Fluidity Paradox)
# ---------------------------------------------------------------------------

W01_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_04_discipline_applications",
    "ch16_range_transitions_and_fluid_synthesis",
    "01_range_chaining_and_bridges.md",
)

W01_MANDATORY_CONCEPTS = [
    "Range Transitions",
    "Fluid Synthesis",
    "Fluidity Paradox",
    "Range Chaining",
    "Inter-Discipline Bridges",
    "Transition Seams",
    "Stylistic Rigidity",
    "Master Equation",
]


def test_ch16_w01_file_exists():
    """Assert Chapter 16 Wave 1 markdown file exists."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"


def test_ch16_w01_word_count_within_budget():
    """Assert Chapter 16 Wave 1 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH16-W01-RANGE-CHAINING-AND-BRIDGES] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch16_w01_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 16 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 16 Wave 1 draft!"


def test_ch16_w01_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 16 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W01_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 16 Wave 1: {missing}"


def test_ch16_w01_passive_voice_under_ceiling():
    """Assert passive voice percentage is strictly under the 10% ceiling in Chapter 16 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return

    passive_pattern = re.compile(
        r"\b(am|is|are|was|were|be|been|being)\b\s+([a-z]+ed|thrown|struck|caught|taken|held|driven|broken|pinned|swept)\b",
        re.IGNORECASE,
    )

    passive_count = sum(1 for s in sentences if passive_pattern.search(s))
    passive_pct = (passive_count / len(sentences)) * 100.0
    print(
        f"\n[PROBE-CH16-W01-RANGE-CHAINING-AND-BRIDGES] Passive voice: {passive_pct:.2f}% ({passive_count}/{len(sentences)} sentences)"
    )
    assert passive_pct <= 10.0, f"Passive voice percentage {passive_pct:.2f}% exceeds 10% ceiling!"


# ---------------------------------------------------------------------------
# Wave 2 Probe Suite: Section 16.2 (Dynamic Range Switching and Part IV Master Capstone)
# ---------------------------------------------------------------------------

W02_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_04_discipline_applications",
    "ch16_range_transitions_and_fluid_synthesis",
    "02_dynamic_switching_and_part_iv_capstone.md",
)

W02_MANDATORY_CONCEPTS = [
    "Range Transitions",
    "Dynamic Range Switching",
    "Kinetic Continuity",
    "Cognitive Switching Latency",
    "Asymmetric Exit Corridor",
    "Master Equation",
    "Part IV Master Capstone",
]


def test_ch16_w02_file_exists():
    """Assert Chapter 16 Wave 2 markdown file exists."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"


def test_ch16_w02_word_count_within_budget():
    """Assert Chapter 16 Wave 2 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH16-W02-DYNAMIC-SWITCHING-AND-CAPSTONE] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch16_w02_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 16 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 16 Wave 2 draft!"


def test_ch16_w02_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 16 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W02_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 16 Wave 2: {missing}"


def test_ch16_w02_passive_voice_under_ceiling():
    """Assert passive voice percentage is strictly under the 10% ceiling in Chapter 16 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return

    passive_pattern = re.compile(
        r"\b(am|is|are|was|were|be|been|being)\b\s+([a-z]+ed|thrown|struck|caught|taken|held|driven|broken|pinned|swept)\b",
        re.IGNORECASE,
    )

    passive_count = sum(1 for s in sentences if passive_pattern.search(s))
    passive_pct = (passive_count / len(sentences)) * 100.0
    print(
        f"\n[PROBE-CH16-W02-DYNAMIC-SWITCHING-AND-CAPSTONE] Passive voice: {passive_pct:.2f}% ({passive_count}/{len(sentences)} sentences)"
    )
    assert passive_pct <= 10.0, f"Passive voice percentage {passive_pct:.2f}% exceeds 10% ceiling!"
