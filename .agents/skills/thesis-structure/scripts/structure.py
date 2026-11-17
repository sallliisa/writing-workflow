"""Freeze Markdown sources and check the coverage of a structural evaluation."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys


def require(condition, message):
    if not condition:
        raise ValueError(message)


def inventory(text, prefix):
    lines = text.splitlines()
    require(lines, "Cannot inventory an empty manuscript")
    root = {"id": f"{prefix}-root", "parent": None, "level": 0,
            "title": "Document", "start_line": 1, "direct_end_line": len(lines),
            "end_line": len(lines)}
    nodes, stack, fence = [root], [root], None
    for number, line in enumerate(lines, 1):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = (marker[1][0], len(marker[1]))
            continue
        heading = re.match(r"^ {0,3}(#{1,6})(?:\s+(.*?)\s*|\s*)$", line)
        if not heading:
            continue
        level = len(heading[1])
        nodes[-1]["direct_end_line"] = number - 1
        while stack[-1]["level"] >= level:
            stack.pop()["end_line"] = number - 1
        node = {"id": f"{prefix}-{len(nodes):04d}", "parent": stack[-1]["id"],
                "level": level, "title": re.sub(r"\s+#+\s*$", "", heading[2] or ""),
                "start_line": number, "direct_end_line": len(lines), "end_line": len(lines)}
        nodes.append(node)
        stack.append(node)
    return nodes


def snapshot(reference, target, destination):
    documents, contents = {}, {}
    for name, path, prefix, filename in [("reference", reference, "R", "reference.md"),
                                         ("target", target, "T", "baseline.md")]:
        raw = path.read_bytes()
        contents[filename] = raw
        text = raw.decode("utf-8")
        documents[name] = {"original_path": str(path.resolve()), "file": filename,
                           "sha256": hashlib.sha256(raw).hexdigest(),
                           "line_count": len(text.splitlines()), "nodes": inventory(text, prefix)}
    destination.mkdir(parents=True, exist_ok=False)
    for filename, raw in contents.items():
        (destination / filename).write_bytes(raw)
    result = {"documents": documents,
              "inventory_limit": "ATX headings outside fenced code. Inspect and register other structural divisions manually."}
    (destination / "inventory.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    return {name: len(doc["nodes"]) for name, doc in documents.items()}


def selected_nodes(nodes, roots):
    by_id = {node["id"]: node for node in nodes}
    require(roots and len(set(roots)) == len(roots), "Scope roots must be nonempty and unique")
    require(set(roots) <= by_id.keys(), "Unknown scope root")
    selected, pending = set(), list(roots)
    while pending:
        current = pending.pop()
        if current in selected:
            continue
        selected.add(current)
        pending.extend(node["id"] for node in nodes if node["parent"] == current)
    return selected


def validate(run):
    saved = json.loads((run / "inventory.json").read_text())
    assessment = json.loads((run / "evaluation.json").read_text())
    documents, scopes, texts, by_document = saved["documents"], {}, {}, {}
    for name in ("reference", "target"):
        doc = documents[name]
        raw = (run / doc["file"]).read_bytes()
        require(hashlib.sha256(raw).hexdigest() == doc["sha256"], f"Changed frozen {name} source")
        texts[name] = raw.decode("utf-8").splitlines()
        require(len(texts[name]) == doc["line_count"], f"Wrong {name} line count")
        nodes = doc["nodes"]
        lookup = {node["id"]: node for node in nodes}
        require(len(lookup) == len(nodes), f"Duplicate {name} node ID")
        detected = inventory(raw.decode("utf-8"), "R" if name == "reference" else "T")
        for original in detected:
            require(original["id"] in lookup, f"Detected heading removed from inventory: {original['id']}")
            for field in ("parent", "level", "title", "start_line", "end_line"):
                require(lookup[original["id"]][field] == original[field], f"Detected heading changed: {original['id']} {field}")
        roots = [node for node in nodes if node["parent"] is None]
        require(len(roots) == 1 and roots[0]["level"] == 0, f"Expected one {name} document root")
        for node in nodes:
            require(1 <= node["start_line"] <= node["end_line"] <= doc["line_count"], f"Invalid node range: {node['id']}")
            require(node["start_line"] - 1 <= node["direct_end_line"] <= node["end_line"], f"Invalid direct range: {node['id']}")
            if node["parent"] is not None:
                require(node["parent"] in lookup, f"Unknown parent: {node['id']}")
                parent = lookup[node["parent"]]
                require(parent["level"] < node["level"], f"Invalid depth or cycle: {node['id']}")
                require(parent["start_line"] <= node["start_line"] <= node["end_line"] <= parent["end_line"], f"Node outside parent: {node['id']}")
        for node in nodes:
            children = sorted((child for child in nodes if child["parent"] == node["id"]), key=lambda child: child["start_line"])
            direct_end = children[0]["start_line"] - 1 if children else node["end_line"]
            require(node["direct_end_line"] == direct_end, f"Direct content does not end at first child: {node['id']}")
            for index, child in enumerate(children):
                require(child["start_line"] > node["start_line"] or node["parent"] is None, "Child overlaps parent heading")
                expected_end = children[index + 1]["start_line"] - 1 if index + 1 < len(children) else node["end_line"]
                require(child["end_line"] == expected_end, f"Children overlap or leave a gap: {node['id']}")
        by_document[name] = lookup
        scopes[name] = selected_nodes(nodes, assessment["scope"][name])

    def evidence(items):
        require(isinstance(items, list) and items, "Each judgment needs evidence")
        for item in items:
            name = item["document"]
            require(name in texts, "Unknown evidence document")
            first, last = item["start_line"], item["end_line"]
            require(type(first) is int and type(last) is int and 1 <= first <= last <= len(texts[name]), "Invalid evidence range")
            require(isinstance(item.get("supports"), str) and item["supports"].strip(), "Evidence must state what it supports")
            if "quote" in item:
                require(item["quote"] and item["quote"] in "\n".join(texts[name][first - 1:last]), "Evidence quote does not match its range")

    def required_text(record, keys):
        for key in keys:
            require(isinstance(record.get(key), str) and record[key].strip(), f"Missing text field: {key}")

    def anchor(items, name, node_id):
        node = by_document[name][node_id]
        require(any(item["document"] == name and item["start_line"] <= node["end_line"]
                    and item["end_line"] >= node["start_line"] for item in items),
                f"Evidence lacks a local anchor for {node_id}")

    findings = assessment["findings"]
    finding_ids = {item["id"] for item in findings}
    require(len(finding_ids) == len(findings), "Duplicate finding ID")
    finding_lookup = {item["id"]: item for item in findings}
    for item in findings:
        required_text(item, ["problem", "reader_consequence", "action", "decision_reason"])
        require(item["target_ids"] and set(item["target_ids"]) <= scopes["target"], "Finding target outside scope")
        require(set(item["reference_ids"]) <= by_document["reference"].keys(), "Unknown finding reference")
        require(item["kind"] in {"missing_explanation", "placement", "organization", "unsupported_claim", "dependency", "unavailable_evidence"}, "Unknown finding kind")
        require(item["severity"] in {"high", "medium", "low"}, "Unknown severity")
        require(item["decision"] in {"accepted", "rejected", "unresolved"}, "Missing final finding decision")
        require(isinstance(item["searched_locations"], list), "searched_locations must be a list")
        require(isinstance(item["needed_evidence"], list), "needed_evidence must be a list")
        require(all(isinstance(value, str) and value.strip() for value in item["searched_locations"] + item["needed_evidence"]), "Search and missing-evidence entries must be nonempty text")
        if item["kind"] == "missing_explanation":
            require(item["searched_locations"], "Omission finding lacks a search record")
        if item["decision"] == "unresolved":
            require(item["needed_evidence"], "Unresolved finding must name missing evidence")
        evidence(item["evidence"])
        for name, key in [("target", "target_ids"), ("reference", "reference_ids")]:
            for node_id in item[key]:
                anchor(item["evidence"], name, node_id)

    linked_findings = set()
    for name, key in [("reference", "reference_reviews"), ("target", "target_reviews")]:
        reviews = assessment[key]
        reviewed = [item["node_id"] for item in reviews]
        require(len(set(reviewed)) == len(reviewed), f"Duplicate {name} assessment")
        require(set(reviewed) == scopes[name], f"Incomplete or out-of-scope {name} coverage: missing {sorted(scopes[name] - set(reviewed))}, extra {sorted(set(reviewed) - scopes[name])}")
        for item in reviews:
            required_text(item, ["rationale"])
            evidence(item["evidence"])
            anchor(item["evidence"], name, item["node_id"])
            if name == "reference":
                required_text(item, ["function"])
                require(any(x["document"] == "reference" for x in item["evidence"]), "Reference function needs reference evidence")
                require(item["disposition"] in {"fulfilled", "adapted", "not_applicable", "unresolved"}, "Unknown reference disposition")
                require(set(item["target_ids"]) <= scopes["target"], "Mapped target has not been assessed")
                if item["disposition"] in {"fulfilled", "adapted"}:
                    require(item["target_ids"], "Mapped reference function needs a target")
                    require({x["document"] for x in item["evidence"]} == {"reference", "target"}, "Mapping needs evidence from both documents")
                if item["disposition"] == "not_applicable":
                    require(not item["target_ids"], "Inapplicable function cannot claim a target counterpart")
                for node_id in item["target_ids"]:
                    anchor(item["evidence"], "target", node_id)
            else:
                required_text(item, ["purpose", "direct_content", "child_organization"])
                require(any(x["document"] == "target" for x in item["evidence"]), "Target assessment needs target evidence")
                require(item["assessment"] in {"sufficient", "needs_change", "unresolved"}, "Unknown target assessment")
                ids = set(item["finding_ids"])
                require(ids <= finding_ids, "Unknown finding link")
                linked_findings.update(ids)
                for fid in ids:
                    require(item["node_id"] in finding_lookup[fid]["target_ids"], "Finding does not concern linked node")
                required_decision = {"needs_change": "accepted", "unresolved": "unresolved"}.get(item["assessment"])
                if required_decision:
                    require(any(finding_lookup[fid]["decision"] == required_decision for fid in ids), "Node assessment lacks a matching finding decision")
                else:
                    require(all(finding_lookup[fid]["decision"] == "rejected" for fid in ids), "Sufficient node has a live finding")

    target_reviews = {item["node_id"]: item for item in assessment["target_reviews"]}
    for item in findings:
        if item["decision"] != "rejected":
            for node_id in item["target_ids"]:
                review = target_reviews[node_id]
                require(item["id"] in review["finding_ids"], "Live finding is absent from an affected node review")
                expected = {"needs_change"} if item["decision"] == "accepted" else {"unresolved", "needs_change"}
                require(review["assessment"] in expected, "Live finding contradicts affected node assessment")

    if not assessment["dependencies"]:
        required_text(assessment, ["dependency_note"])
    for item in assessment["dependencies"]:
        required_text(item, ["relationship"])
        endpoints = set(item["from_ids"] + item["to_ids"])
        require(item["from_ids"] and item["to_ids"] and endpoints <= by_document["target"].keys(), "Invalid dependency endpoints")
        require(endpoints & scopes["target"], "Dependency does not touch scope")
        require(item["assessment"] in {"supported", "gap", "unresolved"}, "Unknown dependency assessment")
        ids = set(item["finding_ids"])
        require(ids <= finding_ids, "Unknown dependency finding")
        for fid in ids:
            require(set(finding_lookup[fid]["target_ids"]) & endpoints, "Dependency finding does not concern an endpoint")
        linked_findings.update(ids)
        needed = {"gap": "accepted", "unresolved": "unresolved"}.get(item["assessment"])
        if needed:
            require(any(finding_lookup[fid]["decision"] == needed for fid in ids), "Dependency lacks a matching finding decision")
        else:
            require(all(finding_lookup[fid]["decision"] == "rejected" for fid in ids), "Supported dependency has a live finding")
        evidence(item["evidence"])
        for node_id in endpoints:
            anchor(item["evidence"], "target", node_id)
    require(linked_findings == finding_ids, "Finding is not linked to an assessment or dependency")
    return {"status": "coverage_and_evidence_locations_valid",
            "inventory_sha256": hashlib.sha256((run / "inventory.json").read_bytes()).hexdigest(),
            "evaluation_sha256": hashlib.sha256((run / "evaluation.json").read_bytes()).hexdigest(),
            "scope": {name: {"reviewed": len(ids), "total_inventory": len(by_document[name]),
                               "by_heading_level": dict(sorted(Counter(by_document[name][key]["level"] for key in ids).items()))}
                      for name, ids in scopes.items()},
            "finding_decisions": dict(Counter(item["decision"] for item in findings)),
            "limit": "This verifies records and source locations, not semantic sufficiency or the truth of judgments."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("snapshot", help="Freeze sources and create a heading inventory in a new directory")
    create.add_argument("reference", type=Path)
    create.add_argument("target", type=Path)
    create.add_argument("run_directory", type=Path)
    check = commands.add_parser("check", help="Validate evaluation.json coverage and evidence")
    check.add_argument("run_directory", type=Path)
    args = parser.parse_args()
    if args.command == "snapshot":
        result = snapshot(args.reference, args.target, args.run_directory)
    else:
        (args.run_directory / "coverage.json").unlink(missing_ok=True)
        result = validate(args.run_directory)
        (args.run_directory / "coverage.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f"structure: {error}", file=sys.stderr)
        sys.exit(2)
