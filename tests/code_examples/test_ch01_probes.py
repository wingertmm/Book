"""
Verification probe for Chapter 01 Wave 1: Why Single-Attribute Tactics Fail & The Master Equation
Probe ID: [PROBE-CH01-TRIAD-PHYSICS]
"""
import os
import re

SECTION_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_01_foundations",
    "ch01_the_triad",
    "01_why_single_attribute_tactics_fail.md",
)

BANNED_WORDS = [
    r"\bseamlessly\b",
    r"\bnatively\b",
    r"\bcleanly\b",
    r"\bsimply\b",
    r"\bobviously\b",
    r"\bphighting\b",
]

MANDATORY_CONCEPTS = [
    "Time, Distance, and Power",
    "Single-Attribute Fallacy",
    "Distance Buys Time",
    "Time Directs Power",
    "Master Equation",
    "Hard Target",
]


def test_section_file_exists():
    """Assert the target section markdown file exists."""
    assert os.path.exists(SECTION_PATH), f"Target file missing: {SECTION_PATH}"


def test_section_word_count_within_budget():
    """Assert word count conforms to the Gate 1 plan budget (1,000 - 1,800 words)."""
    with open(SECTION_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH01-TRIAD-PHYSICS] Actual word count: {word_count}")
    assert 1000 <= word_count <= 1800, f"Word count {word_count} outside budget [1000, 1800]"


def test_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff or spelling errors."""
    with open(SECTION_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    violations = []
    for pattern in BANNED_WORDS:
        matches = re.findall(pattern, text)
        if matches:
            violations.append((pattern, len(matches)))

    assert not violations, f"Banned words detected: {violations}"


def test_mandatory_conceptual_invariants_present():
    """Assert all core concepts required by the Gate 1 plan are articulated in the text."""
    with open(SECTION_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in MANDATORY_CONCEPTS:
        if concept.lower() not in text.lower():
            missing.append(concept)

    assert not missing, f"Mandatory concepts missing from section: {missing}"
