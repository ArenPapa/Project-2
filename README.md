![11e470e9022f4fc5b367429bcbb285bc](https://github.com/comsci-uwc-isak/unit2_2023/assets/53995212/1d14b1d3-ae39-4ef3-8ec9-3329630eacae)

# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning
problem definition//conclusion

A: 500 C: 1500 E: 500

## Problem definition

The client is K.M. who is an ESS student from an international school in Karuizawa prefecture in Japan. He aims to grow roses for the event in the next school year of winter, which generally blooms in spring to early autumn in Karuizawa. In order to successfully bloom roses in winter, he decided to builde a greenhouse for the rose. To handle the greenhouse properly, he needs to know the best condition for rose to grow by analyzing the conditions both inside and outside the dorm to figure out best environment for its growth on campus precisely. In particular, he needs the data of how temperature, humidity, and air pressure affect it. Since he plans to conduct his research from spring to fall which is when roses grow, he requests the system to be durable and feasible in any weather in Karuizawa. He wants to visualize all data as well as the prediction of the conditions. Lastly, he requests the cost to be low because he is a student and wouldn’t be able to afford an expensive system. 

## Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity, temperature, atmospheric pressure and a custom data script that processes and analyzes the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequate precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more elaborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this application the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Raspberry Pi [^3]. "The Raspberry Pi is a very cheap computer that runs Linux, but it also provides a set of GPIO (general purpose input/output) pins, allowing you to control electronic components for physical computing and explore the Internet of Things (IoT).  "[^4]. In addition to the low cost of the Raspberry Pi (> 35USD), this device is programmable and expandable[^1]. I considered alternatives such as different versions of the Pi 400 but their size and price make them a less adequate solution.

Considering the budgetary constraints of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python's open-source nature and platform independence contribute to the long-term viability of the system. The use of Python simplifies potential future enhancements or modifications, allowing for seamless scalability without the need for extensive redevelopment [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is the responsibility of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues promptly.  


## Success Criteria

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]: Industries, Jaycon. “15 Innovative Raspberry Pi Use Cases: What You Can Do with Raspberry Pi.” Jaycon, 8 Nov. 2024, www.jaycon.com/15-innovative-ways-to-use-raspberry-pi/.   
[^4]: Industries, Ravikiran A S, “15 Innovative Raspberry Pi Use Cases: What You Can Do with Raspberry Pi.” Jaycon, 8 Nov. 2024, www.jaycon.com/15-innovative-ways-to-use-raspberry-pi/. 
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 

1. The solution provides a visual representation of the Humidity, Temperature and atmospheric pressure (HL) values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. ```** [Issue tacled] **: This solves the lack of ability to monitor the environment on campus precisely over time. It also helps collecting data of trends within a day and also between days. My client's request, "he needs to know the best condition ... both inside and outside of the dormitory...In particular, he needsthe data of how temperature, humidity, and air pressure affect it. "```
1. ```[HL]``` The local variables will be measure using a set of 3 sensors around the dormitory.```** [Issue tacled] **: This tests the accuracy of the data enhancing the trsut of the data. This meats the cliet's requirement "he needs to know the best condition for rose to grow .... precisely"```
2. The solution provides a mathematical modelling for the Humidity, Temperature and atmospheric pressure (HL) levels for each Local and Remote locations.```(HL: non-lineal model)``` ```** [Issue tacled] **: This simplifies and visualize data that is easy to analyze the trends.```
3. The solution provides a comparative analysis for the Humidity, Temperature and atmospheric pressure (HL) levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median. ```** [Issue tacled] **: Have more clear understanding of the condition and have more general understanding when analyzing data. ```
4. ```(SL)```The Local samples are stored in a csv file and ```(HL)``` posted to the remote server as a backup. ```** [Issue tacled] **: Prevent the data loss by storing data in multiple places. ```
5. The solution provides a prediction for the subsequent 12 hours for Humidity, Temperature and atmospheric pressure (HL). ```** [Issue tacled] **: The prediction allows the customers to adjust the conditions in the greenhouse once he gets to start his project. ```
6. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Humidity, Temperature and atmospheric pressure (HL). ```** [Issue tacled] **: Summarize all the project to visualize it and make it clear what we accomplished by this project.```
7. 
Here’s an exploration of the **TOK connections** based on the questions provided:

---

### **Central Question**  
**To what extent does the use of data science in climate research influence our understanding of environmental issues, and what knowledge questions arise regarding the reliability, interpretation, and ethical implications of data-driven approaches in addressing climate change?**

