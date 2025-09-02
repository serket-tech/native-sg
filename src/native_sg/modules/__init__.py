from native_sg.modules.anti_alias import AntiAliasDownsample
from native_sg.modules.pixel_shuffle import PixelShuffle
from native_sg.modules.pose_estimation_modules import LightweightDEKRHead
from native_sg.modules.conv_bn_act_block import ConvBNAct, Conv
from native_sg.modules.conv_bn_relu_block import ConvBNReLU
from native_sg.modules.repvgg_block import RepVGGBlock
from native_sg.modules.qarepvgg_block import QARepVGGBlock
from native_sg.modules.se_blocks import SEBlock, EffectiveSEBlock
from native_sg.modules.skip_connections import (
    Residual,
    SkipConnection,
    CrossModelSkipConnection,
    BackboneInternalSkipConnection,
    HeadInternalSkipConnection,
)
from native_sg.common.registry.registry import ALL_DETECTION_MODULES

from native_sg.modules.base_modules import BaseDetectionModule
from native_sg.modules.detection_modules import (
    PANNeck,
    NHeads,
    MultiOutputBackbone,
    NStageBackbone,
    MobileNetV1Backbone,
    MobileNetV2Backbone,
    SSDNeck,
    SSDInvertedResidualNeck,
    SSDBottleneckNeck,
    SSDHead,
)
from native_sg.module_interfaces import SupportsReplaceNumClasses

__all__ = [
    "BaseDetectionModule",
    "ALL_DETECTION_MODULES",
    "PixelShuffle",
    "AntiAliasDownsample",
    "Conv",
    "ConvBNAct",
    "ConvBNReLU",
    "RepVGGBlock",
    "QARepVGGBlock",
    "SEBlock",
    "EffectiveSEBlock",
    "Residual",
    "SkipConnection",
    "CrossModelSkipConnection",
    "BackboneInternalSkipConnection",
    "HeadInternalSkipConnection",
    "LightweightDEKRHead",
    "PANNeck",
    "NHeads",
    "MultiOutputBackbone",
    "NStageBackbone",
    "MobileNetV1Backbone",
    "MobileNetV2Backbone",
    "SSDNeck",
    "SSDInvertedResidualNeck",
    "SSDBottleneckNeck",
    "SSDHead",
    "SupportsReplaceNumClasses",
]
