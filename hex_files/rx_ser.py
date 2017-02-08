from microbit import *
import radio

radio.config(length=32, queue=3, channel=7, power=6, address=0x75626974, group=0, data_rate=radio.RATE_2MBIT)
radio.on()
print("running")


def run():
    while True:
        msg = radio.receive()
        if msg is not None:
            display.set_pixel(2,2,9)
            print(msg)
            display.clear()

run()
