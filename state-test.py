#!/usr/bin/env python3

import gpiozero
from gpiozero.pins.pigpiod import PiGPIOPin
from datetime import timedelta
import time

with open('/proc/uptime','r') as f:
    uptime_seconds = float(f.readline().split()[0])



led = gpiozero.LED(PiGPIOPin(2))


assert not led.is_lit

led.on()
assert led.is_lit

input("Led is lit. Press Enter to turn off and quit.")
led.off()
time.sleep(2)

# led turns back on as initial GPIO state is restored
