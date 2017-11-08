from machine import Pin,I2C
import ssd1306
import time

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
lcd = ssd1306.SSD1306_I2C(128, 64, i2c)
lcd.text("Micropython", 0, 0)
lcd.show()
time.sleep(1)

# scroll  (x,y) # scroll the framebuffer
# fill_rect
# vline
# rect
# hline
# text
# line
# pixel
# fill
