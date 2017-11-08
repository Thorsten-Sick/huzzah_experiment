import machine
import neopixel
import time

np = neopixel.NeoPixel(machine.Pin(4), 1)
(r, g, b) = (0, 0, 0)
for r in range(0, 250):
    np[0] = (r, g, b)    # RGB value for first pixel
    np.write()    # Relevant or pixel will not change
    time.sleep_ms(250)
