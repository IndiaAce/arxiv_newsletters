# ML paper digest for 2026-10-21

_window: last 1 days; generated at 2026-10-21T14:56:41.916859+00:00_

## Top picks for Blume

- [DeclineCraft: A RAG Abstention Benchmark for Jointly Measuring Combined Retrieval and Parametric Knowledge](https://arxiv.org/abs/2610.28340v1) (score=2, bucket=retrieval_rag, 2026-10-20)
- [Efficient Edge-aware Attention Network for Graph Generation](https://arxiv.org/abs/2610.28618v1) (score=1, bucket=domain_adaptation, 2026-10-20)
- [Geometry-Agnostic Data-Driven Discovery of Extreme Scenarios](https://arxiv.org/abs/2610.28487v1) (score=1, bucket=retrieval_rag, 2026-10-20)

## Domain Adaptation

### [Efficient Edge-aware Attention Network for Graph Generation](https://arxiv.org/abs/2610.28618v1)
- id: `http://arxiv.org/abs/2610.28618v1`
- published: 2026-10-20
- authors: Vincent Jung, Alba Carballo-Castro, Yiming Qin, Lonneke van der Plas, Pascal Frossard
- categories: cs.LG
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Graph generative models commonly use graph-specific Transformer architectures to jointly update node
and edge features. However, these architectures do not directly benefit from recent hardware-aware
attention implementations, limiting their scalability. The adaptation is, however, non-trivial: edge
and graph-level features must be injected into pairwise attention scores, graph masks must be
respected, and dynamic edge updates remain a major source of quadratic memory usage. We propose an
edg...


## Retrieval Rag

### [Geometry-Agnostic Data-Driven Discovery of Extreme Scenarios](https://arxiv.org/abs/2610.28487v1)
- id: `http://arxiv.org/abs/2610.28487v1`
- published: 2026-10-20
- authors: Angeline Hu, Ava K. Tse, Kaitlyn S. Yasumura, Luciana Sarabia, Malcolm Yeung, Kavin K. Prasanna, Kai Wong, William Hammond, Ioannis G. Keverkidis, Shengkai Li, Trung V. Phan
- categories: cs.LG, math-ph
- query: `all:"neural search"`
- blume_score: 1

We introduce a two-stage data-driven neural framework for discovering dynamically admissible extreme
scenarios. Rather than assuming prior knowledge of the governing equations, the first stage infers
the effective dynamical constraints directly from observational data. When the underlying physical
system possesses suitable symmetries, the learned dynamics can be represented in a geometry-agnostic
form, independent of any fixed grid, coordinate system, dimensionality, and intrinsic curvature. ...

### [DeclineCraft: A RAG Abstention Benchmark for Jointly Measuring Combined Retrieval and Parametric Knowledge](https://arxiv.org/abs/2610.28340v1)
- id: `http://arxiv.org/abs/2610.28340v1`
- published: 2026-10-20
- authors: Atharva Thakur, Abulhair Saparov, Bruno Ribeiro
- categories: cs.CL, cs.IR
- query: `all:"retrieval augmented generation"`
- blume_score: 2

Reliable retrieval-augmented generation (RAG) requires recognizing when neither retrieved documents
nor parametric knowledge supports an answer. We introduce DeclineCraft, a dynamic abstention
benchmark whose unanswerable questions target Minecraft feature additions after a corpus cut-off,
with audits of possible parametric exposure. Later cut-offs support evaluation of future models.
Across 27 LLMs, we measure Correct Abstention Rate (CAR; how often models acknowledge insufficient
knowledge ...

