#include <HardwareSerial.h>
#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo1;  
Servo servo2;  
Servo servo3;  
Servo servo4;  

void setup() {
  servo1.attach(14);  
  servo2.attach(13);  
  servo3.attach(12); 
  servo4.attach(11); 
  Serial.begin(115200); 
}

void loop() {
    if (Serial.available()) {
        String data = Serial.readStringUntil('\n');

        int index1 = data.indexOf(',');
        int index2 = data.indexOf(',', index1 + 1);
        int index3 = data.indexOf(',', index2 + 1);

        String A = data.substring(0, index1);
        String B = data.substring(index1 + 1, index2);
        String C = data.substring(index2 + 1, index3);
        String D = data.substring(index3 + 1);

        if (A.toInt() == 1) {
            servo1.write(15); //Servo Angle
        } else {
            servo1.write(5);
        }

        if (B.toInt() == 2) {
            servo2.write(15);
        } else {
            servo2.write(5);
        }

        if (C.toInt() == 3) {
            servo3.write(10);
        } else {
            servo3 .write(0);
        }

        if (D.toInt() == 4) {
            servo4.write(15);
        } else {
            servo4.write(5);
        }
    }
}
