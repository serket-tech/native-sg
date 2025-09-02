"""
This module is in charge of environment variables and consts.
"""
from native_sg.common.environment.ddp_utils import init_trainer, is_distributed

__all__ = ["init_trainer", "is_distributed"]
