import unittest
from pathlib import Path

from native_sg.training import models
from native_sg.training.dataloaders import coco2017_val_yolo_nas
from native_sg.training import Trainer
from native_sg.training.models.detection_models.sliding_window_detection_forward_wrapper import SlidingWindowInferenceDetectionWrapper
from native_sg.training.metrics import DetectionMetrics


class SlidingWindowWrapperTest(unittest.TestCase):
    def setUp(self):
        self.mini_coco_data_dir = str(Path(__file__).parent.parent / "data" / "tinycoco")

    def test_yolo_nas_s_coco_with_sliding_window(self):
        trainer = Trainer("test_yolo_nas_s_coco_with_sliding_window")
        model = models.get("yolo_nas_s", num_classes=80, pretrained_weights="coco")
        model = SlidingWindowInferenceDetectionWrapper(tile_size=320, tile_step=160, model=model, tile_nms_iou=0.65, tile_nms_conf=0.03)
        dl = coco2017_val_yolo_nas(dataset_params=dict(data_dir=self.mini_coco_data_dir))
        metric = DetectionMetrics(
            normalize_targets=True,
            post_prediction_callback=None,
            num_cls=80,
        )
        metric_values = trainer.test(model=model, test_loader=dl, test_metrics_list=[metric])
        self.assertAlmostEqual(metric_values[metric.map_str], 0.342, delta=0.001)


if __name__ == "__main__":
    unittest.main()