### **Connections to Knowledge Questions**

#### 1. How does our use of technology shape our understanding of the environment?
- **Data as a Lens:** Technology can collect, process, and visualize the environmental data that offers completely new insights into issues such as temperature trends, humidity level, and air pressure. These are enabled by tools like sensors, for example, DHT11 and BME280, which can quantify the phenomena that otherwise would have remained imperceptible.
Bias and Limits of Technology: Our understanding is only as good as the quality and reliability of sensors, data models, and algorithms. For instance, sensors may have calibration errors or be unable to capture phenomena that occur at a very localized scale.
- **Selective focus:** Technology often focuses on measurable aspects of the environment, perhaps to the detriment of subjective or qualitative elements, such as the cultural and community knowledge about climate.  

**Knowledge Question:**  
*To what extent does reliance on technology limit or expand our understanding of complex environmental systems?*

---

#### 2. What are our responsibilities as technologists in handling personal data with respect to our living spaces?
- **Ethical use of data:** During projects involving smart sensors-monitoring indoor humidity or temperature, for example-the following question is raised: *Who owns the data?* If such data has to do with personal living conditions, then there will be privacy concerns.
- **Transparency and consent:** Ethical practices call for clarity on how the data is collected, stored, shared, and used. In your project, it is important to ensure that the school community understands the purpose of data collection.
- **Algorithmic responsibility:** When automating decisions, for example, to predict future environmental trends, the technologist is bound to ensure fairness, avoid biases, and prevent misuse of the data.

**Knowledge Question:**  
*How can technologists balance the need for innovation with the ethical responsibilities of safeguarding personal and environmental data?*

---

#### 3. What cultural and contextual factors could affect our interpretation of the results, particularly in comparing our local readings with those of the campus?
Localized differences Environmental data is inherently contextual. For instance, the microclimate of one region, say near a forest, is very different from another region, say an urban campus.
Cultural perspectives: Communities might value or interpret data through the lens of their value systems. For example, high temperatures might be considered as an indication of imbalance in cultures that believe in living in harmony with nature, while others may consider it a part of normal seasonal variation.
- **Global vs. local scales:** Comparing local readings against broader datasets presents interpretation challenges. A small rise in temperature might seem insignificant locally but could have severe implications globally.

**Knowledge Question:**  
*How do cultural and contextual factors shape the interpretation of environmental data, and to what extent do they affect its global applicability?*

---

### **TOK Themes and Perspectives**

#### **Theme: Knowledge and Technology
Data science represents the interface between human imagination and the natural world. Using sensors and models, we convert environmental phenomena into quantitative knowledge. In so doing, we introduce issues of reliability and representation.
Example: If a sensor misreads data, to what extent can we still have faith in the knowledge produced from it?

#### **Theme: Knowledge and Ethics
Climate research brings four ethical dilemmas in the gathering, use, and interpretation of data. Whose data is collected? How does it get used? For whom?
- Example: How would you compare local data to campus data without the findings being taken out of context or misused to justify unsustainable practices?

---

### Application to Our Project
- **Reliability of data:** The accuracy of the sensors-DHT11 and BME280-is central to your project. Calibration and validation against other datasets will enhance confidence in the findings.
- **Interpretation:** Comparing your data with campus readings raises interpretive challenges. Consider microclimates, building insulation, and human activity.
- **Ethics:** The presentation of findings must be a discussion of the scope and limits of the project. Do not exaggerate conclusions or imply causation from correlation.

---

### **Conclusion**  
Use of data science in climate research will fundamentally alter our perceptions about environmental issues but is not bereft of critical questions related to knowledge, including reliability, ethics, and interpretation. As technologists, it is our responsibility to make sure that our tools are used responsibly, that the data is contextualized, and ethical considerations guide us. This approach not only adds credibility to the results but provides a deeper and richer insight into understanding the environment.

# Criteria B: Design

## Flow Chart

<img width="max" alt="Screenshot 2024-12-09 at 8 36 08" src="https://github.com/user-attachments/assets/97e4c8e4-383e-4f0d-8de1-c70d846a185b">
<img width="max" alt="Screenshot 2024-12-09 at 8 37 35" src="https://github.com/user-attachments/assets/138640f2-50e1-42b6-92dd-4af536ac5369">
<img width="max" alt="Screenshot 2024-12-09 at 8 38 36" src="https://github.com/user-attachments/assets/b38a4ee2-767b-423c-a0dd-e9e9a18ff794">

