from microbit import *
import radio

radio.config(length=32, queue=3, channel=7, power=6, address=0x75626974, group=0, data_rate=radio.RATE_2MBIT)
radio.on()
print("running")

def run():
    while True:
        display.clear()
        x,y,z = accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
        x,y,z = str(x), str(y), str(z)
        msg = "%s,%s,%s" % (x,y,z)
        #print(msg)
        display.set_pixel(2,2,9)
        radio.send(msg)
        #sleep(500)

run()