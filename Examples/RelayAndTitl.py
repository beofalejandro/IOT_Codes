from gpiozero import DigitalInputDevice as Tilt
from gpiozero import OutputDevice as Relay
import time

relay = Relay(21)
tilt_sensor = Tilt(22)

while True:
	if tilt_sensor.value:
		relay.on()
	else:
		relay.off()
	time.sleep(1)
