# InfraCompass for AI Builders

> A Chinese, notebook-based AI infrastructure tutorial for AI product builders and application engineers moving from Agent/RAG demos toward production-grade LLM systems.

![InfraCompass cover](assets/images/ai_infra_stack_cover.png)

![Language](https://img.shields.io/badge/language-Chinese-blue)
![Format](https://img.shields.io/badge/format-Jupyter%20Notebook-orange)
![Focus](https://img.shields.io/badge/focus-AI%20Infra%20%7C%20LLM%20Serving%20%7C%20RAG-green)

## Why This Project Exists

Many AI builders can assemble an Agent or RAG prototype, yet still feel uncertain when the conversation moves to GPU memory, KV cache, serving engines, model gateways, observability, Kubernetes, cost control, and production failure modes.

InfraCompass is designed as a guided learning path for that gap. It explains the foundations first, then connects them to real infrastructure decisions: latency, throughput, context length, GPU sizing, vLLM, serving framework selection, model routing, tracing, evaluation, and RAG/Agent hardening.

The goal is practical fluency: enough depth to reason about AI Infra tradeoffs, communicate with platform teams, and make better product and engineering decisions.

## What You Will Learn

- How tokens, tensors, embeddings, attention, logits, and sampling work during inference.
- Why prefill, decode, KV cache, batching, and prefix caching dominate LLM serving behavior.
- How GPU memory is consumed by model weights, KV cache, activations, and runtime workspace.
- How vLLM works at a system level: PagedAttention, scheduler, OpenAI-compatible serving, metrics, and tuning.
- How to compare vLLM, SGLang, TensorRT-LLM, TGI, Ray Serve LLM, MLX, and llama.cpp.
- How to estimate capacity with QPS, concurrency, token length distribution, latency SLOs, and GPU replicas.
- How model gateways handle routing, fallback, virtual keys, budgets, logs, metrics, and traces.
- How to upgrade RAG/Agent demos with data versioning, permissions, reranking, tool safety, state, evaluation, and observability.

## Who This Is For

This project is most useful if you:

- Build AI products, Agent workflows, RAG systems, or model-powered applications.
- Know Python and application development, and want stronger AI Infra fundamentals.
- Need to explain LLM serving and production tradeoffs in interviews or at work.
- Use a Mac for learning, while still wanting to understand cloud GPU and Kubernetes production paths.

## Learning Path

| Chapter | Notebook | Core Outcome |
|---:|---|---|
| 00 | [AI Infra Learning Map](notebooks/00_ai_infra_learning_map.ipynb) | Build the full mental map: model, serving, gateway, data, observability, evaluation, safety, and cost. |
| 01 | [Deep Learning Inference Basics](notebooks/01_deep_learning_inference_basics.ipynb) | Understand tokenization, tensors, embedding, attention, Transformer blocks, logits, and sampling. |
| 02 | [GPU Memory & Compute Basics](notebooks/02_gpu_memory_compute_basics.ipynb) | Learn GPU/CPU roles, dtype, quantization, model weight memory, KV cache, and GPU utilization. |
| 03 | [LLM Inference Mechanics](notebooks/03_llm_inference_mechanics.ipynb) | Understand prefill, decode, continuous batching, chunked prefill, prefix caching, and latency metrics. |
| 04 | [vLLM Serving Engine](notebooks/04_vllm_serving_engine.ipynb) | Study vLLM, vLLM-Metal, PagedAttention, OpenAI-compatible serving, metrics, and tuning. |
| 05 | [Serving Frameworks Beyond vLLM](notebooks/05_serving_frameworks_beyond_vllm.ipynb) | Compare vLLM, SGLang, TensorRT-LLM, TGI, Ray Serve LLM, MLX, and llama.cpp through selection cases. |
| 06 | [Capacity Planning & Kubernetes](notebooks/06_capacity_planning_and_kubernetes.ipynb) | Estimate replicas, GPU needs, token pressure, KServe deployment shape, and autoscaling risks. |
| 07 | [Gateway, Observability & Cost](notebooks/07_gateway_observability_cost.ipynb) | Design model routing, fallback, budgets, OpenTelemetry-style traces, dashboards, and incident workflows. |
| 08 | [RAG/Agent Infra Hardening](notebooks/08_rag_agent_infra_hardening.ipynb) | Turn RAG/Agent prototypes into production systems with versioning, permissions, tools, state, and evals. |

## Visual Guide

The notebooks include Mermaid diagrams and project images to explain infrastructure concepts visually.

| Concept | Preview |
|---|---|
| AI Infra stack | ![AI Infra stack](assets/images/ai_infra_stack_cover.png) |
| GPU memory and compute | ![GPU memory concept](assets/images/gpu_memory_concept.png) |
| LLM inference pipeline | ![LLM inference pipeline](assets/images/llm_inference_pipeline.png) |
| RAG/Agent production hardening | ![RAG Agent hardening](assets/images/rag_agent_hardening.png) |

## Project Structure

```text
.
├── assets/
│   └── images/                  # Concept images used by the notebooks
├── notebooks/                   # Main tutorial chapters
├── scripts/
│   └── validate_notebooks.py    # Notebook, Mermaid, image, formula, and syntax checks
├── requirements_mac.txt         # Lightweight notebook dependencies
└── README.md
```

## Quick Start

```bash
git clone git@github.com:Yanjieij/infra-compass-for-ai-builders.git
cd infra-compass-for-ai-builders

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_mac.txt

jupyter lab
```

Open the notebooks in order from `00` to `08`.

## Notes for Mac Users

Most notebooks run with lightweight Python dependencies and do not require a GPU. The vLLM chapter includes optional vLLM/vLLM-Metal cells.

For Apple Silicon experiments, install vLLM-Metal separately as described in [Chapter 04](notebooks/04_vllm_serving_engine.ipynb). Keep that environment separate from the general notebook environment.

## Validation

Run the project checks:

```bash
python3 scripts/validate_notebooks.py
```

The validation script checks:

- Notebook JSON and `nbformat`
- Python code cell syntax
- Mermaid block structure
- Image references
- Common broken LaTeX/control-character issues
- Math delimiter balance

## Source Materials

The tutorial text summarizes and explains concepts from official or primary documentation, including:

- [vLLM](https://docs.vllm.ai/en/latest/)
- [vLLM-Metal](https://docs.vllm.ai/projects/vllm-metal/en/latest/)
- [Ray Serve LLM](https://docs.ray.io/en/latest/serve/llm/index.html)
- [SGLang](https://docs.sglang.io/)
- [NVIDIA TensorRT-LLM](https://docs.nvidia.com/tensorrt-llm/)
- [Hugging Face Text Generation Inference](https://huggingface.co/docs/text-generation-inference/index)
- [LiteLLM](https://docs.litellm.ai/)
- [KServe](https://kserve.github.io/website/)
- [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/)
- [OpenTelemetry GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)

## Status

This is an evolving learning project. The current version focuses on conceptual clarity, local runnable examples, and production-oriented mental models for AI product and engineering work.

