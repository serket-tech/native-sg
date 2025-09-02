import torch
from native_sg.common.object_names import Models
from native_sg.training import models

# Note that currently only YoloX, PPYoloE and YOLO-NAS are supported.
model = models.get(Models.YOLO_NAS_L, pretrained_weights="coco")

# We want to use cuda if available to speed up inference.
model = model.to("cuda" if torch.cuda.is_available() else "cpu")

model.predict_webcam()
