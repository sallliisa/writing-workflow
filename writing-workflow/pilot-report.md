# Thesis revision workflow

The project-local workflow is [thesis-revision](../.agents/skills/thesis-revision/SKILL.md). It uses separate reviewer and writer roles, fresh acceptance reviews, a maximum of three revision rounds per subsection, and a retained accepted version. The thesis and original archives have not been edited.

Use it with a bounded request, for example:

> Use $thesis-revision to revise Section 3.2 of thesis_BAB_I_to_Daftar_Pustaka_clean.md. Use my editing history. Save the revised section separately and report unresolved factual questions.

The sibling [academic-writing](../.agents/skills/academic-writing/SKILL.md) and [humanizer-id](../.agents/skills/humanizer-id/SKILL.md) are repaired project-local adaptations. Keep these three skill folders together when moving them. The [audit](skill-audit.md) records the changes. This is an agent-executed skill, not an unattended scheduler or API service.

## What the first pilot showed

Two agents did not automatically produce better writing. In the first run, an independent model review preferred the single writer on three of six passages and tied the two approaches on three. The workflow arm had no wins. Those are model preferences from one small retrospective run, not measurements of the author's satisfaction.

More importantly, both approaches missed known author objections. They expanded the explanation of Pi instead of questioning whether the notation was needed. Both left an explicitly criticized comparison passage unchanged. They also rewrote passages that the historical feedback praised.

The first-run workers saw the general preference profile but not comments on the exact passages. That separation was useful for finding a weakness, but it should not be the deployed workflow. The coordinator now retrieves relevant passage-specific feedback before dispatch. Praise and objections accompany the source. Historical replacements remain proposals rather than gold answers.

| Passage | First-run result | Consequence |
| --- | --- | --- |
| P01, notation and PASS percentage | Both approaches elaborated the notation. The independent reader preferred the single writer. | Ask whether notation is needed before requiring its preservation. |
| P02, repeated access explanation | Both removed the passage using supplied context establishing repetition. | Keep the deletion. |
| P03, two ways of pooling answers | Both kept the criticized text. The independent reader also considered its groupings clear. | Explicit author difficulty must remain an open issue even when models agree with one another. |
| P04, incomplete answers | Both rewrote historically praised prose. The independent reader rejected the loop's replacement because it weakened an explicit reason for FAIL. | Keep the original and provide its positive feedback to the next round. |
| P05, repeated results | Both rewrote historically praised prose. The independent reader preferred the single writer and tied the loop with the original. | Keep the original and provide its positive feedback. |
| P06, missing context | Both preserved the source and separately requested its missing referent and causal evidence. | Keep it unresolved rather than inventing an explanation. |

The first run used one baseline writing call, one diagnostic review call, one workflow writing call, and one shared blinded comparison call. The same writing model was used in both arms. The comparison model was different but from the same model family. The historical feedback was examined after the blinded comparison to identify disagreement with the author's actual comments.

## Changes supported by the pilot

The workflow now passes relevant comments to the reviewer, writer, and acceptance reviewer. The reviewer must account for an author's stated reading difficulty. It can explain a technical disagreement, but cannot close a complaint by declaring the unchanged text clear.

The reviewer distinguishes research meaning from notation. It checks downstream dependencies before treating a temporary symbol as an invariant. The academic methods reference now explicitly preserves pooled comparisons, avoiding a template that could turn them into comparisons within each condition.

The second round uses the original text except for the accepted deletion of P02. It receives exact author comments without historical replacements. This is feedback-informed calibration on the same passages. It is not a second independent test or evidence of generalization.

## Final pilot output

The fresh [second review](passages/verdict-2.md) preferred the new P01 and P03 wording. P02 remained deleted. P04 and P05 were retained exactly as supplied. P06 remained unchanged with its missing referent and causal evidence explicitly unresolved.

The coordinator read every output and accepted those decisions. The final [passage text](passages/accepted.md), [diff](passages/accepted.diff), and [decision record](passages/decisions.json) are separate from the thesis. P06 is retained provisionally and is not publication-ready.

P01 now reads:

> Untuk setiap kasus, tiga pengulangan pada model dan kondisi konteks bisnis yang sama menghasilkan tiga jawaban. Persentase PASS dihitung dengan membagi jumlah jawaban berstatus PASS dengan tiga, lalu mengalikan hasilnya dengan 100%.

P03 now reads:

> Untuk membandingkan kedua kondisi pengujian, seluruh jawaban yang dihasilkan dengan konteks bisnis dibandingkan dengan seluruh jawaban yang dihasilkan tanpa konteks bisnis. Masing-masing kelompok mencakup jawaban dari kedua model. Untuk membandingkan model, jawaban Muse Spark 1.3 dari kedua kondisi digabungkan, lalu dibandingkan dengan gabungan jawaban DeepSeek v4 dari kedua kondisi yang sama.

These are model-reviewed proposals. The author has not yet endorsed their wording. P03 preserves the pooled comparison described by its historical source. The pilot does not establish that this is the method the current thesis should use.

The second round added a diagnostic review, a writing call, and a fresh acceptance review. Across both rounds, the passage pilot used seven agent calls, excluding the separate skill-repair work and coordinator actions. It stopped after two rounds because no supported language finding remained in the supplied packet. P06 requires unavailable evidence, so further stylistic revisions would not resolve it.

## Verification

All three skills passed the bundled structural validator. Local Markdown references resolve. The source packet hash matched at the end of the pilot. Exact text comparison confirms preservation of P04, P05, and P06 in the final draft. The four original input files still match their starting SHA-256 hashes. The [verification record](verification.json) stores these checks.

The [tool trace](pilot-tool-trace.json) records actual tool calls from the scoped worker sessions. Those calls were inspected to check source access rather than relying only on agents' final summaries. Skill snapshots are recorded before and after the demonstrated corrections. These checks establish what ran and what was preserved. They do not establish better writing across the whole thesis.

Prove It Works shaped the decision to run actual passage revisions before calling the skill ready. Separate Before Serializing Shared State shaped the separate findings, draft, verdict, and accepted files. Explain the Number shaped the decision to report one small retrospective result rather than a writing-quality improvement percentage.

## Evidence and limits

The [source packet](passages/source.md), [first verdict](passages/verdict.md), [method](pilot-method.md), and [provenance](pilot-provenance.json) preserve the initial setup. Source record numbers refer to parsed CSV records, not physical lines. The CSV has no timestamps or acceptance field.

The authoring agent had already inspected the full history. No result here qualifies as an untouched holdout. The packet contains five historical passages and one constructed missing-context probe. It does not cover full-chapter continuity, source verification against research papers, or document page layout.

Keep factual questions outside the clean replacement text. Preserving citations is different from verifying their support. The pilot demonstrates the behavior on these passages, not a guarantee that the whole thesis is ready.

## Project-neutral wording

After the pilot, project identifiers were removed from the generated skills and anonymized in the source context and provenance excerpt. Those excerpts are no longer verbatim. The provenance retains the source hash from the run and records the hash of the anonymized packet. The supplied thesis, CSV, and archives remain unchanged.
