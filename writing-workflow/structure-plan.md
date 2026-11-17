# Structure workflow implementation

- [x] Use skill-creator and writing-for-agents to design the skill.
- [x] Validate frontmatter, referenced files, and cross-skill links.
- [x] Test structural behavior with nested sections and a bounded manuscript pilot.
- [x] Opening a PR. Skip: this workspace task requests a local workflow, with no remote publication.

## Scope and completion

Create a separate evaluation skill. The revised thesis is the baseline and the friend's thesis is a structural reference. Evaluation covers every heading, its direct content, its descendants, and dependencies across sections. Evaluate the function a section serves rather than title similarity, heading count, length, or an aggregate score. A reference section can map to several target sections or be inapplicable. A target section can have no reference counterpart and still be necessary.

The default deliverable is an evidence-backed structural assessment and change plan. Applying changes is a separate requested operation. Preserve research facts and previously established writing preferences. Do not edit either manuscript during workflow construction.

Throughput checkpoint. Build one inventory and coverage tool, write the coordinator and reviewer instructions, then test the workflow on nested evaluation sections and a deliberately incomplete synthetic outline. The pilot tests whether the workflow distinguishes valid adaptation from a genuine omission. It does not certify the whole thesis.

## Design choices

The existing prose skill accepts exact passage replacements after fresh comparison. Structural evaluation needs a different unit: a section node with a parent, direct text, and a subtree, plus explicit reasoning dependencies. Reusing prose block acceptance would miss unreviewed descendants and misplaced explanations.

Keep reference correspondence separate from target sufficiency. Save immutable sources and address evidence by document and line range. A deterministic check verifies coverage, links, and evidence locations. Agents judge purpose, relevance, and reasoning. Only the coordinator accepts findings.

The default reference policy is to follow useful organization with justified adaptations. A section is changed only for a demonstrated research or reader need. The latest user instruction overrides historical preferences.

The author confirmed that policy. Two design reviews compared reference-first mapping with a target-first argument audit. The chosen workflow establishes target obligations first, then extracts and maps reference functions. This retains the reference as an organizational guide while reducing pressure to import its metrics or section count. The helper uses two trees and explicit links rather than a heading-similarity score.
