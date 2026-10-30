"""
Verification probe suite for Chapter 03: Timing, Precision, and the Opportunity Window
Probe ID: [PROBE-CH03-W01-GEOMETRY-MISTAKES]
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
# Wave 1 Probe Suite: Section 3.1 (The Geometry of Mistakes)
# ---------------------------------------------------------------------------

W01_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_01_foundations",
    "ch03_timing_and_windows",
    "01_the_geometry_of_mistakes.md",
)

W01_MANDATORY_CONCEPTS = [
    "Geometry of Mistakes",
    "Center of Mass",
    "Base of Support",
    "Off-Balance",
    "Over-Commitment",
    "Inertia",
]


def test_ch03_w01_file_exists():
    """Assert Chapter 03 Wave 1 markdown file exists."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"


def test_ch03_w01_word_count_within_budget():
    """Assert Chapter 03 Wave 1 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH03-W01-GEOMETRY-MISTAKES] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch03_w01_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 03 Wave 1."""
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    violations = []
    for pattern in BANNED_WORDS:
        matches = re.findall(pattern, text)
        if matches:
            violations.append((pattern, len(matches)))

    assert not violations, f"Banned words detected in Chapter 03 Wave 1: {violations}"


def test_ch03_w01_mandatory_concepts_present():
    """Assert all mandatory concepts required for Chapter 03 Wave 1 are present."""
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W01_MANDATORY_CONCEPTS:
        if concept.lower() not in text.lower():
            missing.append(concept)

    assert not missing, f"Mandatory concepts missing from Chapter 03 Wave 1: {missing}"


# ---------------------------------------------------------------------------
# Wave 2 Probe Suite: Section 3.2 (Skill Disparity: White Belt Windows vs. Milliseconds)
# ---------------------------------------------------------------------------

W02_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_01_foundations",
    "ch03_timing_and_windows",
    "02_skill_disparity_and_opportunity_windows.md",
)

W02_MANDATORY_CONCEPTS = [
    "Opportunity Window",
    "Skill Disparity",
    "White Belt Windows",
    "Millisecond Windows",
    "Perceptual Horizon",
    "Anticipatory Cue Detection",
]


def test_ch03_w02_file_exists():
    """Assert Chapter 03 Wave 2 markdown file exists."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"


def test_ch03_w02_word_count_within_budget():
    """Assert Chapter 03 Wave 2 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH03-W02-SKILL-DISPARITY] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch03_w02_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 03 Wave 2."""
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    violations = []
    for pattern in BANNED_WORDS:
        matches = re.findall(pattern, text)
        if matches:
            violations.append((pattern, len(matches)))

    assert not violations, f"Banned words detected in Chapter 03 Wave 2: {violations}"


def test_ch03_w02_mandatory_concepts_present():
    """Assert all mandatory concepts required for Chapter 03 Wave 2 are present."""
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W02_MANDATORY_CONCEPTS:
        if concept.lower() not in text.lower():
            missing.append(concept)

    assert not missing, f"Mandatory concepts missing from Chapter 03 Wave 2: {missing}"

