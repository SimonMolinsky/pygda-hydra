import pandas as pd


def get_series(data, time_column: str, value_column: str, sort_index=True):
    """Function transforms given data into series for further processing.

    :param data: pd.DataFrame
    :param time_column: str
    :param value_column: str
    :param sort_index: bool
    :return: pd.Series
    """
    series = data[[time_column, value_column]].copy()

    series[time_column] = pd.to_datetime(series[time_column])
    series.set_index(time_column, inplace=True)
    if sort_index:
        series.sort_index(inplace=True)

    return series[value_column]