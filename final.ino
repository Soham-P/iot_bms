#include <math.h>
#include <Wire.h>
#include "rgb_lcd.h"

const int SENSOR_PIN = A0;  // Input pin for measuring Vout
const int RS = 10;          // Shunt resistor value (in ohms)
const int VOLTAGE_REF = 5;  // Reference voltage for analog read
float sensorValue;          // Variable to store value from analog read
float current;              // Calculated current value
float new_current;
float integral_current = 0;
const int B = 4275;         // B value of the thermistor
const int R0 = 100000;      // R0 = 100k
int analogInput = A2;
float vout = 0.0;
float vin = 0.0;
float R1 = 30000.0; //  
float R2 = 7500.0; // 
int value = 0;

rgb_lcd lcd;

int colorR = 255;
int colorG = 255;
int colorB = 255;


void setup() {

  // Initialize serial monitor
  Serial.begin(9600);
  pinMode(analogInput, INPUT);
  lcd.begin(16, 2);
  lcd.setRGB(colorR, colorG, colorB);

}
void loop() {
  lcd.setRGB(colorR, colorG, colorB);
  colorR = random(0, 255);
  colorG = random(0, 255);
  colorB = random(0, 255);
  int a = analogRead(A1);
  float R = 1023.0/a-1.0;
  R = R0*R;
  float temperature = 1.0/(log(R/R0)/B+1/298.15)-273.15; // convert to temperature via datasheet
  value = analogRead(analogInput);
  vout = (value * 5.0) / 1023.0; // see text
  vin = vout / (R2/(R1+R2)); 
  
  
  sensorValue = analogRead(SENSOR_PIN);
  sensorValue = (sensorValue * VOLTAGE_REF) / 1023; //assume 10k for load resistor
  current = sensorValue / (10 * RS);
  
  Serial.println(temperature);
  Serial.println(current, 3);
  Serial.println(vin,4); // voltage
  if (Serial.available()) 
    {
        // wait a bit for the entire message to arrive
        delay(100);
        // clear the screen
        lcd.clear();
        // read all the available characters
        while (Serial.available() > 0) 
        {
            // display each character to the LCD
            lcd.write(Serial.read());
        }
    }
  delay(5000);
}

