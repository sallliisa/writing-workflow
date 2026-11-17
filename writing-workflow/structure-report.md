# Structure evaluation workflow

The [thesis-structure skill](../.agents/skills/thesis-structure/SKILL.md) evaluates the revised thesis against the friend's thesis at every section depth. It produces an assessment and a structural change plan. Neither manuscript was edited while building or testing the workflow.

## How it works

1. Freeze both sources and inventory their headings, direct content, and nested sections.
2. Establish what the target research needs to explain, then identify the functions of the reference's sections.
3. Assess every target node and map useful reference functions to their target locations. Merging, splitting, relocation, and target-only explanations are valid when justified.
4. Check relationships within and across sections, including the research question, methods, evaluation, comparisons, and conclusions.
5. Have a fresh reviewer challenge findings and selected no-change judgments. The coordinator resolves every finding and checks complete coverage of the declared scope.

Two separate judgments prevent outline imitation:

| Question | Possible decisions |
| --- | --- |
| How does the reference function apply here? | Fulfilled, adapted, inapplicable, unresolved |
| Does this target section fulfill its own purpose? | Sufficient, needs change, unresolved |

An adapted section can still need improvement. A target-only section can be sufficient and necessary. A matching heading can conceal a missing explanation. Each node receives a separate assessment of its direct content and child organization. Paragraph sequences, tables, equations, and examples count as content even without a heading.

The workflow does not optimize a similarity score or require equal subsection counts. A proposed change must resolve a demonstrated reader or research need. Missing evidence remains unresolved. Authorized restructuring is followed by a new structural check and then the existing prose-revision workflow.

## Use it

Ask: “Use $thesis-structure to evaluate the full revised thesis against fikbas_skripsi_full.md. Assess every nested section and produce a structural change plan.”

The project profile selects `thesis_BAB_I_to_Daftar_Pustaka_revised.md` as the baseline. The old clean file remains a historical input. The skills now link to this workflow, and the obsolete statement that the reference thesis is unavailable has been removed.

For reproducible source preparation and record checks:

```sh
python3 .agents/skills/thesis-structure/scripts/structure.py snapshot fikbas_skripsi_full.md thesis_BAB_I_to_Daftar_Pustaka_revised.md writing-workflow/structure-runs/first-full-audit
python3 .agents/skills/thesis-structure/scripts/structure.py check writing-workflow/structure-runs/first-full-audit
```

The second command runs after reviewers create `evaluation.json`. The script does not invoke agents or judge reasoning. The skill supplies those steps. New snapshot directories cannot overwrite earlier runs. The inventory recognizes Markdown ATX headings outside fenced code; the evaluator must inspect other divisions before claiming complete coverage.

## Validation and pilot

Nineteen automated checks passed. They cover recursive scope, omitted children, altered inventories and sources, overlapping content ranges, invalid evidence anchors, many-to-one adaptation, inconsistent finding decisions, and stale success records. Run them with:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s .agents/skills/thesis-structure/scripts -p 'test_*.py' -v
```

A fresh behavioral reviewer assessed two neutral synthetic versions. It recognized the valid adaptation to count correctness and found the omitted operational rule in a sixth-level subsection. It also found a real shared reporting omission in the samples. It did not require the reference's metric, extra introductory paragraphs, or matching heading counts. See the [behavior review](structure-tests/behavior-review.md) and [recorded outcome](structure-tests/behavior-result.json). This is a designed probe, not a reliability estimate.

A bounded [manuscript pilot](structure-pilot/assessment.md) assessed 10 reference nodes and 9 target nodes, including every descendant in its selected evaluation sections. A fresh [challenger](structure-pilot/challenge.md) checked both proposed findings and all eight locally sufficient target nodes. The final result retains the existing broad organization, accepts one low-severity placement clarification as a proposal, and leaves the cited appendix's actual coverage unresolved. The challenge narrowed the appendix obligation and one reference mapping to avoid importing unsupported requirements. No proposed manuscript change was applied.

The helper's inventory contains 61 reference nodes and 74 target nodes, each including one document root. Those totals are inventory counts, not full-review counts. The pilot's [coverage artifact](structure-pilot/coverage.json) distinguishes them. A full thesis structure evaluation has not yet been run.

## Audit resolution and limits

The [fresh audit](structure-audit.md) found three classes of checker weakness. All were corrected:

- Direct-content boundaries now follow the first child, and sibling ranges must partition their parent without overlap or gaps.
- Reviews and mappings require source-local anchors, including unresolved mappings. Contextual evidence elsewhere remains allowed.
- Findings must agree with affected node assessments and related dependencies. A supported dependency cannot hide a live finding. Search records require actual text.

Eight additional regression checks reproduce these failures and now reject them. The stricter checker also required three additional local evidence anchors in the real pilot; those were inspected and added before its final successful check. The [decision trail](structure-decisions.tsv) records these corrections.

Model the Domain informed the separate section trees, correspondence records, and target judgments. Build the Lever produced the reusable inventory and coverage checker. Prove It Works informed the negative tests, source checks, and independent behavioral challenge.

The audit used `gpt-6.2-sol`, with fresh reviewers for the behavioral probe and manuscript challenge. Only GPT-family models were available. Coverage validity establishes record completeness and traceable locations, not semantic correctness, research validity, or advisor approval. The workflow has been tested on a bounded real scope and synthetic examples; it has not been established as reliable across all chapters or other theses.
