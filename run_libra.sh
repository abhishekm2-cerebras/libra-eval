#!/bin/bash

export LIBRA_API_KEY=sk-wuR4GgqlYDvG3NUB5gA7wiZO2E4W6S9DLlkkA5CC3wJXZtqyUv
export CUDA_VISIBLE_DEVICES=0,1
# Run a single evaluation task (need openai_api_key)
python -m libra_eval.run_eval \
    --client local \
    --models 8b_new_ift_exp2_2epoch \
    --tasks all \
    --mode evaluation \
    --output_dir /mnt/local/shared/abhishekm/libra-eval/outputs/results/8b-new-ift-exp2-2epoch