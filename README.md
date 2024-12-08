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
2. The solution provides a mathematical modelling for the Humidity, Temperature and atmospheric pressure (HL) levels for each Local and Remote locations.```(HL: non-lineal model)``` ```** [Issue tacled] **: ```
3. The solution provides a comparative analysis for the Humidity, Temperature and atmospheric pressure (HL) levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median. ```** [Issue tacled] **: fill in here```
4. ```(SL)```The Local samples are stored in a csv file and ```(HL)``` posted to the remote server as a backup. ```** [Issue tacled] **: fill in here```
5. The solution provides a prediction for the subsequent 12 hours for Humidity, Temperature and atmospheric pressure (HL). ```** [Issue tacled] **: fill in here```
6. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Humidity, Temperature and atmospheric pressure (HL). ```** [Issue tacled] **: fill in here```

_TOK Connection: To what extent does ```the use of data science``` in climate research influence our understanding of environmental issues, and what knowledge questions arise regarding the ```reliability, interpretation, and ethical implications``` of data-driven approaches in addressing climate change_

1. How does our use of technology shape our understanding of the environment
2. What responsibilities do we have as technologists when it comes to handling personal data related to our living spaces?
3. What cultural and contextual factors might impact our interpretation of the results, especially when comparing our local readings with those from the campus? 

# Criteria B: Design

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

# Criteria C: Development

(1000 words max): Code not included, comments not included

## List of techniques used

1. Moving_average for filtering noisy signals from sensors
2. Data visualization
3. Connecting to server using API
4. Create data models

## Moving average for filtering noisy signals from sensors

one problems that I had while solving success criteria #1 was that the sensor are quite noisy
which presented a problem at the moment of creating a model. I thought about using a pre-processing
step to smooth the data before proceeding with visialization and modeling.
(copy the specific code that we use this)

・・・.py
def moving_average(windowSize: int, x:list) -> list:
    x_smoothed = []
    for i in range(0, len(x)-windowSize):
        x_section = x[i:i+windowSize]
        x_average = sum(x_section)/windowSize
        x_smoothed += [x_average]

    return x_smoothed


I decided to create a function to contain the algorithm for a moving average. This allows for code reuse and modelarity. 
The function receives two inputs, the size of the window (windowSize) and continue the description.....

## Development




# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration
