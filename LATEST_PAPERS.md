# ML paper digest for 2026-10-16

_window: last 1 days; generated at 2026-10-16T14:39:26.295249+00:00_

## Top picks for Blume

- [Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries](https://arxiv.org/abs/2610.22273v1) (score=4, bucket=entity_linking_graph, 2026-10-15)
- [Close Enough is Nowhere Near: Fidelity-Consumability Decoupling in KV Caches](https://arxiv.org/abs/2610.22016v1) (score=1, bucket=domain_adaptation, 2026-10-15)

## Entity Linking Graph

### [Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries](https://arxiv.org/abs/2610.22273v1)
- id: `http://arxiv.org/abs/2610.22273v1`
- published: 2026-10-15
- authors: Anikait Singh, Teresa Zhang, Yoonho Lee, Roshen Sanjay Nair, Aviral Kumar, Chelsea Finn
- categories: cs.LG, cs.AI, cs.CL
- query: `all:"knowledge graph" AND all:"construction"`
- blume_score: 4

Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard
retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document
reasoning at inference time, while precomputed structures like knowledge graphs often fall short
because they rely on rigid heuristics. Instead, can we allow agents to perform anticipatory directed
curation: learning to proactively reorganize unstructured corpora prior to inference to efficiently
serve...


## Domain Adaptation

### [Close Enough is Nowhere Near: Fidelity-Consumability Decoupling in KV Caches](https://arxiv.org/abs/2610.22016v1)
- id: `http://arxiv.org/abs/2610.22016v1`
- published: 2026-10-15
- authors: Adam Deng, Shicheng Liu, Yada Zhu
- categories: cs.LG
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Multi-agent LLM systems communicate in text, which is lossy and wasteful: the sender throws away the
reading it already did. A growing literature instead transmits the KV cache, the natural carrier of
that reading. We study the most appealing form of the idea: both models stay frozen and the sender's
cache is substituted for the reader's with nothing trained. It does not work, and the obstruction
belongs to the reader. A frozen transformer reads only caches close to the one it would have writ...

