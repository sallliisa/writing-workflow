# Structural evaluation contract

## Judge function and evidence

For each node, answer the following questions with source locations:

1. What question must this section or its mapped counterparts answer for the reader, given the target research and applicable reference functions? Establish the purpose before judging the current text. Do not narrow it to whatever the target already provides.
2. Does its direct text, table, figure, equation, or example provide the needed explanation or evidence? What must the reader infer without support?
3. Is the material placed where readers need it? Do its children divide the purpose coherently, and does their order establish prerequisites before use?
4. Does the assembled subtree fulfill the parent's purpose? Is any apparent repetition useful orientation, a distinct application, or avoidable duplication?
5. What earlier material supports it, and what later claims depend on it? Are those relationships consistent?

Apply these questions at every depth. Use enough context to judge the function. A title match is neither evidence of sufficiency nor a requirement. More subsections, more words, or more equations do not inherently improve structure. A short section can be complete, and an empty organizing heading can be valid.

Keep reference correspondence separate from target sufficiency. An adaptation can still contain a gap. A reference-only topic can be inapplicable. A target-only explanation can be essential. Match by argumentative function before naming a structural operation.

Apply [explanatory adequacy](adequacy.md) to each correspondence. Read the full reference section before extracting its functions, including later paragraphs that justify or qualify earlier claims. Account for the strongest relevant explanatory move as well as identification and definitions. For every distinct function, record the reader question, its relevance to this research, actual target coverage, and any remaining gap. These function checks belong in the existing `function`, `rationale`, and `evidence` fields; no separate schema is needed.

Use `covered`, `partial`, `missing`, `unresolved`, or `unnecessary` in the rationale for each distinct function. A covered function needs an evidence location and an explanation of what the target text establishes. A relocated function names its actual destination and evidence there. An unnecessary function needs a reason based on the target's research, not its present length. Partial or missing necessary functions produce findings at their appropriate target locations. Unknown source facts can prevent a repair without making the existing explanation sufficient.

Before reporting missing content, search the full target for equivalent explanations and inspect the candidate locations. Record the search and the locations checked. If the explanation exists elsewhere, assess whether a reference or move would help. If only an unavailable appendix could establish coverage, mark the relevant judgment unresolved.

Classify the problem precisely:

- `missing_explanation`: a necessary link or explanation is absent from the supplied text.
- `placement`: relevant material appears where its purpose or prerequisites are unclear.
- `organization`: grouping, division, order, or repetition impedes understanding.
- `unsupported_claim`: a claim exceeds or lacks the evidence documented in the thesis.
- `dependency`: definitions, methods, comparisons, or conclusions do not connect consistently.
- `unavailable_evidence`: the supplied material cannot resolve the judgment.

Use `high` for a gap that prevents interpreting or defending a central claim, `medium` for a material local explanation or navigation problem, and `low` for a localized improvement with a concrete reader benefit. Separate the importance of a problem from confidence that it exists. Do not invent observations, parameters, citations, experiments, or results to repair it. Report uncertainty and the evidence required.

## Save the assessment

Write `evaluation.json` with these top-level arrays. IDs refer to the frozen `inventory.json`. `scope` selects subtree roots, and all descendants belong to the evaluation. Selecting `R-root` and `T-root` evaluates both whole documents.

```json
{
  "scope": {"reference": ["R-root"], "target": ["T-root"]},
  "reference_reviews": [],
  "target_reviews": [],
  "dependencies": [],
  "findings": []
}
```

Each `reference_reviews` entry contains:

- `node_id`, `function`, and `target_ids`. Several entries may share targets, and one entry may name several targets.
- `disposition`: `fulfilled`, `adapted`, `not_applicable`, or `unresolved`.
- `rationale` explaining applicability and the chosen mapping, with a function check for every distinct contribution identified in the reference. For mixed sections, account separately for useful background, study-specific choices, and irrelevant or unsupported material. A single blanket adaptation verdict cannot hide a missing contribution.
- `evidence`, citing where each reference function is performed and its actual target coverage when mapped. Include the reference's justification or limitation passage when that is the function being assessed; an introductory identity sentence cannot stand in for it.

