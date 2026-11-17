# Bounded structural assessment

The scoped target already follows the useful reasoning pattern of the reference: define the evaluation, establish the reference answer, demonstrate a decision, then explain aggregation and comparisons. Preserve that structure. The only proposed textual change is small: state the existing `is_accident = true` condition in the T5 row of Table 3.4 before readers encounter the T5 PASS/FAIL example. The results already explain the condition and show why it matters. This is [F-01 in evaluation.json](evaluation.json), a low-severity placement issue, accepted by the coordinator after independent challenge.

No manuscript changes have been made. The coordinator resolved the findings after the [independent challenge](challenge.md).

## Useful adaptations to retain

- The target's §2.8 explains exact answer correctness, percentage of PASS answers, and repeated-case consistency. These serve its operational-analysis question. Four separate text-similarity metrics would not improve that explanation.
- The two examples have different jobs. §3.2.3 derives 8.86 seconds from seven duration values and shows its output attribute. §3.5.1 compares a reference JSON with passing and failing responses. Keep both where they are.
- The success-rate equation and explicit denominator rules in §3.5.2 support the existing results. A separate arithmetic example is not a demonstrated need.
- §3.5.3 connects nine task types to six discussion groups and states how model, context, and combined comparisons are calculated. Its repeated-case comparison supports the later observation that equal total PASS counts can hide different failed cases.

These judgments are supported by baseline.md:184–200, 298–337, 441–473, and 815–817. The complete mapping, including each metric child of the reference, is in [reference-functions.md](reference-functions.md). Shared demonstration functions are merged in the target. Metric-specific calculations, synonym allowances, and embedding scores are inapplicable to its correctness criterion. The target does not need a matching number of subsections.

## Proposed action and unresolved evidence

1. **F-01 — establish the T5 filter before using it.** Extend the existing T5 rule in §3.2.3/Table 3.4 with the condition documented at baseline.md:642–655. Preserve §4.5.3's detailed error explanation and §3.5.1's paired examples. The method currently says “data kecelakaan,” yet the results show that a false-flagged incident can still have an accident report. Naming the filter therefore provides information a reader cannot safely infer from the table label. No headings, numbers, or research results need to change.
2. **F-02 — inspect Appendix 1 before diagnosing a coverage omission.** This remains unresolved. The supplied baseline points to expected-result material at line 337 and case/run records at 817, but ends at the bibliography. The needed evidence is the existing appendix, followed by the affected case artifacts only if a concrete ambiguity remains. Do not invent a new validation procedure or require every reference answer to be reproduced in the main text.

F-01 is a proposed local edit that the supplied body supports. F-02 is a limit on this review's ability to assess all-case artifact coverage. It does not establish an incorrect result or an omission from the complete thesis. There are no proposed new experiments, metrics, or section moves.

## Coverage and boundaries

| Document | Scoped roots | Depth 2 | Depth 3 | Total assessed |
| --- | --- | ---: | ---: | ---: |
| Reference | R-0024, R-0038 | 2 | 8 | 10 |
| Target | T-0021, T-0030, T-0038 | 2 | 7 | 9 |

Every scoped descendant has a separate record. Each target record assesses direct content, child organization, and the combined contribution. Tables, displayed equations, and unheaded examples are included in those judgments. No deeper heading exists within this bounded scope. The surrounding research question, design, prompts, selected results, interpretation, and conclusions were read to check boundary dependencies, not to claim a whole-thesis audit.

Eight target nodes are locally sufficient. T-0030 needs the proposed local clarification and also carries the unresolved appendix limitation. Seven dependency records cover the question-to-evaluation boundary, conceptual-to-operational scoring, expected-result prerequisites, denominators, repetition, and the comparison-to-conclusion boundary. A supported boundary means the stated structural relationship is documented, not that the underlying experiment has been independently reproduced.

The coordinator accepted F-01, retained F-02 as an evidence limitation, narrowed the appendix obligation to the materials actually promised, and distinguished the R-0041 demonstration from target-specific expected-result construction. The validator returned `coverage_and_evidence_locations_valid` for all 10 reference and 9 target records. It checked frozen-source identity, recursive record coverage, identifiers, and evidence locations. This does not establish semantic sufficiency or the truth of the findings. The final [coverage check](coverage.json) additionally checks content boundaries, local evidence anchors, and consistency between findings and node assessments. The original evaluator proposal is preserved in evaluation-proposed.json.
