# ML paper digest for 2026-11-20

_window: last 1 days; generated at 2026-11-20T18:24:41.047009+00:00_

## Top picks for Blume

- [One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning](https://arxiv.org/abs/2611.26617v1) (score=1, bucket=domain_adaptation, 2026-11-19)

## Domain Adaptation

### [One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning](https://arxiv.org/abs/2611.26617v1)
- id: `http://arxiv.org/abs/2611.26617v1`
- published: 2026-11-19
- authors: Yuxin Jiang, Wenqiang Sun, Jiaqi Li, Yuchao Gu, Lvmin Zhang, Ivor Tsang, Mike Zheng Shou
- categories: cs.CV, cs.AI, cs.LG, cs.RO
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Videos reveal how the world changes, but rarely the actions that cause those changes. Latent action
learning recovers such supervision from visual transitions, yet often learns the underlying dynamics
largely from scratch. We ask whether a pretrained video generator can instead provide the prior for
both inverse and forward dynamics. We introduce O$^{2}$LaF, built on a simple principle: one prior,
two dynamics. We initialize both models from the same pretrained video DiT and adapt them to the...

