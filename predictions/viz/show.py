import matplotlib.pyplot as plt


def plot_single(series):
    plt.figure(figsize=(10, 16))
    plt.plot(series)
    plt.title(series.name)
    plt.show()


def plot_with_confidence(frame):
    plt.figure(figsize=(10, 16))
    plt.plot(frame['lower_ci'], '-b')
    plt.plot(frame['_y_'], 'r')
    plt.plot(frame['upper_ci'], '-.b')
    plt.legend(['Lower CI', 'Predicted', 'Upper CI'])
    plt.show()
