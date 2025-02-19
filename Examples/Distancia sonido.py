from  gpiozero import DistanceSensor
from gpiozero import Buzzer
import time

buzzer = Buzzer(18)

distancesensor = DistanceSensor(echo = 12,trigger = 16, max_distance = 5)


while True:
    distance = distancesensor.distance * 100
    print('Distance:',distance,"cm")
    
    if distance <=50:
        buzzer.on()
    else:
        buzzer.off()
    time.sleep(0.1)  # Pequeña pausa para evitar rebotes