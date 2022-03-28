import pandas as pd


def set_future_series(forecasted_values, series_name, last_date, steps_ahead, frequency):
    """
    Function sets future predictions.

    :param forecasted_values: array of predictions,
    :param series_name: name of the forecasted series,
    :param last_date: the last observation time,
    :param steps_ahead: how many steps ahead of predictions,
    :param frequency: frequency of time steps.

    :return: Series with predicted values and time index.
    """
    new_index = pd.date_range(start=last_date,
                              periods=steps_ahead + 1,
                              freq=frequency)
    new_index = new_index[1:]

    y_pred = pd.Series(forecasted_values, index=new_index)

    y_pred.name = series_name
    y_pred.index.freq = frequency

    return y_pred
