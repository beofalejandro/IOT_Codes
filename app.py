from flask import Flask as fk, render_template as rt, request as rq
from flask_socketio import SocketIO
from gpiozero import LED, Buzzer
import time
from time import strftime, sleep
from DFRobot_DHT20 import DFRobot_DHT20 as DFRobot

import random as rdm
import threading as threating

app = fk(__name__)
socketio = SocketIO(app)

I2C_BUS = 0x01  # default use I2C1 bus
I2C_ADDRESS = 0x38  # default I2C device address

dht20 = DFRobot(I2C_BUS, I2C_ADDRESS)


@app.route('/')
def index():

    return rt('index.html')


def generate_data():
    while True:
        if not dht20.begin():
            print("DHT20 sensor initialization failed")
        else:
            while True:
                print(strftime("%Y-%m-%d %H:%M:%S %Z"))
                T_celcius, humidity, crc_error = dht20.get_temperature_and_humidity()
        if crc_error:
            print("CRC               : Error\n")
        else:
            T_fahrenheit = T_celcius*9/5 + 32
            print("Temperature       : %f\u00b0C / %f\u00b0F" %(T_celcius, T_fahrenheit))
            print("Relative Humidity : %f %%" %humidity)
            print("CRC               : OK\n")
            sleep(5)  
        tdata = rdm.randint(1, 100)
        hdata = rdm.randint(1, 1000)
        socketio.emit('t_new_data', {'value':T_celcius})
        socketio.emit('h_new_data', {'value':humidity})
        time.sleep(5)

@app.route('/iraprueba')
def prueba():
    return rt('prueba.html')

if __name__ == '__main__':
    thread = threating.Thread(target=generate_data)
    thread.start()
    socketio.run(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)