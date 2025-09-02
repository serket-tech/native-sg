from native_sg.common.factories.type_factory import TypeFactory
from native_sg.training.datasets.data_formats.default_formats import DEFAULT_CONCATENATED_TENSOR_FORMATS


class ConcatenatedTensorFormatFactory(TypeFactory):
    def __init__(self):
        super().__init__(DEFAULT_CONCATENATED_TENSOR_FORMATS)
