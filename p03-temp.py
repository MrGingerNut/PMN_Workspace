# ## ################################################################
# blink.py
#
# Author:  Mauricio Matamoros
# License: MIT
#
# Reads the temperature of the ESP32 in Farenheit
#
# ## ################################################################

import esp32                        # Processor special functions
from utime import sleep_ms          # Delay function in milliseconds

def main():                         # Main function
    while(True):                    # Repeat forever
        temp_fahr = esp32.raw_temperature() # Read temperature, in °F
        temp_cels = 5 / 9 * (temp_fahr - 32) # convert temperature to °C
        print(f'Temperature in fahrenheit: {temp_fahr}°F')       # Print temperature
        print(f"Temperature in celcius: {temp_cels}°C\n") # print celsius temp
        sleep_ms(1000)              # Wait for 1000ms
#end def

if __name__ == '__main__':
    main()
