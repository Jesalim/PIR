import machine
import time

# Set the PIR sensor input pin and the LED output pin
pir_pin = machine.Pin(15, machine.Pin.IN)
led_pin = machine.Pin(2, machine.Pin.OUT)

def motion_detected():
    return pir_pin.value()  # Read the value of the PIR sensor (HIGH if motion is detected, LOW otherwise)

try:
    while True:
        if motion_detected():
            print("Motion detected!")
            led_pin.value(1)  # Turn on the LED
        else:
            print("No motion detected.")
            led_pin.value(0)  # Turn off the LED
        time.sleep(0.5)  # Add a small delay to avoid rapid changes in LED state

except KeyboardInterrupt:
    led_pin.value(0)  # Turn off the LED before exiting on Ctrl+C
    print("\nMotion detection program stopped.")