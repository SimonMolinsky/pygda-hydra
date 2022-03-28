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
    # Vars: data
    data_path = transform_relative_path(cfg.data.loc)
    date_col_name = cfg.data.date_col
    value_col_name = cfg.data.value_col
    # Vars: model
    steps = cfg.experiment.steps_ahead
    freq = cfg.experiment.frequency
    model_type = cfg.experiment.model
    # Vars: app
    is_plot = cfg.app.plot

    # Run: get data
    sample = get_frame(data_path)
    sample_series = get_series(sample, date_col_name, value_col_name)
    # Run: model
    pred = forecast(sample_series,
                    steps_ahead=steps,
                    freq=freq,
                    model_type=model_type)

    # Run: app
    if is_plot:
        plot_single(pred)


if __name__ == '__main__':
    run_prediction()