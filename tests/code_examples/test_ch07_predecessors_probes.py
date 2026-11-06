"""
Verification probe suite for Part II Strategic Lenses Predecessor Additions:
- Chapter 07B: The Special Operations Lens (Rangers, SEALs, SOCP)
- Chapter 07C: The Algorithmic Combatives Lens (John Danaher)
- Chapter 07D: The Predecessor Synthesis Matrix
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

BASE_DIR = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "manuscript",
    "part_02_strategic_lenses",
)

FILES = [
    os.path.join(BASE_DIR, "ch07b_the_special_operations_lens", "01_ranger_battle_drill_4_and_violence_of_action.md"),
    os.path.join(BASE_DIR, "ch07b_the_special_operations_lens", "02_naval_special_warfare_and_socp_doctrine.md"),
    os.path.join(BASE_DIR, "ch07c_the_algorithmic_combatives_lens", "01_danaher_four_step_algorithm_on_concrete.md"),
    os.path.join(BASE_DIR, "ch07c_the_algorithmic_combatives_lens", "02_wedges_vs_levers_and_the_attackers_dilemma.md"),
    os.path.join(BASE_DIR, "ch07d_the_predecessor_synthesis", "01_the_grand_predecessor_synthesis_matrix.md"),
]


def test_predecessor_files_exist():
    for f in FILES:
        assert os.path.exists(f), f"Missing predecessor file: {f}"


def test_predecessor_zero_banned_words():
    for f in FILES:
        with open(f, "r", encoding="utf-8") as fp:
            text = fp.read().lower()
        for pattern in BANNED_WORDS:
            match = re.search(pattern, text)
            assert match is None, f"Found banned marketing word '{pattern}' in {f}!"


def test_predecessor_callout_count():
    for f in FILES:
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()
        callouts = re.findall(r"^> \[!NOTE\]", content, re.MULTILINE)
        assert len(callouts) == 1, f"Expected 1 callout in {f}, found {len(callouts)}"


def test_predecessor_passive_voice_under_ceiling():
    passive_pattern = re.compile(
        r"\b(am|is|are|was|were|be|been|being)\b\s+([a-z]+ed|thrown|struck|caught|taken|held|driven|broken|pinned|swept)\b",
        re.IGNORECASE,
    )
    for f in FILES:
        with open(f, "r", encoding="utf-8") as fp:
            text = fp.read()
        sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
        passives = [s for s in sentences if passive_pattern.search(s)]
        pct = (len(passives) / len(sentences)) * 100 if sentences else 0
        print(f"\n[{os.path.basename(f)}] Passive voice: {pct:.2f}% ({len(passives)}/{len(sentences)})")
        assert pct <= 10.0, f"Passive voice {pct:.2f}% in {f} exceeds 10% ceiling!"


def test_predecessor_word_counts():
    for f in FILES:
        with open(f, "r", encoding="utf-8") as fp:
            text = fp.read()
        words = len(text.split())
        print(f"\n[{os.path.basename(f)}] Words: {words}")
        assert 1300 <= words <= 2800, f"Word count {words} in {f} outside [1300, 2800]"
