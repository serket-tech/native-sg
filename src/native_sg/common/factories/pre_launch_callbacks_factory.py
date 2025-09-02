from native_sg.common.factories.base_factory import BaseFactory
from native_sg.common.registry.registry import ALL_PRE_LAUNCH_CALLBACKS


class PreLaunchCallbacksFactory(BaseFactory):
    def __init__(self):
        super().__init__(ALL_PRE_LAUNCH_CALLBACKS)
