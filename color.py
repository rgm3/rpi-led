#!/usr/bin/env python3

# Common cathode RGB led.

import argparse
from gpiozero import RGBLED
from gpiozero.pins.pigpiod import PiGPIOPin
from signal import pause
import gpiozero.devices

parser = argparse.ArgumentParser(description = 'Light up the world!')
parser.add_argument('rgb', metavar='0-255', type=int, nargs=3,
                   help='Red, Green, and Blue color values (0-255).')
args = parser.parse_args()

gpiozero.devices.pin_factory = PiGPIOPin

from time import sleep
import sys
import os

led = RGBLED(2,3,4)

# Set a color by giving R, G, and B values of 0-255.
def setColor(rgb = []):
    # Convert 0-255 range to 0-1.
    rgb = [(x / 255.0) for x in rgb]
    led.color = (rgb[0], rgb[1], rgb[2])


setColor(args.rgb)

try:
  pause()
except KeyboardInterrupt:
  pass

led.off()


#sys.exit()
#exit()
#quit()
os._exit(0)
