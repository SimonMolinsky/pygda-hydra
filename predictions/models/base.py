from typing import Union

import pandas as pd

from predictions.models.naive import naive_forecast
from predictions.models.polynomial import polynomial_forecast
from predictions.models.trandom import random_forecast
from predictions.models.bootstrap import bootstrap_forecasts


def forecast(data: pd.Series, steps_ahead: int, freq: str, model_type: str) -> Union[pd.DataFrame, pd.Series]:
    """Perform predictions with a given model type.

    Parameters
    ----------
    data : numpy array
           One-dimensional array of float values.

    steps_ahead : int

    freq : str
           'D' for days, 'W' for weeks, 'Y' for annual.

    model_type : str
                 Forecasting method. Available types:
                     - 'bootstrap': for weighted mean of all models (bootstrapped model),
                     - 'naive': for naive model,
                     - 'random': for random model,
                     - 'trend': for polynomial model.

    Raises
    ------
    

    :param data: series with observed values and time index
    :param model_type: selected model
    :return: DataFrame or Series with predictions
    """
    model_types = ['bootstrap', 'naive', 'random', 'trend']

    if model_type == 'bootstrap':
        naive = naive_forecast(data, steps_ahead, freq)
        poly = polynomial_forecast(data, steps_ahead, freq)
        rando = random_forecast(data, steps_ahead, freq)
        bootstrapped = bootstrap_forecasts([naive, poly, rando])
        return bootstrapped
    elif model_type == 'naive':
        naive = naive_forecast(data, steps_ahead, freq)
        return naive
    elif model_type == 'random':
        rnd = random_forecast(data, steps_ahead, freq)
        return rnd
    elif model_type == 'trend':
        poly = polynomial_forecast(data, steps_ahead, freq)
        return poly
    else:
        AttributeError(f'Chosen model type not in the available model types. Available model types are: {model_types}')
