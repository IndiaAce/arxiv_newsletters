# ML paper digest for 2025-11-19

_window: last 1 days; generated at 2025-11-19T10:08:20.326051+00:00_

## Top picks for Blume

- [Ground Truth Generation for Multilingual Historical NLP using LLMs](https://arxiv.org/abs/2511.14688v1) (score=4, bucket=ner_extraction, 2025-11-18)
- [AdamHD: Decoupled Huber Decay Regularization for Language Model Pre-Training](https://arxiv.org/abs/2511.14721v1) (score=1, bucket=domain_adaptation, 2025-11-18)
- [\textit{FLARE}: Adaptive Multi-Dimensional Reputation for Robust Client Reliability in Federated Learning](https://arxiv.org/abs/2511.14715v1) (score=1, bucket=domain_adaptation, 2025-11-18)
- [Strategic Innovation Management in the Age of Large Language Models Market Intelligence, Adaptive R&D, and Ethical Governance](https://arxiv.org/abs/2511.14709v1) (score=1, bucket=domain_adaptation, 2025-11-18)
- [Adapformer: Adaptive Channel Management for Multivariate Time Series Forecasting](https://arxiv.org/abs/2511.14632v1) (score=1, bucket=domain_adaptation, 2025-11-18)
- [ForensicFlow: A Tri-Modal Adaptive Network for Robust Deepfake Detection](https://arxiv.org/abs/2511.14554v1) (score=1, bucket=domain_adaptation, 2025-11-18)
- [nnterp: A Standardized Interface for Mechanistic Interpretability of Transformers](https://arxiv.org/abs/2511.14465v1) (score=1, bucket=domain_adaptation, 2025-11-18)

## Ner Extraction

### [Ground Truth Generation for Multilingual Historical NLP using LLMs](https://arxiv.org/abs/2511.14688v1)
- id: `http://arxiv.org/abs/2511.14688v1`
- published: 2025-11-18
- authors: Clovis Gladstone, Zhao Fang, Spencer Dean Stewart
- categories: cs.CL, cs.AI
- query: `all:"named entity recognition"`
- blume_score: 4

Historical and low-resource NLP remains challenging due to limited annotated data and domain
mismatches with modern, web-sourced corpora. This paper outlines our work in using large language
models (LLMs) to create ground-truth annotations for historical French (16th-20th centuries) and
Chinese (1900-1950) texts. By leveraging LLM-generated ground truth on a subset of our corpus, we
were able to fine-tune spaCy to achieve significant gains on period-specific tests for part-of-
speech (POS) ann...


## Domain Adaptation

### [AdamHD: Decoupled Huber Decay Regularization for Language Model Pre-Training](https://arxiv.org/abs/2511.14721v1)
- id: `http://arxiv.org/abs/2511.14721v1`
- published: 2025-11-18
- authors: Fu-Ming Guo, Yingfang Fan
- categories: cs.LG, math.OC
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Adaptive optimizers with decoupled weight decay, such as AdamW, are the de facto standard for pre-
training large transformer-based generative models. Yet the quadratic nature of the $\ell_2$ penalty
embedded in weight decay drives all parameters toward the origin at the same rate, making the update
vulnerable to rare but extreme gradient directions and often over-penalizing well-conditioned
coordinates. We propose AdamHuberDecay, a drop-in replacement for AdamW that substitutes the
$\ell_2$ p...

### [\textit{FLARE}: Adaptive Multi-Dimensional Reputation for Robust Client Reliability in Federated Learning](https://arxiv.org/abs/2511.14715v1)
- id: `http://arxiv.org/abs/2511.14715v1`
- published: 2025-11-18
- authors: Abolfazl Younesi, Leon Kiss, Zahra Najafabadi Samani, Juan Aznar Poveda, Thomas Fahringer
- categories: cs.LG, cs.AI, cs.CR, cs.DC, cs.MA
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Federated learning (FL) enables collaborative model training while preserving data privacy. However,
it remains vulnerable to malicious clients who compromise model integrity through Byzantine attacks,
data poisoning, or adaptive adversarial behaviors. Existing defense mechanisms rely on static
thresholds and binary classification, failing to adapt to evolving client behaviors in real-world
deployments. We propose FLARE, an adaptive reputation-based framework that transforms client
reliabilit...

### [Strategic Innovation Management in the Age of Large Language Models Market Intelligence, Adaptive R&D, and Ethical Governance](https://arxiv.org/abs/2511.14709v1)
- id: `http://arxiv.org/abs/2511.14709v1`
- published: 2025-11-18
- authors: Raha Aghaei, Ali A. Kiaei, Mahnaz Boush, Mahan Rofoosheh, Mohammad Zavvar
- categories: cs.CL
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

This study analyzes the multiple functions of Large Language Models (LLMs) in transforming research
and development (R&D) processes. By automating knowledge discovery, boosting hypothesis creation,
integrating transdisciplinary insights, and enabling cooperation within innovation ecosystems, LLMs
dramatically improve the efficiency and effectiveness of research processes. Through extensive
analysis of scientific literature, patent databases, and experimental data, these models enable more
fle...

### [Adapformer: Adaptive Channel Management for Multivariate Time Series Forecasting](https://arxiv.org/abs/2511.14632v1)
- id: `http://arxiv.org/abs/2511.14632v1`
- published: 2025-11-18
- authors: Yuchen Luo, Xinyu Li, Liuhua Peng, Mingming Gong
- categories: cs.LG, cs.AI
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

In multivariate time series forecasting (MTSF), accurately modeling the intricate dependencies among
multiple variables remains a significant challenge due to the inherent limitations of traditional
approaches. Most existing models adopt either \textbf{channel-independent} (CI) or \textbf{channel-
dependent} (CD) strategies, each presenting distinct drawbacks. CI methods fail to leverage the
potential insights from inter-channel interactions, resulting in models that may not fully exploit
the ...

### [ForensicFlow: A Tri-Modal Adaptive Network for Robust Deepfake Detection](https://arxiv.org/abs/2511.14554v1)
- id: `http://arxiv.org/abs/2511.14554v1`
- published: 2025-11-18
- authors: Mohammad Romani
- categories: cs.CV, cs.CR, cs.LG
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Deepfakes generated by advanced GANs and autoencoders severely threaten information integrity and
societal stability. Single-stream CNNs fail to capture multi-scale forgery artifacts across spatial,
texture, and frequency domains, limiting robustness and generalization. We introduce the
ForensicFlow, a tri-modal forensic framework that synergistically fuses RGB, texture, and frequency
evidence for video Deepfake detection. The RGB branch (ConvNeXt-tiny) extracts global visual
inconsistencies;...

### [nnterp: A Standardized Interface for Mechanistic Interpretability of Transformers](https://arxiv.org/abs/2511.14465v1)
- id: `http://arxiv.org/abs/2511.14465v1`
- published: 2025-11-18
- authors: Clément Dumas
- categories: cs.LG, cs.AI
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Mechanistic interpretability research requires reliable tools for analyzing transformer internals
across diverse architectures. Current approaches face a fundamental tradeoff: custom implementations
like TransformerLens ensure consistent interfaces but require coding a manual adaptation for each
architecture, introducing numerical mismatch with the original models, while direct HuggingFace
access through NNsight preserves exact behavior but lacks standardization across models. To bridge
this ...

