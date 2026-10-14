# ML paper digest for 2026-10-14

_window: last 1 days; generated at 2026-10-14T14:56:08.645324+00:00_

## Top picks for Blume

- [Legal-R1: Agentic Retrieval for Evidence-Based Legal Reasoning](https://arxiv.org/abs/2610.18611v1) (score=2, bucket=retrieval_rag, 2026-10-13)
- [Read the Room Before Your Model Generates](https://arxiv.org/abs/2610.18820v1) (score=1, bucket=domain_adaptation, 2026-10-13)
- [UniW(A)M: A Unified Mixture-of-Experts Framework for World and World-Action Models](https://arxiv.org/abs/2610.18697v1) (score=1, bucket=domain_adaptation, 2026-10-13)
- [Geometric Calibration of Supervised Fine-Tuning](https://arxiv.org/abs/2610.18634v1) (score=1, bucket=domain_adaptation, 2026-10-13)
- [LLM Agents for Automated Post-Training via Structured Recipe Optimization](https://arxiv.org/abs/2610.18572v1) (score=1, bucket=domain_adaptation, 2026-10-13)
- [Retrieval Disagreement as a Signal: Diagnosing and Steering Multilingual Dense Embedders](https://arxiv.org/abs/2610.18526v1) (score=1, bucket=retrieval_rag, 2026-10-13)

## Domain Adaptation

### [Read the Room Before Your Model Generates](https://arxiv.org/abs/2610.18820v1)
- id: `http://arxiv.org/abs/2610.18820v1`
- published: 2026-10-13
- authors: Muyao Kong, Zhihao Lin
- categories: cs.AI, cs.CL
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Large language models (LLMs) generally rely on sampling temperature to regulate the amount of
randomness in their outputs. Mainstream methods for selecting temperature typically involve fixed,
heuristic global settings and context or token-level calibration, rather than a geometrically
interpretable representation of the communicative scenario. In this work, we introduce a simple and
interpretable temperature selection framework, the \textbf{Scenario-Actor}, which adapts decoding to
the infer...

### [UniW(A)M: A Unified Mixture-of-Experts Framework for World and World-Action Models](https://arxiv.org/abs/2610.18697v1)
- id: `http://arxiv.org/abs/2610.18697v1`
- published: 2026-10-13
- authors: Jingbo Xu, Jianjie Fang, Zhuohang Li, Zihao Song, Zhaolu Wang, Xvyuan Liu, Xin Zhang, Haisheng Su, Yinzhou Tang, Chen Gao, Wei Wu, Yong Li
- categories: cs.RO, cs.AI, cs.CV, cs.LG
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

World models (WMs) and world-action models (WAMs) focus on future world prediction and executable
action generation, respectively. Although these models learn shared physical dynamics and
interaction semantics from embodied trajectories, they are typically trained in isolation, which
restricts knowledge reuse between prediction and control. The central challenge is therefore to
develop a unified learning framework that shares these dynamics while preserving the distinct
modeling capabilities ...

### [Geometric Calibration of Supervised Fine-Tuning](https://arxiv.org/abs/2610.18634v1)
- id: `http://arxiv.org/abs/2610.18634v1`
- published: 2026-10-13
- authors: Jianzhu Bao, Jia-Chen Gu, Qingyuan Liu, Haozhen Zhang, Kai-Wei Chang, Nanyun Peng, Wenya Wang
- categories: cs.LG, cs.AI
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Recent studies investigate the weight geometry through its spectral structure, which characterizes
how the weights transform different input directions. Within this view, supervised fine-tuning (SFT)
is shown to induce dense updates that perturb the spectral geometry of pre-SFT weights along their
principal directions, potentially disrupting the model's prior knowledge. These observations
motivate using the geometry of pre-SFT weights as a reference for refining learned SFT updates. We
study ...

### [LLM Agents for Automated Post-Training via Structured Recipe Optimization](https://arxiv.org/abs/2610.18572v1)
- id: `http://arxiv.org/abs/2610.18572v1`
- published: 2026-10-13
- authors: Ruohong Liu, Bohan Tang, Lekang Jiang, Jack Umenberger, Yiwen Guo
- categories: cs.AI, cs.LG
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Automated post-training transforms pre-trained large language models (LLMs) into models capable of
handling diverse domains by automatically constructing and optimizing a recipe of coupled decisions
over data sources, data processing, cross-domain composition, and training configuration under a
limited experimental budget. Existing automation either searches predefined recipe spaces that
enable systematic optimization but remain fixed rather than adapting their available choices to the
target...


## Retrieval Rag

### [Legal-R1: Agentic Retrieval for Evidence-Based Legal Reasoning](https://arxiv.org/abs/2610.18611v1)
- id: `http://arxiv.org/abs/2610.18611v1`
- published: 2026-10-13
- authors: Huaiwen Pang, Jiale Han, Junying Chen, Wenjun Xiao, Benyou Wang
- categories: cs.CL
- query: `all:"retrieval augmented generation"`
- blume_score: 2

Legal question answering requires answers that are not only plausible, but also grounded in legally
valid and citable evidence. Standard retrieval-augmented generation often relies on one-shot
semantic matching, which is insufficient when legal evidence must be selected according to
authority, applicability, and diversity across heterogeneous sources. We introduce Legal-R1, an
agentic retrieval framework for evidence-based legal reasoning. Legal-R1 decomposes legal reasoning
into a multi-agen...

### [Retrieval Disagreement as a Signal: Diagnosing and Steering Multilingual Dense Embedders](https://arxiv.org/abs/2610.18526v1)
- id: `http://arxiv.org/abs/2610.18526v1`
- published: 2026-10-13
- authors: Faeze Ghorbanpour, Shaghayegh Kolli, Jana Diesner, Alexander Fraser
- categories: cs.CL, cs.IR
- query: `all:"dense retrieval"`
- blume_score: 1

Multilingual dense retrievers place all languages in one shared space so that a question finds
relevant documents, regardless of which language they are written in. We show that the same
question, asked in different languages, retrieves substantially different documents, and this
disagreement is not because of weak language understanding. Each language performs well on its own
and ranks candidates consistently with the other languages; divergence appears only when languages
share an index. We...

