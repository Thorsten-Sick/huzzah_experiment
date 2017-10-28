from machine import Pin, PWM
import time

print("Starting")
servo = PWM(Pin(5), freq=50)

while True:
    servo.duty(30)
    time.sleep(1)
    servo.duty(60)
    time.sleep(1)
    servo.duty(90)
    time.sleep(1)
    servo.duty(130)
    time.sleep(1)
