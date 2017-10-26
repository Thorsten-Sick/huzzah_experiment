# huzzah_experiment

I got a Huzzah Feather board and a bunch of sensors that need to be tested. I also want to test-drive Micro Python

(https://learn.adafruit.com/adafruit-feather-huzzah-esp8266)

Pinout: https://learn.adafruit.com/assets/46249

## Serial connection

```
screen /dev/tty.board_name 115200
```

Running a script on the ESP8266 and doing a "print" will directly write to serial


## Package: Huzzah starter kit
https://www.adafruit.com/product/2680

### Micro servo
https://www.adafru.it/169

### Door sensor

### PIR Sensor
https://www.adafruit.com/product/189

### Humidity/temperature sensor (DHT22 AM2302)

The DHT has an own driver.

### Fast Vibration Sensor Switch
https://www.adafru.it/1766

### Piezo Buzzer

### Photo cell light sensors

### 10k Trim Potentiometer

### LEDs

## Micro Python
### First Flash

https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/esp8266

#### Install tools
```
sudo pip install esptool
sudo pip install --upgrade esptool
sudo pip3 install adafruit-ampy
```

ampy for put command, esptool for flashing (https://github.com/adafruit/ampy)

#### Get firmware
https://micropython.org/download/#esp8266

#### Flashing
Erase:
```esptool.py --port /path/to/ESP8266 erase_flash```

Install:
```
esptool.py --port /path/to/ESP8266 --baud 460800 write_flash --flash_size=detect 0 firmware.bin
```
### Update program

### Micro Python
Tutorial:
http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/index.html

Reference:
http://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html

A serial connection and "REPL" is directly available after install.


#### Code files

First boot.py is executed after boot. Then main.py

To edit files, ampy can be used. Pre-set the port with
```
export AMPY_PORT=/dev/tty.SLAB_USBtoUART
```
to simplify the process.
