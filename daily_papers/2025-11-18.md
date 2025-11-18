# ML paper digest for 2025-11-18

_window: last 1 days; generated at 2025-11-18T10:08:54.691158+00:00_

## Top picks for Blume

- [Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents](https://arxiv.org/abs/2511.13593v1) (score=3, bucket=entity_linking_graph, 2025-11-17)
- [Graph Out-of-Distribution Detection via Test-Time Calibration with Dual Dynamic Dictionaries](https://arxiv.org/abs/2511.13541v1) (score=3, bucket=entity_linking_graph, 2025-11-17)
- [A Quantum Tensor Network-Based Viewpoint for Modeling and Analysis of Time Series Data](https://arxiv.org/abs/2511.13514v1) (score=3, bucket=entity_linking_graph, 2025-11-17)
- [Mem-PAL: Towards Memory-based Personalized Dialogue Assistants for Long-term User-Agent Interaction](https://arxiv.org/abs/2511.13410v1) (score=2, bucket=retrieval_rag, 2025-11-17)
- [Weight-sparse transformers have interpretable circuits](https://arxiv.org/abs/2511.13653v1) (score=1, bucket=domain_adaptation, 2025-11-17)
- [Likelihood-guided Regularization in Attention Based Models](https://arxiv.org/abs/2511.13221v1) (score=1, bucket=domain_adaptation, 2025-11-17)

## Entity Linking Graph

### [Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents](https://arxiv.org/abs/2511.13593v1)
- id: `http://arxiv.org/abs/2511.13593v1`
- published: 2025-11-17
- authors: Piaohong Wang, Motong Tian, Jiaxian Li, Yuan Liang, Yuqing Wang, Qianben Chen, Tiannan Wang, Zhicong Lu, Jiawei Ma, Yuchen Eleanor Jiang, Wangchunshu Zhou
- categories: cs.CL
- query: `all:"relation extraction"`
- blume_score: 3

Recent advancements in LLM-powered agents have demonstrated significant potential in generating
human-like responses; however, they continue to face challenges in maintaining long-term
interactions within complex environments, primarily due to limitations in contextual consistency and
dynamic personalization. Existing memory systems often depend on semantic grouping prior to
retrieval, which can overlook semantically irrelevant yet critical user information and introduce
retrieval noise. In t...

### [Graph Out-of-Distribution Detection via Test-Time Calibration with Dual Dynamic Dictionaries](https://arxiv.org/abs/2511.13541v1)
- id: `http://arxiv.org/abs/2511.13541v1`
- published: 2025-11-17
- authors: Yue Hou, Ruomei Liu, Yingke Su, Junran Wu, Ke Xu
- categories: cs.LG
- query: `all:"knowledge graph" AND all:"construction"`
- blume_score: 3

A key challenge in graph out-of-distribution (OOD) detection lies in the absence of ground-truth OOD
samples during training. Existing methods are typically optimized to capture features within the in-
distribution (ID) data and calculate OOD scores, which often limits pre-trained models from
representing distributional boundaries, leading to unreliable OOD detection. Moreover, the latent
structure of graph data is often governed by multiple underlying factors, which remains less
explored. To ...

### [A Quantum Tensor Network-Based Viewpoint for Modeling and Analysis of Time Series Data](https://arxiv.org/abs/2511.13514v1)
- id: `http://arxiv.org/abs/2511.13514v1`
- published: 2025-11-17
- authors: Pragatheeswaran Vipulananthan, Kamal Premaratne, Dilip Sarkar, Manohar N. Murthi
- categories: cs.LG, cs.IT
- query: `all:"knowledge graph" AND all:"construction"`
- blume_score: 3

Accurate uncertainty quantification is a critical challenge in machine learning. While neural
networks are highly versatile and capable of learning complex patterns, they often lack
interpretability due to their ``black box'' nature. On the other hand, probabilistic ``white box''
models, though interpretable, often suffer from a significant performance gap when compared to
neural networks. To address this, we propose a novel quantum physics-based ``white box'' method that
offers both accurate...


## Domain Adaptation

### [Weight-sparse transformers have interpretable circuits](https://arxiv.org/abs/2511.13653v1)
- id: `http://arxiv.org/abs/2511.13653v1`
- published: 2025-11-17
- authors: Leo Gao, Achyuta Rajaram, Jacob Coxon, Soham V. Govande, Bowen Baker, Dan Mossing
- categories: cs.LG, cs.AI
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

Finding human-understandable circuits in language models is a central goal of the field of
mechanistic interpretability. We train models to have more understandable circuits by constraining
most of their weights to be zeros, so that each neuron only has a few connections. To recover fine-
grained circuits underlying each of several hand-crafted tasks, we prune the models to isolate the
part responsible for the task. These circuits often contain neurons and residual channels that
correspond to ...

### [Likelihood-guided Regularization in Attention Based Models](https://arxiv.org/abs/2511.13221v1)
- id: `http://arxiv.org/abs/2511.13221v1`
- published: 2025-11-17
- authors: Mohamed Salem, Inyoung Kim
- categories: stat.ML, cs.LG
- query: `all:"adapter" AND all:"transformer"`
- blume_score: 1

The transformer architecture has demonstrated strong performance in classification tasks involving
structured and high-dimensional data. However, its success often hinges on large- scale training
data and careful regularization to prevent overfitting. In this paper, we intro- duce a novel
likelihood-guided variational Ising-based regularization framework for Vision Transformers (ViTs),
which simultaneously enhances model generalization and dynamically prunes redundant parameters. The
proposed...


## Retrieval Rag

### [Mem-PAL: Towards Memory-based Personalized Dialogue Assistants for Long-term User-Agent Interaction](https://arxiv.org/abs/2511.13410v1)
- id: `http://arxiv.org/abs/2511.13410v1`
- published: 2025-11-17
- authors: Zhaopei Huang, Qifeng Dai, Guozheng Wu, Xiaopeng Wu, Kehan Chen, Chuan Yu, Xubin Li, Tiezheng Ge, Wenxuan Wang, Qin Jin
- categories: cs.CL
- query: `all:"retrieval augmented generation"`
- blume_score: 2

With the rise of smart personal devices, service-oriented human-agent interactions have become
increasingly prevalent. This trend highlights the need for personalized dialogue assistants that can
understand user-specific traits to accurately interpret requirements and tailor responses to
individual preferences. However, existing approaches often overlook the complexities of long-term
interactions and fail to capture users' subjective characteristics. To address these gaps, we
present PAL-Benc...

