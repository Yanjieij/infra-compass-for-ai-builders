# InfraCompass for AI Builders

面向 AI 产品/研发的 AI Infra 入门教程项目。

这是一个面向 AI 产品/研发的中文教程项目。假设你已经有 Python、应用开发、Agent/RAG 构建基础，但深度学习、GPU、模型推理、serving 和生产治理基础不扎实。

本项目目标不是列参考资料，而是把必要基础和官方资料消化成可以直接学习的 Notebook。每章都包含概念解释、公式、图示、代码实验、生产场景、常见误区和面试/工作表达。

## 推荐学习顺序

| 顺序 | Notebook | 学习目标 |
|---:|---|---|
| 00 | `notebooks/00_ai_infra_learning_map.ipynb` | 建立 AI Infra 全景，理解 Agent/RAG 经验如何迁移到 Infra 视角 |
| 01 | `notebooks/01_deep_learning_inference_basics.ipynb` | 补齐 token、tensor、embedding、attention、logits/sampling 基础 |
| 02 | `notebooks/02_gpu_memory_compute_basics.ipynb` | 理解 GPU、显存、dtype、量化、KV cache 和资源瓶颈 |
| 03 | `notebooks/03_llm_inference_mechanics.ipynb` | 理解 prefill、decode、continuous batching、prefix caching 和指标 |
| 04 | `notebooks/04_vllm_serving_engine.ipynb` | 系统学习 vLLM、vLLM-Metal、PagedAttention、serving、metrics 和 tuning |
| 05 | `notebooks/05_serving_frameworks_beyond_vllm.ipynb` | 学会比较 vLLM、SGLang、TensorRT-LLM、TGI、Ray Serve LLM、MLX/llama.cpp |
| 06 | `notebooks/06_capacity_planning_and_kubernetes.ipynb` | 学容量规划、Docker/K8s/GPU Operator/KServe 基础 |
| 07 | `notebooks/07_gateway_observability_cost.ipynb` | 学模型网关、routing、fallback、budget、OpenTelemetry GenAI 和事故排查 |
| 08 | `notebooks/08_rag_agent_infra_hardening.ipynb` | 把 RAG/Agent demo 升级为生产化系统能力 |

## 运行方式

```bash
cd /Users/yanjieij/CodeX/Infra
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_mac.txt
jupyter lab
```

第 4 章中的 vLLM/vLLM-Metal 服务调用单元需要你先在终端启动本地 server。其他基础实验默认不依赖 GPU、不调用付费 API。

## 项目结构

- `notebooks/`：教程 Notebook。
- `assets/images/`：生成的概念图。
- `scripts/validate_notebooks.py`：Notebook、公式、Mermaid、图片和代码校验脚本。
- `requirements_mac.txt`：运行 Notebook 的轻量依赖。vLLM-Metal 建议按第 4 章说明单独安装到 `~/.venv-vllm-metal`。

## 官方资料来源

正文已经吸收关键内容；下面链接用于核对最新细节：

- vLLM: <https://docs.vllm.ai/en/latest/>
- vLLM-Metal: <https://docs.vllm.ai/projects/vllm-metal/en/latest/>
- Ray Serve LLM: <https://docs.ray.io/en/latest/serve/llm/index.html>
- SGLang: <https://docs.sglang.io/>
- NVIDIA TensorRT-LLM: <https://docs.nvidia.com/tensorrt-llm/>
- Hugging Face TGI: <https://huggingface.co/docs/text-generation-inference/index>
- LiteLLM: <https://docs.litellm.ai/>
- KServe: <https://kserve.github.io/website/>
- NVIDIA GPU Operator: <https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/>
- OpenTelemetry GenAI: <https://opentelemetry.io/docs/specs/semconv/gen-ai/>
