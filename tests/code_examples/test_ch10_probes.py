"""
Verification probe suite for Chapter 10: Principles 7–9: Surprise, Avoidance, and Persistence
Probe IDs:
- [PROBE-CH10-W01-SURPRISE]
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
# Wave 1 Probe Suite: Section 10.1 (Principle 7: Surprise / Unpreparedness)
# ---------------------------------------------------------------------------

W01_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_03_the_11_principles",
    "ch10_principles_7_to_9",
    "01_principle_7_surprise.md",
)

W01_MANDATORY_CONCEPTS = [
    "Surprise",
    "Unpreparedness",
    "Broken Cadence",
    "Baiting Doctrine",
    "Reaction Latency",
    "Master Equation",
]


def test_ch10_w01_file_exists():
    """Assert Chapter 10 Wave 1 markdown file exists."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"


def test_ch10_w01_word_count_within_budget():
    """Assert Chapter 10 Wave 1 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH10-W01-SURPRISE] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch10_w01_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 10 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 10 Wave 1 draft!"


def test_ch10_w01_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 10 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W01_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 10 Wave 1: {missing}"


# ---------------------------------------------------------------------------
# Wave 2 Probe Suite: Section 10.2 (Principle 8: Avoidance When Superior)
# ---------------------------------------------------------------------------

W02_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_03_the_11_principles",
    "ch10_principles_7_to_9",
    "02_principle_8_avoidance.md",
)

W02_MANDATORY_CONCEPTS = [
    "Avoidance When Superior",
    "Clean Exit",
    "Asymmetric Risk",
    "Expected Value",
    "Egress Corridor",
    "Master Equation",
]


def test_ch10_w02_file_exists():
    """Assert Chapter 10 Wave 2 markdown file exists."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"


def test_ch10_w02_word_count_within_budget():
    """Assert Chapter 10 Wave 2 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH10-W02-AVOIDANCE] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch10_w02_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 10 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 10 Wave 2 draft!"


def test_ch10_w02_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 10 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W02_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 10 Wave 2: {missing}"

