from native_sg.common.registry.registry import register_callback
from native_sg.common.object_names import Callbacks
from native_sg.training.utils.callbacks import TrainingStageSwitchCallbackBase, PhaseContext


@register_callback(Callbacks.PPYOLOE_TRAINING_STAGE_SWITCH)
class PPYoloETrainingStageSwitchCallback(TrainingStageSwitchCallbackBase):
    """
    PPYoloETrainingStageSwitchCallback

    Training stage switch for PPYolo training.
    It changes static bbox assigner to a task aligned assigned after certain number of epochs passed

    """

    def __init__(
        self,
        static_assigner_end_epoch: int = 30,
    ):
        super().__init__(next_stage_start_epoch=static_assigner_end_epoch)

    def apply_stage_change(self, context: PhaseContext):
        from native_sg.training.losses import PPYoloELoss

        if not isinstance(context.criterion, PPYoloELoss):
            raise RuntimeError(
                f"A criterion must be an instance of PPYoloELoss when using PPYoloETrainingStageSwitchCallback. " f"Got criterion {repr(context.criterion)}"
            )
        context.criterion.use_static_assigner = False
