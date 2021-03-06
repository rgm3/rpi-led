#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Raspberry Pi networked LED rainbow."""

from time import sleep
from gpiozero import RGBLED
from gpiozero.pins.pigpiod import PiGPIOPin
import gpiozero.devices

gpiozero.devices.pin_factory = PiGPIOPin

def cluster_led(hostname):
    """Return an RGB LED object for the given host"""
    return RGBLED(
        PiGPIOPin(2, host=hostname),
        PiGPIOPin(3, host=hostname),
        PiGPIOPin(4, host=hostname))

LED1 = cluster_led('localhost')
LED2 = cluster_led('piceph2')
LED3 = cluster_led('piceph3')
LED4 = cluster_led('piceph4')

LEDS = [LED1, LED2, LED3, LED4]

DELAY = 0.02 # time to sleep between color steps


def wheel(position):
    """ Input a value 0 to 255 to get a gpiozero color tuple with values 0 - 1."""
    if position < 0 or position > 255:
        if position >= -255: position = 255 + position
        else: position %= 255
    if position < 85:
        rgb = (position * 3, 255 - position * 3, 0)
    elif position < 170:
        position -= 85
        rgb = (255 - position * 3, 0, position * 3)
    else:
        position -= 170
        rgb = (0, position * 3, 255 - position * 3)

    return tuple([x/255.0 for x in rgb])


def main():
    """Rainbow wheel on all LEDs."""
    try:
        while True:
            for pos in range(0, 255, 8):
                for idx, led in enumerate(LEDS):
                    led.color = wheel(pos - (idx * 16))
                    sleep(DELAY)
    except KeyboardInterrupt:
        pass

    for led in LEDS:
        led.off()


if __name__ == '__main__':
    main()

# vim: sw=4 ts=4 expandtab
