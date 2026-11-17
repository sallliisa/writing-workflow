# Full thesis review

## Requested work and models

Review the entire latest revised thesis for writing quality and structure. Use GPT 6.2 Astra (`gpt-6.2-astra`) as coordinator and for every reviewer, including fresh comparison and challenge reviewers. Use GPT 6 Astra (`gpt-6-astra`) for writers. The user explicitly requested a separate Codex thread and these model roles. When spawning with a model override, use `fork_turns="none"` and provide a self-contained task and file pointers. Report unavailable model choices rather than silently substituting.

## Inputs and preferences

- Baseline: `thesis_BAB_I_to_Daftar_Pustaka_revised.md`. Freeze and hash it before work. The original clean manuscript is historical, not the baseline.
- Structural reference: `fikbas_skripsi_full.md`.
- Author feedback: `thesis_writing_taste_all.csv`. The parsed records in `writing-workflow/runs/full-thesis-2026-11-18/feedback.json` can help locate relevant comments. Historical replacements are not necessarily approved prose.
- Read `.agents/skills/thesis-structure/SKILL.md`, `.agents/skills/thesis-revision/SKILL.md`, and their linked project profiles and role instructions. Apply `academic-writing` and `humanizer-id`, including the updated diagnostics and exceptions.
- Follow the reference's reasoning where it serves the target research. Explain adaptations. Assess chapters, subchapters, subsubchapters, and every deeper division separately, including the function of unheaded content and dependencies across chapters.
- Preserve existing project names inside manuscript text. Use neutral descriptions in instructions, reports, and messages, including quoted excerpts from the thesis.
- Preserve the spelling `antarperiode`. The historical request to split it has been withdrawn.
- Preserve facts, evidence, uncertainty, technical distinctions, quotations, and experimental artifacts. Keep explicitly praised explanations unless a concrete problem justifies a change. Every writing finding needs a specific reader problem, not merely a tic label.

## Execution and deliverables

Create a new run directory under `writing-workflow/runs/`. Work from frozen sources and leave the baseline manuscript intact. Previous structural work was a bounded pilot, not a complete audit. Prior findings are leads to verify against the current source.

Complete the full structural evaluation, fresh challenge, resolutions, and recursive coverage checks. Produce a structural change plan in dependency order. For accepted findings that can be addressed from supplied evidence, have the writer prepare a separate candidate, including proposed structural changes and prose revisions. This candidate is review material, not an overwrite of the baseline. Record evidence gaps rather than inventing research details.

Review writing throughout the manuscript, not only in sections with structural findings. Use the bounded reviewer/writer loop and fresh comparisons prescribed by the skills. Assess any proposed structural repairs against the original target obligations and recheck affected ancestors, dependencies, and cross-references. Review the assembled candidate for continuity and duplication.

Deliver a concise combined report linking the structural assessment and coverage, writing findings and verdicts, structural plan, separate candidate and diff if changes were accepted, and unresolved questions. Record actual model roles and verification limitations. A clear passage may remain unchanged. Do not claim full coverage until every scoped node and passage has a decision. Do not commit the new review artifacts unless the user requests it.
