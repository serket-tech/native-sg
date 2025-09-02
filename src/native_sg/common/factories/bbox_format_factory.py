from native_sg.common.factories.base_factory import BaseFactory
from native_sg.training.datasets.data_formats.bbox_formats import BBOX_FORMATS


class BBoxFormatFactory(BaseFactory):
    def __init__(self):
        super().__init__(BBOX_FORMATS)
