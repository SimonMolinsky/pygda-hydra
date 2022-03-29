import os
import hydra
import pandas as pd
from hydra.utils import get_original_cwd, to_absolute_path
from omegaconf import DictConfig

from predictions import forecast
from predictions.utils import get_frame, get_series
from predictions.viz.show import plot_single, plot_with_confidence


@hydra.main(config_path='conf', config_name='config')
def run_prediction(cfg: DictConfig) -> None:
    print(cfg)
    _dloc = cfg.data.loc
    if isinstance(_dloc, str):
        data_path = [to_absolute_path(_dloc)]
    else:
        data_path = [
            to_absolute_path(rel_path) for rel_path in _dloc
        ]

    # Vars: data
    date_col_name = cfg.data.date_col
    value_col_name = cfg.data.value_col
    # Vars: model
    steps = cfg.experiment.steps_ahead
    freq = cfg.experiment.frequency
    model_type = cfg.experiment.model
    # Vars: app
    is_plot = cfg.app.plot

    # Run: get data
    for dpath in data_path:
        sample = get_frame(dpath)
        sample_series = get_series(sample,
                                   date_col_name,
                                   value_col_name)

        # Run: forecast
        naive_pred = forecast(sample_series,
                              steps_ahead=steps,
                              freq=freq,
                              model_type=model_type)

        # Run: app
        if is_plot:
            if isinstance(naive_pred, pd.DataFrame):
                plot_with_confidence(naive_pred)
            else:
                plot_single(naive_pred)

if __name__ == '__main__':
    run_prediction()