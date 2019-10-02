#include <SimpleMessageSystem.h>


const int Stickx = 34;      // select the pin for the LED
const int Sticky = 35;
const int Butt = 13;
const int Switch = 27;

int valx = 0;  // variable to store the value coming from the sensor
int valy = 0;
int valButt = 0;
int valSwitch = 0;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  delay(1000);

}

void loop() {
  // put your main code here, to run repeatedly:
  valx = analogRead(Stickx);
  valy = analogRead(Sticky);
  valButt = digitalRead(Butt);
  valSwitch= digitalRead(Switch);
  
  messageSendInt(valx);
  messageSendInt(valy);
  messageSendInt(valButt);
  messageSendInt(valSwitch);
  messageEnd();
  delay(132);

}
