from gpiozero import DigitalInputDevice as MOTION
from gpiozero import LED
import time

led = LED(26)
motion = MOTION(23)

while True:
   if(motion.value == 0):
		led.off()
   elif(motion.value == 1):
		led.on()
	time.sleep(0.1)
