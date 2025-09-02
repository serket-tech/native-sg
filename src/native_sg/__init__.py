__version__ = "3.7.1"

from native_sg.common import init_trainer, is_distributed, object_names
from native_sg.training import losses, utils, datasets_utils, DataAugmentation, Trainer, KDTrainer, QATTrainer
from native_sg.common.registry.registry import ARCHITECTURES
from native_sg.sanity_check import env_sanity_check
from native_sg.training.utils.distributed_training_utils import setup_device
from native_sg.training.pre_launch_callbacks import AutoTrainBatchSizeSelectionCallback, QATRecipeModificationCallback

__all__ = [
    "ARCHITECTURES",
    "losses",
    "utils",
    "datasets_utils",
    "DataAugmentation",
    "Trainer",
    "KDTrainer",
    "QATTrainer",
    "object_names",
    "init_trainer",
    "is_distributed",
    "env_sanity_check",
    "setup_device",
    "QATRecipeModificationCallback",
    "AutoTrainBatchSizeSelectionCallback",
]

env_sanity_check()
