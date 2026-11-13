# ML paper digest for 2026-11-13

_window: last 1 days; generated at 2026-11-13T17:33:55.909973+00:00_

## Top picks for Blume

- [FLEX-LBP: Learning Local Binary Patterns with Exact Binary Inference for Texture Classification](https://arxiv.org/abs/2611.17302v1) (score=1, bucket=domain_adaptation, 2026-11-12)

## Domain Adaptation

### [FLEX-LBP: Learning Local Binary Patterns with Exact Binary Inference for Texture Classification](https://arxiv.org/abs/2611.17302v1)
- id: `http://arxiv.org/abs/2611.17302v1`
- published: 2026-11-12
- authors: Mohamed Alimoussa, Amal El Kaid
- categories: cs.CV, cs.LG
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Local Binary Patterns (LBP) remain among the most widely used texture descriptors, from industrial
inspection to medical imaging. Yet their radius, sampling angles, color transform and thresholds are
fixed by hand for each dataset. We present FLEX-LBP, which learns these parameters by
backpropagation while every forward pass computes exact binary codes and hard histogram counts. A
straight-through estimator acts only in the backward pass, so the deployed descriptor is an
interpretable hard-bi...

