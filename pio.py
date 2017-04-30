#!/usr/bin/python
# -*- coding: utf-8 -*-

import pigpio

pi = pigpio.pi()

pi.set_mode(2, pigpio.OUTPUT)
pi.set_mode(3, pigpio.OUTPUT)
pi.set_mode(4, pigpio.OUTPUT)

pi.write(2, 0)
pi.write(3, 0)
pi.write(4, 0)

pi.stop()

