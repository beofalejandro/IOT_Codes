#!/usr/bin/env python3
import time
import HD44780MCP
import MCP230XX
from gpiozero import DistanceSensor, Buzzer  # Corregido: "Afrom" a "from"

# Variable global para la distancia
global_distance = 0.0

buzzer = Buzzer(18)

# Inicializar MCP
i2cAddr = 0x21  # Dirección i2c para MCP23008/17
MCP = MCP230XX.MCP230XX('MCP23008', i2cAddr)
# MCP = MCP230XX.MCP230XX('MCP23017', i2cAddr)

# Encender el backlight (para el Adafruit LCD backpack que usa MCP23008)
blPin = 7  # Pin del backlight
MCP.set_mode(blPin, 'output')
MCP.output(blPin, True)  # Enciende el backlight

# Configurar el LCD de 16x2 sin pin RW, en modo 4 bits
LCD = HD44780MCP.HD44780(MCP, 1, -1, 2, [3,4,5,6], rows=2, characters=16, mode=0, font=0)

# Inicializar sensor de distancia
distance_sensor = DistanceSensor(echo=12, trigger=16, max_distance=5)

def update_distance():
    global global_distance
    # Se obtiene la distancia en metros y se convierte a centímetros
    global_distance = distance_sensor.distance * 100

while True:
    update_distance()
    print('Distance:', global_distance, "cm")
    
    # Activar buzzer si la distancia es menor o igual a 50 cm, y desactivarlo en caso contrario
    if global_distance <= 50:
        buzzer.on()
    else:
        buzzer.off()
    
    time.sleep(0.1)  # Pequeña pausa para evitar activaciones muy rápidas
    
    # Mostrar la distancia en el LCD
    LCD.clear_display()
    LCD.display_string("Distance:")
    LCD.set_cursor(2, 1)  # Mueve el cursor a la 2ª fila, 1ª posición
    LCD.display_string(f"{global_distance:.1f} cm")  # Muestra la distancia formateada con 1 decimal
    time.sleep(1)
