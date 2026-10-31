"""
Verification probe suite for Chapter 09: Principles 4–6: Initiative, Concentration, and Economy of Force
Probe IDs:
- [PROBE-CH09-W01-INITIATIVE]
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
# Wave 1 Probe Suite: Section 9.1 (Principle 4: Initiative)
# ---------------------------------------------------------------------------

W01_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_03_the_11_principles",
    "ch09_principles_4_to_6",
    "01_principle_4_initiative.md",
)

W01_MANDATORY_CONCEPTS = [
    "Initiative",
    "Admiration Pause",
    "Decision Cycle Compression",
    "Preemptive Interception",
    "Psychological Refractory Period",
    "Master Equation",
]


def test_ch09_w01_file_exists():
    """Assert Chapter 09 Wave 1 markdown file exists."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"


def test_ch09_w01_word_count_within_budget():
    """Assert Chapter 09 Wave 1 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH09-W01-INITIATIVE] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch09_w01_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 09 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 09 Wave 1 draft!"


def test_ch09_w01_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 09 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W01_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 09 Wave 1: {missing}"


# ---------------------------------------------------------------------------
# Wave 2 Probe Suite: Section 9.2 (Principle 5: Concentration)
# ---------------------------------------------------------------------------

W02_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_03_the_11_principles",
    "ch09_principles_4_to_6",
    "02_principle_5_concentration.md",
)

W02_MANDATORY_CONCEPTS = [
    "Concentration",
    "Decisive Point",
    "Kinetic Chain",
    "Impulse",
    "Cervical Torque",
    "Master Equation",
]


def test_ch09_w02_file_exists():
    """Assert Chapter 09 Wave 2 markdown file exists."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"


def test_ch09_w02_word_count_within_budget():
    """Assert Chapter 09 Wave 2 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH09-W02-CONCENTRATION] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch09_w02_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 09 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 09 Wave 2 draft!"


def test_ch09_w02_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 09 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W02_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 09 Wave 2: {missing}"


# ---------------------------------------------------------------------------
# Wave 3 Probe Suite: Section 9.3 (Principle 6: Economy of Force)
# ---------------------------------------------------------------------------

W03_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_03_the_11_principles",
    "ch09_principles_4_to_6",
    "03_principle_6_economy_of_force.md",
)

W03_MANDATORY_CONCEPTS = [
    "Economy of Force",
    "Asymmetric Limb Ratio",
    "Skeletal Framing",
    "Metabolic Work",
    "Chapter 09 Capstone",
    "Master Equation",
]


def test_ch09_w03_file_exists():
    """Assert Chapter 09 Wave 3 markdown file exists."""
    assert os.path.exists(W03_PATH), f"Target Wave 3 file missing: {W03_PATH}"


def test_ch09_w03_word_count_within_budget():
    """Assert Chapter 09 Wave 3 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W03_PATH), f"Target Wave 3 file missing: {W03_PATH}"
    with open(W03_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH09-W03-ECONOMY-FORCE] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch09_w03_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 09 Wave 3."""
    assert os.path.exists(W03_PATH), f"Target Wave 3 file missing: {W03_PATH}"
    with open(W03_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 09 Wave 3 draft!"


def test_ch09_w03_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 09 Wave 3."""
    assert os.path.exists(W03_PATH), f"Target Wave 3 file missing: {W03_PATH}"
    with open(W03_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W03_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 09 Wave 3: {missing}"


