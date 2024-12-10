# CHEM501_Group5_Project
This GitHub repository contains the code used in a research project for CHEM501 - Digital Alchemy: Synthesising Code and Chemistry at the University of Liverpool.

## Description
The project investigates the temperature and air quality fluctuations in an office in the Department of Chemistry building at the University of Liverpool. This room is used as an office and 3D-printing suite, but also contains a PerkinElmer Spectrum 100 FT-IR Spectrometer with an ATR Sampling Accessory and an PerkinElmer Lambda 25 UV-Vis Spectrophotometer. To investigate these fluctuations, three identical setups were used containing an Arduino Nicla Sense ME, an Arduino MKR WiFi 1010, and an Ansmann 10.000 mAh powerbank (PB212). This project primarily utilised the functionality of the BME688 - Digital low power gas, pressure, temperature & humidity sensor with AI.

This repository contains four sets of code:
- CHEM501_Nicla_Project_Code.ino

  C++ code which connects the Nicla Sense ME to the MKR WiFi 1010 via an ESLOV cable.
- CHEM501_MKR_Project_Code.ino

  C++ code which codes the functionality of the Nicla Sense ME, such as how many measurements to obtain using which sensor.
- CHEM501_MQTT_Project_Code.py

  A minimal piece of Python code for reading messages via MQTT (Message Queuing Telemetry Transport).
- Project Data Visualisation.py

  Python code which converts the data read from a csv file into a graph.
## Prerequisites
The following software is required to run the code and acquire the appropriate data:
- Visual Studio Code (or other code editor) - https://code.visualstudio.com/download
- Arduino IDE - https://www.arduino.cc/en/software
- Python (Anaconda is recommended. To install, click "Free Download using the URL") - https://www.anaconda.com/

The following pieces of equipment are also required:
- Arduino Nicla Sense ME - https://store.arduino.cc/products/nicla-sense-me
- Arduino MKR WiFi 1010 - https://store.arduino.cc/products/arduino-mkr-wifi-1010
- Powerbank (we recommend an Ansmann 10.000 mAh powerbank (PB212)) - https://shop.ansmann.de/en/powerbank-10000-pb212

## Installation
If using Anaconda, the pyserial module must be installed.
If using Windows:
1. Open Anaconda Prompt
2. Type "conda install pyserial"
3. Press "Enter"

If using macOS:
1. Open Terminal
2. Type "conda install pyserial"
3. Press "Enter"


Next, open Arduino IDE and navigate to Tools --> Board --> Board Manager and install the following:
- Aruino Mbed OS Nicla Boards
- Arduino SAMD Boards

Finally, in the Arduino IDE, navigate to Tools --> Manage Libraries, and install the following:
- Arduino_BHY2
- ArduinoBLE
- Arduino_BHY2Host
- WiFiNina
- ArduinoMqttClient

## Usage
Below is a set of instructions for collecting data using the hardware listed before and the code provided.

1. Connect the Arduino Nicla Sense ME to your computer via a USB-A to micro USB.
2. Run CHEM501_Nicla_Project_Code.ino in Arduino IDE. This "tells" the Nicla to "listen" to the MKR.
3. Connect the Arduino Nicla Sense ME to the Arduino MKR WiFi 1010 via an ESLOV cable.
4. Connect the Arduino MKR WiFi 1010 to your computer via a USB-A to micro USB.
5. Run CHEM501_MKR_Project_Code.ino in Arduino IDE. This "tells" the MKR to start collecting temperature and gas measurements.
6. Run CHEM501_MQTT_Project_Code.py in a code editor. This will convert the data readings to csv and db files.
7. Disconnect the Arduino MKR WiFi 1010 from your computer and connect it to a powerbank. This will now run remotely.
8. Once the desired number of readings has been obtained, stop the CHEM501_MQTT_Project_Code.py code.
9. Run Project Data Visualisation.py. This will convert your numerical data into three graphs.

## Authors
If you have any questions or would like additional information, please contact:
- Marion Ridgway (sgmridgw@liverpool.ac.uk)
- Justin Trojillo (sgjtroji@liverpool.ac.uk)
- Michael Gillin (sgmgilli@liverpool.ac.uk).

## License
This project is not currently licensed.

## Acknowledgements
The authors would like to thank Dr Joe Forth, Professor Anna Slater, and Harvey West for their assistance during this project. The authors would also like to thank Dr Anthony Bradley and Dr Gemma Holliday for sharing their knowledge on SQL (Structured Query Language) and FAIR (Findable, Accessibility, Interoperable, Reusable) Principles, respectively. Lastly, the authors would like to thank Sebastian Romero for authoring the "Arduino Nicla Sense ME Cheat Sheet", which proved to be invaluable in carrying out the research.
