# ML paper digest for 2026-10-23

_window: last 1 days; generated at 2026-10-23T14:45:19.743258+00:00_

## Top picks for Blume

- [How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions](https://arxiv.org/abs/2610.31606v1) (score=2, bucket=retrieval_rag, 2026-10-22)
- [From Structured Records to Patient Narratives: Preserving Clinical Alignment in LLM-Generated Health Summaries](https://arxiv.org/abs/2610.31467v1) (score=2, bucket=retrieval_rag, 2026-10-22)
- [SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing](https://arxiv.org/abs/2610.31659v1) (score=1, bucket=domain_adaptation, 2026-10-22)
- [METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning](https://arxiv.org/abs/2610.31656v1) (score=1, bucket=domain_adaptation, 2026-10-22)

## Domain Adaptation

### [SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing](https://arxiv.org/abs/2610.31659v1)
- id: `http://arxiv.org/abs/2610.31659v1`
- published: 2026-10-22
- authors: Sy-Tuyen Ho, Anirudh Satheesh, Soham Chawathe, Huy Nghiem, Yongkyun Lee, Andrew Adams Schoen, Furong Huang
- categories: cs.CV, cs.LG
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Auditing whether a text-to-image (T2I) model was fine-tuned on a particular image collection is
difficult: a model can absorb collection-level visual characteristics without reproducing training
images. Proactive dataset-use auditing plants a shared signal in a dataset before release, then
later checks whether that signal appears in a suspect model's generated outputs. Existing approaches
often trade off verifiability, fidelity, robustness, and deployability. We introduce
$\textbf{SpectralCan...

### [METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning](https://arxiv.org/abs/2610.31656v1)
- id: `http://arxiv.org/abs/2610.31656v1`
- published: 2026-10-22
- authors: Ali Najar, Hosein Hasani, Amir Kooshan Fattah, Yasamin Rajabi, Mahdieh Soleymani Baghshah
- categories: cs.LG, cs.AI
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited
interaction, but this requires representing task evidence over long interaction histories. Classical
recurrent agents compress experience into hidden states, while transformer-based agents retrieve
from past trajectories at quadratic memory and computation cost. In this work, we propose Memory-
Enhanced Test-Time Adaptation (METTA) for meta-reinforcement learning. It decomposes the fast
adaptation ...


## Retrieval Rag

### [How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions](https://arxiv.org/abs/2610.31606v1)
- id: `http://arxiv.org/abs/2610.31606v1`
- published: 2026-10-22
- authors: Miguel Mochizuki Silva, Samuel Ismael, Mateus C. Dias, Thaís Gaudêncio, Yuri Malheiros, Barufaldi
- categories: cs.CL, cs.AI
- query: `all:"retrieval augmented generation"`
- blume_score: 2

Purpose: To describe an evidence-aware retrieval evaluation protocol for a clinical retrieval-
augmented generation (RAG) system over breast lesion management literature, addressing the
dependence of retrieval scores on annotation coverage. Methods: An 18-document corpus and an
18-query development benchmark, with one Yes/No or WH-question per document, were used. Retrieval
combined dense embeddings, BM25, and cross-encoder reranking. Chunk sizes of 128 to 1024 tokens,
overlaps of 0 to 20%, an...

### [From Structured Records to Patient Narratives: Preserving Clinical Alignment in LLM-Generated Health Summaries](https://arxiv.org/abs/2610.31467v1)
- id: `http://arxiv.org/abs/2610.31467v1`
- published: 2026-10-22
- authors: Bayram Ayadi, Florian Geissler, Johanna Schmidhuber
- categories: cs.CL
- query: `all:"retrieval augmented generation"`
- blume_score: 2

As wearable and digital health systems increasingly generate longitudinal physiological records,
communicating these observations in patient-accessible language remains a significant challenge.
Large Language Models (LLMs) offer a promising mechanism for translating structured clinical
information into readable narratives, but this process may introduce semantic drift, where
clinically precise meaning is distorted during simplification. We investigate evidence-grounded
health summarization fo...

