from typing import Tuple

import torch.nn.functional
from torch import nn, Tensor

from native_sg.common.object_names import Losses
from native_sg.common.registry import register_loss


@register_loss(name=Losses.RESCORING_LOSS, deprecated_name="rescoring_loss")
class RescoringLoss(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, predictions: Tuple[Tensor, Tensor], targets):
        """

        :param predictions: Tuple of (poses, scores)
        :param targets: Target scores
        :return: KD loss between predicted scores and target scores
        """
        return torch.nn.functional.binary_cross_entropy_with_logits(predictions[1], targets)
