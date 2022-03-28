import hydra
from hydra.utils import to_absolute_path
from omegaconf import DictConfig
from predictions import forecast
from predictions.utils import get_frame, get_series
from predictions.viz.show import plot_single


def transform_relative_path(relative_path: str):
    """
    Function gets absolute path to the static files used in a predictions.

    :param relative_path: (str) path to the static files from the main script directory.
    :return: (str)
    """
    abs_path = to_absolute_path(relative_path)
    return abs_path


@hydra.main(config_path='conf', config_name='config')
def run_prediction(cfg: DictConfig) -> None:
    data_path = transform_relative_path(cfg.experiment.data_loc)
    sample = get_frame(data_path)
    sample_series = get_series(sample, cfg.experiment.date_col, cfg.experiment.value_col)
    pred = forecast(sample_series,
                    cfg.experiment.steps_ahead,
                    cfg.experiment.frequency,
                    cfg.experiment.model)
    if cfg.experiment.plot:
        plot_single(pred)


if __name__ == '__main__':
    run_prediction()