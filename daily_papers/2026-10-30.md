# ML paper digest for 2026-10-30

_window: last 1 days; generated at 2026-10-30T16:34:43.694770+00:00_

## Top picks for Blume

- [Glance: The Generator Is Its Own Reranker](https://arxiv.org/abs/2610.40454v1) (score=2, bucket=retrieval_rag, 2026-10-29)
- [Numerical Integration on Bounded Domains via Learned Reflected Diffusions](https://arxiv.org/abs/2610.40499v1) (score=1, bucket=domain_adaptation, 2026-10-29)

## Domain Adaptation

### [Numerical Integration on Bounded Domains via Learned Reflected Diffusions](https://arxiv.org/abs/2610.40499v1)
- id: `http://arxiv.org/abs/2610.40499v1`
- published: 2026-10-29
- authors: Kirill Korolev, Artur Goldman, Timofei Gritsaev, Tigran Ramazyan, Nikita Morozov
- categories: cs.LG, stat.ML
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

We study high-dimensional integration on bounded convex domains. Given a non-negative integrand $r$,
the goal is to estimate $Z=\int_{D}r(x)\,\mathrm dx$ on $D\subset\mathbb R^d$. Standard Quasi-Monte
Carlo does not adapt its evaluation points to the integrand, while effective importance sampling
requires a proposal that captures its concentration. Learned diffusion samplers can supply such a
proposal, but existing methods are formulated on $\mathbb R^d$ and do not respect the domain
constrai...


## Retrieval Rag

### [Glance: The Generator Is Its Own Reranker](https://arxiv.org/abs/2610.40454v1)
- id: `http://arxiv.org/abs/2610.40454v1`
- published: 2026-10-29
- authors: Adilet Metinov, Chingiz Arziev
- categories: cs.CL, cs.IR
- query: `all:"retrieval augmented generation"`
- blume_score: 2

Retrieval-augmented generation commonly serves separate models for reranking and answering,
duplicating model residency and passage processing. We introduce Glance, which equips the generator
with a lightweight decision adapter and pointer head to score candidate passages from a shared
prefill. Short relevance probes branch from the cached context, producing one score per passage
without separately prefilling each query-passage pair. A single resident 9B backbone supports
generation, general ...

