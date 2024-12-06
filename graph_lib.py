from matplotlib import pyplot as plt
import numpy as np
import matplotlib.dates as mdates
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
    #converting datetime format to numerical format
    x_numeric = [mdates.date2num(time) for time in x]
    # adjusting the length of the list to the y_list
    x_numeric = x_numeric[:len(y)]
    m, b, c = np.polyfit(x_numeric, y, deg = 2)

    timeStep = dt.timedelta(hours = 1)

    x_pred_time = [x[-1] + timeStep * i for i in range(1,25)]
    x_pred_numeric = [mdates.date2num(time) for time in x_pred_time]
    y_pred = [m * i ** 2 + b * i + c for i in x_pred_numeric]

    return x_pred_time, y_pred
