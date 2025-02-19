from  gpiozero import DistanceSensor, Servo
import time

servo = Servo(25)

distancesensor = DistanceSensor(echo = 12,trigger = 16, max_distance = 5)


while True:
    distance = distancesensor.distance * 100
    print('Distance:',distance,"cm")
    
    if distance <=50:
        servo.max()
    else:
        servo.min()
    time.sleep(0.1)  # Pequeña pausa para evitar rebotes
