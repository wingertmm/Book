"""
Verification probe suite for Chapter 02: Distance as Space Control Across the Four Ranges
Probe ID: [PROBE-CH02-W01-ATTRIBUTES-ELIGIBILITY]
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
# Wave 1 Probe Suite: Sections 2.1 - 2.2
# ---------------------------------------------------------------------------

W01_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_01_foundations",
    "ch02_the_four_ranges",
    "01_relative_attributes_and_weapon_eligibility.md",
)

W01_MANDATORY_CONCEPTS = [
    "Relative Attributes",
    "Reach Advantage",
    "Law of Weapon Eligibility",
    "Base of Support",
    "Center of Mass",
]


def test_ch02_w01_file_exists():
    """Assert Chapter 02 Wave 1 markdown file exists."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"


def test_ch02_w01_word_count_within_budget():
    """Assert Chapter 02 Wave 1 word count is within Gate 1 budget (1,100 - 1,700 words)."""
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH02-W01-ATTRIBUTES-ELIGIBILITY] Actual word count: {word_count}")
    assert 1100 <= word_count <= 1700, f"Word count {word_count} outside budget [1100, 1700]"


def test_ch02_w01_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 02 Wave 1."""
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    violations = []
    for pattern in BANNED_WORDS:
        matches = re.findall(pattern, text)
        if matches:
            violations.append((pattern, len(matches)))

    assert not violations, f"Banned words detected in Chapter 02 Wave 1: {violations}"


def test_ch02_w01_mandatory_concepts_present():
    """Assert all mandatory concepts required for Chapter 02 Wave 1 are present."""
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W01_MANDATORY_CONCEPTS:
        if concept.lower() not in text.lower():
            missing.append(concept)

    assert not missing, f"Mandatory concepts missing from Chapter 02 Wave 1: {missing}"


# ---------------------------------------------------------------------------
# Wave 2 Probe Suite: Sections 2.3 - 2.6 (The Four Combat Ranges)
# ---------------------------------------------------------------------------

W02_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_01_foundations",
    "ch02_the_four_ranges",
    "02_the_four_combat_ranges.md",
)

W02_MANDATORY_CONCEPTS = [
    "Long Distance",
    "Medium Distance",
    "Close Distance",
    "Near Distance",
    "Jamming",
    "Rotational Clearance",
]


def test_ch02_w02_file_exists():
    """Assert Chapter 02 Wave 2 markdown file exists."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"


def test_ch02_w02_word_count_within_budget():
    """Assert Chapter 02 Wave 2 word count is within Gate 1 budget (1,300 - 1,900 words)."""
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH02-W02-FOUR-RANGES] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1900, f"Word count {word_count} outside budget [1300, 1900]"


def test_ch02_w02_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 02 Wave 2."""
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    violations = []
    for pattern in BANNED_WORDS:
        matches = re.findall(pattern, text)
        if matches:
            violations.append((pattern, len(matches)))

    assert not violations, f"Banned words detected in Chapter 02 Wave 2: {violations}"


def test_ch02_w02_mandatory_concepts_present():
    """Assert all mandatory concepts required for Chapter 02 Wave 2 are present."""
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W02_MANDATORY_CONCEPTS:
        if concept.lower() not in text.lower():
            missing.append(concept)

    assert not missing, f"Mandatory concepts missing from Chapter 02 Wave 2: {missing}"

