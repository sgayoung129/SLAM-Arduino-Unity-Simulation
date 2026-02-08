#include <Servo.h>

#define TRIG 9
#define ECHO 10

Servo myServo;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  
  myServo.attach(3); // 서보 신호선 D3
}

long getDistance() {
  long duration;
  float distance;

  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  duration = pulseIn(ECHO, HIGH);
  distance = duration * 0.034 / 2;

  return distance;
}

void loop() {

  for(int angle = 30; angle <= 150; angle += 5) {
    myServo.write(angle);
    delay(200);

    long d = getDistance();
    Serial.print(angle);
    Serial.print(",");
    Serial.println(d);
  }

  for(int angle = 150; angle >= 30; angle -= 5) {
    myServo.write(angle);
    delay(200);

    long d = getDistance();
    Serial.print(angle);
    Serial.print(",");
    Serial.println(d);
  }
}
