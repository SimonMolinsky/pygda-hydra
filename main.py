import os

import hydra
from hydra.utils import get_original_cwd, to_absolute_path
from omegaconf import DictConfig
from predictions import forecast
from predictions.utils import get_frame, get_series
from predictions.viz.show import plot_single


@hydra.main(config_path='conf', config_name='config')
def run_prediction(cfg: DictConfig) -> None:
    print('Experiment data directory:', cfg.experiment.data_loc)
    print('Current working directory:', os.getcwd())
    print('Original working directory:', get_original_cwd())
    print('Absolute path to the data file:', to_absolute_path(cfg.experiment.data_loc))
    sample = get_frame(cfg.experiment.data_loc)
    sample_series = get_series(sample, cfg.experiment.date_col, cfg.experiment.value_col)
    pred = forecast(sample_series,
                    cfg.experiment.steps_ahead,
                    cfg.experiment.frequency,
                    cfg.experiment.model)
    if cfg.experiment.plot:
        plot_single(pred)


if __name__ == '__main__':
    run_prediction()