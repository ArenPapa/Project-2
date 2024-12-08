import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import requests
import datetime as dt
import matplotlib.dates as mdates
from matplotlib.lines import lineStyles
from matplotlib.pyplot import subplot, plot_date
import matplotlib
from matplotlib.ticker import MaxNLocator
from graph_lib import *

matplotlib.use("MacOSX")
plt.style.use('ggplot')

server_ip= '192.168.4.137'
request = requests.get(f"http://{server_ip}/readings")
data = request.json()

readings = data['readings'][0]

# getting all the data from the server
sensor = {
    10: {"name": "temp", "values": [], "timestamps": []},
    455: {"name": "hum", "values": [], "timestamps": []},
    456: {"name": "pressure", "values": [], "timestamps": []},
}

count = 0
for r in readings:
    if r['sensor_id'] in sensor:
        # getting the value and store them into each sensor_ib
        sensor[r["sensor_id"]]["values"].append(r['value'])
        timestamp = dt.datetime.fromisoformat(r['datetime'])
        sensor[r['sensor_id']]['timestamps'].append(timestamp)

sensor[10]['values'] = sensor[10]['values'][0:1440]
sensor[10]['timestamps'] = sensor[10]['timestamps'][0:1440]
sensor[455]['values'] = sensor[455]['values'][0:1440]
sensor[455]['timestamps'] = sensor[455]['timestamps'][0:1440]
sensor[456]['values'] = sensor[456]['values'][0:1440]
sensor[456]['timestamps'] = sensor[456]['timestamps'][0:1440]

print(len(sensor[455]['values']))

#temperature------------------------------------------------------------------------------------------------------------

plt.subplot(3,1,1)

temp = sensor[10]['values'] # 48hours of temperature
y_temp = smooth(50, temp) # moving_average
x_time = sensor[10]['timestamps'][0:len(y_temp)] # datetime
x = list(np.arange(len(y_temp))) # list of number of index

minTemp = np.min(y_temp)
minX = y_temp[0]
for i in range(len(sensor[10]['values'])):
    if sensor[10]['values'][i] == minTemp:
        minX = x[i]

maxTemp = np.max(y_temp)
maxX_bmp = x[0]
for i in range(len(y_temp)):
    if sensor[10]['values'][i] == maxTemp:
        maxX_bmp = x_time[i]

plt.plot(x,y_temp, label = "Temperature BMP", color = 'r')
plt.plot(x, non_linear(x,y_temp), label = "Model", color = 'b')
plt.axhline(float(np.mean(y_temp)), label="Mean", color='g')
plt.axhline(float(np.std(y_temp)), label = "Standard Deviation", color = 'gold')
plt.scatter(minX, minTemp, label = "Minimum", color = 'purple')
plt.scatter(maxX_bmp, maxTemp, label = 'Maximum', color = 'pink')
plt.axhline(float(np.median(y_temp)), label = "Median", color = 'orange')
print("Temperature Graph Succeed")

# x_pred_time, y_pred_value = prediction_model(x_time,y_temp)
# plt.plot(x_pred_time, y_pred_value, label = "Prediction", color = "black")
# print("Graph Succeed")

plt.title("Temperature")
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=6))  # Major ticks every 1 hour
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

plt.legend()
plt.xlabel('Time')
plt.ylabel("Temperature")
plt.xticks(rotation = 45)

#humidity---------------------------------------------------------------------------------------------------------------
plt.subplot(3,1,2)

hum = sensor[455]['values']
y_hum = smooth(50, hum)
x = list(np.arange(len(y_hum))) # list of number of index
x_time = sensor[455]['timestamps'] #datetime format

min_hum = np.min(y_hum)
minX_hum = x_time[0]
for i in range(len(sensor[455]['values'])):
    if sensor[455]['values'][i] == min_hum:
        minX_hum = x[i]

maxHum = np.max(y_hum)
maxX_bmp = x[0]
for i in range(len(y_hum)):
    if sensor[455]['values'][i] == maxHum:
        maxX_bmp = x_time[i]


plt.plot(x,y_hum,label= "Humidity",color='red')
plt.plot(x, non_linear(x,y_hum),label = "Non-linear Model", color = 'blue')
plt.axhline(float(np.mean(y_hum)), label="Mean", color='green')
plt.axhline(float(np.std(y_hum)),label = "Standard Deviation", color = 'gold')
plt.plot(np.max(y_hum), label = "Maximum", color = "pink")
plt.axhline(float(np.median(y_hum)), label = "Median", color = "orange")
print("Humidity Graph Succeed")
#prediction
x_pred_time, y_pred_value = prediction_model(x_time,y_hum)
plt.plot(x_pred_time, y_pred_value, label = "Prediction", color = "black")
print("Prediction Succeed")

plt.title("Humidity DHT")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=6))
plt.legend()
plt.xlabel('Time')
plt.ylabel("Humidity")
plt.xticks(rotation = 45)

#Atmosphere Pressure----------------------------------------------------------------------------------------------------
plt.subplot(3,1,3)
pressure = sensor[456]['values']


hum = sensor[456]['values']
y_atm = smooth(50, pressure)
x = list(np.arange(len(y_atm))) # list of number of index
x_time = sensor[456]['timestamps'] #datetime format

min_atm = np.min(y_hum)
minX_atm = x_time[0]
for i in range(len(sensor[456]['values'])):
    if sensor[456]['values'][i] == minX_atm:
        minX_atm = x[i]

maxAtm = np.max(y_atm)
maxX_bmp = x[0]
for i in range(len(y_atm)):
    if sensor[456]['values'][i] == maxAtm:
        maxX_bmp = x_time[i]


plt.plot(x,y_atm,label= "Temperature DHT",color='red')
plt.plot(x, non_linear(x,y_atm),label = "Non-linear Model", color = 'blue')
plt.axhline(float(np.mean(y_atm)), label="Mean", color='green')
plt.axhline(float(np.std(y_atm)),label = "Standard Deviation", color = 'gold')
plt.plot(np.max(y_atm), label = "Maximum", color = "pink")
plt.axhline(float(np.median(y_atm)), label = "Median", color = "orange")
print("Atmospheric Pressure Graph Succeed")
#prediction
x_pred_time, y_pred_value = prediction_model(x_time,y_atm)
plt.plot(x_pred_time, y_pred_value, label = "Prediction", color = "black")
print("Prediction Succeed")

plt.title("Atmospheric Pressure")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=6))
plt.legend()
plt.xlabel('Time')
plt.xticks(rotation = 45)
plt.ylabel("Atmospheric Pressure (hPa)")
plt.tight_layout()

plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True, prune='both'))
plt.show()
