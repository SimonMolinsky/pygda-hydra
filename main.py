from predictions import forecast
from predictions.utils import get_frame, get_series


def run_prediction() -> None:
    steps_ahead = 15
    time_freq = 'D'
    sample = get_frame('data/dev/input_temperature.csv')
    sample_series = get_series(sample, 'time', 'temperature')
    naive_pred = forecast(sample_series, steps_ahead, time_freq, 'naive')


if __name__ == '__main__':
    run_prediction()