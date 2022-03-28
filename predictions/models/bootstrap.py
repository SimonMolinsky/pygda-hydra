import pandas as pd


def bootstrap_forecasts(forecasts: list):
    """

    :param forecasts: list with forecasted series
    :return:
    """
    df = pd.concat(forecasts, axis=1)
    stds = df.std(axis=1)
    df['mean'] = df.mean(axis=1)
    df['lower_ci'] = df['mean'] - stds
    df['upper_ci'] = df['mean'] + stds

    df = df[['mean', 'lower_ci', 'upper_ci']]
    df.columns = ['_y_', 'lower_ci', 'upper_ci']
    return df
