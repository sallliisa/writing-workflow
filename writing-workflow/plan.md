# Work plan

- [x] Use your skill-authoring skill: **create-skill** in Cursor (built in), or Anthropic's `skill-creator` elsewhere. With neither, follow the Agent Skills format at agentskills.io.
- [x] Validate the skill: frontmatter has `name` and `description`, referenced files exist, cross-skill links resolve.
- [x] Test cases if structural. Skip if subjective. The user-approved passage pilot supplies behavioral evidence in addition to structural checks.
- [x] Run **Opening a PR**. Skipped. This workspace has no commits or configured delivery request. Keep reviewable local artifacts.
- [x] Frame. Compare one writer with a bounded reviewer and writer workflow on the same retrospective passages.
- [x] Fan out. Isolate the single writer and initial reviewer from each other's outputs and historical answers.
- [x] Cross-judge. Compare anonymized outputs using comprehension, meaning, relevance, preservation, and restraint.
- [x] Pick. Inspect every output and reconcile disagreements.
- [x] Graft. Revise instructions only for demonstrated failures.
- [x] Verify. Validate files and confirm the four source artifacts are unchanged.

Throughput checkpoint. Repair independent supporting skills while the coordinator writes the workflow and prepares passage packets. Writing depends on review findings. Acceptance depends on completed replacements. No parallel writes to the same artifact.

The original CSV has no timestamps or explicit acceptance field. Record numbers are parsed data-row numbers, excluding the header. They are not physical line numbers. A later row position does not establish a later revision.

Model limitation. The installed playbook names Claude and Grok families, which are unavailable here. Use isolated available GPT agents and disclose the lack of cross-family evidence. Use the same model for writing arms to avoid confounding workflow with model choice.
