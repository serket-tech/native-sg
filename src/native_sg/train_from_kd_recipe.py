"""
Example code for running SuperGradient's recipes.

General use: python -m native_sg.train_from_kd_recipe --config-name="DESIRED_RECIPE".
For recipe's specific instructions and details refer to the recipe's configuration file in the recipes directory.
"""

from omegaconf import DictConfig
import hydra

from native_sg import init_trainer
from native_sg.training.kd_trainer import KDTrainer


@hydra.main(config_path="recipes", version_base="1.2")
def _main(cfg: DictConfig) -> None:
    KDTrainer.train_from_config(cfg)


def main() -> None:
    init_trainer()  # `init_trainer` needs to be called before `@hydra.main`
    _main()


if __name__ == "__main__":
    main()
