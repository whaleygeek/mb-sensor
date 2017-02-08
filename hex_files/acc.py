from microbit import *

def run():
    while True:
        print(accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z())
        sleep(100)

run()
