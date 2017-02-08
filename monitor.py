import microbit # will auto connect
import pygame

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.mixer.init()

A = pygame.mixer.Sound("sounds/A.wav")


FILENAME = "log.csv"
f = open(FILENAME, "a+")

playing = False

while True:
    row = microbit.read()
    if row is not None:
        try:
            x,y,z = row.split(' ')
            x,y,z = int(x), int(y), int(z)
            if not playing and z < -510:
                A.play()
                playing = True
            elif playing and z >= -490:
                playing = False

            print(x,y,z)
            f.write("%d,%d,%d\n" % (x,y,z))
            f.flush()
        except ValueError as e:
            print("Can't unpack:%s" % row)

