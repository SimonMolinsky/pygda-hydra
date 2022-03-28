import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from statsmodels.api import OLS

from predictions.utils.future import set_future_series


def polynomial_forecast(series, steps_ahead=3, freq='D', series_name='polynomial'):
    """
    Function fits data into OLS.

    INPUT:

    :param series: pandas Series of data,
    :param steps_ahead: number of steps into the future to predict, default is 3,
    :param freq: (str) representation of a time frequency,
    :param series_name: str

    OUTPUT:

    :return: series with extrapolated values
    """
    x = np.arange(0, len(series))
    vals = series.values
    level = 1

    polynomial_features = PolynomialFeatures(degree=level)
    transformed = polynomial_features.fit_transform(x.reshape(-1, 1))
    model = OLS(vals, transformed).fit()

    # Predict
    x_pred = np.arange(len(series), len(series) + steps_ahead)
    transformed = polynomial_features.fit_transform(x_pred.reshape((-1, 1)))
    predicted = model.predict(transformed)

    future = set_future_series(forecasted_values=predicted,
                               series_name=series_name,
                               last_date=series.index[-1],
                               steps_ahead=steps_ahead,
                               frequency=freq)
    return future
