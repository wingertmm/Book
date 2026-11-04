"""
Verification test suite for Two-Volume Split Architecture:
- Volume 1: Time, Distance, and Power — The Combat Doctrine
- Volume 2: The Machine Under Load — Stress, Conditioning, and Survival Realities
"""

import os
import re
from pathlib import Path

REPO_ROOT = Path("C:/Book")
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"
EXPORTS_DIR = REPO_ROOT / "exports" / "docx"

VOL1_MD = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_VOL1_DOCTRINE.md"
VOL2_MD = MANUSCRIPT_DIR / "TIME_DISTANCE_AND_POWER_VOL2_HUMAN_FACTOR.md"

VOL1_CODA = MANUSCRIPT_DIR / "volume_1_coda" / "01_the_five_invariant_laws_of_the_human_operator.md"
VOL2_PREFACE = MANUSCRIPT_DIR / "front_matter_volume_2" / "01_preface_volume_2.md"

VOL1_DOCX = EXPORTS_DIR / "TIME_DISTANCE_AND_POWER_VOL1_DOCTRINE.docx"
VOL2_DOCX = EXPORTS_DIR / "TIME_DISTANCE_AND_POWER_VOL2_HUMAN_FACTOR.docx"

BANNED_WORDS = [
    r"\bseamlessly\b",
    r"\bnatively\b",
    r"\bcleanly\b",
    r"\bsimply\b",
    r"\bobviously\b",
    r"\bphighting\b",
]

def test_volume_1_coda_integrity_and_word_budget():
    """Assert Volume 1 Coda exists, has 0 banned words, and stays under 1,500 words."""
    assert VOL1_CODA.exists(), f"Volume 1 Coda file missing: {VOL1_CODA}"
    text = VOL1_CODA.read_text(encoding="utf-8")
    words = len(text.split())
    print(f"\n[VOL 1 CODA] Word count: {words}")
    assert 800 <= words <= 1500, f"Volume 1 Coda words ({words}) outside budget [800, 1500]"

    text_lower = text.lower()
    for pattern in BANNED_WORDS:
        match = re.search(pattern, text_lower)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Volume 1 Coda!"

def test_volume_1_assembled_and_word_budget():
    """Assert Volume 1 assembled manuscript exists and is within [65,000, 85,000] word budget."""
    assert VOL1_MD.exists(), f"Volume 1 compiled markdown missing: {VOL1_MD}"
    text = VOL1_MD.read_text(encoding="utf-8")
    words = len(text.split())
    print(f"\n[VOL 1 MASTER] Word count: {words}")
    assert 65000 <= words <= 85000, f"Volume 1 words ({words}) outside budget [65000, 85000]"

def test_volume_2_preface_integrity():
    """Assert Volume 2 Preface exists and contains 0 banned words."""
    assert VOL2_PREFACE.exists(), f"Volume 2 Preface file missing: {VOL2_PREFACE}"
    text = VOL2_PREFACE.read_text(encoding="utf-8")
    text_lower = text.lower()
    for pattern in BANNED_WORDS:
        match = re.search(pattern, text_lower)
        assert match is None, f"Found banned marketing word matching '{pattern}' in Volume 2 Preface!"

def test_volume_2_assembled_and_word_budget():
    """Assert Volume 2 assembled manuscript exists and is within [25,000, 38,000] word budget."""
    assert VOL2_MD.exists(), f"Volume 2 compiled markdown missing: {VOL2_MD}"
    text = VOL2_MD.read_text(encoding="utf-8")
    words = len(text.split())
    print(f"\n[VOL 2 MASTER] Word count: {words}")
    assert 25000 <= words <= 38000, f"Volume 2 words ({words}) outside budget [25000, 38000]"

def test_two_volume_docx_exports_exist():
    """Assert both Volume 1 and Volume 2 Word review documents exist and are populated."""
    assert VOL1_DOCX.exists(), f"Volume 1 DOCX missing: {VOL1_DOCX}"
    assert VOL2_DOCX.exists(), f"Volume 2 DOCX missing: {VOL2_DOCX}"
    assert VOL1_DOCX.stat().st_size > 50 * 1024, f"Volume 1 DOCX is under 50 KB: {VOL1_DOCX.stat().st_size}"
    assert VOL2_DOCX.stat().st_size > 50 * 1024, f"Volume 2 DOCX is under 50 KB: {VOL2_DOCX.stat().st_size}"

def test_two_volume_chapter_docx_directories_and_pruning():
    """Assert volume chapter directories are populated and legacy omnibus is pruned."""
    legacy_file = EXPORTS_DIR / "TIME_DISTANCE_AND_POWER_COMPLETE_REVIEW.docx"
    assert not legacy_file.exists(), f"Legacy single-volume review file should be pruned: {legacy_file}"

    vol1_chap_dir = EXPORTS_DIR / "volume_1_chapters"
    vol2_chap_dir = EXPORTS_DIR / "volume_2_chapters"

    assert vol1_chap_dir.exists(), f"Missing Volume 1 chapters dir: {vol1_chap_dir}"
    assert vol2_chap_dir.exists(), f"Missing Volume 2 chapters dir: {vol2_chap_dir}"

    v1_files = list(vol1_chap_dir.glob("*.docx"))
    v2_files = list(vol2_chap_dir.glob("*.docx"))

    assert len(v1_files) == 18, f"Expected 18 Volume 1 chapter docx files, found {len(v1_files)}"
    assert len(v2_files) == 8, f"Expected 8 Volume 2 chapter docx files, found {len(v2_files)}"

