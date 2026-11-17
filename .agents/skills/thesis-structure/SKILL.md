---
name: thesis-structure
description: Evaluate a thesis's organization and reasoning at every section depth, adapting a supplied reference thesis to the target research. Use for structural alignment audits, nested-section completeness, placement, and argument continuity. Produce an assessment and revision plan before any requested restructuring.
---

# Evaluate thesis structure

Assess what each section helps the reader understand and whether that function is fulfilled by the target research. Use the reference's useful organization with explained adaptations. Preserve the target's research question, actual methods, evidence, and writing preferences.

## Prepare the evaluation

Identify the reference, baseline, available appendices, institutional requirements, and requested scope. For this workspace, read [the thesis profile](references/thesis-profile.md). For another project, establish these facts from its supplied materials. The user's latest instructions override historical preferences.

Freeze the two manuscripts and inventory their complete heading trees:

```sh
python3 .agents/skills/thesis-structure/scripts/structure.py snapshot REFERENCE.md BASELINE.md RUN_DIRECTORY
```

The command saves `reference.md`, `baseline.md`, and `inventory.json` in a new run directory. Inspect the resulting tree against both documents. The helper recognizes Markdown ATX headings outside fenced code. Register omitted numbered or unheaded divisions as additional child nodes when they perform distinct structural functions. Preserve detected heading nodes and use unique IDs for additions. Adjust the parent's direct-content endpoint when needed. Check tables, figures, equations, and paragraph sequences within each node even when they have no heading. If the file's real hierarchy cannot be represented this way, record the limitation and prepare a faithful Markdown transcription before claiming complete coverage.

For a whole-thesis evaluation, select both document roots in `scope`. For a bounded evaluation, select the relevant subtree roots and include needed counterparts. Scope includes every descendant. Read outside the scope for context, and identify the result as partial.

## Establish the target's needs first

Read the target question, objectives, scope, methods, results, and conclusions before comparing outlines. Save a short `target-brief.md` identifying what the thesis needs to explain for its own claims to follow. Cite the baseline. Distinguish documented facts from unclear reporting and unavailable research evidence. An obligation to explain an existing comparison does not authorize inventing a new experiment.

Extract the reference's section functions into `reference-functions.md` before mapping them to the target. Read each complete section, including its ending and children. Separate distinct contributions such as identification, explanation of relevant characteristics, comparison, justification, and limitations. A label such as "introduces the models" must not erase the other jobs performed by the section. Record useful organizational choices and reference weaknesses that should not transfer.

Read [explanatory adequacy](references/adequacy.md) before judging sufficiency. Establish which reader questions the target must answer from its research needs and the applicable reference functions. The target's existing brevity is not evidence that its purpose is narrow.

## Review every level

Use [the evaluation contract](references/evaluation.md) for criteria, evidence, and the JSON format. Give a structural reviewer both frozen sources, the target brief, reference functions, inventory, and applicable author preferences. Have it write `evaluation.json` and a short `assessment.md`.

For every target node, assess its direct content and the organization of its children. Then check the assembled subtree. Review every descendant separately, including subsubchapters and deeper divisions. A parent marked sufficient cannot stand in for its children. An organizing heading can legitimately have no introductory prose.

Map reference functions to target locations. Allow a function to be merged, split, relocated, or distributed across several sections. Allow target-specific sections and justified inapplicable reference functions. Search the target and inspect likely counterparts before alleging an omission. Assess adaptations against the target's needs, including when the target needs more explanation than the reference provides.

For each correspondence, account for each distinct reference function as covered, partial, missing, unresolved, or unnecessary for this research. Cite the actual explanation, wherever it belongs. Identification, a heading, a citation, or a specification table does not by itself establish explanatory coverage. Record these checks in the existing evaluation fields as specified by the evaluation contract. Preserve needed explanations while adapting their placement to the target's chapter responsibilities.

Check dependencies within and across chapters: problem to question, question to design, design to evaluation, evaluation to reported comparisons, and results to conclusions. Also inspect local dependencies such as a definition before its use, a worked example after its rule, and a table's interpretation. Keep claims about findings within the limits of the actual evidence.

## Challenge and decide

Use a fresh reviewer to challenge the structural findings against the frozen sources and target brief. Ask it to search for overlooked coverage elsewhere, unnecessary imitation, unsupported additions, misplaced material, and mistaken assumptions about figures or appendices. It must independently inspect the central comparison, intervention, and evaluation subtrees, all correspondences with substantially reduced explanatory depth or a narrower stated purpose, and a sample of other sufficient nodes at different depths. A reduction in length is a trigger to investigate, not a defect or a target word count. The challenger reconstructs the reference's functions from the complete passages and checks whether the first reviewer dropped any. Save `challenge.md` with finding IDs, evidence, and decisions on the sufficiency claims it challenged.

The coordinator resolves each finding as accepted, rejected, or unresolved. A proposed addition must meet a demonstrated target need. A proposed move or deletion must name its destination or explain why the function is unnecessary, and account for affected references and dependencies. Resolve disagreements by source evidence and research purpose. Preserve the current structure when a preference alone cannot justify a change.

Use at most two challenge-and-resolution rounds for a finding unless the user sets another limit. Stop sooner when the evidence resolves it or further review needs unavailable information. If delegation is unavailable, separate the roles into recorded passes and disclose that the review was not independent.

Run the coverage check after resolving findings:

```sh
python3 .agents/skills/thesis-structure/scripts/structure.py check RUN_DIRECTORY
```

This checks source identity, recursive coverage, content boundaries, finding consistency, and local evidence anchors. It does not assess the truth of a structural judgment. Read the final assessment against the documents before delivery.

## Deliver and connect to revision

Deliver the function map, section assessments, accepted changes in dependency order, unresolved questions, and coverage by depth. State which differences are useful adaptations and which require correction. Describe reader consequences rather than a similarity percentage or a single quality score. Report missing supplied material as a limitation, not proof that the complete thesis omits it.

Evaluation produces a diagnosis and a structural change plan. Apply changes only when the user requests revision. For an authorized revision, save a separate candidate and compare it with the frozen baseline using the same obligations. Recheck moved content, all affected ancestors, cross-references, and dependencies. Preserve quotations, experimental prompts, identifiers, numbers, conditions, and citation attachment.

Run [thesis-revision](../thesis-revision/SKILL.md) on affected prose after structural changes settle. Clearer wording does not resolve a missing argument, and a structural pass does not establish good prose. Completion means that every scoped node has an assessment, every reference function has a disposition, every finding has a decision, and remaining uncertainty is visible.
