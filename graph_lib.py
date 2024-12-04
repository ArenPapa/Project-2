from matplotlib import pyplot as plt
import numpy as np
import datetime as dt

# non-linear model
# what is getting here is the model of the
def non_linear(x:list,y:list):
    m, b, c = np.polyfit(x, y, deg = 2)
    y_quad = []
    for i in x:
            y_quad += [m*i**2 + b*i +c]
    return y_quad

# make the graph line smooth
def smooth(windowSize: int, x:list) -> list:
    x_smoothed = []
    for i in range(0, len(x)-windowSize):
        x_section = x[i:i+windowSize]
        x_average = sum(x_section)/windowSize
        x_smoothed += [x_average]

    return x_smoothed


def prediction_model(x: list, y: list):
    m, b, c = np.polyfit(x, y, deg = 2)
    x_pred = []
    y_pred = []

    x_pred = list(np.arange(x[-1] + 1, x[-1] + 1 + 1440))
    y_pred=[m * i ** 2 + b * i + c for i in x_pred]

    timeStep = int(dt.timedelta(minutes = 1))

    x_predTime = [x[-1] + timeStep * i for i in range(1,1441)]

    return x_predTime, y_pred
