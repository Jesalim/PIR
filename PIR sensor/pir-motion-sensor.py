import machine

# Define PIR sensor pin
pir_pin = machine.Pin(15, machine.Pin.IN)

# Define LED pin
led_pin = machine.Pin(25, machine.Pin.OUT)

while True:
    # Read PIR sensor input
    pir_value = pir_pin.value()

    if pir_value == 1:
        # PIR sensor detected motion
        led_pin.on()
    else:
        # No motion detected
        led_pin.off()