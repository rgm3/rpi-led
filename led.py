#!/usr/bin/env python3

# Common cathode RGB led.

from gpiozero import RGBLED
from time import sleep
import sys
import os

led = RGBLED(2, 3, 4, active_high=True)
delay = 1

led.red = 1  # full red
sleep(delay)
led.red = 0.5  # half red
sleep(delay)
led.color = (0, 1, 0)  # full green
sleep(delay)
led.color = (0, 0.5, 0) # half green
sleep(delay)
led.color = (0, 0, 1)  # full blue
sleep(delay)
led.color = (0, 0, 0.5) # half blue
sleep(delay)

led.color = (1, 0, 1)  # magenta
sleep(delay)
led.color = (1, 1, 0)  # yellow
sleep(delay)
led.color = (0, 1, 1)  # cyan
sleep(delay)
led.color = (1, 1, 1)  # white
sleep(delay)

led.off()

# slowly increase intensity of blue
for n in range(100):
    led.blue = n/100
    sleep(0.1)

led.off()

#sys.exit()
#exit()
#quit()
os._exit(0)
