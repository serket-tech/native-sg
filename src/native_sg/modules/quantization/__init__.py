# Imports for backward compatibility
from native_sg.training.utils.quantization.modules import (
    QuantBottleneck,
    QuantSTDCBlock,
    QuantAttentionRefinementModule,
    QuantFeatureFusionModule,
    QuantContextPath,
    QuantHeadInternalSkipConnection,
    QuantResidual,
    QuantCrossModelSkipConnection,
    QuantBackboneInternalSkipConnection,
    QuantSkipConnection,
)


__all__ = [
    "QuantSTDCBlock",
    "QuantAttentionRefinementModule",
    "QuantFeatureFusionModule",
    "QuantContextPath",
    "QuantBottleneck",
    "QuantSkipConnection",
    "QuantHeadInternalSkipConnection",
    "QuantResidual",
    "QuantCrossModelSkipConnection",
    "QuantBackboneInternalSkipConnection",
]
