# ML paper digest for 2026-11-03

_window: last 1 days; generated at 2026-11-03T17:37:50.217344+00:00_

## Top picks for Blume

- [BISECT: Bilevel Spectral Decomposition for Low-Rank Continual Learning](https://arxiv.org/abs/2611.03574v1) (score=1, bucket=domain_adaptation, 2026-11-02)
- [Library of Layers (LoL): Adaptively Ordering Transformer Layers at Runtime](https://arxiv.org/abs/2611.03526v1) (score=1, bucket=domain_adaptation, 2026-11-02)
- [RASP: Read-All, Sparse-Plasticity Continual Learning in a Stationary-Size LoRA](https://arxiv.org/abs/2611.03513v1) (score=1, bucket=domain_adaptation, 2026-11-02)

## Domain Adaptation

### [BISECT: Bilevel Spectral Decomposition for Low-Rank Continual Learning](https://arxiv.org/abs/2611.03574v1)
- id: `http://arxiv.org/abs/2611.03574v1`
- published: 2026-11-02
- authors: Tom Saliencro, Wen-Hsuan Liu, Rohan Desai, Amara Okonkwo, Maya Lindqvist
- categories: cs.LG
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Exemplar-free continual learning on pre-trained Vision Transformers increasingly relies on Low-Rank
Adaptation (LoRA), yet prevailing methods govern the low-rank update space through strict subspace
isolation. By projecting each incoming task into the approximate null space of historical token
activations, isolation-based learners equate any cross-task feature overlap with catastrophic
interference. We show that this orthogonality premise induces a structural bottleneck we term
\emph{spectral...

### [Library of Layers (LoL): Adaptively Ordering Transformer Layers at Runtime](https://arxiv.org/abs/2611.03526v1)
- id: `http://arxiv.org/abs/2611.03526v1`
- published: 2026-11-02
- authors: Abdellah Rahmani, Sean McLeish, Ang Li, Sanae Lotfi, Pascal Frossard, Micah Goldblum
- categories: cs.LG, cs.AI, cs.CL
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Computer programmers chain together the same reusable computational primitives, for example,
conditional statements or loops, but in different orders to implement different algorithms. In
contrast, existing language model architectures always execute their layers in the same order. We
introduce Library of Layers (LoL), an architecture that dynamically orders its layers during
inference to solve the problem at hand. LoL has a single hyperparameter, the size of its global
library of transformer...

### [RASP: Read-All, Sparse-Plasticity Continual Learning in a Stationary-Size LoRA](https://arxiv.org/abs/2611.03513v1)
- id: `http://arxiv.org/abs/2611.03513v1`
- published: 2026-11-02
- authors: Wen-Hsuan Liu, Amara Okonkwo, Tom Saliencro, Rohan Desai, Maya Lindqvist
- categories: cs.LG
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Parameter-efficient continual learning on pre-trained Vision Transformers largely relies on a costly
premise: preventing catastrophic forgetting requires either spawning a dedicated LoRA branch per
session---causing adapter parameters to scale linearly with task horizon---or applying sparse
Mixture-of-Experts gating symmetrically to both forward and backward passes, which sacrifices
representational rank at test time. We argue that reading consolidated knowledge and writing new
task credit ar...

