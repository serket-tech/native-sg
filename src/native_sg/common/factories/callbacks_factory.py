from native_sg.common.factories.base_factory import BaseFactory
from native_sg.common.registry.registry import CALLBACKS


class CallbacksFactory(BaseFactory):
    def __init__(self):
        super().__init__(CALLBACKS)
