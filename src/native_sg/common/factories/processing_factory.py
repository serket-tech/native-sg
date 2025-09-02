from typing import Union, Mapping

from native_sg.common.factories.base_factory import BaseFactory
from native_sg.common.factories.list_factory import ListFactory
from native_sg.common.registry.registry import PROCESSINGS


class ProcessingFactory(BaseFactory):
    def __init__(self):
        super().__init__(PROCESSINGS)

    def get(self, conf: Union[str, dict]):
        if isinstance(conf, Mapping) and "ComposeProcessing" in conf:
            conf["ComposeProcessing"]["processings"] = ListFactory(ProcessingFactory()).get(conf["ComposeProcessing"]["processings"])
        return super().get(conf)
