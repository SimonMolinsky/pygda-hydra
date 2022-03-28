import numpy as np
from predictions.utils.future import set_future_series


def random_forecast(series, steps_ahead=3, freq='D', series_name='random'):
    """
    Function fits data into the random values within the interval given by a one standard deviation of a data.

    INPUT:

    :param series: pandas Series of data,
    :param steps_ahead: number of steps into the future to predict, default is 3,
    :param freq: (str) representation of a time frequency.

    OUTPUT:

    :return: series with extrapolated values

    """

    _std = series.std()
    _mean = series.mean()
    _bottom = _mean - _std
    _top = _mean + _std
    preds = np.random.uniform(low=_bottom, high=_top, size=steps_ahead)
    future = set_future_series(forecasted_values=preds,
                               series_name=series_name,
                               last_date=series.index[-1],
                               steps_ahead=steps_ahead,
                               frequency=freq)
    return future
