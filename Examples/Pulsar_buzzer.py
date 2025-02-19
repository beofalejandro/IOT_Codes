#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

from gpiozero import DigitalInputDevice as Touch
import time
from gpiozero import Buzzer

# define touch pin
touch_sensor = Touch(17)
buzzer = Buzzer(18)

while True:
    # check if touch detected
    if touch_sensor.value :
        print('Touch Detected')
        buzzer.on()
    else:
        buzzer.off()
    time.sleep(0.1)  # Pequeña pausa para evitar rebotes
