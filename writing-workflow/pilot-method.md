# Retrospective passage pilot

Compare one writing pass with a reviewer and writer loop. Both writing arms use the same available model, source packet, academic guidance, and project preference profile. The loop adds diagnosis and fresh acceptance review. The comparison does not isolate model quality or establish long-term reliability.

The supplied Claude and Grok model settings cannot run in this host. Writing and initial review use gpt-6.2-astra with high reasoning. Independent comparison uses gpt-6.2-sol with high reasoning. Both are from the same model family. This limits independence.

## Passage selection

The packet contains five passages from CSV records 4, 70, 79, 38, and 40, plus a constructed missing-context passage. The historical feedback and replacements are stored separately in pilot-provenance.json. Workers may read only their source packet and relevant skill files. Fresh workers receive no parent conversation.

P01 concerns unnecessary notation. P02 concerns repetition. P03 concerns an explanation of pooled results where simplifying the wording can change the method. P04 and P05 have positive historical feedback. P06 requires restraint because its referent and evidence are missing.

The authoring agent inspected the entire CSV before selection. These passages are therefore retrospective probes, not an untouched holdout. Specific historical replacement text and praise are withheld from workers. P03's historical replacement changes the comparison described in the source, so it is not a gold answer.

## Comparison criteria

Judge both outputs under neutral labels, with label order alternated by passage. Read the source and context, but withhold the writer notes, arm identities, historical feedback, and proposed historical replacements until after the initial comparison.

For each passage inspect:

1. Comprehension. Can the reader identify the object, action, comparison, and condition without reconstructing omitted meaning?
2. Relevance and continuity. Does the text belong here and connect to its context without repetition or invented transitions?
3. Research meaning. Are quantities, units, populations, comparisons, conditions, uncertainty, and citation relationships preserved?
4. Restraint. Is every change justified by a reader problem? Is already-clear text preserved?
5. Missing evidence. Does the editor identify unresolved facts rather than guessing or making an unsupported claim more fluent?

Record a preference or tie with quoted evidence. Any material semantic regression disqualifies a replacement regardless of fluency. Distinguish identical text from different but equally acceptable versions. Compare selected output against the frozen source before acceptance.

## Limits and stopping

Use at most three rounds for the loop. Stop earlier if the proposed text resolves all actionable issues or no change earns acceptance. Preserve unresolved source questions in notes. A comparison between agents is provisional evidence of editorial quality, not proof of the author's preference.

Report actual agent calls, cases, acceptance decisions, preserved passages, and remaining questions. Inspect every output. A small one-run result supports workflow changes only for demonstrated defects. It does not justify a percentage improvement in writing quality.
