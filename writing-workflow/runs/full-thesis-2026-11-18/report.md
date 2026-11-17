# Full thesis revision

The workflow reviewed all five chapters and the bibliography. After the author's spelling correction, 21 block replacements remain in the separate [revised manuscript](../../../thesis_BAB_I_to_Daftar_Pustaka_revised.md). The original manuscript is unchanged. Existing names remain in the revised text.

The workflow and earlier pilot were committed before this run as `1567cc3`, `feat(writing): add calibrated thesis revision workflow`. The revised manuscript, this run's artifacts, and the subsequent skill correction are included in a separate follow-up commit.

## What changed

- Clarified what is compared, which records are counted, and what PASS/FAIL describes. Specific changes explain indicator status across periods, the incident-selection error, and consistency across repetitions.
- Made the methods explain the three result views: pooling by business-context condition, pooling by model, and presenting each model/context combination separately.
- Restored three displayed equations using existing quantities. These show total duration, mean duration, and success percentage.
- Applied the author's terminology preferences where supported by the editing history.
- Replaced an unexplained methodological label in the literature table with its concrete procedure. The explanation preserves one SQL query per question without execution feedback or revision, as described in Section 4.2 of the [primary paper](https://arxiv.org/pdf/2604.25149). This was a targeted source check, not a reference audit.

Detailed explanations that the author praised remain. The workflow did not use shortness, a numerical style score, or an AI detector as the acceptance criterion.

## Decisions and stopping point

The first round accepted 28 of 31 proposals. Three proposals required reconsideration because they removed a useful qualification, repeated an explanation, or introduced an ambiguous category label. The second round accepted four of five proposals, including two terminology corrections found during coordinator review. One shortening tied with the source, so the source remained.

The author subsequently withdrew the spacing correction for `antarperiode`. All 13 such changes were reverted. Eleven spelling-only replacements were removed, and two mixed replacements retain their substantive clarifications. The skill no longer instructs this spelling change, and the withdrawn historical request is marked inactive. The [correction record](user-correction.json) lists the affected decisions. The current manuscript differs from the previously delivered version only by these spelling reversions.

The [final ledger](decisions-final.json) resolves all 36 proposals. The [diff](revision.diff) shows the accepted changes. The [continuity review](continuity-review.json) found no additional actionable defect after reading the assembled manuscript and checking the final one-paragraph reversion. The run stopped after those findings were resolved, within the three-round limit.

The phrase `antarpengulangan` remains in a results passage that closely matches a praised historical version. Record 40 praises that version, which uses a shorter model name; record 104 objects to the word elsewhere. The history has no chronology that resolves this conflict. The current passage was retained because its following sentences make the comparison clear. This is not a blanket terminology rule.

## Verification

The [verification artifact](verification.json) records these checks:

- The original matches its frozen SHA-256 hash. The revised manuscript can be reconstructed exactly from the accepted replacements.
- All 46 protected blocks remain unchanged, including experimental excerpts and the complete bibliography.
- All 214 table rows retain their structure and numeric cell contents. All 48 displayed PASS/total percentages agree with their ratios when rounded to two decimal places.
- Parenthetical year-citation counts and the exact heading sequence are preserved.
- The three added equations use the existing data. The added counts in the incident explanation match the source results table and its discussion.

Run `python3 writing-workflow/runs/full-thesis-2026-11-18/verify.py` from the workspace to repeat the mechanical checks. They establish preservation and arithmetic consistency. Editorial review separately assesses meaning, attribution, conditions, and readability. Neither replaces verification of experimental records or all cited research.

## Still needs the complete document

- Figures 3.1 and 3.2 have captions, but their images are not included in the supplied Markdown. Their contents and layout were not assessed.
- Appendix references remain, but Appendices 1–3 are not included in the supplied file. Their cross-referenced contents cannot be checked here.
- Justified bibliography alignment, boxed prompts, equation rendering, captions, and pagination require the actual formatted document.
- A semicolon remains inside a verbatim experimental prompt. It was preserved as research material despite the author's preference against semicolons in thesis prose.

These are limits of the supplied artifact, not claims that the full thesis lacks those materials.

The coverage record accounts for all 363 source blocks. Coverage and agent agreement do not establish ideal writing or author approval. The revised manuscript is ready for the author's reading and review.

## Audit

Prove It Works guided the decision to verify the saved manuscript against its frozen source and accepted replacements. A fresh `gpt-6.2-sol` reviewer checked the original run's decision trail against the tool record and reproduced its diff and mechanical results. Its minor documentation flags were addressed in the [audit resolution](audit-resolution.md). Only GPT-family models were available, so this review does not provide validation from a different model family. After the author's spelling correction, the coordinator confirmed that only those spelling changes were reverted and reran the mechanical checks. The earlier review artifacts describe the original run.
