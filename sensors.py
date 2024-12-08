''py

      import time
      import board
      import adafruit_dht
      import adafruit_bmp280
      import csv
      import os
      import sys
      import paramiko  # for SCP transfer
      
      # Initialize sensors
      dht_device = adafruit_dht.DHT11(board.D4)  # DHT11 on GPIO4 (OUT)
      i2c = board.I2C()  # Use the default I2C bus (GPIO2 - SDA, GPIO3 - SCL)
      bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)  # BMP280 on I2C (SDA, SCL)
      
      # File to store the data
      csv_file = "sensor_data.csv"
      log_file = "error_log.txt"
      
      # Number of consecutive errors allowed before restarting
      MAX_CONSECUTIVE_ERRORS = 5
      consecutive_dht_errors = 0
      consecutive_bmp_errors = 0
      
      # Function to log errors
      def log_error(message):
          with open(log_file, mode="a") as log:
              log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
              print(f"ERROR: {message}")
      
      # Function to restart the program
      def restart_program():
          log_error("Restarting program due to sensor issues.")
          os.execv(sys.executable, ['python'] + sys.argv)
      
      # Function to read DHT11 sensor data
      def read_dht():
          try:
              temperature = dht_device.temperature
              humidity = dht_device.humidity
              return temperature, humidity
          except RuntimeError as error:
              log_error(f"DHT11 error: {error}")
              return None, None
      
      # Function to read BMP280 sensor data
      def read_bmp():
          try:
              temperature = bmp280.temperature
              pressure = bmp280.pressure
              humidity = getattr(bmp280, "humidity", None)  
              return temperature, pressure, humidity
          except RuntimeError as error:
              log_error(f"BME/BMP280 error: {error}")
              return None, None, None
      
      # Check if CSV file exists; if not, create it with headers
      if not os.path.exists(csv_file):
          with open(csv_file, mode="w", newline="") as file:
              writer = csv.writer(file)
              writer.writerow([
                  "Timestamp", 
                  "DHT Temp (C)", "DHT Humidity (%)", 
                  "BMP Temp (C)", "BMP Pressure (hPa)", "BMP Humidity (%)", 
                  "Avg Temp (C)", "Avg Humidity (%)"
              ])
      
      # Function to send the CSV file via SCP
      def send_csv_via_scp():
          remote_host = "192.168.1.100" 
          remote_user = "your_username"  
          remote_password = "your_password"  
          remote_path = "/path/to/destination/sensor_data.csv"  
      
          try:
              # Initialize SCP client
              ssh = paramiko.SSHClient()
              ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
              ssh.connect(remote_host, username=remote_user, password=remote_password)
              scp = paramiko.SFTPClient.from_transport(ssh.get_transport())
              
              # Upload the CSV file
              scp.put(csv_file, remote_path)
              print(f"File successfully uploaded to {remote_host}:{remote_path}")
              
              # Close the connection
              scp.close()
              ssh.close()
      
          except Exception as e:
              log_error(f"Error sending file via SCP: {e}")
      
      # Main loop to collect data
      def main():
          global consecutive_dht_errors, consecutive_bmp_errors
          start_time = time.time()
          end_time = start_time + 48 * 3600  # Run for 48 hours
      
          print("Starting data collection...")
      
          while time.time() < end_time:
              # Read from DHT11
              dht_temp, dht_humidity = read_dht()
              if dht_temp is None or dht_humidity is None:
                  consecutive_dht_errors += 1
                  log_error(f"Consecutive DHT11 errors: {consecutive_dht_errors}")
              else:
                  consecutive_dht_errors = 0
      
              # Read from BMP280
              bmp_temp, bmp_pressure, bmp_humidity = read_bmp()
              if bmp_temp is None or bmp_pressure is None:
                  consecutive_bmp_errors += 1
                  log_error(f"Consecutive BME/BMP280 errors: {consecutive_bmp_errors}")
              else:
                  consecutive_bmp_errors = 0
      
              # If either sensor exceeds error threshold, restart program
              if consecutive_dht_errors >= MAX_CONSECUTIVE_ERRORS or consecutive_bmp_errors >= MAX_CONSECUTIVE_ERRORS:
                  log_error("Max consecutive errors reached. Restarting program.")
                  restart_program()
      
              # Calculate averages
              avg_temp = None
              avg_humidity = None
      
              # Average temperature
              if dht_temp is not None and bmp_temp is not None:
                  avg_temp = (dht_temp + bmp_temp) / 2
              elif dht_temp is not None:
                  avg_temp = dht_temp
              elif bmp_temp is not None:
                  avg_temp = bmp_temp
      
              # Average humidity (only if BME280 is used, not BMP280)
              if dht_humidity is not None and bmp_humidity is not None:
                  avg_humidity = (dht_humidity + bmp_humidity) / 2
              elif dht_humidity is not None:
                  avg_humidity = dht_humidity
              elif bmp_humidity is not None:
                  avg_humidity = bmp_humidity
      
              # Log data if at least one sensor provides valid readings
              if dht_temp is not None or bmp_temp is not None:
                  timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                  with open(csv_file, mode="a", newline="") as file:
                      writer = csv.writer(file)
                      writer.writerow([
                          timestamp, 
                          dht_temp, dht_humidity, 
                          bmp_temp, bmp_pressure, bmp_humidity, 
                          avg_temp, avg_humidity
                      ])
                      print(
                          f"Logged: {timestamp}, "
                          f"DHT Temp: {dht_temp}°C, DHT Hum: {dht_humidity}%, "
                          f"BMP Temp: {bmp_temp}°C, BMP Press: {bmp_pressure} hPa, BMP Hum: {bmp_humidity}%, "
                          f"Avg Temp: {avg_temp}°C, Avg Hum: {avg_humidity}%"
                      )
      
              time.sleep(30)
      
          # After 48 hours, send the CSV file to the remote server
          send_csv_via_scp()
      
      if __name__ == "__main__":
          main()
