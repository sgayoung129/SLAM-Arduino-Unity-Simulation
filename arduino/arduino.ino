
#include <Servo.h>

#define SERVO_PIN 9
#define TRIG_PIN 10
#define ECHO_PIN 11

Servo servo;

void setup() {
  Serial.begin(9600);
  servo.attach(SERVO_PIN);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  for (int angle = 0; angle <= 180; angle++) {
    servo.write(angle);
    delay(30);
    long duration, distance;
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);
    duration = pulseIn(ECHO_PIN, HIGH);
    distance = (duration / 2) / 29.1;
    Serial.print(angle);
    Serial.print(",");
    Serial.println(distance);
  }
  for (int angle = 180; angle >= 0; angle--) {
    servo.write(angle);
    delay(30);
    long duration, distance;
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);
    duration = pulseIn(ECHO_PIN, HIGH);
    distance = (duration / 2) / 29.1;
    Serial.print(angle);
    Serial.print(",");
    Serial.println(distance);
  }
}
