from flask import Flask as fk, render_template as rt, request as rq
from gpiozero import LED, Buzzer

from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import time
import threading

app = fk(__name__)
socketio = SocketIO(app)

#import HD44780MCP
#import time
#import MCP230XX

#led = LED(14)
#buzzer = Buzzer(18)
#i2cAddr = 0x21
#MCP = MCP230XX.MCP230XX('MCP23008', i2cAddr)

#blPin = 7
#MCP.set_mode(blPin, 'output')
#MCP.output(blPin, True)

#LCD = HD44780MCP.HD44780(
#    MCP, 1, -1, 2, [3, 4, 5, 6], rows=2, characters=16, mode=0, font=0)
#led_state = False
#buzzer_state = False


@app.route('/')
def index():
#    global led_state, buzzer_state
#    if led_state:
#        LCD.clear_display()
#        LCD.display_string("LED: Ensendido")
#    else:
#        LCD.clear_display()
#        LCD.display_string("LED: Apagado")

#   LCD.set_cursor(2, 1)

#    if buzzer_state:
#        LCD.display_string("Buzzer:Encendido")
#    else:
#        LCD.display_string("Buzzer:Apagado")

    return rt('index.html')

def generate_data():
    while True:
        # Genera datos aleatorios
        tdata = random.randint(1, 100)
        hdata = random.randint(1, 1000)
        socketio.emit('t_new_data', {'value':tdata})
        socketio.emit('h_new_data', {'value':hdata})
        time.sleep(5)


@app.route('/iraprueba')
def prueba():
    return rt('prueba.html')


if __name__ == '__main__':
    thread = threading.Thread(target=generate_data)
    thread.start()
    socketio.run(app)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)  