Each `target_reviews` entry contains:

- `node_id` and `purpose`.
- `direct_content`: a concise judgment of the node's own content, including non-prose evidence or its legitimate role as an organizing heading.
- `child_organization`: a judgment of grouping and order, or a statement that this is a leaf. Include the subtree's combined contribution where there are children.
- `assessment`: `sufficient`, `needs_change`, or `unresolved`.
- `rationale`, `evidence`, and `finding_ids`. Explain why the necessary reader questions have been answered before assigning `sufficient`. Resolve applicable reference-function gaps against this judgment. Every `needs_change` or `unresolved` entry links to a finding. A sufficient node may have no finding or retain a rejected finding for traceability.

Each `dependencies` entry contains:

- `from_ids` and `to_ids`, naming target nodes.
- `relationship`, describing the prerequisite or claim-support relationship.
- `assessment`: `supported`, `gap`, or `unresolved`.
- `evidence` and `finding_ids`. A gap or unresolved relationship links to a finding.

Include the relevant local relationships and the research-question-to-conclusion chain for a whole-thesis evaluation. Scope-limited evaluations check their boundary dependencies using outside context. An empty dependency array requires a top-level `dependency_note` explaining why no relationship can be assessed.

Each `findings` entry contains:

- `id`, `target_ids`, and `reference_ids`. Reference IDs may be empty for a target-specific need.
- `kind`, `severity`, `problem`, and `reader_consequence`.
- `evidence` and `searched_locations`. For an alleged omission, list the searches and source locations checked. Do not represent a search miss as proof of absence without reading likely alternatives.
- `action`: a concrete structural proposal, including destinations for moves, affected references, and the information needed for any addition. Preserve existing useful content.
- `decision`: `accepted`, `rejected`, or `unresolved`, followed by `decision_reason` and `needed_evidence`. An unresolved finding names what would resolve it. Rejected findings remain visible.

Every `evidence` array contains objects of this form:

```json
{"document": "target", "start_line": 20, "end_line": 24, "supports": "This passage states the comparison the methods must support."}
```

Use `reference` or `target` as the document. Include a local evidence anchor within each reviewed node, each mapped target, each finding's affected node, and each dependency endpoint. Supplement those anchors with context elsewhere when needed. Evidence for absence points to where the explanation would be needed and is accompanied by the search record. Evidence ranges must resolve, but range validity does not prove the accompanying claim. For assertions about specific wording, include an optional `quote` copied exactly from within that range.

List search records and missing evidence as nonempty text entries. Every live finding must also appear in each affected target's assessment. Accepted findings require `needs_change`; an unresolved finding can coexist there or belong to an `unresolved` node. Supported dependencies can retain rejected findings, but cannot close a live finding. A dependency's linked finding must concern one of its named endpoints.

Keep entries concise. The JSON is the complete coverage record; `assessment.md` is the reader's summary. In the summary, lead with the most consequential accepted changes and useful adaptations. Link findings rather than reproducing every node entry. Name unresolved research questions separately from edits the available material supports.

## Challenge the evaluation

Give the fresh challenger the baseline, reference, target brief, and proposed assessment. It reads complete passages, not only the first reviewer's anchors, and searches for competing explanations. It independently checks the central comparison, intervention, and evaluation subtrees even if all their nodes passed. It also checks every substantially reduced or narrowed correspondence and a sample of other sufficient nodes across depths. For these checks, record the reference functions, target answers and locations, justified exclusions, and a retain-or-revise decision. Challenge silent reductions in explanatory purpose as well as unjustified additions. There is no quota for changes.

The coordinator incorporates supported corrections into the final JSON. A machine-checked complete inventory is a coverage claim only. The final report must still explain why accepted changes improve the target's argument.
