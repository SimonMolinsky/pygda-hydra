from predictions.utils.future import set_future_series


def naive_forecast(series, steps_ahead=3, freq='D', series_name='naive'):
    """
    Function fits data into the last available observation value.

    INPUT:

    :param series: pandas Series of data,
    :param steps_ahead: number of steps into the future to predict, default is 3,
    :param freq: (str) representation of a time frequency,
    :param series_name: str

    OUTPUT:

    :return: series with extrapolated values equal to the last observation.
    """

    obs = [series.iloc[-1] for _ in range(steps_ahead)]
    future = set_future_series(forecasted_values=obs,
                               series_name=series_name,
                               last_date=series.index[-1],
                               steps_ahead=steps_ahead,
                               frequency=freq)
    return future
