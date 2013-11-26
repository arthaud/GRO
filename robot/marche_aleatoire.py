#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from nxt.locator import find_one_brick
from nxt.motor import Motor, PORT_A, PORT_B, PORT_C
from nxt.sensor import Touch, Ultrasonic, PORT_1, PORT_2, PORT_3, PORT_4
from time import sleep

def main(robot):
    # Définition des moteurs / capteurs
    m_left = Motor(robot, PORT_B)
    m_right = Motor(robot, PORT_A)

    touch_right = Touch(robot, PORT_2)
    touch_left = Touch(robot, PORT_1)
    ultrason = Ultrasonic(robot, PORT_3)

    DEFAULT_POWER = 80
    DISTANCE_LIMIT = 20
    TURN_TIME = 1.5

    # Début
    while True:
        m_left.run(power=DEFAULT_POWER)
        m_right.run(power=DEFAULT_POWER)

        while not touch_right.is_pressed() and not touch_left.is_pressed() and ultrason.get_distance() > DISTANCE_LIMIT:
            sleep(0.01)

        print("Aieee")
        if touch_right.is_pressed():
            m_left.run(power=DEFAULT_POWER)
            m_left.run(power=-DEFAULT_POWER)
        else:
            m_left.run(power=-DEFAULT_POWER)
            m_left.run(power=DEFAULT_POWER)

        sleep(TURN_TIME)

main(find_one_brick())
