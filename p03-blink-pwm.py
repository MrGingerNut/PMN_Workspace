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
from machine import PWM # pwm magic 

pwm_percent = 100
pwm_value = int(65536 - 65536 * pwm_percent / 100)

led = Pin(4, Pin.OUT)          # Setup pin 4 (rgB LED) as output
                               
pwm = PWM(led, freq=1000, duty_u16=pwm_value) # create a pmw object on led, set freq to 1khz and duty to the calculated uint16 value

