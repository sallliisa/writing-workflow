# Model background and selection in four fictional theses

| Excerpt | BAB II model background | BAB III selection rationale |
|---|---|---|
| K | Partial. Identification and specifications are present. Shared explanation is missing. | Missing. Actual reasons are unavailable. |
| M | Fulfilled across §2.7 and its children. | Fulfilled in §3.4. |
| R | Partial. Methods clarify the comparison and tool requirement. The conceptual explanation is missing. | Fulfilled in §3.4. |
| V | Fulfilled across §2.7 and its children. | Missing. Actual reasons are unavailable. |

## Functions carried over from the reference

Reference §2.7 identifies the models and states what the comparison can address. In §2.7.1, “Instruksi menentukan aspek jawaban yang perlu dibahas” explains how an input affects the task. The closing sentence explains the need for independent evaluation because “jawaban yang lancar belum tentu tepat.” Section 2.7.2 explains local operation, the hardware constraint, and why access and feedback quality matter to this comparison. Section 3.4 supplies distinct practical reasons for choosing the models and identifies the inputs held constant.

Each target asks about answer correctness “dengan dan tanpa dokumen aturan bisnis” and checks values against a reference. Its background therefore needs to explain the documented capability that supports data retrieval, the limitation that warrants checking values, and what comparisons of two API models under common conditions can show. Its methods need to distinguish the author's choice of models from how the models were tested. The reference's instructor ratings, local weights, and hardware constraints belong to its own design. S1 and S2 support shared capabilities and limitations for the target pair. Neither documents internal architecture.

## K

Sections 2.7.1 and 2.7.2 identify each provider and state “diakses melalui API dengan context window 32.000 token.” BAB I supplies the analytical question and benchmark. Section 3.4 documents common tools, data, questions and call limits. Together these establish what was compared and controlled. They leave the reader to infer what each model can do with a tool and why a well-formed answer can still fail the value check.

Add one shared explanation in BAB II §2.7, retaining both concise profiles. Attribute to S1 and S2 the ability to request a tool call and use its result, explain its relevance to answering a data question, and connect the limits of structured output to the stated benchmark. Frame model and business-document conditions as the comparison, with API access common to both.

Section 3.4 says “Pengujian menggunakan API kedua penyedia.” This establishes operation. Neither it nor BAB I or II supplies the author's reason for choosing these two models. Obtain that reason from the author for BAB III §3.4. API use, a shared window size, and documented tool support cannot independently establish the historical decision.

## M

Section 2.7 attributes “mengeluarkan permintaan pemanggilan tool dan menggunakan hasilnya” to both models, connects that capability to data retrieval, and explains why “keluaran terstruktur tidak menjamin kebenaran nilainya” requires checking against an expected value. Its discussion of two API models bounds the comparison. Sections 2.7.1 and 2.7.2 complete the identification with provider, access and window size. Preserve the shared parent paragraph and both short profiles.

Section 3.4 explicitly attributes the choice to available API access during testing and support for “tool yang diperlukan.” It separately specifies common inputs and call limits, then identifies the model and presence of business-rule documents as the factors tested. Both scoped functions are fulfilled in their appropriate chapters. No repair is needed.

## R

Sections 2.7.1 and 2.7.2 supply providers, API access and “context window 32.000 token.” Section 3.4 supplies genuine additional coverage. Its research note explains the choice through available access and required tool support, and “Perbedaan yang diuji adalah model dan ada atau tidaknya dokumen aturan bisnis” defines the comparison alongside the common controls. Retain the complete selection explanation and procedures in BAB III.

The phrase “mendukung tool yang diperlukan” identifies an eligibility criterion. It leaves the reader without an account of the request and result that make the capability relevant to an analytical answer. BAB I identifies the value check but leaves its motivation implicit. Add the S1/S2-supported capability, task relevance, and structured-output limitation once in BAB II §2.7. Relate them briefly to comparison under common API conditions. The detailed factor and control list is already in §3.4. No extra architectural evidence or duplicated profile prose is needed.

## V

Section 2.7 explains that tools “digunakan untuk mengambil data sebelum menghasilkan jawaban analitis,” ties possible incorrect values to benchmark checking, and frames the two-model comparison under common API conditions. Both children identify their respective model. Preserve this complete background and its placement.

Section 3.4 records “tool, data, pertanyaan, serta batas jumlah pemanggilan yang sama” and API use. These are controls and implementation details. BAB I states the question, and BAB II establishes technical suitability. None of the three chapters states which criteria actually motivated selection. Retain the controls and obtain the author's account for BAB III §3.4. The available documentation supports the background, while the selection explanation remains open pending that evidence.
