# Evidence Pack: [Chapter & Section Name / Wave ID]

> **Target Archival Location**: `archives/evidence_packs/<TAG>_evidence_pack.md` (per [SOP_Evidence_Pack_Publishing.md](file:///c:/Book/.agent/book_sops/SOP_Evidence_Pack_Publishing.md))
>
> 🛑 **MANDATORY POLICY**: This Evidence Pack, along with the pasted diffstat and targeted prose hunks, MUST be submitted for **Editor Gate 2 Review**. No chapter section may be promoted to `Frozen` without explicit Editor acceptance.

---

### Artifact 1: Mandatory Diff Presentation (Diffstat + Targeted Hunks)
- `git diff --stat` output (verbatim):
```text
[Paste raw git diff --stat output here]
```
- **Targeted Unified Diff Hunks** (`git diff -U3 <target_files>` on newly authored markdown prose and code tests):
```diff
[Paste relevant unified diff hunks here]
```

---

### Artifact 2: Master Invariant Checklist (Locks)
| Safety Invariant / Lock | Status (Yes/No) | Verification Method |
| :--- | :---: | :--- |
| Lock 1: Terminology consistency | YES | `CONCEPT_REGISTER.md` regex alignment |
| Lock 2: Code reproducibility (Exit 0) | YES | Executed pytest / test runner tail |
| Lock 3: Word count within budget | YES | Markdown word count check (`wc -w`) |
| Lock 4: Linguistic hygiene (<10% passive, 0 banned adverbs) | YES | Style linter check |
| Lock 5: Modular severability (0 forward circular refs) | YES | Outline dependency graph inspection |
| Lock 6: Primary sources verified | YES | Citation check in `CITATIONS.md` |

---

### Artifact 3: Code Probe Execution Command + Raw Output Tail
- **Designated Probe ID**: `[e.g. PROBE-CH02-PORTS]`
- **Command Run**: `pytest tests/code_examples/test_ch02_domain_ports.py`
- **Exit Code**: `0`
- **Target Test Node IDs**:
  - `tests/code_examples/test_ch02_domain_ports.py::test_port_contract_execution`
  - `tests/code_examples/test_ch02_domain_ports.py::test_invalid_port_payload_raises`
- **Raw Tail (Last 20 lines of console output - NOT summarized)**:
```text
[Paste exact 20-line console output tail here]
```

---

### Artifact 4: Linter & Style Hygiene Report
- **Word Count**: `[e.g. 1,240 words]` (Target: 800–1,500)
- **Passive Voice Percentage**: `[e.g. 4.8%]` (Ceiling: 10%)
- **Banned Adverb Count**: `0` ("seamlessly", "natively", "cleanly", "robustly", etc.)
- **Flesch-Kincaid Reading Grade Level**: `[e.g. 11.2]`

---

### Artifact 5: Citation & Source Backing
```json
{
  "claims_asserted": [
    {
      "claim": "Hexagonal Architecture decouples application core from technical details",
      "citation": "Alistair Cockburn, 'Hexagonal Architecture', 2005",
      "verification_status": "verified"
    }
  ]
}
```

---

### Artifact 6: Negative Blast Radius Affirmation
- **Confirmed Out-of-Scope Bounds**:
  - Confirmed did NOT alter previous chapters: `[e.g. Chapter 01 remains byte-identical]`
  - Confirmed did NOT introduce unintroduced concepts: `[e.g. Database schema migrations absent]`

---

### 🛑 EDITOR GATE 2 SUBMISSION
> **CRITICAL POLICY NOTICE**:  
> Submit this Evidence Pack directly to the Editor (`/editor`).  
> Await **`[GATE 2: ACCEPTED]`** before recording freeze tag or marking the section `Done`.
