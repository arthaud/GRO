#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from nxt.locator import find_one_brick
from nxt.motor import Motor, PORT_A, PORT_B, PORT_C

robot = find_one_brick()

for port in (PORT_A, PORT_B, PORT_C):
    try:
        Motor(robot, port).brake()
    except:
        pass
