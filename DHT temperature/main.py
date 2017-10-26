import dht
import machine
import time

d = dht.DHT22(machine.Pin(5))
while True:
    d.measure()
    print("Temp {0}".format(d.temperature()))
    print("Hum {0}".format(d.humidity()))
    time.sleep(1)
