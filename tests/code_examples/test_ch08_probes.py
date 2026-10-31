"""
Verification probe suite for Chapter 08: Principles 1–3: Purpose First, Security of Position, and Maneuver to Advantage
Probe IDs:
- [PROBE-CH08-W01-PURPOSE-FIRST]
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
# Wave 1 Probe Suite: Section 8.1 (Principle 1: Purpose First)
# ---------------------------------------------------------------------------

W01_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_03_the_11_principles",
    "ch08_principles_1_to_3",
    "01_principle_1_purpose_first.md",
)

W01_MANDATORY_CONCEPTS = [
    "Purpose First",
    "Clear Purpose + Flexible Method",
    "Exit Filter",
    "Primary Objective",
    "Decision Tree Pruning",
    "Master Equation",
]


def test_ch08_w01_file_exists():
    """Assert Chapter 08 Wave 1 markdown file exists."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"


def test_ch08_w01_word_count_within_budget():
    """Assert Chapter 08 Wave 1 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH08-W01-PURPOSE-FIRST] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch08_w01_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 08 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 08 Wave 1 draft!"


def test_ch08_w01_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 08 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W01_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 08 Wave 1: {missing}"


# ---------------------------------------------------------------------------
# Wave 2 Probe Suite: Section 8.2 (Principle 2: Security of Position)
# ---------------------------------------------------------------------------

W02_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_03_the_11_principles",
    "ch08_principles_1_to_3",
    "02_principle_2_security_of_position.md",
)

W02_MANDATORY_CONCEPTS = [
    "Security of Position",
    "Positional Anchor",
    "Kinetic Chasing",
    "Law of Non-Sacrifice",
    "Reset Latency",
    "Master Equation",
]


def test_ch08_w02_file_exists():
    """Assert Chapter 08 Wave 2 markdown file exists."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"


def test_ch08_w02_word_count_within_budget():
    """Assert Chapter 08 Wave 2 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH08-W02-SECURITY-POSITION] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch08_w02_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 08 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 08 Wave 2 draft!"


def test_ch08_w02_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 08 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W02_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 08 Wave 2: {missing}"

