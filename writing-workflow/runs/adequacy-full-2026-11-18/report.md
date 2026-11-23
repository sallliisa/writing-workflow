# Full writing and structure rerun · 18 November 2026

**The frozen baseline did not pass §2.7. The separately reviewed candidate now fulfills the BAB II background and comparison obligations. The author’s reason for selecting these two versions is still missing from §3.4.1.** The candidate revises eight prose passages and appends one primary-source bibliography entry. The final reviewer accepted the assembled manuscript for delivery with the listed evidence questions open. [Candidate manuscript](candidate.md) · [Diff from the previous candidate](candidate.diff) · [Final independent review](continuity-review.md)

## What the model comparison now explains

| Reader question | Decision |
|---|---|
| What do the models have in common for this comparison? | §2.7 connects tool requests, returned data, and the use of business rules to the outcome measured with and without access to the documents. Table 2.2 gives the same nominal context capacity for both versions. Capacity alone establishes neither actual token use nor accuracy. |
| What does the Muse profile add? | §2.7.1 connects Meta’s description of training for multistep work to a concrete possibility. Information about columns returned by one call can guide the next data request. The example illustrates the capability without attributing it to a particular run. |
| What does the DeepSeek profile add? | §2.7.2 identifies the release behind the documented API name and connects tool calls and structured output to the study’s task. The prompt requires a JSON object. No claim of a specific JSON-mode setting is needed. |
| Why did the author select this pair? | BAB III reports the versions, environment, settings and controls. An author account or contemporaneous design record is still needed to explain the choice. Vendor descriptions and the observed PASS rates cannot supply this fact. |

The reference’s ending paragraphs make its deployment distinction central to its model comparison. The target compares analytical answers under two document-access conditions. The revised profiles use properties relevant to that question and omit the reference’s local/cloud rationale and vision architecture. [Reference-function register](reference-functions.md) · [Primary-source findings](primary-sources.md)

## What else changed

The candidate clarifies what the judge assessed in a cited retail study, names the file that directs an agent to topical references, and makes the pattern of failures across repetitions easier to follow. It also explains why testing the seven documents together limits attribution to any individual document. A neutral-label reviewer preferred the new limitation wording. Its acceptance in this review does not establish author approval.

Beyond §2.7, the fresh evaluation overturned earlier sufficiency judgments for **§§3.3, 3.3.2, 3.4.1, 3.5 and 3.5.1**. The missing explanations concern how new sessions gained or lacked access to the documents, how the models were selected, and how the actual verdicts were assigned. §3.4.1 also needs evidence distinguishing the reported output cap from the public API maximum. For §§3.2.2, 4.8 and 4.8.3, the status moved to unresolved pending the indicator-level T9-C2 expected result. [Structural assessment](assessment.md) · [All changes from historical judgments](historical-judgment-changes.json)

**A06 concerns how the author observed an action.** All seven passages reporting run-specific actions were retained verbatim, including the distinction in T752 between the DeepSeek rounding action and the Muse status values. The open question belongs in §3.5.3. It asks what source the author used and how it was matched to each repetition. [Independent challenge and per-passage A06 decisions](challenge.md)

## Coverage, decisions and verification

| Check | Result |
|---|---|
| Structure | Both document roots, all headings, and registered unheaded divisions were reviewed to depth five. The inventory includes 201 reference nodes and 106 target nodes. The baseline assessment covers 22 dependencies. Seven of ten structural findings were accepted and three require evidence to determine the underlying fact. The candidate closes A01–A03. |
| Writing | All 368 baseline passages have decisions. Eight prose passages changed, one bibliography passage gained the cited entry, and 359 passages were retained. All 139 author-feedback records have dispositions. The two neutral-label rounds evaluated nine and three pairs. The second round resolved the three model passages whose first proposals repeated shared information. |
| Results | All 48 displayed percentage rows reconcile with their fractions and both marginal comparisons in the six task groups. The manuscript reports 90/90 PASS with access to the documents and 80/90 without access, for 170/180 overall. This is an internal check against the reported tables. Independent rescoring requires the original answers. |
| Preservation | The snapshots match the requested sources. Checks cover the system and case prompts, schema, routing quotation, worked JSON pair, displayed equations, 34 numbered tables, 2 figure captions, manuscript names, and all 13 instances of *antarperiode* including the heading. Page layout, figure artwork, and appendix contents need the full submission. |

[Full baseline decisions](evaluation.json) · [Coverage by depth](coverage.json) · [Candidate structural decisions](candidate-structure.json) · [All passage decisions](passage-decisions.json) · [Writing verdicts](writing-verdicts.json) · [Feedback dispositions](writing-feedback-dispositions.json) · [Revision decisions](revision-decisions.json) · [Arithmetic](arithmetic.json) · [Preservation checks](verification.json)

## Evidence still needed

The open register specifies the smallest evidence needed for each item. It covers model choice, document access, the source of business rules, actual scoring, observation provenance, configuration and provider defaults, T9-C2, and three bibliography entries whose citations may be outside the supplied chapters. [Questions for the author](evidence-questions.md)

The coordinator, structural and writing reviewers, challenger, two comparison reviewers, and final reviewer ran on gpt-6.2-astra. The manuscript writer ran on gpt-6-astra in both rounds. The run started from the previous candidate, retained the canonical manuscript and all previous runs, and created no commit. [Actual model roles](model-roles.json) · [Frozen baseline](baseline.md) · [Structural decisions and placement](structural-plan.md)
