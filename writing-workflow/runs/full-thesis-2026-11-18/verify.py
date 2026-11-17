"""Verify this revision's saved artifacts. Run with Python 3 from any directory."""

import hashlib
import json
import re
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

run = Path(__file__).resolve().parent
workspace = run.parents[2]
manifest = json.loads((run / "manifest.json").read_text())
source_path = workspace / manifest["source"]
source = (run / "source.md").read_text()
revised = (workspace / "thesis_BAB_I_to_Daftar_Pustaka_revised.md").read_text()
blocks = json.loads((run / "blocks.json").read_text())
by_id = {block["id"]: block for block in blocks}
edits = json.loads((run / "accepted-final.json").read_text())
protected = json.loads((run / "protected.json").read_text())

assert hashlib.sha256(source_path.read_bytes()).hexdigest() == manifest["source_sha256"]
assert source_path.read_bytes() == (run / "source.md").read_bytes()
assert len({edit["block_id"] for edit in edits}) == len(edits)
assert not {edit["block_id"] for edit in edits} & {item["block_id"] for item in protected}

rebuilt = source
for edit in sorted(edits, key=lambda item: by_id[item["block_id"]]["start"], reverse=True):
    block = by_id[edit["block_id"]]
    assert edit["before"] == block["text"] == source[block["start"]:block["end"]]
    rebuilt = rebuilt[:block["start"]] + edit["after"] + rebuilt[block["end"]:]
assert rebuilt == revised

for item in protected:
    text = by_id[item["block_id"]]["text"]
    assert revised.count(text) == source.count(text)
bibliography_start = by_id["B0324"]["start"]
assert revised.endswith(source[bibliography_start:])

source_rows = [line for line in source.splitlines() if line.startswith("|")]
revised_rows = [line for line in revised.splitlines() if line.startswith("|")]
assert len(source_rows) == len(revised_rows)
for before, after in zip(source_rows, revised_rows):
    assert before.count("|") == after.count("|")
    for old_cell, new_cell in zip(before.split("|"), after.split("|")):
        assert re.findall(r"\d+(?:[.,]\d+)?", old_cell) == re.findall(r"\d+(?:[.,]\d+)?", new_cell)

citation_pattern = r"\([^()\n]*\b(?:19|20)\d{2}[a-z]?[^()\n]*\)"
assert Counter(re.findall(citation_pattern, source)) == Counter(re.findall(citation_pattern, revised))
source_headers = [line for line in source.splitlines() if line.startswith("#")]
revised_headers = [line for line in revised.splitlines() if line.startswith("#")]
assert source_headers == revised_headers

percentage_checks = []
for line_number, line in enumerate(revised.splitlines(), 1):
    if not line.startswith("|"):
        continue
    cells = [cell.strip() for cell in line.split("|")]
    for index, cell in enumerate(cells[:-1]):
        ratio = re.fullmatch(r"(\d+)/(\d+)", cell)
        percentage = re.fullmatch(r"(\d+(?:[.,]\d+)?)%", cells[index + 1])
        if not ratio or not percentage:
            continue
        numerator, denominator = map(Decimal, ratio.groups())
        expected = (numerator / denominator * 100).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        shown = Decimal(percentage.group(1).replace(",", "."))
        assert expected == shown, (line_number, cell, shown, expected)
        percentage_checks.append({"line": line_number, "ratio": cell, "percentage": str(shown)})
assert len(percentage_checks) == 48
assert revised.count("$$") - source.count("$$") == 6
assert 6 * 10 + 2 == 62
assert (Decimal(62) / 7).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) == Decimal("8.86")

numeric_changes = []
for edit in edits:
    before = re.findall(r"\d+(?:[.,]\d+)?", edit["before"])
    after = re.findall(r"\d+(?:[.,]\d+)?", edit["after"])
    if before != after:
        numeric_changes.append({"id": edit["id"], "block_id": edit["block_id"], "before": before, "after": after})
assert {item["block_id"] for item in numeric_changes} == {"B0130", "B0131", "B0179", "B0310"}

report = {
    "source_sha256": manifest["source_sha256"],
    "revised_sha256": hashlib.sha256(revised.encode()).hexdigest(),
    "accepted_edits": len(edits),
    "source_unchanged": True,
    "output_reconstructed_from_accepted_edits": True,
    "protected_blocks_unchanged": len(protected),
    "bibliography_unchanged": True,
    "table_rows_checked": len(source_rows),
    "table_structure_and_numeric_cells_unchanged": True,
    "parenthetical_year_citation_counts_unchanged": True,
    "heading_sequence_unchanged": True,
    "percentage_checks": percentage_checks,
    "added_equations": 3,
    "numeric_changes_requiring_editorial_review": numeric_changes,
    "limits": "These checks establish artifact preservation and arithmetic consistency. They do not establish semantic correctness, source validity, or document layout. Read the editorial verdicts and report too.",
}
(run / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(f"Verified {len(edits)} edits, {len(protected)} protected blocks, {len(source_rows)} table rows, and 48 percentages.")
