#!/usr/bin/env python3

# Common cathode RGB led.

import argparse
from gpiozero import RGBLED
from gpiozero.pins.pigpiod import PiGPIOPin
from signal import pause
import gpiozero.devices

#parser = argparse.ArgumentParser(description = 'Light up the world!')
#parser.add_argument('rgb', metavar='0-255', type=int, nargs=3,
#                   help='Red, Green, and Blue color values (0-255).')
#args = parser.parse_args()

gpiozero.devices.pin_factory = PiGPIOPin

from time import sleep
import sys
import os

led = RGBLED(2,3,4)


# Input a value 0 to 255 to get a color value.
def Wheel(position):
  if position < 85:
    setColor(position * 3, 255 - position * 3, 0)
  elif position < 170:
    position -= 85;
    setColor(255 - position * 3, 0, position * 3)
  else:
    position -= 170;
    setColor(0, position * 3, 255 - position * 3)


def setColor(red, green, blue):
    # Convert 0-255 range to 0-1.
    led.color = (red/255.0, green/255.0, blue/255.0)


try:
  i = 0
  while True:
    Wheel(i)
    i += 1
    if i > 255:
      i = 0
    sleep(0.05)
except KeyboardInterrupt:
  pass


led.off()


#sys.exit()
#exit()
#quit()
os._exit(0)
