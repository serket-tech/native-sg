from native_sg.training.losses.focal_loss import FocalLoss
from native_sg.training.losses.kd_losses import KDLogitsLoss
from native_sg.training.losses.label_smoothing_cross_entropy_loss import CrossEntropyLoss
from native_sg.training.losses.r_squared_loss import RSquaredLoss
from native_sg.training.losses.shelfnet_ohem_loss import ShelfNetOHEMLoss
from native_sg.training.losses.shelfnet_semantic_encoding_loss import ShelfNetSemanticEncodingLoss
from native_sg.training.losses.yolox_loss import YoloXDetectionLoss, YoloXFastDetectionLoss
from native_sg.training.losses.ssd_loss import SSDLoss
from native_sg.training.losses.bce_dice_loss import BCEDiceLoss
from native_sg.training.losses.dice_ce_edge_loss import DiceCEEdgeLoss
from native_sg.training.losses.ppyolo_loss import PPYoloELoss
from native_sg.training.losses.dekr_loss import DEKRLoss
from native_sg.training.losses.stdc_loss import STDCLoss
from native_sg.training.losses.rescoring_loss import RescoringLoss
from native_sg.training.losses.yolo_nas_pose_loss import YoloNASPoseLoss
from native_sg.common.object_names import Losses
from native_sg.common.registry.registry import LOSSES

__all__ = [
    "LOSSES",
    "Losses",
    "FocalLoss",
    "CrossEntropyLoss",
    "ShelfNetOHEMLoss",
    "ShelfNetSemanticEncodingLoss",
    "YoloXDetectionLoss",
    "YoloXFastDetectionLoss",
    "RSquaredLoss",
    "SSDLoss",
    "BCEDiceLoss",
    "KDLogitsLoss",
    "DiceCEEdgeLoss",
    "PPYoloELoss",
    "DEKRLoss",
    "STDCLoss",
    "RescoringLoss",
    "YoloNASPoseLoss",
]