**Fig.1** Fig. 1 Main function for posting the data. Call register_user() function to create a user account and call authenticate() function to log in and gain an authentication token. It iterates through each sensors to register them, and get sensor_ids. Open the CSV file and iterate by each row. Then, if either temperature, humidiy, or pressure is found, the value is posted to the server. Error is being handled using try-except. 

<img width="623" alt="Screenshot 2024-12-09 at 8 50 24" src="https://github.com/user-attachments/assets/f04d4d17-9ac0-4940-8c75-cef8768c0822">
**Fig.1** Fig. 1 This is the function called register_sensor which registers sensor handling the erorrs. Getting two inputs from the parameters, send post request to the server. If the status code is 201 which indicates success in registering sensor, it gets the sensor's ID. If it is not successfully registered, then it does error handling.





## System Diagram **HL**

![System Diagrams unit 2 (2)](https://github.com/user-attachments/assets/36775cba-6730-45d3-bccb-57b4d8a8179d)

**Fig.3** Fig. 3 System diagram (HL+) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally on a Raspberry Pi. A remote server provides and API for remote monitoring and storage (192.162.6.142) via the ISAK-S network. A laptop for remote work is included.

## Record of Tasks

| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Write the Problem context                                      | Clearly describe the problem the project aims to solve.                                                           | 10min         | Nov 22                 | A         |
| 2       | Identify project requirements (hardware/software)             | List all components required (Raspberry Pi, DHT11, BME280, software).                                            | 20min         | Nov 22                 | A         |
| 3       | Research sensor capabilities (DHT11 and BME280)               | Understand sensor specifications, data ranges, and potential issues.                                              | 30min         | Nov 23                 | A         |
| 4       | Set up Raspberry Pi and necessary software                     | Ensure the Raspberry Pi is functional with Raspbian OS, Python, and libraries for sensors.                      | 1 hour        | Nov 23                 | B         |
| 5       | Connect DHT11 sensor to Raspberry Pi                           | Successfully wire the DHT11 sensor to Raspberry Pi and verify functionality.                                     | 30min         | Nov 24                 | B         |
| 6       | Connect BME280 sensor to Raspberry Pi                          | Successfully wire the BME280 sensor to Raspberry Pi and verify functionality.                                   | 30min         | Nov 24                 | B         |
| 7       | Write Python code to collect data from DHT11                    | Write a script to read temperature and humidity data from DHT11 sensor and store it in a CSV file.               | 1 hour        | Nov 25                 | B         |
| 8       | Write Python code to collect data from BME280                   | Write a script to read temperature and pressure data from BME280 sensor and store it in a CSV file.             | 1 hour        | Nov 25                 | B         |
| 9       | Combine code for both sensors into a single Python script      | Integrate both DHT11 and BME280 data collection into a unified Python script.                                    | 30min         | Nov 26                 | B         |
| 10      | Test data collection process for 48 hours                      | Run the Raspberry Pi to collect data from both sensors for 48 hours and ensure proper CSV storage.              | 2 hours       | Dec 2                  | B         |
| 11      | Set up data transmission from Raspberry Pi to computer         | Implement code to send the CSV data file from the Raspberry Pi to a computer after 48 hours of data collection. | 1 hour        | Dec 3                  | C         |
| 12      | Write Python script on computer to receive data from Raspberry Pi | Ensure the computer successfully receives and stores the CSV data file from Raspberry Pi.                        | 1 hour        | Dec 3                  | C         |
| 13      | Implement API to upload CSV data                              | Write API integration to post the CSV data to a remote server or cloud platform.                                 | 2 hours       | Dec 4                  | C         |
| 14      | Fetch data from API and store it on the computer               | Write code to fetch the data from the API and store it on the computer for analysis.                             | 1 hour        | Dec 4                  | C         |
| 15      | Prepare data for plotting (extract relevant columns)          | Organize the data into format suitable for plotting temperature, pressure, and humidity.                         | 1 hour        | Dec 5                  | C         |
| 16      | Plot temperature data                                          | Use Python libraries (matplotlib) to plot temperature data over time.                                            | 1 hour        | Dec 5                  | D         |
| 17      | Plot pressure data                                             | Use Python libraries (matplotlib) to plot pressure data over time.                                               | 1 hour        | Dec 5                  | D         |
| 18      | Plot humidity data                                             | Use Python libraries (matplotlib) to plot humidity data over time.                                               | 1 hour        | Dec 5                  | D         |
| 19      | Analyze data and identify trends                               | Compare temperature, pressure, and humidity patterns across the 48-hour period.                                  | 2 hours       | Dec 6                  | D         |
| 20      | Compare data with school data                                  | Compare the collected data with the school’s environmental data (if available).                                  | 1 hour        | Dec 6                  | D         |
| 21      | Write analysis and conclusions based on comparison             | Summarize findings from the data comparison and present insights.                                               | 2 hours       | Dec 7                  | D         |
| 22      | Finalize project documentation                                | Document the entire process, including code snippets, results, and analysis.                                    | 2 hours       | Dec 7                  | D         |
| 23      | Review and refine project documentation                       | Proofread and make necessary revisions to the project documentation.                                             | 1 hour        | Dec 8                  | D         |
| 24      | Prepare project presentation                                  | Create a slide deck to present the project, including results and conclusions.                                   | 1 hour        | Dec 8                  | D         |
| 25      | Test the full project from data collection to plotting         | Run the full project to ensure that all components function seamlessly together.                                | 2 hours       | Dec 8                  | D         |
| 26      | Debug any issues in project functionality                     | Resolve any bugs or issues found during the final testing of the project.                                        | 1 hour        | Dec 8                  | D         |
| 27      | Upload project documentation to the submission platform       | Submit final project documentation for grading.                                                                  | 30min         | Dec 8                  | A         |
| 28      | Evaluate project success against objectives                    | Assess whether the project met all its objectives and whether the results are valid.                             | 1 hour        | Dec 8                  | D         |
| 29      | Get feedback on the project                                   | Ask for feedback from peers or teachers to improve the project.                                                 | 30min         | Dec 8                  | A         |
| 30      | Prepare for project presentation (rehearse)                   | Rehearse the project presentation to ensure clarity and confidence during the final presentation.               | 1 hour        | Dec 8                  | D         |
| 31      | Submit final presentation                                      | Deliver the final project presentation.                                                                           | 30min         | Dec 8                  | A         |
| 32      | Review feedback after presentation                            | Reflect on feedback received during the presentation for future improvements.                                   | 1 hour        | Dec 8                  | A         |
| 33      | Final project evaluation                                        | Evaluate the overall success of the project and determine improvements for future work.                         | 1 hour        | Dec 8                  | A         |
| 34      | Document lessons learned from the project                     | Write a section of lessons learned to improve future projects.                                                   | 1 hour        | Dec 8                  | A         |
| 35      | Organize project files and code for future reference          | Clean up and organize project files, including source code, diagrams, and final documentation.                 | 1 hour        | Dec 8                  | A         |
| 36      | Conduct a final check on the project                          | Double-check all components of the project to ensure nothing is overlooked.                                      | 30min         | Dec 8                  | A         |
| 37      | Submit the final project files                                | Submit the completed project files to the designated platform.                                                  | 30min         | Dec 8                  | A         |
| 38      | Archive the project                                          | Save the entire project for future reference or portfolio purposes.                                             | 30min         | Dec 8                  | A         |
| 39      | Record a post-project reflection                              | Write a reflection on the challenges and successes of the project.                                               | 1 hour        | Dec 8                  | A         |
| 40      | Reflect on potential improvements for similar future projects | Consider possible improvements or changes for a similar future project.                                          | 1 hour        | Dec 8                  | A         |
## Test Plan
Here’s an expanded **step-by-step test plan table** with additional detailed steps to cover the entire process thoroughly. Each stage is explicitly outlined for clarity.

---

| **Step** | **Action**                                                                                      | **Expected Outcome**                                            | **Test Result** | **Notes**                                               |
|----------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-----------------|---------------------------------------------------------|
| 1        | Turn on your Mac and open the Terminal application.                                             | Mac boots up, and Terminal is ready for commands.               | Pass/Fail       | Ensure Wi-Fi connection is active.                     |
| 2        | Power up the Raspberry Pi using a micro-USB or USB-C power supply.                              | Raspberry Pi boots up and connects to Wi-Fi.                    | Pass/Fail       | Confirm the Pi's status with a green activity light.   |
| 3        | Use your Mac Terminal to connect to the Raspberry Pi via SSH.                                   | SSH connection is established, and Pi command line is accessible.| Pass/Fail       | Run `ssh pi@<IP_ADDRESS>`. Use `hostname -I` to find Pi's IP. |
| 4        | Update the Raspberry Pi's operating system and libraries.                                       | Raspberry Pi is updated without errors.                         | Pass/Fail       | Run `sudo apt update && sudo apt upgrade -y`.          |
| 5        | Open Raspberry Pi configuration to enable necessary interfaces (I2C, GPIO).                     | Interfaces are enabled successfully.                            | Pass/Fail       | Use `sudo raspi-config` to enable settings.            |
| 6        | Reboot the Raspberry Pi to apply the changes.                                                   | Pi restarts and reconnects to Wi-Fi.                            | Pass/Fail       | Reconnect via SSH after rebooting.                     |
| 7        | Connect the DHT11 sensor to the Raspberry Pi's GPIO pins using jumper wires.                    | DHT11 is securely connected to power, ground, and GPIO pin 4.    | Pass/Fail       | Use a pull-up resistor (10kΩ) between data and VCC.    |
| 8        | Connect the BME280 sensor to the Raspberry Pi’s I2C pins (SDA, SCL).                            | BME280 is securely connected to power, ground, SDA, and SCL.     | Pass/Fail       | Ensure wires are connected to the correct I2C pins.    |
| 9        | Install Python libraries required for sensors and data processing on the Raspberry Pi.          | All libraries are installed without errors.                     | Pass/Fail       | Run `pip3 install adafruit-circuitpython-dht smbus matplotlib`. |
| 10       | Test the DHT11 sensor by running a basic Python script.                                         | DHT11 outputs temperature and humidity data to the terminal.     | Pass/Fail       | Use a simple script to confirm functionality.          |
| 11       | Test the BME280 sensor by running a Python script.                                              | BME280 outputs temperature, pressure, and humidity data.         | Pass/Fail       | Verify that realistic data is displayed in the terminal. |
| 12       | Apply a moving average filter to the sensor data.                                               | Filtered data reduces noise while maintaining realistic trends.  | Pass/Fail       | Verify by comparing filtered data with raw data.       |
| 13       | Save collected data from both sensors to a CSV file.                                            | CSV file is created and updated with data in real-time.          | Pass/Fail       | Ensure file is correctly formatted and data is complete. |
| 14       | Transfer the CSV file to your Mac using SCP (Secure Copy Protocol).                             | CSV file is successfully copied to the Mac.                     | Pass/Fail       | Run `scp pi@<IP_ADDRESS>:<file_path> <destination>`.   |
| 15       | Create a Python script on your Mac to post the CSV data to an API server.                       | Data is successfully posted to the server.                      | Pass/Fail       | Confirm a successful HTTP 200 response code.          |
| 16       | Retrieve data from the server API to validate successful storage.                               | Retrieved data matches the data posted from the Raspberry Pi.    | Pass/Fail       | Compare the API response with the original dataset.    |
| 17       | Use Python's `Matplotlib` on your Mac to visualize data in graphs (temperature, humidity, pressure). | Graphs are generated, showing clear trends and patterns.         | Pass/Fail       | Ensure proper labeling of axes and units.             |
| 18       | Compare collected data with school’s environmental data for accuracy and validation.            | Differences and similarities are documented.                    | Pass/Fail       | Note potential environmental or measurement anomalies. |
| 19       | Clean up the Raspberry Pi by disconnecting sensors and shutting it down safely.                 | Raspberry Pi powers off safely and sensors are disconnected.     | Pass/Fail       | Run `sudo shutdown now` before removing power.         |
| 20       | Prepare project documentation, including detailed analysis, results, and visualizations.        | Documentation is clear, concise, and meets the project criteria. | Pass/Fail       | Include details on challenges faced and solutions.     |

---

### **Additional Notes**  

- **Step 7–8 (Sensor Setup)**: Double-check the wiring for both sensors before powering on the Raspberry Pi. Incorrect wiring could damage the sensors or the Pi.  
- **Step 10–11 (Sensor Testing)**: Test each sensor independently to isolate potential issues.  
- **Step 12 (Moving Average Filter)**: Include a mechanism to compare raw vs. filtered data for better understanding.  
- **Step 15–16 (API Testing)**: Use tools like Postman to verify API endpoints before writing Python scripts.  

# Criteria C: Development

---

## Techniques Used in the Project

### 1. **Data Collection from Sensors**  
   - **DHT11** and **BME280** sensors are used to measure temperature, humidity, and pressure.  
   - Python libraries like `Adafruit_DHT` and `smbus2` enable seamless interaction with these sensors.

#### Example Code:  
```python
import Adafruit_DHT
from smbus2 import SMBus
from bme280 import BME280

# Initialize sensors
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO pin for DHT11
bme280 = BME280(i2c_dev=SMBus(1))

# Read data from DHT11
humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

# Read data from BME280
pressure = bme280.get_pressure()

print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure} hPa")
```

---

### 2. **Data Storage and Formatting**  
   - Collected sensor data is stored in a **CSV file**, which ensures easy retrieval and compatibility with other programs.  
   - Each row represents a single timestamped reading, making it suitable for time-series analysis.

#### Example Code:  
```python
import csv
from datetime import datetime

# Store data in a CSV file
with open('sensor_data.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    writer.writerow([timestamp, temperature, humidity, pressure])
```

---

### 3. **Noise Filtering Using Moving Average**  
   - Sensor readings can be noisy. To address this, the **moving average technique** smoothens data by averaging values over a sliding window.  

#### Example Code:  
```python
def moving_average(data, window_size=5):
    smoothed_data = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        smoothed_data.append(sum(window) / window_size)
    return smoothed_data

# Example usage with temperature data
temperature_data = [23, 24, 25, 23, 26, 24, 23]
smoothed_temperatures = moving_average(temperature_data, window_size=3)
print("Smoothed Temperatures:", smoothed_temperatures)
```

---

### 4. **Data Visualization**  
   - Visualizing data helps identify trends and anomalies. Libraries like **Matplotlib** and **Seaborn** are used to plot temperature, humidity, and pressure graphs.  
   - Multiple plots are created for better comparison.

#### Example Code:  
```python
import matplotlib.pyplot as plt

# Example data
timestamps = ["2024-12-07 12:00", "2024-12-07 12:10", "2024-12-07 12:20"]
temperatures = [22.5, 23.0, 22.8]

# Plot temperature data
plt.plot(timestamps, temperatures, marker='o', label='Temperature (°C)')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

### 5. **API Integration**  
   - After storing the data locally, it is sent to a server using an **API**. The same API retrieves the processed data for visualization.  
   - Libraries like `requests` enable sending HTTP POST and GET requests.

#### Example Code:  
```python
import requests

API_URL = 'http://example.com/api/data'

# Send data to the API
payload = {'temperature': temperature, 'humidity': humidity, 'pressure': pressure}
response = requests.post(API_URL, json=payload)

# Retrieve data from the API
if response.status_code == 200:
    data = requests.get(API_URL).json()
    print("Received Data:", data)
else:
    print("Error:", response.status_code)
```

---

### 6. **Data Modeling and Analysis**  
   - Analyze sensor data to uncover patterns. For example, **linear regression** predicts future trends based on historical data.  
   - This can be used to predict environmental conditions or compare trends with school datasets.

#### Example Code:  
```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Example temperature data
timestamps = [1, 2, 3, 4, 5]
temperatures = [22, 23, 23.5, 24, 24.5]

# Reshape data for Linear Regression
X = np.array(timestamps).reshape(-1, 1)
y = np.array(temperatures)

# Train a linear regression model
model = LinearRegression().fit(X, y)

# Predict future temperatures
future_timestamps = np.array([6, 7, 8]).reshape(-1, 1)
predicted_temperatures = model.predict(future_timestamps)
print("Predicted Temperatures:", predicted_temperatures)
```

---

### 7. **Comparing with School Data**  
   - The collected data is compared with existing school data to identify discrepancies and validate sensor accuracy.

---

### 8. **Project Documentation**  
   - **Criteria A (Analysis):** Includes problem identification, justification, and research on sensor technology.  
   - **Criteria B (Design):** Demonstrates the system architecture, such as data flow diagrams.  
   - **Criteria C (Development):** Explains the implementation process with annotated code snippets.  
   - **Criteria D (Evaluation):** Assesses the effectiveness of the project by comparing results with initial goals.

---

### Complete Workflow  

1. **Initialization:** Configure Raspberry Pi and connect sensors.  
2. **Data Collection:** Read data from DHT11 and BME280.  
3. **Data Storage:** Save data locally in a CSV file.  
4. **Data Filtering:** Apply moving average to reduce noise.  
5. **Data Analysis:** Build regression models and identify trends.  
6. **API Communication:** Post and retrieve data using an API.  
7. **Visualization:** Generate comparative graphs of collected and external data.  
8. **Evaluation:** Compare with school datasets to validate findings.

---




## Development




# Criteria D: Functionality

https://www.canva.com/design/DAGYtM1qFs8/-F-tnVXwE4MusvYYKBIcMQ/edit?utm_content=DAGYtM1qFs8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

A 7 min video demonstrating the proposed solution with narration
