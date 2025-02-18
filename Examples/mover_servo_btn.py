from gpiozero import Servo, Button
import time

servo = Servo(25)
button = Button(19)  # Cambia 19 por el número de GPIO correcto

current_angle = 0
step = 10

def move_servo():
    global current_angle
    if current_angle < 180:
        current_angle += step
    else:
        current_angle = 0  # Reiniciar cuando llegue a 180°

    position = (current_angle / 180.0) * 2 - 1  # Convertir a rango -1 a 1
    servo.value = position
    print(f"Ángulo: {current_angle}°")
    time.sleep(0.2)  # Antirrebote

button.when_pressed = move_servo

while True:
    time.sleep(0.1)

