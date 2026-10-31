"""
Verification probe suite for Chapter 05: The Classical Lens — Sun Tzu's Philosophy of Violence
Probe ID: [PROBE-CH05-W01-SUNTZU-FOUNDATIONS]
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
# Wave 1 Probe Suite: Section 5.1 (Subduing Without Fighting & Avoidance)
# ---------------------------------------------------------------------------

W01_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_02_strategic_lenses",
    "ch05_the_sun_tzu_lens",
    "01_subduing_without_fighting.md",
)

W01_MANDATORY_CONCEPTS = [
    "Subduing Without Fighting",
    "Avoidance",
    "Asymmetric Risk",
    "The Tactical Fence",
    "Verbal De-escalation",
    "Five Elements of Lawful Self-Defense",
]


def test_ch05_w01_file_exists():
    """Assert Chapter 05 Wave 1 markdown file exists."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"


def test_ch05_w01_word_count_within_budget():
    """Assert Chapter 05 Wave 1 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH05-W01-SUNTZU-FOUNDATIONS] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch05_w01_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 05 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 05 Wave 1 draft!"


def test_ch05_w01_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 05 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W01_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 05 Wave 1: {missing}"
