# ML paper digest for 2026-10-22

_window: last 1 days; generated at 2026-10-22T14:56:43.434725+00:00_

## Top picks for Blume

- [Graph Topology Meets Energy-Driven Pathfinding: Preserving Contextual Consistency in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.29933v1) (score=5, bucket=entity_linking_graph, 2026-10-21)
- [GoiBERT: Compact Vietnamese Language Models via Two-Stage Knowledge Distillation](https://arxiv.org/abs/2610.30067v1) (score=4, bucket=ner_extraction, 2026-10-21)
- [Graph Topology Meets Energy-Driven Pathfinding: Preserving Contextual Consistency in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.29933v1) (score=3, bucket=retrieval_rag, 2026-10-21)
- [Code Comprehensor: Hierarchical Documentation and Cross-Modal Retrieval for Large Repositories](https://arxiv.org/abs/2610.30016v1) (score=2, bucket=retrieval_rag, 2026-10-21)
- [How Do DiTs Denoise? An Aggregator-Predictor View of Attention and MLPs](https://arxiv.org/abs/2610.29854v1) (score=1, bucket=domain_adaptation, 2026-10-21)

## Ner Extraction

### [GoiBERT: Compact Vietnamese Language Models via Two-Stage Knowledge Distillation](https://arxiv.org/abs/2610.30067v1)
- id: `http://arxiv.org/abs/2610.30067v1`
- published: 2026-10-21
- authors: Quang Anh Kiet Tran, Nam Anh Tran, Manh Hung Trinh, Thanh Danh Le, Khang Nhat Hoang Vo, Huynh Dai Nhan Tran
- categories: cs.CL
- query: `all:"named entity recognition"`
- blume_score: 4

Vietnamese pre-trained encoders have improved rapidly, but the strongest ones are large,
multilingual-vocabulary models or depend on external word segmentation, which makes them costly to
deploy. We present GoiBERT, a family of two compact Vietnamese encoders with 26M and 49M parameters
that operate directly on raw text. GoiBERT learns from two complementary teachers. A same-tokenizer
Vietnamese encoder first teaches general-purpose representations. A much larger teacher then
provides task-le...


## Entity Linking Graph

### [Graph Topology Meets Energy-Driven Pathfinding: Preserving Contextual Consistency in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.29933v1)
- id: `http://arxiv.org/abs/2610.29933v1`
- published: 2026-10-21
- authors: Yufeng Li, Zaijing Li, Fuchen Zhang, Zongzong Wu, Ming Zhao, Fengxiao Tang
- categories: cs.CL, cs.AI
- query: `all:"knowledge graph" AND all:"construction"`
- blume_score: 5

Retrieval-augmented generation (RAG) frequently integrates knowledge graphs (KGs) for complex multi-
hop question answering. However, their performance is increasingly bottlenecked by the knowledge
structuring and reasoning processes. (i) Severe semantic loss: Distilling continuous texts into
discrete symbols strips away contextual nuances and narrative coherence. (ii) Pronounced modality
mismatch: Fragmented graph structures clash with the continuous texts LLMs are pre-trained on, while
rewri...


## Domain Adaptation

### [How Do DiTs Denoise? An Aggregator-Predictor View of Attention and MLPs](https://arxiv.org/abs/2610.29854v1)
- id: `http://arxiv.org/abs/2610.29854v1`
- published: 2026-10-21
- authors: Gyeonghun Kang, William Xingxu Chen, Xiang Cheng
- categories: cs.CV, stat.ML
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

How do diffusion transformers (DiTs) represent image content and learn rules for reusing it to
generalize? We develop an aggregator--predictor view of DiTs as input-adaptive local denoisers, in
which context aggregation and patch prediction provide functional roles for interpreting attention
and MLPs. We first establish that, for Gaussian Markov random field (GMRF) priors, the global Bayes
denoiser can be approximated using only a subset of context patches, with error decaying
exponentially i...


## Retrieval Rag

### [Code Comprehensor: Hierarchical Documentation and Cross-Modal Retrieval for Large Repositories](https://arxiv.org/abs/2610.30016v1)
- id: `http://arxiv.org/abs/2610.30016v1`
- published: 2026-10-21
- authors: Sujoy Roychowdhury, Joseph H. R. Isaac, Jiangning Gao, Martin Klitte, Diarmuid Corcoran
- categories: cs.SE, cs.AI, cs.LG
- query: `all:"hybrid retrieval"`
- blume_score: 2

Understanding large, complex, and rapidly evolving code bases remains a core challenge for software
engineering at scale, hindering onboarding, maintenance, refactoring, and impact analysis. Providing
this information to a Large-Language Model (LLM) is another hurdle, as the LLM must understand not
only the required code method but also its associated methods in the grand scheme of the repository.
We propose Code Comprehensor, a hybrid retrieval-reasoning framework combining (i) a code depend...

### [Graph Topology Meets Energy-Driven Pathfinding: Preserving Contextual Consistency in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.29933v1)
- id: `http://arxiv.org/abs/2610.29933v1`
- published: 2026-10-21
- authors: Yufeng Li, Zaijing Li, Fuchen Zhang, Zongzong Wu, Ming Zhao, Fengxiao Tang
- categories: cs.CL, cs.AI
- query: `all:"retrieval augmented generation"`
- blume_score: 3

Retrieval-augmented generation (RAG) frequently integrates knowledge graphs (KGs) for complex multi-
hop question answering. However, their performance is increasingly bottlenecked by the knowledge
structuring and reasoning processes. (i) Severe semantic loss: Distilling continuous texts into
discrete symbols strips away contextual nuances and narrative coherence. (ii) Pronounced modality
mismatch: Fragmented graph structures clash with the continuous texts LLMs are pre-trained on, while
rewri...

