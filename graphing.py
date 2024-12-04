import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import requests
import datetime as dt
import matplotlib.dates as mdates
from matplotlib.pyplot import subplot
import matplotlib

from graph_lib import *

matplotlib.use("MacOSX")
plt.style.use('ggplot')

server_ip= '192.168.4.137'
request = requests.get(f"http://{server_ip}/readings")
data = request.json()

readings = data['readings'][0]


# getting all the data from the server
sensor = {
    185: {"name": "temp_dht", "values": [], "timestamps": []}, #change sensor_id
    186: {"name": "hum_dht", "values": [], "timestamps": []},  #change sensor_id
    187: {"name": "temp_bmp", "values": [], "timestamps": []}, #change sensor_id
    188: {"name": "hum_bmp", "values": [], "timestamps": []},  #change sensor_id
    197: {"name": "pressure_bmp", "values": [], "timestamps": []}, #change sensor_id
}


for r in readings:
    if r['sensor_id'] in sensor:
        sensor[r["sensor_id"]]["values"].append(r["value"])
        sensor[r['sensor_id']]["timestamps"].append(dt.datetime.fromisoformat(r["datetime"]))

# Temperature DHT ------------------------------------------------------------------------------------------------------
plt.subplot(3,2,1)

temp = sensor[185]['values']
y_temp = smooth(50, temp)
x = list(range(len(y_temp)))
x_time = [dt.datetime.fromisoformat(date_str) for date_str in sensor[185]['datetime']]

plt.plot(x,y_temp,label= "Temperature DHT",color='red')
plt.plot(x, non_linear(x,y_temp),label = "Non-linear Model", color = 'blue')
plt.axhline(float(np.mean(y_temp)), label="Mean", color='green')
plt.axhline(float(np.std(y_temp)),label = "Standard Deviation", color = 'gold')
plt.axhline(np.min(y_temp), label = "Minimum", color = 'purple')
plt.axhline(np.max(y_temp), label = "Maximum", color = "pink")
plt.axhline(float(np.median(y_temp)), label = "Median", color = "orange")

#prediction
x_pred_time, y_pred_value = prediction_model(x_time,y_temp)
plt.plot(x_pred_time, y_pred_value, label = "Prediction", color = "black")

plt.title("Temperature DHT")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=20))  # Major ticks every 20 mins
plt.legend()
plt.xlabel('Time')
plt.ylabel("Temperature")

# Temperature BMP-------------------------------------------------------------------------------------------------------
plt.subplot(3,2,2)

tempBMP = sensor[187]['values']
y_temp_bmp = smooth(50, tempBMP)
plt.plot(x,y_temp_bmp, label = "Temperature BMP", color = 'red')
plt.plot(x, non_linear(x,y_temp_bmp), label = "Model", color = 'blue')
plt.axhline(float(np.mean(y_temp_bmp)), label="Mean", color='green')
plt.axhline(float(np.std(y_temp_bmp)), label = "Standard Deviation", color = 'gold')
plt.axhline(np.min(y_temp_bmp), label = "Minimum", color = 'purple')
plt.axhline(np.max(y_temp_bmp), label = 'Maximum', color = 'pink')
plt.axhline(float(np.median(y_temp_bmp)), label = "Median", color = 'orange')

x_pred_time, y_pred_value = prediction_model(x_time,y_temp_bmp)
plt.plot(x_pred_time, y_pred_value, label = "Prediction", color = "black")

plt.title("Temperature BMP")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=20))  # Major ticks every 20 mins
plt.legend()
plt.xlabel('Time')
plt.ylabel("Temperature")

# Humidity DHT----------------------------------------------------------------------------------------------------------
plt.subplot(3,2,3)

humDHT = sensor[186]['values']
y_hum_dht = smooth(50, humDHT)
plt.plot(x, y_hum_dht, label = "Humidity DHT", color = 'red')
plt.plot(x, non_linear(x,y_hum_dht), label = 'Model', color = 'blue')
plt.axhline(float(np.mean(y_hum_dht)), label="Mean", color='green')
plt.axhline(float(np.std(y_hum_dht)), label = "Standard Deviation", color = 'gold')
plt.axhline(np.min(y_hum_dht), label = "Minimum", color = 'purple')
plt.axhline(np.max(y_hum_dht), label = 'Maximum', color = 'pink')
plt.axhline(float(np.median(y_hum_dht)), label = "Median", color = 'orange')

x_pred_time, y_pred_value = prediction_model(x_time,y_hum_dht)
plt.plot(x_pred_time, y_pred_value, label = "Prediction", color = "black")

plt.title("Humidity DHT")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=20))  # Major ticks every 20 mins
plt.legend()
plt.xlabel('Time')
plt.ylabel("Humidity")

# Humidity BMP----------------------------------------------------------------------------------------------------------
plt.subplot(3,2,4)

humBMP = sensor[188]['values']
y_hum_bmp = smooth(50, humBMP)
plt.plot(x, y_hum_bmp, label = "Humidity BMP", color = 'red')
plt.plot(x, non_linear(x,y_hum_bmp), label = "Model", color = 'blue')
plt.axhline(float(np.mean(y_hum_bmp)), label="Mean", color='green')
plt.axhline(float(np.std(y_hum_bmp)), label = "Standard Deviation", color = 'gold')
plt.axhline(np.min(y_hum_bmp), label = "Minimum", color = 'purple')
plt.axhline(np.max(y_hum_bmp), label = 'Maximum', color = 'pink')
plt.axhline(float(np.median(y_hum_bmp)), label = "Median", color = 'orange')

x_pred_time, y_pred_value = prediction_model(x_time,y_hum_bmp)
plt.plot(x_pred_time, y_pred_value, label = "Prediction", color = "black")

plt.title("Humidity DHT")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=20))  # Major ticks every 20 mins
plt.legend()
plt.xlabel('Time')
plt.ylabel("Humidity ()")

# pressure BMP----------------------------------------------------------------------------------------------------------
plt.subplot(3,2,5)
pressure = sensor[197]['values']
y_atm = smooth(50, pressure)
plt.plot(x, y_atm, label = "Humidity BMP", color = 'red')
plt.plot(x, non_linear(x,y_atm), label = "Model", color = 'blue')
plt.axhline(float(np.mean(y_atm)), label="Mean", color='green')
plt.axhline(float(np.std(y_atm)), label = "Standard Deviation", color = 'gold')
plt.axhline(np.min(y_atm), label = "Minimum", color = 'purple')
plt.axhline(np.max(y_atm), label = 'Maximum', color = 'pink')
plt.axhline(float(np.median(y_atm)), label = "Median", color = 'orange')

x_pred_time, y_pred_value = prediction_model(x_time,y_atm)
plt.plot(x_pred_time, y_pred_value, label = "Prediction", color = "black")

plt.title("Atmospheric Pressure")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=20))  # Major ticks every 20 mins
plt.legend()
plt.xlabel('Time')
plt.ylabel("Atmospheric Pressure (hPa)")

plt.show()
