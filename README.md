# Piano Tiles Robot with ESP32 and OpenCV

## Introduction
This project aims to play Piano Tiles/Magic Tiles as fast as possible without any misses or errors. Using servo motors controlled by ESP32 and OpenCV, this robot can earn 3 crowns on almost every song. The project is also made as simple as possible, with a fairly low cost and a program that is not too complex.

## Demo Video 
[Piano Tiles Robot](https://youtube.com/shorts/shP5OKNPN6c)

## components
1. 1 x ESP32
2. 4 x Micro Servo SG90
3. Straw with aluminium foil at the tip (simulate touching the screen)
4. USB Module for external power
   
## Setup Instructions
1. Connect the ESP32 to the micro servos as shown in the schematic and external power for each servo.
2. Mirror the game to PC with SCRCPY, for the best performance I use video bitrate at 4M and no audio.
3. Install all dependencies on Python and ESP32.
4. Upload the C++ code to the ESP32.
5. Run the PianoBot.py and adjust the detector line to align with the start tile".
6. Use the spacebar to start detecting.
## Tips
Adjust the distance between the stylus and the reading on the detector line for each song, the faster the song the further the detector line reading should be from the tip of the stylus (the detector line is at the top of the tiles, and the stylus is at the bottom of the tiles)
## Schematic
![Schematic](https://github.com/user-attachments/assets/9922c74e-9062-49c5-8f4b-a234d7f9fdc5)

For best performance, external 5V 2A power is highly recommended for the servo.

## How it works
The robot uses the ESP32 to control four servo motors, each attached to a stylus made of straw with aluminium foil at the tip. OpenCV detects the piano tiles on the screen, and the ESP32 sends signals to the servos to tap the corresponding tiles.
![How](https://github.com/user-attachments/assets/91fe6a8d-5405-4543-b3ee-84a68f6f0b15)

## Pros
1. quite cheap under 100k rupiah (without esp32)
2. Minimum delay because everything uses cable
3. No sensor needed
4. Can handle long-hold tiles
5. Simple program
   
## Limitations
1. Cannot read the slide tiles (on Magic Tiles 3)
2. There will be a missed touch if it is too fast
3. Use too many USB Cable (serial communication, SCRCPY mirroring, servo power)

## The Robot
![image](https://github.com/user-attachments/assets/a7876236-d75f-4e4c-b040-42c6130d3de0)

