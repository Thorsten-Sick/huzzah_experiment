from machine import Pin
import time

print("Starting")
# Using internal pull upp we do not neet a resistor
# Connect other side of the button to ground
p5 = Pin(5, Pin.IN, Pin.PULL_UP)
p4 = Pin(4, Pin.OUT)
while True:
    print(p5.value())  # Will be 0 when pressed
    p4.value(p5.value())
    time.sleep(1)
