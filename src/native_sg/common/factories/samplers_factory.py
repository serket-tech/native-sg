from native_sg.common.factories.base_factory import BaseFactory
from native_sg.common.registry.registry import SAMPLERS


class SamplersFactory(BaseFactory):
    def __init__(self):
        super().__init__(SAMPLERS)
