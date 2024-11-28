#include "Arduino.h"
#include "Arduino_BHY2.h"

void setup(){
  // Connect to attached chip via ESLOV cable
  BHY2.begin(NICLA_I2C, NICLA_VIA_ESLOV);
}

void loop(){
  // Update and then sleep
  BHY2.update(1);
}