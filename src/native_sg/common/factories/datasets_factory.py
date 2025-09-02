from native_sg.common.factories.base_factory import BaseFactory
from native_sg.common.registry.registry import ALL_DATASETS


class DatasetsFactory(BaseFactory):
    def __init__(self):
        super().__init__(ALL_DATASETS)
