# ## ################################################################
# blink.py
#
# Author:  Mauricio Matamoros
# License: MIT
#
# Blinking sentinel led in the ESP32 using timers
#
# ## ################################################################

from machine import Pin        # Board IO Pin
from machine import Timer      # Hardware timer
from utime import sleep_us

brightness = 99

def blink(timer):              # Callback function
    led.value(0) # turn off the led
    sleep_us(brightness) # 
    led.value(1) # turn on the led
#end def

led = Pin(4, Pin.OUT)          # Setup pin 4 (rgB LED) as output
                               
timer = Timer(0)               # Create the Timer object
timer.init(
    freq=10000,           	   # Timer frequency set to 10kHz for a 100us period
    mode=Timer.PERIODIC,       # Timer will run endlessly (not one-shot)
    callback=blink             # Set callback function: blink
)
