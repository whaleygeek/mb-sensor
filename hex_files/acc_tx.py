from microbit import *
import radio

radio.config(length=32, queue=3, channel=7, power=6, address=0x75626974, group=0, data_rate=radio.RATE_2MBIT)
radio.on()
print("running")

addr = 0

def config():
    a = 0
    display.show('?')
    while True:
        if button_a.was_pressed():
            a = (a + 1) % 10
            display.show(str(a))

        elif button_b.was_pressed():
            display.clear()
            return a

        else:
            sleep(100)

def run():
    seq = 0
    while True:
        if button_a.is_pressed():
            display.clear()
            x,y,z = accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
            x,y,z = str(x), str(y), str(z)
            msg = "%s,%s,%s,%s,%s" % (addr,seq,x,y,z)
            seq = (seq + 1) % 65536
            #print(msg)
            display.set_pixel(2,2,9)
            radio.send(msg)
            #sleep(500)

addr = config()
run()