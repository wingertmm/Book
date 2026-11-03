"""
Verification probe suite for Chapter 19: Train Like You Fight — The Law of Neural Conditioning
Probe IDs:
- [PROBE-CH19-W01-NEURAL-CONDITIONING]
- [PROBE-CH19-W02-STRESS-INOCULATION-AND-CAPSTONE]
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
# Wave 1 Probe Suite: Section 19.1 & 19.2 (Neural Conditioning and The Law of Permanence)
# ---------------------------------------------------------------------------

W01_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_06_training_doctrine",
    "ch19_neural_conditioning",
    "01_neural_conditioning_and_permanence.md",
)

W01_MANDATORY_CONCEPTS = [
    "Neural Conditioning",
    "Myelination",
    "Law of Permanence",
    "Asymmetry of Unlearning",
    "Motor Engram",
    "Subconscious Automation",
    "Master Equation",
    "Deliberate Practice",
]


def test_ch19_w01_file_exists():
    """Assert Chapter 19 Wave 1 markdown file exists."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"


def test_ch19_w01_word_count_within_budget():
    """Assert Chapter 19 Wave 1 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH19-W01-NEURAL-CONDITIONING] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch19_w01_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 19 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 19 Wave 1 draft!"


def test_ch19_w01_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 19 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W01_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 19 Wave 1: {missing}"


def test_ch19_w01_passive_voice_under_ceiling():
    """Assert passive voice percentage is strictly under the 10% ceiling in Chapter 19 Wave 1."""
    assert os.path.exists(W01_PATH), f"Target Wave 1 file missing: {W01_PATH}"
    with open(W01_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return

    passive_pattern = re.compile(
        r"\b(am|is|are|was|were|be|been|being)\b\s+([a-z]+ed|thrown|struck|caught|taken|held|driven|broken|pinned|swept)\b",
        re.IGNORECASE,
    )

    passive_count = sum(1 for s in sentences if passive_pattern.search(s))
    passive_pct = (passive_count / len(sentences)) * 100.0
    print(
        f"\n[PROBE-CH19-W01-NEURAL-CONDITIONING] Passive voice: {passive_pct:.2f}% ({passive_count}/{len(sentences)} sentences)"
    )
    assert passive_pct <= 10.0, f"Passive voice percentage {passive_pct:.2f}% exceeds 10% ceiling!"


# ---------------------------------------------------------------------------
# Wave 2 Probe Suite: Section 19.3 & 19.4 (Stress Inoculation, Decision Points, and Capstone)
# ---------------------------------------------------------------------------

W02_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_06_training_doctrine",
    "ch19_neural_conditioning",
    "02_stress_inoculation_and_capstone.md",
)

W02_MANDATORY_CONCEPTS = [
    "Stress Inoculation",
    "Controlled Chaos",
    "Decision Points",
    "Compliant Scripting",
    "Outcome Focus",
    "Training Scars",
    "Master Equation",
    "Chapter 19 Capstone",
]


def test_ch19_w02_file_exists():
    """Assert Chapter 19 Wave 2 markdown file exists."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"


def test_ch19_w02_word_count_within_budget():
    """Assert Chapter 19 Wave 2 word count is within Gate 1 budget (1,300 - 1,800 words)."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    print(f"\n[PROBE-CH19-W02-STRESS-INOCULATION-AND-CAPSTONE] Actual word count: {word_count}")
    assert 1300 <= word_count <= 1800, f"Word count {word_count} outside budget [1300, 1800]"


def test_ch19_w02_zero_banned_marketing_words():
    """Assert zero occurrences of banned marketing fluff in Chapter 19 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read().lower()

    for pattern in BANNED_WORDS:
        match = re.search(pattern, text)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Chapter 19 Wave 2 draft!"


def test_ch19_w02_mandatory_concepts_present():
    """Assert all mandatory conceptual invariants are present in Chapter 19 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    missing = []
    for concept in W02_MANDATORY_CONCEPTS:
        pattern = re.compile(re.escape(concept), re.IGNORECASE)
        if not pattern.search(text):
            missing.append(concept)

    assert not missing, f"Missing mandatory conceptual invariants in Chapter 19 Wave 2: {missing}"


def test_ch19_w02_passive_voice_under_ceiling():
    """Assert passive voice percentage is strictly under the 10% ceiling in Chapter 19 Wave 2."""
    assert os.path.exists(W02_PATH), f"Target Wave 2 file missing: {W02_PATH}"
    with open(W02_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return

    passive_pattern = re.compile(
        r"\b(am|is|are|was|were|be|been|being)\b\s+([a-z]+ed|thrown|struck|caught|taken|held|driven|broken|pinned|swept)\b",
        re.IGNORECASE,
    )

    passive_count = sum(1 for s in sentences if passive_pattern.search(s))
    passive_pct = (passive_count / len(sentences)) * 100.0
    print(
        f"\n[PROBE-CH19-W02-STRESS-INOCULATION-AND-CAPSTONE] Passive voice: {passive_pct:.2f}% ({passive_count}/{len(sentences)} sentences)"
    )
    assert passive_pct <= 10.0, f"Passive voice percentage {passive_pct:.2f}% exceeds 10% ceiling!"
