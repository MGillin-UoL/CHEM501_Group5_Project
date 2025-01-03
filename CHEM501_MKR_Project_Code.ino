#include <ArduinoMqttClient.h>
#include <WiFiNINA.h>
#include "Arduino_BHY2Host.h"

///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = "VodafoneMobileWiFi-595195";        // your network SSID (name)
char pass[] = "6264171888";    // your network password (use for WPA, or use as key for WEP)

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

const char broker[] = "pf-eveoxy0ua6xhtbdyohag.cedalo.cloud";
int        port     = 1883;
const char topic1[] = "Temp"; // Temp
const char topic3[] = "Gas"; // Gas

//set interval for sending messages (milliseconds)
const long interval = 5000;
unsigned long previousMillis = 0;

int count = 0;

Sensor temp(SENSOR_ID_TEMP);
Sensor gas(SENSOR_ID_GAS);

void setup() { 
   //Initialize serial and wait for port to open:
  Serial.begin(115200);

  // attempt to connect to Wifi network:
  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    // failed, retry
    Serial.print(".");
    delay(5000);
  }

  Serial.println("You're connected to the network");
  Serial.println();

  Serial.print("Attempting to connect to the MQTT broker: ");
  Serial.println(broker);

  if (!mqttClient.connect(broker, port)) {
    Serial.print("MQTT connection failed! Error code = ");
    Serial.println(mqttClient.connectError());

    while (1);
  }

  Serial.println("You're connected to the MQTT broker!");
  Serial.println();
  Serial.begin(115200);
  BHY2Host.begin();
  temp.begin();
//  pressure.begin();
  gas.begin();
}

void loop() {
   // call poll() regularly to allow the library to send MQTT keep alive which
  // avoids being disconnected by the broker
  mqttClient.poll();

  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    // save the last time a message was sent
    previousMillis = currentMillis;   
    send_data(1, 1000, millis()); //sends 1 reading, 1 second apart
  }
} // end loop()

void send_data(int n_readings, float d_time, float t0){
  // Initialise the time stamp variable
  float dataT = 0;

  for (int n = 0; n < n_readings; n++)  {
    // Update the sensor readings 
    BHY2Host.update();    

    // Collect the data
    dataT = millis() - t0;
    float dataTemp = temp.value();
    float dataG = gas.value();

    //sends temperature data to MQTT
    mqttClient.beginMessage(topic1);
    mqttClient.print(dataTemp);
    mqttClient.endMessage();

    //sends gas data to MQTT
    mqttClient.beginMessage(topic3);
    mqttClient.print(dataG);
    mqttClient.endMessage();

    // Write the data to the serial port
    Serial.print("Time:");
    Serial.print(millis() - t0);
    Serial.print("(ms), Temperature:");
    Serial.print(dataTemp);
    Serial.print("(°C), Gas:");
    Serial.print(dataG);
    Serial.print("(Ω)");
    Serial.print('\n');
  } // ends for() loop
}
