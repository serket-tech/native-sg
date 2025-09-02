from __future__ import absolute_import
import cv2

from native_sg.training.datasets.data_augmentation import DataAugmentation
from native_sg.training.datasets.sg_dataset import ListDataset, DirectoryDataSet
from native_sg.training.datasets.classification_datasets import ImageNetDataset, Cifar10, Cifar100
from native_sg.training.datasets.detection_datasets import (
    DetectionDataset,
    COCODetectionDataset,
    PascalVOCDetectionDataset,
    YoloDarknetFormatDetectionDataset,
    PascalVOCFormatDetectionDataset,
)
from native_sg.training.datasets.segmentation_datasets.segmentation_dataset import SegmentationDataSet
from native_sg.training.datasets.segmentation_datasets.pascal_voc_segmentation import (
    PascalVOC2012SegmentationDataSet,
    PascalAUG2012SegmentationDataSet,
    PascalVOCAndAUGUnifiedDataset,
)
from native_sg.training.datasets.segmentation_datasets.cityscape_segmentation import CityscapesDataset, CityscapesConcatDataset
from native_sg.training.datasets.segmentation_datasets.coco_segmentation import CoCoSegmentationDataSet
from native_sg.training.datasets.segmentation_datasets.supervisely_persons_segmentation import SuperviselyPersonsDataset
from native_sg.training.datasets.pose_estimation_datasets import (
    COCOKeypointsDataset,
    BaseKeypointsDataset,
    COCOPoseEstimationDataset,
)


__all__ = [
    "BaseKeypointsDataset",
    "DataAugmentation",
    "ListDataset",
    "DirectoryDataSet",
    "SegmentationDataSet",
    "CityscapesDataset",
    "CityscapesConcatDataset",
    "PascalVOC2012SegmentationDataSet",
    "PascalAUG2012SegmentationDataSet",
    "PascalVOCAndAUGUnifiedDataset",
    "CoCoSegmentationDataSet",
    "DetectionDataset",
    "COCODetectionDataset",
    "YoloDarknetFormatDetectionDataset",
    "PascalVOCDetectionDataset",
    "PascalVOCFormatDetectionDataset",
    "ImageNetDataset",
    "Cifar10",
    "Cifar100",
    "SuperviselyPersonsDataset",
    "COCOKeypointsDataset",
    "COCOPoseEstimationDataset",
]

cv2.setNumThreads(0)
