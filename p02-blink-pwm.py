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

counter = 0
pwmfreq = 100
pwmValue = 90

timefreq = pwmfreq * 100

def blink(timer):           # Callback function
    global counter
    if(counter < pwmValue):
        led.value(1)
    else:
        led.value(0)
    counter += 1
    if(counter >= 100):
        counter = 0
#end def

led = Pin(25, Pin.OUT)      # Setup pin 25 (sentinel LED) as output
timer = Timer()             # Create the Timer object
timer.init(
    freq=timefreq, 		        # Timer frequency set to 100Hz, period 10ms
    mode=Timer.PERIODIC,    # Timer will run endlessly (not one-shot)
    callback=blink          # Set callback function: blink
)


    