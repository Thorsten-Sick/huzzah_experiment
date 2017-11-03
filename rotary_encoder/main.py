from rencoder import Encoder
import machine
import time

p4 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
p5 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
e = Encoder(p4, p5, max=4*12)

while True:
    time.sleep_ms(250)
    print(e.position)
