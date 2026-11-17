# Skill repairs

The project-local skills were adapted from the supplied archives on 18 November 2026. The ZIP archives, editing history, and thesis were preserved. These changes repair instruction conflicts. Their effect on writing quality requires the passage pilot and user feedback.

## Academic writing

| Source location | Problem found | Local change |
| --- | --- | --- |
| `academic-writing/SKILL.md`, Establish the target | Treating prior revisions as a minimum floor encouraged continued rewriting without a demonstrated defect. | Require a concrete reader problem. Keep clear passages and stop when the problem is resolved. |
| `references/examples.md`, Name the evaluation unit | The recommended wording contains "tersimpan menjadi satu unit penilaian" and "terkait dengan satu kasus". The CSV criticizes those phrases as technical and unnecessarily detailed. | Removed the stale example. Replaced the example collection with explicitly proposed illustrations and a keep-as-is case. |
| `references/examples.md`, Explain the data relationship | "Catatan durasi" conflicts with feedback favoring data. | Removed that example. A new proposed calculation example uses "data durasi" and makes source support a condition. |
| Entrypoint and `references/thesis-workflow.md` | Relevance, section ownership, claim scope, and evidence guidance appeared repeatedly. | Keep those decisions in the entrypoint. The workflow reference covers chapter responsibilities, reference theses, comparison tables, and method explanations. |
| Thesis-specific terminology and formatting | Project conventions were mixed with reusable academic guidance. | Link the thesis preference profile maintained by the workflow skill. The generic skill does not duplicate those conventions. |
| Prior examples labeled accepted | Some replacement wording also appears in criticized passages. The CSV does not establish chronology. | Treat an `after` value as a revision record rather than approval. Check linked feedback before calibration. |

Preserved protections cover unsupported claims, citation attachment, uncertainty, causal language, calculations, denominators, rounding, source integrity, technical identifiers, and authorized scope. A source claim may be removed or relocated when appropriate, but its evidence must be accounted for. Review requests still do not authorize whole-document rewrites.

## Humanizer ID

| Source location | Problem found | Local change |
| --- | --- | --- |
| Section 5, sentence fusion | Required combining two or three short sentences into a complex sentence. | Split or combine only when comprehension improves. |
| Section 5, paragraph ending | Required a short concluding sentence for rhythm. | End the paragraph when its explanation is complete. |
| Calque table, introductory participle | Adding "karena" can introduce causation absent from the original. | Inspect the supported relationship before choosing a conjunction. |
| Modality calibration | Listed "menunjukkan" and "membuktikan" together as empirical certainty and treated "berkorelasi" as a general inference marker. | Distinguish observation, proof, causal interpretation, and correlation. Preserve the supported scope of certainty. |
| Cross-domain glossary | Generic translations can conflict with established technical terms. | Use the manuscript's terminology and inspect each proposed replacement in context. |
| Citation weaving | Mechanical movement and grouping can obscure attribution or conflict with project punctuation. | Preserve useful narrative attribution. Group sources only when their claims support that grouping. |
| Mandatory annotated diff | Required every changed sentence in a table regardless of the user's requested artifact. | Follow the requested format. Supply a full change table when requested. |
| `scripts/audit.py` | Its no-match report claims clear prose despite checking only phrase patterns. | Omitted the scanner from the local adaptation. Explicitly state that phrase matches cannot establish semantic or writing quality. The archived scanner remains unchanged. |

The local Humanizer skill contains its entrypoint, a focused diagnostic reference, and the original MIT license. It does not copy unrelated legal or business workflow material, glossary datasets, the promotional image, or alternative prompt files. Those resources remain in the original archive. The local metadata identifies this as an adaptation of version 1.5.0.

## Validation

Both skills passed the bundled validator with these commands:

```sh
uv run --with pyyaml python /Users/gamer/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/academic-writing
uv run --with pyyaml python /Users/gamer/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/humanizer-id
```

The system `python3` lacked PyYAML. `uv` supplied the validator dependency without changing project dependencies. Structural validation does not establish better writing. The workflow pilot evaluates the generated passages separately.

The repaired skills depend on `../thesis-revision/references/thesis-profile.md` for this thesis's local rules. Keep that sibling skill when moving these project-local copies. Their generic branches remain usable with another manuscript's own conventions.

## Original artifact hashes

SHA-256 values checked after the repairs matched the original values:

| Artifact | SHA-256 |
| --- | --- |
| `academic-writing.zip` | `fc10152922a2e23cb97204694d5df30a03bbba9e7320c32b4ac35a2581b5fa61` |
| `humanizer-id.zip` | `74655c33144421e06df973bc0bb9ad17b6d1eebce41b2680a876bb29ffe65de8` |
| `thesis_writing_taste_all.csv` | `4958882dfae543b77d4dac1c781700ee277cc0a74128f0bc3d16ed08f534e5eb` |
| `thesis_BAB_I_to_Daftar_Pustaka_clean.md` | `1e245efd6135f89a25ffcc2cf6aefa39e3eb072773988b475032422461d7fab2` |
