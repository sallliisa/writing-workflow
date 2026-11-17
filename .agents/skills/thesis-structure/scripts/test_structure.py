import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from structure import inventory, snapshot, validate


class StructureChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.reference = self.directory / "reference-input.md"
        self.target = self.directory / "target-input.md"
        self.reference.write_text("# Methods\nExplain the procedure.\n## Evaluation\nCompare to a reference.\n#### Example\nShow a scored answer.\n")
        self.target.write_text("# Methods\nExplain the procedure.\n## Rules and example\nA mismatched value fails.\n#### Repeated runs\nUse the same rules each time.\n")
        self.run = self.directory / "run"
        snapshot(self.reference, self.target, self.run)
        self.saved = json.loads((self.run / "inventory.json").read_text())
        self.evaluation = {"scope": {"reference": ["R-root"], "target": ["T-root"]},
                           "reference_reviews": [], "target_reviews": [], "findings": [],
                           "dependencies": [], "dependency_note": "Synthetic fixture checks record validation only."}
        for name, document in self.saved["documents"].items():
            for node in document["nodes"]:
                evidence = {"document": name, "start_line": node["start_line"], "end_line": node["end_line"], "supports": "Fixture location."}
                if name == "reference":
                    self.evaluation["reference_reviews"].append({"node_id": node["id"], "function": "Explain evaluation.",
                        "disposition": "adapted", "target_ids": ["T-0002"], "rationale": "Combined explanation and example.",
                        "evidence": [evidence, {"document": "target", "start_line": 3, "end_line": 4, "supports": "Combined function."}]})
                else:
                    self.evaluation["target_reviews"].append({"node_id": node["id"], "purpose": "Explain the procedure.",
                        "direct_content": "Present.", "child_organization": "Reviewed in context.", "assessment": "sufficient",
                        "rationale": "Fixture judgment.", "evidence": [evidence], "finding_ids": []})

    def check(self):
        (self.run / "evaluation.json").write_text(json.dumps(self.evaluation))
        return validate(self.run)

    def test_fences_preamble_and_skipped_depth(self):
        nodes = inventory("Preamble\n# Methods\n```md\n## Not a section\n```\n#### Example\nText\n# Results\nDone\n", "T")
        self.assertEqual([node["title"] for node in nodes], ["Document", "Methods", "Example", "Results"])
        self.assertEqual(nodes[0]["direct_end_line"], 1)
        self.assertEqual(nodes[2]["parent"], nodes[1]["id"])
        self.assertEqual(nodes[1]["end_line"], 7)

    def test_many_to_one_adaptation_is_valid(self):
        result = self.check()
        self.assertEqual(result["scope"]["target"]["reviewed"], 4)

    def test_parent_review_cannot_hide_missing_descendant(self):
        self.evaluation["target_reviews"].pop()
        with self.assertRaisesRegex(ValueError, "Incomplete.*target coverage"):
            self.check()

    def test_inventory_cannot_hide_a_detected_heading(self):
        self.saved["documents"]["target"]["nodes"].pop()
        (self.run / "inventory.json").write_text(json.dumps(self.saved))
        self.evaluation["target_reviews"].pop()
        with self.assertRaisesRegex(ValueError, "heading removed"):
            self.check()

    def test_source_mutation_invalidates_evaluation(self):
        with (self.run / "baseline.md").open("a") as file:
            file.write("New result.\n")
        with self.assertRaisesRegex(ValueError, "Changed frozen target"):
            self.check()

    def test_quote_must_match_cited_lines(self):
        self.evaluation["target_reviews"][0]["evidence"][0]["quote"] = "An invented quotation"
        with self.assertRaisesRegex(ValueError, "quote does not match"):
            self.check()

    def test_unknown_mapping_rejected(self):
        self.evaluation["reference_reviews"][0]["target_ids"] = ["T-nonexistent"]
        with self.assertRaisesRegex(ValueError, "Mapped target"):
            self.check()

    def test_partial_scope_still_includes_all_descendants(self):
        self.evaluation["scope"]["target"] = ["T-0002"]
        self.evaluation["target_reviews"] = self.evaluation["target_reviews"][2:]
        self.assertEqual(self.check()["scope"]["target"]["reviewed"], 2)
        self.evaluation["target_reviews"].pop()
        with self.assertRaisesRegex(ValueError, "Incomplete.*target coverage"):
            self.check()

    def test_snapshot_never_overwrites_an_existing_run(self):
        before = (self.run / "baseline.md").read_bytes()
        with self.assertRaises(FileExistsError):
            snapshot(self.reference, self.target, self.run)
        self.assertEqual((self.run / "baseline.md").read_bytes(), before)

    def test_unresolved_node_cannot_be_marked_complete_without_evidence(self):
        self.evaluation["target_reviews"][-1]["assessment"] = "unresolved"
        with self.assertRaisesRegex(ValueError, "matching finding decision"):
            self.check()

    def test_failed_cli_check_removes_stale_success(self):
        self.check()
        script = Path(__file__).with_name("structure.py")
        command = [sys.executable, str(script), "check", str(self.run)]
        first = subprocess.run(command, capture_output=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertTrue((self.run / "coverage.json").exists())
        (self.run / "evaluation.json").write_text("{}")
        failed = subprocess.run(command, capture_output=True)
        self.assertNotEqual(failed.returncode, 0)
        self.assertFalse((self.run / "coverage.json").exists())

    def add_live_finding(self):
        self.evaluation["findings"] = [{"id": "F1", "target_ids": ["T-0003"], "reference_ids": [],
            "kind": "missing_explanation", "severity": "medium", "problem": "Rule missing.",
            "reader_consequence": "Cannot apply rule.", "action": "Explain the documented rule here.",
            "decision": "accepted", "decision_reason": "Fixture evidence supports correction.",
            "searched_locations": ["Read the complete target."], "needed_evidence": [],
            "evidence": [{"document": "target", "start_line": 5, "end_line": 6, "supports": "Relevant location."}]}]
        self.evaluation["target_reviews"][-1].update(assessment="needs_change", finding_ids=["F1"])

    def test_parent_direct_text_cannot_consume_children(self):
        self.saved["documents"]["target"]["nodes"][1]["direct_end_line"] = 6
        (self.run / "inventory.json").write_text(json.dumps(self.saved))
        with self.assertRaisesRegex(ValueError, "Direct content"):
            self.check()

    def test_manual_children_cannot_overlap(self):
        nodes = self.saved["documents"]["target"]["nodes"]
        nodes[-1]["direct_end_line"] = 5
        for number in (1, 2):
            nodes.append({"id": f"T-manual-{number}", "parent": "T-0003", "level": 5, "title": "Manual division",
                          "start_line": 6, "end_line": 6, "direct_end_line": 6})
        (self.run / "inventory.json").write_text(json.dumps(self.saved))
        with self.assertRaisesRegex(ValueError, "overlap or leave a gap"):
            self.check()

    def test_in_range_but_unrelated_evidence_rejected(self):
        self.evaluation["target_reviews"][-1]["evidence"] = [{"document": "target", "start_line": 1,
            "end_line": 1, "supports": "Unrelated introduction."}]
        with self.assertRaisesRegex(ValueError, "local anchor"):
            self.check()

    def test_unresolved_mapping_needs_target_evidence(self):
        review = self.evaluation["reference_reviews"][0]
        review["disposition"] = "unresolved"
        review["evidence"] = review["evidence"][:1]
        with self.assertRaisesRegex(ValueError, "local anchor"):
            self.check()

    def test_dependency_cannot_use_an_unrelated_finding(self):
        self.add_live_finding()
        self.evaluation["dependencies"] = [{"from_ids": ["T-root"], "to_ids": ["T-0001"],
            "relationship": "Overall question supports design.", "assessment": "gap", "finding_ids": ["F1"],
            "evidence": [{"document": "target", "start_line": 1, "end_line": 2, "supports": "Endpoints."}]}]
        with self.assertRaisesRegex(ValueError, "does not concern an endpoint"):
            self.check()

    def test_supported_dependency_cannot_hide_live_finding(self):
        self.add_live_finding()
        self.evaluation["dependencies"] = [{"from_ids": ["T-0002"], "to_ids": ["T-0003"],
            "relationship": "Rule used by repetition.", "assessment": "supported", "finding_ids": ["F1"],
            "evidence": [{"document": "target", "start_line": 3, "end_line": 6, "supports": "Endpoints."}]}]
        with self.assertRaisesRegex(ValueError, "Supported dependency has a live finding"):
            self.check()

    def test_live_finding_requires_affected_node_assessment(self):
        self.add_live_finding()
        self.evaluation["target_reviews"][-1].update(assessment="sufficient", finding_ids=[])
        with self.assertRaisesRegex(ValueError, "absent from an affected node"):
            self.check()

    def test_null_does_not_count_as_an_omission_search(self):
        self.add_live_finding()
        self.evaluation["findings"][0]["searched_locations"] = [None]
        with self.assertRaisesRegex(ValueError, "nonempty text"):
            self.check()


if __name__ == "__main__":
    unittest.main()
