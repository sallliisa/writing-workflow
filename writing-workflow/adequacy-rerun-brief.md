# Rerun after the explanatory-depth failure

## Request and baseline

The user rejected the preceding workflow evaluation because it passed thin BAB II model sections without establishing that their relevant explanatory functions were fulfilled. The user requested a workflow repair and a fresh writing and structure evaluation with GPT 6.2 Astra as reviewer and GPT 6 Astra as writer.

Use `writing-workflow/runs/fresh-full-review-2026-11-18/candidate.md` as the baseline for this rerun. It is the latest reviewed candidate. Freeze it in a new run directory under `writing-workflow/runs/` and preserve it. The canonical `thesis_BAB_I_to_Daftar_Pustaka_revised.md`, all historical sources, and previous runs remain unchanged. Use `fikbas_skripsi_full.md` as the reference and `thesis_writing_taste_all.csv` as author preference evidence.

Use `gpt-6.2-astra` for the coordinator and all reviewers, including fresh challenge, neutral-label comparison, and final continuity reviews. Use `gpt-6-astra` for manuscript writers. For model overrides, spawn with `fork_turns="none"` and self-contained tasks. Record actual model roles; do not silently substitute.

## Required evaluation

Read the current local `thesis-structure`, `thesis-revision`, `academic-writing`, and `humanizer-id` skills and relevant references. The structure skill's `references/adequacy.md` and revised evaluation contract govern sufficiency. Review the entire manuscript's writing and all structural depths, including distinct unheaded content and cross-chapter dependencies. The prior full run is evidence of earlier decisions, not a list of unquestionable passes.

Read complete reference sections before mapping their functions. For every distinct applicable function, establish the reader question, target answer and location, and any remaining gap. Explain exclusions from the reference using the target's needs. Do not reduce a section's purpose to whatever the current target already contains. Record function checks in the existing evaluation fields and independently challenge central comparison, intervention, and evaluation subtrees, all substantially reduced or narrowed counterparts, and sampled other sufficient sections.

For §2.7, distinguish identification, relevant model-specific background, the conceptual basis of comparison, and the actual selection rationale. BAB II can explain the first three, including shared background where appropriate. BAB III documents actual selection and configuration. Search both chapters before calling content absent or relocated. The reference's local/cloud distinction, unrelated architecture exposition, paragraph counts, and length are not mandatory properties of the target. A short section is acceptable only when necessary explanations are fulfilled. Do not invent why the author chose the models.

If an accepted background repair needs factual support beyond the supplied manuscript, consult primary documentation and record the exact sources and supported claims. Clearly distinguish verified documentation from unsupported claims in an existing draft. Missing documentation or author decisions remain specific evidence questions; they do not become a sufficiency pass. Do not invent model properties, citations, experiments, selection reasons, or results.

## Revision and delivery

Create a separate candidate from the frozen baseline. Apply only repairs justified by the new assessment and supported evidence. Use the bounded reviewer/writer loop and fresh neutral-label comparisons. Preserve accepted prior repairs unless the new review identifies a specific regression. Recheck structural obligations and affected ancestors after revisions, then check assembled prose, citations, technical distinctions, numbers, experimental prompts, and cross-references.

Preserve existing names within manuscripts. Use neutral project descriptions in reports, instructions, messages, and quoted review excerpts. Preserve `antarperiode`; the historical spelling request was withdrawn. Protect the author's praised explanations and distinguish historical rewrite proposals from explicit approval.

Deliver a combined report, complete structural evaluation and coverage, a fresh challenge with explicit sufficiency decisions, writing decisions for every passage, a separate candidate and diff, preservation checks, and unresolved evidence needs. Specifically state how §2.7 fares under the repaired criteria and which other sections changed from sufficient to needing explanation, if any. Separate checked coverage from semantic judgment and evidence completeness. Save actual model roles. Leave all baseline files intact and do not commit new run artifacts unless requested.
