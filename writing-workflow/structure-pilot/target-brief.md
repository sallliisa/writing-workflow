# Target brief — bounded workflow pilot

The target evaluates the correctness of analytical answers from two models, each with and without business context. Its question concerns agreement with expected results for operational analysis, not the similarity of generated prose (baseline.md:19–27). This brief was established before extracting the reference functions.

## Documented research and explanatory obligations

- The experiment uses 15 cases from nine task types, 237 synthetic operational rows, two models, two context conditions, and three repetitions. The resulting 180 answers must be connected to the denominators used in comparisons (baseline.md:40–44, 218–230).
- Both conditions share data access, tools, prompts, cases, and expected results. Seven business-context documents form the treatment, and their individual effects are not separated (baseline.md:42–43, 210–214, 364–385).
- Expected results are computed from the case data and business rules, stored as JSON, reused for all runs, and withheld from the agent. The explanation must connect data selection and calculation to the values used for scoring (baseline.md:298–337).
- Correctness includes valid JSON, the requested structure, every value, and array order. Property order is irrelevant, and numerical equality permits 10 and 10.0. The reader must understand why an otherwise plausible or partly correct answer fails (baseline.md:188–190, 441–455).
- Success rate counts PASS answers, including every repetition. Case consistency is shown as 0/3 through 3/3. Comparisons are descriptive, both marginal and within each model/context combination (baseline.md:194–200, 459–473).
- Results report 170/180 PASS, with all ten failures in the condition without business context. The conclusions are limited to the tested cases and final-answer correctness. The methods therefore need to support those existing comparisons, not a new experiment or an inference about operational usefulness (baseline.md:805–819, 827–835).

## Scope and available evidence

The detailed review covers T-0021 and all its children (theory of evaluation), T-0030 (expected-result construction), and T-0038 and all its children (evaluation procedure). This is nine target nodes at heading depths 2 and 3. The question, experimental design, prompts, result explanations, and conclusions are boundary context, not a full audit of those chapters.

The supplied baseline ends at the bibliography (baseline.md:841–919). It cites Appendix 1 for expected results and per-run records (337, 817), Appendix 2 for tool details (427), and Appendix 3 for business context (385), but their contents are not in this frozen file. Their absence from this pilot does not establish that the complete thesis lacks them. Figures 3.1 and 3.2 are represented here by captions (216, 409), so their visual content is not assessable from this Markdown. Neither figure is needed to infer the scored-answer rules already stated in prose.

The supplied body supports a worked expected-result calculation and a concrete PASS/FAIL example. It cannot establish whether the unavailable appendix fulfills the promised all-case summary, complete T1-C2 example, and per-case/per-run tables. No new validator, human review procedure, experiment, or numerical result may be invented to fill this limitation.

## Author preferences applied

Preserve concrete case explanations, displayed equations, identifiers, and the distinctions among null, false, zero, absent, and not applicable. Keep concepts in Chapter II and the actual study procedure in Chapter III. Recommend a structural change only when it helps readers follow a documented claim. Existing manuscript names are unchanged. This report uses neutral project descriptions.
