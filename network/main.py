import network
import secrets  # On the device secrets will also be in the main folder,
# from .. import secrets for same directory structure

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(secrets.SSID, secrets.WIFIPWD)
while True:
    print(sta_if.isconnected())
    print(sta_if.ifconfig())
