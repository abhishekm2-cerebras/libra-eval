#!/bin/bash
source /mnt/local/shared/abhishekm/venvs/librai/bin/activate
export CUDA_VISIBLE_DEVICES=0,1

python -m vllm.entrypoints.openai.api_server \
  --model /insert/jais/ckpt/path/here \
  --port 8000 \
  --dtype bfloat16 \
  --served-model-name ptmodel \
  --tensor-parallel-size 2 \
  --gpu-memory-utilization 0.90 \
  --enable-chunked-prefill \
  # --pipeline-parallel-size 2