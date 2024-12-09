import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

# Load the CSV file
file_path = "sensor_data.csv"  
data = pd.read_csv(file_path)

# Convert Timestamp to datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Extract columns
timestamps = data['Timestamp']
temperature = data['Temperature (°C)']
humidity = data['Humidity (%)']
pressure = data['Pressure (hPa)']

# Convert timestamps to numeric values for regression
time_numeric = (timestamps - timestamps.min()).dt.total_seconds().values.reshape(-1, 1)

# Define a function to predict next 12 hours
def predict_next_12_hours(time_numeric, values, time_step=3600, future_hours=12):
    model = LinearRegression()
    model.fit(time_numeric, values)
    
    future_times = np.arange(time_numeric[-1][0] + time_step, 
                             time_numeric[-1][0] + time_step * (future_hours + 1), 
                             time_step).reshape(-1, 1)
    future_values = model.predict(future_times)
    return future_times, future_values

# Prediction
time_step = 3600  # 1 hour intervals
future_hours = 12

future_time_temp, future_temp = predict_next_12_hours(time_numeric, temperature, time_step, future_hours)
future_time_hum, future_hum = predict_next_12_hours(time_numeric, humidity, time_step, future_hours)
future_time_pres, future_pres = predict_next_12_hours(time_numeric, pressure, time_step, future_hours)

# Create time labels for the future
future_time_labels = [timestamps.max() + timedelta(seconds=i * time_step) for i in range(1, len(future_temp) + 1)]

# Plotting
plt.figure(figsize=(15, 10))

# Temperature
plt.subplot(3, 1, 1)
plt.plot(timestamps, temperature, label="Observed Temperature", color="blue")
plt.plot(future_time_labels, future_temp, label="Predicted Temperature", color="red", linestyle="--")
plt.title("Temperature Prediction (Next 12 Hours)")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.legend()

# Humidity
plt.subplot(3, 1, 2)
plt.plot(timestamps, humidity, label="Observed Humidity", color="blue")
plt.plot(future_time_labels, future_hum, label="Predicted Humidity", color="red", linestyle="--")
plt.title("Humidity Prediction (Next 12 Hours)")
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.legend()

# Pressure
plt.subplot(3, 1, 3)
plt.plot(timestamps, pressure, label="Observed Pressure", color="blue")
plt.plot(future_time_labels, future_pres, label="Predicted Pressure", color="red", linestyle="--")
plt.title("Pressure Prediction (Next 12 Hours)")
plt.xlabel("Time")
plt.ylabel("Pressure (hPa)")
plt.legend()

plt.tight_layout()
plt.show()
