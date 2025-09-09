## Arduino SLAM

This folder contains the Arduino code for the SLAM project.

### Hardware

*   Arduino UNO
*   Ultrasonic Sensor (HC-SR04)
*   Servo Motor (SG90)
*   Breadboard and jumper wires

### Circuit

*   **Servo Motor:**
    *   VCC -> 5V
    *   GND -> GND
    *   Signal -> Pin 9
*   **Ultrasonic Sensor:**
    *   VCC -> 5V
    *   GND -> GND
    *   Trig -> Pin 10
    *   Echo -> Pin 11

### Software

*   [Arduino IDE](https://www.arduino.cc/en/software)
*   [Processing](https://processing.org/download)

### Instructions

1.  Connect the hardware as described above.
2.  Open the `arduino.ino` file in the Arduino IDE.
3.  Select your board and port, and upload the sketch.
4.  Open the Processing sketch in the `processing` folder.
5.  Run the Processing sketch to visualize the data.
