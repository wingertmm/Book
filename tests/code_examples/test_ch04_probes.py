"""
Verification probe suite for Chapter 04: The Command Center — Fighting as a Contest of Minds
Probe ID: [PROBE-CH04-W01-COMMAND-CENTER]
Probe ID: [PROBE-CH04-W02-OFFLOADING-CHAOS]
Probe ID: [PROBE-CH04-W03-IRON-LAW-QUALITY]
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
# Wave 1 Probe Suite: Sections 4.1 & 4.2 (Mind as Primary Weapon & Dual-Brain Paradox)
# ---------------------------------------------------------------------------

W01_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_01_foundations",
    "ch04_the_command_center",
    "01_the_mind_as_primary_weapon_and_dual_brain_paradox.md",
)

W01_MANDATORY_CONCEPTS = [
    "The Mind as the Primary Weapon",
    "Intent Cues",
    "The Dual-Brain Paradox",
    "The Command Center",
    "The Lizard Brain",
    "Cognitive Bottleneck",
]


def test_ch04_w01_file_exists():
    """Assert Chapter 04 Wave 1 markdown file exists."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"


def test_ch04_w01_word_count_within_budget():
    """Assert Chapter 04 Wave 1 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH04-W01-COMMAND-CENTER] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch04_w01_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 04 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 04 Wave 1 draft!"


def test_ch04_w01_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 04 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W01_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 04 Wave 1: {missing}"


# ---------------------------------------------------------------------------
# Wave 2 Probe Suite: Sections 4.3 & 4.4 (Offloading to Lizard Brain & Controlled Chaos)
# ---------------------------------------------------------------------------

W02_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_01_foundations",
    "ch04_the_command_center",
    "02_offloading_to_lizard_brain_and_controlled_chaos.md",
)

W02_MANDATORY_CONCEPTS = [
    "The Offloading Principle",
    "Controlled Chaos",
    "Closed-Loop",
    "Open-Loop",
    "Boundary Conditions",
    "Weaponized Entropy",
]


def test_ch04_w02_file_exists():
    """Assert Chapter 04 Wave 2 markdown file exists."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"


def test_ch04_w02_word_count_within_budget():
    """Assert Chapter 04 Wave 2 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH04-W02-OFFLOADING-CHAOS] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch04_w02_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 04 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 04 Wave 2 draft!"


def test_ch04_w02_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 04 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W02_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 04 Wave 2: {missing}"


# ---------------------------------------------------------------------------
# Wave 3 Probe Suite: Sections 4.5 & 4.6 (Iron Law & Quality Constraint)
# ---------------------------------------------------------------------------

W03_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_01_foundations",
    "ch04_the_command_center",
    "03_the_iron_law_and_the_quality_constraint.md",
)

W03_MANDATORY_CONCEPTS = [
    "The Iron Law of Combat Mastery",
    "Hesitation",
    "Rigidity",
    "The Quality Constraint",
    "The Asymmetry of Unlearning",
    "External Outcome Focus",
]


def test_ch04_w03_file_exists():
    """Assert Chapter 04 Wave 3 markdown file exists."""
    assert os.path.exists(W03_PATH), f"Target Wave 3 file missing: {W03_PATH}"


def test_ch04_w03_word_count_within_budget():
    """Assert Chapter 04 Wave 3 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W03_PATH), f"Target Wave 3 file missing: {W03_PATH}"
    with open(W03_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH04-W03-IRON-LAW-QUALITY] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch04_w03_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 04 Wave 3."""
    assert os.path.exists(W03_PATH), f"Target Wave 3 file missing: {W03_PATH}"
    with open(W03_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 04 Wave 3 draft!"


def test_ch04_w03_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 04 Wave 3."""
    assert os.path.exists(W03_PATH), f"Target Wave 3 file missing: {W03_PATH}"
    with open(W03_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W03_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 04 Wave 3: {missing}"
