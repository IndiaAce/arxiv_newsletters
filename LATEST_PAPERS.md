# ML paper digest for 2026-10-20

_window: last 1 days; generated at 2026-10-20T14:49:32.868440+00:00_

## Top picks for Blume

- [A Semantic Knowledge Graph Construction Pipeline for Vehicle Intention Prediction in nuScenes](https://arxiv.org/abs/2610.26528v1) (score=4, bucket=entity_linking_graph, 2026-10-19)
- [EpiLens: Lightweight RAG for Epidemiological Knowledge Acquisition](https://arxiv.org/abs/2610.26730v1) (score=2, bucket=retrieval_rag, 2026-10-19)
- [TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning](https://arxiv.org/abs/2610.26754v1) (score=1, bucket=domain_adaptation, 2026-10-19)
- [recAMPLIFY: Large-Scale Pretraining of Recursive Protein Language Models](https://arxiv.org/abs/2610.26747v1) (score=1, bucket=domain_adaptation, 2026-10-19)

## Entity Linking Graph

### [A Semantic Knowledge Graph Construction Pipeline for Vehicle Intention Prediction in nuScenes](https://arxiv.org/abs/2610.26528v1)
- id: `http://arxiv.org/abs/2610.26528v1`
- published: 2026-10-19
- authors: Khaled Nowara, Mohamed Manzour, Catherine Elias
- categories: cs.AI, cs.LG
- query: `all:"knowledge graph" AND all:"construction"`
- blume_score: 4

Knowledge graphs (KGs) are increasingly used in autonomous driving (AD) to make traffic scene
entities and relations explicit for prediction and reasoning. Existing traffic-scene KGs, however,
primarily emphasize trajectory forecasting or general scene understanding. This paper presents the
nuScenes Intention Knowledge Graph (NIKG), a focused Web Ontology Language (OWL)-based semantic
representation and construction pipeline for ego-centric vehicle intention context. NIKG
instantiates nuScene...


## Domain Adaptation

### [TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning](https://arxiv.org/abs/2610.26754v1)
- id: `http://arxiv.org/abs/2610.26754v1`
- published: 2026-10-19
- authors: Liana Patel, Rishabh Ranjan, Ion Stoica, Matei Zaharia, Carlos Guestrin
- categories: cs.CL, cs.AI
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Expert human readers process large inputs (e.g., code repositories and long documents) by skimming
to closely read only what matters. On the other hand, language models process all input tokens
through each model layer, resulting in significant processing costs for long-context inputs. We
introduce TokenGate, a small, drop-in component that extends existing trained models to enable end-
to-end learnable token pruning over long-context inputs for fast and memory-efficient prefill. To
enable end...

### [recAMPLIFY: Large-Scale Pretraining of Recursive Protein Language Models](https://arxiv.org/abs/2610.26747v1)
- id: `http://arxiv.org/abs/2610.26747v1`
- published: 2026-10-19
- authors: Saurav Jha, Qianli Liao, Robert Vernon, Sarath Chandar, Quentin Fournier
- categories: cs.LG, cs.AI, cs.CL
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Protein language models (pLMs) are powerful tools for protein annotation and mutation-effect
prediction, but progress has largely depended on scaling model size and data, making them expensive
and prone to memorization. Test-time scaling offers a complementary path, but methods developed for
autoregressive LLMs do not transfer directly: masked encoders lack a generation loop, and amino
acids do not verbalize in a reasoning language. Instead, we adapt recursive pretraining to masked
pLMs, wher...


## Retrieval Rag

### [EpiLens: Lightweight RAG for Epidemiological Knowledge Acquisition](https://arxiv.org/abs/2610.26730v1)
- id: `http://arxiv.org/abs/2610.26730v1`
- published: 2026-10-19
- authors: Vincenzo Perri, Ciro Cattuto, Daniela Paolotti
- categories: cs.CL, cs.DL, physics.soc-ph
- query: `all:"retrieval augmented generation"`
- blume_score: 2

To prepare for future outbreaks, researchers need to know what studies have been done and what data
they use. Mapping a large literature by hand is slow, while large language models alone can misstate
or conflate sources. We present EpiLens, a lightweight, open-source retrieval-augmented generation
package that applies a fixed retrieval template and output schema to every paper in a corpus and
links outputs to source passages. We build a corpus of 2,297 papers from the sources of a multi-
path...

