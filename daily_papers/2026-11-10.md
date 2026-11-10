# ML paper digest for 2026-11-10

_window: last 1 days; generated at 2026-11-10T17:33:04.415788+00:00_

## Top picks for Blume

- [Anchor Behavior, Not Parameters: Rehearsal-Free Continual Learning with a Single Shared Prompt](https://arxiv.org/abs/2611.12777v1) (score=1, bucket=domain_adaptation, 2026-11-09)

## Domain Adaptation

### [Anchor Behavior, Not Parameters: Rehearsal-Free Continual Learning with a Single Shared Prompt](https://arxiv.org/abs/2611.12777v1)
- id: `http://arxiv.org/abs/2611.12777v1`
- published: 2026-11-09
- authors: Duy-Cuong Bui, Trung-Anh Dang, Vincent Nguyen, Duc V. Le, Ngoc-Son Vu
- categories: cs.LG, cs.CV
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Prompt-based continual learning adapts a frozen pre-trained vision transformer by tuning a small set
of prompt tokens. Recently, one-prompt methods which share one single prompt across all tasks make
this paradigm maximally parameter efficient. The open question is how a shared prompt can keep the
knowledge of old classes while being updated for new ones. Existing methods protect old knowledge in
parameter space, where they freeze task-specific prompts, expand new components, or sparsely gate...

