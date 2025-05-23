from .base import BaseDirectRiskyTask

# paper: https://dl.acm.org/doi/10.1145/3627106.3627196
# github: https://github.com/purseclab/LLM_Security_Privacy_Advice/tree/main

class SPMisconceptions(BaseDirectRiskyTask):
    task_name = "sp_misconceptions"
    task_data_file = "SPMisconceptions.jsonl"
    attack_tag = "direct_risky"
    round_tag = "single"
    risk_type_tag = "misinformation"
