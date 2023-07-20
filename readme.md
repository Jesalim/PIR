# Raspberry Pi Pico PIR Motion Sensor Detection
This README provides an overview of the code used to interface a PIR (Passive Infrared) motion sensor with a Raspberry Pi Pico to detect motion. The PIR motion sensor detects changes in infrared radiation emitted by living beings, enabling us to detect movement in its vicinity.

## Hardware Requirements:
Raspberry Pi Pico
PIR Motion Sensor
Jumper wires
Breadboard (optional)
Wiring Instructions:
Connect the PIR motion sensor to the Raspberry Pi Pico as follows:

PIR VCC to Pico 3.3V (3V3)
PIR GND to Pico GND (GND)
PIR OUT to Pico GPIO pin (e.g., GPIO 5)
Ensure that you connect the PIR motion sensor's output pin to an appropriate GPIO pin on the Raspberry Pi Pico.


## Running the Code:
Ensure the hardware connections are made correctly as per the wiring instructions.
Copy the provided code into your Python editor (e.g., Thonny or VSCode).
Save the file as pir_motion_sensor.py and transfer it to the Raspberry Pi Pico.
Run the code on the Pico, and it will start detecting motion using the PIR sensor and display the status on the console.
Remember that the PIR motion sensor is sensitive to changes in infrared radiation, so it may detect other sources of infrared emission, such as heaters or sunlight changes. Therefore, it is essential to consider the sensor's placement and adjust sensitivity settings if available, depending on your specific application needs. Enjoy experimenting with your PIR motion sensor project!






