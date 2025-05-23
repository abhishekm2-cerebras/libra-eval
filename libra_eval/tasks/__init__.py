from .Advbench import AdvBench
from .BeaverTails import (
    BeaverTailsBad,
    # BeaverTailsGood # Data not suitable, the original label is for QA pairs rather than for prompt only.
)
from .DoNotAnswer import (
    DoNotAnswer,
    DoNotAnswerFP,
    DoNotAnswerFN
)
from .CoNa import CoNa
from .PromptInjection import PromptInjection
from .DecodingTrust import (
    DecodingTrustStereotype,
    DecodingTrustPrivacy,
    DecodingTrustMachineEthics
)
from .DialogueSafety import DialogueSafety
from .ConfAIde import ConfAIde
from .ControversialInstructions import ControversialInstructions
from .CyberattackAssistance import CyberattackAssistance
from .PhysicalSafetyInstructions import (
    PhysicalSafetyInstructionsSafe,
    PhysicalSafetyInstructionsUnsafe,
)
from .MaliciousInstructions import MaliciousInstructions
from .PersonalInfoLeak import (
    # PersonalInfoLeak_context, # task in completion format, not chat format
    # PersonalInfoLeak_zero_shot, # task in completion format, not chat format
    PersonalInfoLeak_few_shot, # task in completion format, but with fwe-shot, it can be valid
)
from .MoralChoice import MoralChoice
from .PromptExtractionRobustness import PromptExtractionRobustness
from .PromptHijackingRobustness import PromptHijackingRobustness
# from .QHarm import QHarm  # evaluation need double check, many questions are not risky
from .HypothesisStereotypes import HypothesisStereotypes
from .LatentJailbreak import LatentJailbreak
from .MaliciousInstruct import MaliciousInstruct
# from .StrongREJECT import StrongREJECT  # sourced from other datasets
from .SycophancyEval import (
    SycophancyEvalAnswer,
    SycophancyEvalAreYouSure,
    # SycophancyEvalFeedback, # scores are all the same, need debug
    # SycophancyEvalMimicry,
)
from .TDCRedTeaming import TDCRedTeaming
from .HackAPrompt import HackAPrompt  # data need double check
from .HarmBench import HarmBench
from .HarmfulQ import HarmfulQ
from .DoAnythingNow import (
    DoAnythingNowJailbreak,
    DoAnythingNowRegular
)
from .GandalfIgnoreInstructions import GandalfIgnoreInstructions
from .RedEval import (
    RedEvalHarmfulQA,
    RedEvalDangerousQA,
)
from .SafeText import SafeText
from .HExPHI import HExPHI
from .TruthfulQA import (
    TruthfulQA_mc1,
    # TruthfulQA_mc2,  # evaluation need revise
    # TruthfulQA_gen  # similar to mc1 task, while the evaluation seems not always correct and meaningful
)
from .XSTest import XSTest
from .Toxigen import Toxigen
from .Aart import Aart
from .SimpleSafetyTest import SimpleSafetyTest
from .SPMisconceptions import SPMisconceptions
# from .SafetyPrompt import SafetyPrompt  # Chinese
# from .AnthropicHarmlessBase import AnthropicHarmlessBase # The dataset is suitable for DPO training, but not for chat-based evaluation
from .DICES350 import DICES350
from .BBQ import BBQ
from .AnthropicRedTeam import AnthropicRedTeam
from .BAD import BAD
from .LibrAI_Adversarial import (
    # AttackCiphering, # Drop due to the difficulty of evaluation, sometimes model resopnse is ciphered and hard to judge
    AttackDeepInception,
    AttackDoAnythingNow,
    AttackEffectToCause,
    AttackFewShots,
    AttackMultilingual,
    AttackOneSidedStatement,
    AttackPersonaModulation,
    AttackPromptInjection,
    AttackRefusalSuppression,
    AttackTenseChange
)

# General evaluation
# from .MTBench import MTBench # multi-turn not implemented
from .VicunaBench import VicunaBench
from .RuozhiBench import RuozhiBench

try:
    from .InternalIQTest import InternalIQTest
except:
    pass

TASKS = {}
for cls_name, cls_obj in list(locals().items()):
    if isinstance(cls_obj, type) and hasattr(cls_obj, 'task_name'):
        TASKS[cls_obj.task_name] = cls_obj
