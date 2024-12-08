import requests
import csv
from datetime import datetime

# API Configuration
BASE_URL = "http://192.168.4.137"
USERNAME = "arma"
PASSWORD = "uwcisak2024"

# Sensor Registration Data
SENSORS = [
    {"type": "Temperature", "location": "R1-11B", "name": "arma1", "unit": "C"},
    {"type": "Humidity", "location": "R1-11B", "name": "arma2", "unit": "%"},
    {"type": "Pressure", "location": "R1-11B", "name": "arma3", "unit": "hPa"},
]

# Register the user first
def register_user():
    user = {"username": USERNAME, "password": PASSWORD}
    response = requests.post(f"{BASE_URL}/register", json=user)
    
    if response.status_code == 201:
        print("User registered successfully.")
    else:
        raise Exception(f"User registration failed: {response.text}")

# Authenticate and retrieve token
def authenticate():
    user = {"username": USERNAME, "password": PASSWORD}
    response = requests.post(f"{BASE_URL}/login", json=user)
    
    if response.status_code == 200:
        access_token = response.json().get("access_token")
        print("Authentication successful.")
        return {"Authorization": f"Bearer {access_token}"}
    else:
        raise Exception(f"Authentication failed: {response.text}")

# Register sensors and return their IDs
def register_sensor(auth, sensor_data):
    response = requests.post(f"{BASE_URL}/sensor/new", json=sensor_data, headers=auth)
    if response.status_code == 201:
        sensor_id = response.json().get("id")
        print(f"Sensor registered: {sensor_data['name']} (ID: {sensor_id})")
        return sensor_id
    else:
        raise Exception(f"Sensor registration failed: {response.text}")

# Post sensor readings
def post_reading(auth, datetime_str, sensor_id, value):
    # Ensure the timestamp from CSV is in ISO 8601 format
    try:
        # If datetime_str isn't in the correct format, you can parse and reformat it here
        # Assuming the datetime format in CSV is already correct (e.g., '2024-12-08 12:34:56')
        datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")  # Modify this if your format is different
        formatted_datetime = datetime_obj.isoformat()  # Convert to ISO format

        new_record = {"datetime": formatted_datetime, "sensor_id": sensor_id, "value": value}
        response = requests.post(f"{BASE_URL}/reading/new", json=new_record, headers=auth)  # Correct endpoint
        if response.status_code == 201:
            print(f"Reading posted: {new_record}")
        else:
            raise Exception(f"Failed to post reading: {response.text}")
    except Exception as e:
        print(f"Error in parsing datetime: {e}")

# Main function
def main():
    try:
        # Step 1: Register the user
        register_user()

        # Step 2: Authenticate and get authorization header
        auth = authenticate()

        # Step 3: Register sensors
        sensor_ids = {}
        for sensor in SENSORS:
            sensor_id = register_sensor(auth, sensor)
            sensor_ids[sensor["type"]] = sensor_id

        # Step 4: Parse CSV file and post readings
        csv_file_path = "/Users/areneun/Downloads/sensor_data.csv"
        with open(csv_file_path, mode="r") as file:
            reader = csv.DictReader(file)

            print("Posting data from CSV...\n")
            for row in reader:
                datetime_str = row["Timestamp"]  # Use the timestamp from the CSV file
                temperature = row.get("Temperature (°C)")
                humidity = row.get("Humidity (%)")
                pressure = row.get("Pressure (hPa)")

                # Post temperature readings
                if temperature:
                    post_reading(auth, datetime_str, sensor_ids["Temperature"], float(temperature))

                # Post humidity readings
                if humidity:
                    post_reading(auth, datetime_str, sensor_ids["Humidity"], float(humidity))

                # Post pressure readings
                if pressure:
                    post_reading(auth, datetime_str, sensor_ids["Pressure"], float(pressure))

        print("All data posted successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Run the script
if __name__ == "__main__":
    main()

