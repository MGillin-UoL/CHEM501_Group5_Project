# CHEM501_Group5_Project
This GitHub repository contains the code used in a research project for CHEM501 - Digital Alchemy: Synthesising Code and Chemistry at the University of Liverpool. This code was written by Marion Ridgway, Justin Trojillo, and Michael Gillin (Group 5).

The project investigates the temperature and air quality fluctuations in an office in the Department of Chemistry building at the University of Liverpool. This room is used as an office and 3D-printing suite, but also contains a PerkinElmer Spectrum 100 FT-IR Spectrometer with an ATR Sampling Accessory and an PerkinElmer Lambda 25 UV-Vis Spectrophotometer. To investigate these fluctuations, three identical setups were used containing an Arduino Nicla Sense ME, an Arduino MKR WiFi 1010, and an Ansmann 10.000 mAh powerbank. This project primarily utilised the functionality of the BME688 - Digital low power gas, pressure, temperature & humidity sensor with AI.

This repository contains three sets of code:
- CHEM501_Nicla_Project_Code.ino
  C++ code which connects the Nicla Sense ME to the MKR WiFi 1010 via an ESLOV cable.
- CHEM501_MKR_Project_Code.ino
  C++ code which codes the functionality of the Nicla Sense ME, such as how many measurements to obtain using which sensor.
- CHEM501_Project_Code.py
  A minimal piece of Python code for reading messages via MQTT (Message Queuing Telemetry Transport).

If you have any questions or would like additional information, please contact Marion (sgmridgw@liverpool.ac.uk), Justin (sgjtroji@liverpool.ac.uk), or Michael (sgmgilli@liverpool.ac.uk).
