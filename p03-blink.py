# ## ################################################################
# blink.py
#
# Author:  Mauricio Matamoros
# License: MIT
#
# Blinking sentinel led in the ESP32 using delays
#
# ## ################################################################

from machine import Pin        # Board IO Pin
from utime import sleep_ms     # Delay in milliseconds

led = Pin(4, Pin.OUT)          # Setup pin 4 (rgB LED) as output
                               # Use pin 2 for ESP32 DevKit DoIt

while(True):                   # Repeat forever
    led.value(not led.value()) # Toggle the led
    sleep_ms(500)              # Wait for 500ms
