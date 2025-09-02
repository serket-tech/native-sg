from native_sg.training.utils.predict import Prediction, DetectionPrediction
import warnings

warnings.warn(
    "Importing from native_sg.training.models.predictions is deprecated. "
    "Please update your code to import from native_sg.training.utils.predict instead.",
    DeprecationWarning,
)


__all__ = ["Prediction", "DetectionPrediction"]
