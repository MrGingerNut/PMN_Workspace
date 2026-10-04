# ## ################################################################
# blink.py
#
# Author:  Mauricio Matamoros
# License: MIT
#
# Blinking sentinel led in the Raspberry Pi Pico using timers
#
# ## ################################################################

from machine import Pin     # Board IO Pin
from machine import Timer   # Hardware timer
from utime import sleep_ms

brightness = 10

def blink(timer):           # Callback function
    led.toggle()            # Toggle the led
    sleep_ms(brightness)				# wait 1ms, led on during 10%
    led.toggle()			# led off during the rest of the time
#end def

led = Pin(25, Pin.OUT)      # Setup pin 25 (sentinel LED) as output
timer = Timer()             # Create the Timer object
timer.init(
    freq=100, 		        # Timer frequency set to 100Hz, period 10ms
    mode=Timer.PERIODIC,    # Timer will run endlessly (not one-shot)
    callback=blink          # Set callback function: blink
)
