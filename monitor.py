import microbit # will auto connect
import pygame

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.mixer.init()

names = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
notes = []
for n in names:
    notes.append(pygame.mixer.Sound('sounds/%s.wav' % n))

FILENAME = "log.csv"
f = open(FILENAME, "a+")

playing = False
index = 0

while True:
    row = microbit.read()
    if row is not None:
        try:
            x,y,z = row.split(' ')
            x,y,z = int(x), int(y), int(z)

            x = x + 1024
            x = min(x, 2048) # 0..2048
            x = max(x, 0)
            #print(x)

            x = x / (2048/len(notes))
            x = min(x, len(notes)-1)
            notes[x].play()
            print(x)
            #if not playing and z < -510:
            #    notes[index].play()
            #    playing = True
            #elif playing and z >= -490:
            #    playing = False
            #    index = (index + 1) % len(notes)

            #print(x,y,z)
            f.write("%d,%d,%d\n" % (x,y,z))
            f.flush()
        except ValueError as e:
            print("Can't unpack:%s" % row)

