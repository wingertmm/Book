"""
Verification probe suite for Chapter 14: Wrestling & Clinch-to-Takedown — Posture, Base, Level Changes, and Anti-Takedown Defense
Probe IDs:
- [PROBE-CH14-W01-POSTURE-AND-TAKEDOWN-DEFENSE]
- [PROBE-CH14-W02-TIE-UPS-AND-SPORT-TRAPS]
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
# Wave 1 Probe Suite: Section 14.1 (Posture, Base, Level Changes, and Anti-Takedown Defense)
# ---------------------------------------------------------------------------

W01_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_04_discipline_applications",
    "ch14_wrestling_and_clinch_to_takedown",
    "01_posture_base_and_anti_takedown_defense.md",
)

W01_MANDATORY_CONCEPTS = [
    "Wrestling",
    "Posture and Base",
    "Level Change",
    "Anti-Takedown Defense",
    "The Sprawl",
    "Predictive Funneling",
    "Crossface",
    "Asymmetric Tactical ROI",
    "Ankle Pick",
    "Double Leg",
    "Master Equation",
]


def test_ch14_w01_file_exists():
    """Assert Chapter 14 Wave 1 markdown file exists."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"


def test_ch14_w01_word_count_within_budget():
    """Assert Chapter 14 Wave 1 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH14-W01-POSTURE-AND-TAKEDOWN-DEFENSE] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch14_w01_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 14 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 14 Wave 1 draft!"


def test_ch14_w01_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 14 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W01_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 14 Wave 1: {missing}"


def test_ch14_w01_passive_voice_under_ceiling():
    """Assert passive voice percentage is strictly under the 10% ceiling in Chapter 14 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return

    passive_regex = re.compile(
        r"\b(am|is|are|was|were|be|been|being)\b\s+([a-z]+ed|[a-z]+en|hit|done|made|seen|broken|caught|thrown|struck)\b",
        re.IGNORECASE,
    )

    passive_count = 0
    for s in sentences:
        if passive_regex.search(s):
            passive_count += 1

    passive_pct = (passive_count / len(sentences)) * 100
    print(f"\n[PROBE-CH14-W01-POSTURE-AND-TAKEDOWN-DEFENSE] Passive voice: {passive_pct:.2f}% ({passive_count}/{len(sentences)} sentences)")
    assert passive_pct < 10.0, f"Passive voice percentage {passive_pct:.2f}% exceeds 10% ceiling!"


# ---------------------------------------------------------------------------
# Wave 2 Probe Suite: Section 14.2 (Tie-Ups, Pummeling, and Escaping the Grappling Vortex: Sport Wrestling Pitfalls on Asphalt)
# ---------------------------------------------------------------------------

W02_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_04_discipline_applications",
    "ch14_wrestling_and_clinch_to_takedown",
    "02_tie_ups_pummeling_and_sport_traps.md",
)

W02_MANDATORY_CONCEPTS = [
    "Tie-Ups",
    "Pummeling",
    "Underhook Dominance",
    "Grappling Vortex",
    "The Four Sport Traps",
    "Grappling Exit Filter",
    "Master Equation",
    "Wrestling Capstone",
]


def test_ch14_w02_file_exists():
    """Assert Chapter 14 Wave 2 markdown file exists."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"


def test_ch14_w02_word_count_within_budget():
    """Assert Chapter 14 Wave 2 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH14-W02-TIE-UPS-AND-SPORT-TRAPS] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch14_w02_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 14 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 14 Wave 2 draft!"


def test_ch14_w02_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 14 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W02_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 14 Wave 2: {missing}"


def test_ch14_w02_passive_voice_under_ceiling():
    """Assert passive voice percentage is strictly under the 10% ceiling in Chapter 14 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return

    passive_regex = re.compile(
        r"\b(am|is|are|was|were|be|been|being)\b\s+([a-z]+ed|[a-z]+en|hit|done|made|seen|broken|caught|thrown|struck)\b",
        re.IGNORECASE,
    )

    passive_count = 0
    for s in sentences:
        if passive_regex.search(s):
            passive_count += 1

    passive_pct = (passive_count / len(sentences)) * 100
    print(f"\n[PROBE-CH14-W02-TIE-UPS-AND-SPORT-TRAPS] Passive voice: {passive_pct:.2f}% ({passive_count}/{len(sentences)} sentences)")
    assert passive_pct < 10.0, f"Passive voice percentage {passive_pct:.2f}% exceeds 10% ceiling!"
