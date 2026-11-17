# Calibrate from editing history

Parse the supplied history according to its actual columns. Preserve raw source text and assign stable record identifiers. Keep source location, feedback, replacement, and interpretation separate.

Classify evidence by what it establishes:

- Explicit praise supports preserving the praised text, within its original context.
- Explicit rejection establishes a problem or preference, not the correctness of the proposed replacement.
- A nonempty replacement is a proposed revision unless separate evidence establishes acceptance.
- An empty replacement may indicate removal or unavailable output. Use feedback to decide, and record uncertainty.
- Literal `null` carries no replacement. Praise, rejection, and layout requests can all have this value.
- A question or invitation to disagree is not a settled rule.

Group duplicate passages and linked revisions before extracting examples. Exact or overlapping text can suggest a chain, but row order alone cannot establish chronology. Mark supersession only when the evidence supports it. Keep disagreements visible.

Separate language preferences, research facts, terminology choices, and document layout. Check historical factual replacements against current authoritative material before reusing them. Keep project preferences local. A request to use one word in a particular sentence does not justify replacing it everywhere.

Write a short profile containing the decision, its scope, and source record identifiers. Select a few positive and negative examples with reliable status. Name unresolved preferences. Keep the raw history available for targeted lookup rather than loading it into every worker.

## Check whether the workflow helps

Use comparable passage groups for a single-writer baseline and the reviewer and writer workflow. Include passages that need no changes and cases that require missing evidence. Give both arms the same prose guidance, source context, and time or round limits. Record differing call budgets.

Reserve passage groups before tuning when making a generalization claim. Keep all versions of a passage in the same group. If the authoring agent already inspected the entire history, call the result a retrospective pilot. Withhold historical answers and feedback from workers even in that pilot.

Have an independent reader compare outputs under neutral labels. Record comprehension, relevance, meaning preservation, unnecessary edits, and unresolved omissions. Inspect actual outputs and the files workers read. Report counts with their denominator and method. One small run cannot establish reliability across chapters or models.

Ask the author to review a small number of meaningful disagreements. Update the profile only from attributable evidence. Keep model preferences distinct from the author's preferences.
