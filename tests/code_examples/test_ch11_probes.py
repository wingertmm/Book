"""
Verification probe suite for Chapter 11: Dynamic Principles — Actions on Contact and Situational Knowledge
Probe IDs:
- [PROBE-CH11-W01-ACTIONS-ON-CONTACT]
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
# Wave 1 Probe Suite: Section 11.1 (Principle 10: Actions on Contact)
# ---------------------------------------------------------------------------

W01_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_03_the_11_principles",
    "ch11_principles_10_to_11",
    "01_principle_10_actions_on_contact.md",
)

W01_MANDATORY_CONCEPTS = [
    "Actions on Contact",
    "Subconscious Drilled Response",
    "Battle Drill",
    "Hick's Law",
    "Command Center",
    "Master Equation",
]


def test_ch11_w01_file_exists():
    """Assert Chapter 11 Wave 1 markdown file exists."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"


def test_ch11_w01_word_count_within_budget():
    """Assert Chapter 11 Wave 1 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH11-W01-ACTIONS-ON-CONTACT] Actual word count: {word_count}")
    assert 1300 <= word_count <= 2600, f"Word count {word_count} outside budget [1300, 2600]"


def test_ch11_w01_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 11 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 11 Wave 1 draft!"


def test_ch11_w01_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 11 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W01_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 11 Wave 1: {missing}"


# ---------------------------------------------------------------------------
# Wave 2 Probe Suite: Section 11.2 (Principle 11: Know the Situation & Capstone)
# ---------------------------------------------------------------------------

W02_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_03_the_11_principles",
    "ch11_principles_10_to_11",
    "02_principle_11_know_the_situation.md",
)

W02_MANDATORY_CONCEPTS = [
    "Know the Situation",
    "Dynamic Threat Audit",
    "Skill Disparity",
    "Tunnel Vision",
    "Part III Capstone",
    "Master Equation",
]


def test_ch11_w02_file_exists():
    """Assert Chapter 11 Wave 2 markdown file exists."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"


def test_ch11_w02_word_count_within_budget():
    """Assert Chapter 11 Wave 2 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH11-W02-KNOW-THE-SITUATION] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch11_w02_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 11 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 11 Wave 2 draft!"


def test_ch11_w02_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 11 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W02_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 11 Wave 2: {missing}"

