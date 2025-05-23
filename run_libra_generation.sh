#!/bin/bash

export LIBRA_API_KEY=ABCDEF
source /mnt/local/shared/abhishekm/venvs/librai/bin/activate
# export CUDA_VISIBLE_DEVICES=0,1
# Run a single evaluation task (need openai_api_key)
python -m libra_eval.run_eval \
    --client local \
    --models ptmodel \
    --tasks all \
    --mode inference \
    --output_dir /mnt/local/shared/abhishekm/libra-eval/outputs/results-v2/8b-new-ift-exp2-2epoch \
    --generation_params '{"temperature": 1, "top_p": 0.5}'