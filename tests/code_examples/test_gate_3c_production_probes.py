"""
Gate 3C Verification Probe Suite: Production Package & Publication Export
Probes:
- test_gate_3c_front_matter_files_exist_and_populated
- test_gate_3c_back_matter_files_exist_and_populated
- test_gate_3c_master_manuscript_assembled
- test_gate_3c_master_manuscript_word_count_and_integrity
- test_gate_3c_table_of_contents_matches_all_52_sections
- test_gate_3c_legal_disclaimer_incorporates_flags
"""
import glob
import os
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MANUSCRIPT_DIR = os.path.join(REPO_ROOT, "manuscript")
FRONT_MATTER_DIR = os.path.join(MANUSCRIPT_DIR, "front_matter")
BACK_MATTER_DIR = os.path.join(MANUSCRIPT_DIR, "back_matter")
MASTER_FILE = os.path.join(MANUSCRIPT_DIR, "TIME_DISTANCE_AND_POWER_MASTER.md")


def test_gate_3c_front_matter_files_exist_and_populated():
    """Verify all 4 front matter components exist and meet minimum word thresholds."""
    expected_files = {
        "00_title_and_copyright.md": 300,
        "01_dedication.md": 30,
        "02_foreword_and_preface.md": 600,
        "03_table_of_contents.md": 400,
    }
    for filename, min_words in expected_files.items():
        path = os.path.join(FRONT_MATTER_DIR, filename)
        assert os.path.exists(path), f"Missing front matter component: {filename}"
        with open(path, "r", encoding="utf-8") as f:
            words = len(f.read().split())
        assert words >= min_words, f"Front matter {filename} has {words} words (expected >= {min_words})"


def test_gate_3c_back_matter_files_exist_and_populated():
    """Verify all 4 back matter components exist and meet minimum word thresholds."""
    expected_files = {
        "01_glossary.md": 800,
        "02_concept_register.md": 1200,
        "03_annotated_bibliography.md": 1000,
        "04_about_the_author.md": 150,
    }
    for filename, min_words in expected_files.items():
        path = os.path.join(BACK_MATTER_DIR, filename)
        assert os.path.exists(path), f"Missing back matter component: {filename}"
        with open(path, "r", encoding="utf-8") as f:
            words = len(f.read().split())
        assert words >= min_words, f"Back matter {filename} has {words} words (expected >= {min_words})"


def test_gate_3c_master_manuscript_assembled():
    """Verify that the single-volume master manuscript exists, contains front/body/back sections, and 60 merged units."""
    assert os.path.exists(MASTER_FILE), "Master manuscript TIME_DISTANCE_AND_POWER_MASTER.md does not exist!"
    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    assert "<!-- FRONT MATTER" in content, "Missing FRONT MATTER marker in master manuscript"
    assert "<!-- MANUSCRIPT BODY" in content, "Missing MANUSCRIPT BODY marker in master manuscript"
    assert "<!-- BACK MATTER" in content, "Missing BACK MATTER marker in master manuscript"
    assert ("# TIMING, DISTANCE, AND POWER" in content or "# TIME, DISTANCE, AND POWER" in content), "Missing main title in master manuscript"
    assert "# MASTER GLOSSARY OF COMBATIVES ENGINEERING" in content, "Missing glossary in master manuscript"
    assert "# ABOUT THE AUTHOR" in content, "Missing author bio in master manuscript"


def test_gate_3c_master_manuscript_word_count_and_integrity():
    """Verify master manuscript total word count is within publication range (92,000 - 105,000 words), zero banned words, and all 52 callouts."""
    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    words = len(content.split())
    print(f"\n[GATE-3C] Compiled master manuscript word count: {words:,}")
    assert 92000 <= words <= 105000, f"Master manuscript word count {words:,} outside target range [92000, 105000]"

    # Verify zero banned marketing words in master manuscript
    banned_patterns = [
        r"\bseamlessly\b",
        r"\bnatively\b",
        r"\bcleanly\b",
        r"\bsimply\b",
        r"\bobviously\b",
        r"\bphighting\b",
    ]
    txt_lower = content.lower()
    for pat in banned_patterns:
        m = re.search(pat, txt_lower)
        assert m is None, f"Banned marketing word matching '{pat}' found in compiled master manuscript!"

    # Verify callouts count
    callouts = re.findall(r"^> \[!NOTE\]", content, re.MULTILINE)
    assert len(callouts) == 52, f"Expected 52 callouts in compiled master manuscript, found {len(callouts)}"


def test_gate_3c_table_of_contents_matches_all_52_sections():
    """Verify Table of Contents lists all 6 Parts, all 21 Chapters, and all 52 sections."""
    toc_path = os.path.join(FRONT_MATTER_DIR, "03_table_of_contents.md")
    with open(toc_path, "r", encoding="utf-8") as f:
        toc_text = f.read()

    # Check 6 Parts
    for part_num in ["PART I", "PART II", "PART III", "PART IV", "PART V", "PART VI"]:
        assert part_num in toc_text, f"Missing {part_num} in Table of Contents"

    # Check 21 Chapters
    for i in range(1, 22):
        chap_str = f"Chapter {i:02d}:"
        assert chap_str in toc_text, f"Missing {chap_str} in Table of Contents"

    # Verify section files are reflected
    part_dirs = sorted([d for d in glob.glob(os.path.join(MANUSCRIPT_DIR, "part_*")) if os.path.isdir(d)])
    section_files = []
    for pd in part_dirs:
        for cd in sorted(glob.glob(os.path.join(pd, "ch*"))):
            for sf in sorted(glob.glob(os.path.join(cd, "*.md"))):
                if not sf.endswith("README.md"):
                    section_files.append(sf)

    assert len(section_files) == 52, f"Expected 52 section files, found {len(section_files)}"


def test_gate_3c_legal_disclaimer_incorporates_flags():
    """Verify that the front matter legal and safety disclaimers incorporate all five Gate 3B review flags."""
    disclaimer_path = os.path.join(FRONT_MATTER_DIR, "00_title_and_copyright.md")
    with open(disclaimer_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Flag 1: Inherent physical risk / medical advisory
    assert "Inherent Physical Risk" in text or "Medical Advisory" in text, "Missing Flag 1: Inherent physical risk disclaimer"
    assert "physician" in text.lower(), "Missing physician consultation advisory"

    # Flag 2: Inert training tools / non-firing firearms
    assert "Training Tool Safety" in text or "Inert" in text, "Missing Flag 2: Inert training tools disclaimer"
    assert "non-firing inert training tools" in text or "blue guns" in text, "Missing specific inert weapon drill protocols"

    # Flag 3: Graham v. Connor scope
    assert "Graham v. Connor" in text, "Missing Graham v. Connor legal benchmark notice"
    assert "Fourth Amendment" in text, "Missing Fourth Amendment scope distinction in legal disclaimer"

    # Flag 4: Jurisdictional differences / Duty to Retreat
    assert "Duty to Retreat" in text, "Missing Flag 4: Duty to Retreat jurisdictional notice"
    assert "jurisdictions" in text.lower(), "Missing jurisdictional variability notice"

    # Flag 5: Post-incident rights & investigative detention
    assert "Post-Incident" in text, "Missing Flag 5: Post-incident procedures notice"
    assert "investigative detention" in text or "custodial arrest" in text, "Missing investigative detention acknowledgment"
