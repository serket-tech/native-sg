# PACKAGE IMPORTS FOR EXTERNAL USAGE
import cv2

from native_sg.training.transforms.transforms import (
    DetectionStandardize,
    DetectionMosaic,
    DetectionRandomAffine,
    DetectionHSV,
    DetectionRGB2BGR,
    DetectionPaddedRescale,
    DetectionTargetsFormatTransform,
    Standardize,
    DetectionTransform,
)
from native_sg.training.transforms.keypoints import (
    AbstractKeypointTransform,
    KeypointTransform,
    KeypointsHSV,
    KeypointsRescale,
    KeypointsCompose,
    KeypointsMosaic,
    KeypointsMixup,
    KeypointsRandomAffineTransform,
    KeypointsRandomRotate90,
    KeypointsRandomVerticalFlip,
    KeypointsRandomHorizontalFlip,
    KeypointsImageToTensor,
    KeypointsImageNormalize,
    KeypointsImageStandardize,
    KeypointsPadIfNeeded,
    KeypointsBrightnessContrast,
    KeypointsLongestMaxSize,
    KeypointsReverseImageChannels,
    KeypointsRemoveSmallObjects,
)
from native_sg.common.object_names import Transforms
from native_sg.common.registry.registry import TRANSFORMS
from native_sg.common.registry.albumentation import ALBUMENTATIONS_TRANSFORMS, ALBUMENTATIONS_COMP_TRANSFORMS, imported_albumentations_failure
from native_sg.training.transforms.detection import AbstractDetectionTransform, DetectionPadIfNeeded, DetectionLongestMaxSize

__all__ = [
    "TRANSFORMS",
    "ALBUMENTATIONS_TRANSFORMS",
    "ALBUMENTATIONS_COMP_TRANSFORMS",
    "imported_albumentations_failure",
    "Transforms",
    "DetectionTransform",
    "AbstractDetectionTransform",
    "DetectionStandardize",
    "DetectionMosaic",
    "DetectionRandomAffine",
    "DetectionHSV",
    "DetectionRGB2BGR",
    "DetectionPaddedRescale",
    "DetectionTargetsFormatTransform",
    "Standardize",
    "AbstractKeypointTransform",
    "KeypointTransform",
    "KeypointsBrightnessContrast",
    "KeypointsCompose",
    "KeypointsHSV",
    "KeypointsImageNormalize",
    "KeypointsImageStandardize",
    "KeypointsLongestMaxSize",
    "KeypointsMixup",
    "KeypointsMosaic",
    "KeypointsPadIfNeeded",
    "KeypointsRandomAffineTransform",
    "KeypointsRandomHorizontalFlip",
    "KeypointsRandomVerticalFlip",
    "KeypointsRescale",
    "KeypointsRandomRotate90",
    "KeypointsImageToTensor",
    "KeypointsRemoveSmallObjects",
    "KeypointsReverseImageChannels",
    "DetectionPadIfNeeded",
    "DetectionLongestMaxSize",
    "AbstractDetectionTransform",
]

cv2.setNumThreads(0)
