from microbit import *
import radio

radio.config(length=32, queue=3, channel=7, power=6, address=0x75626974, group=0, data_rate=radio.RATE_2MBIT)
radio.on()
print("running")

UPDATE_RATE_MS = 1000

def run():
    next_clear = running_time() + UPDATE_RATE_MS
    while True:
        try:
            now = running_time()
            if now > next_clear:
                display.clear()
                next_clear = now + UPDATE_RATE_MS

            msg = radio.receive()
            if msg is not None:
                print("%s,%d" % (msg,now))
                try:
                    parts = msg.split(',')
                    a = int(parts[0])
                    x = int(a % 5)
                    y = int(a / 5)
                    display.set_pixel(x,y,9)
                except:
                    pass
                    
        except ValueError as e:
            # received packet is not a string? (collision corruption)
            #display.show('X')
            # radio hangs on collision error, so reset it
            radio.off()
            radio.on()

run()
