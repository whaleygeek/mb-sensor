import microbit # will auto connect
import time

#RED = (255,0,0)
#GREEN = (0,255,0)
#BLACK = (0,0,0)
#WIDTH = 10
#RATE = 0.05

#pygame.init()
#surface = pygame.display.set_mode((1024, 512))


FILENAME = "log.csv"
f = open(FILENAME, "a+")

#playing = False
#index = 0

#next_update = time.time() + RATE

def analyse_acc():
    while True:
        row = microbit.read()
        if row is not None:
            try:
                a,s,x,y,z,t = row.split(',')
                a,s,x,y,z,t = int(a), int(s), int(x), int(y), int(z), int(t)

                #x += 1024
                #x = min(x, 2048) # 0..2048
                #x = max(x, 0)
                #x /= 2

                #y += 1024
                #y = min(y, 2048)
                #y = max(y, 0)
                #y /= 4

                #x = x / (2048/len(notes))
                #x = min(x, len(notes)-1)
                #notes[x].play()
                #print(x)
                #if not playing and z < -510:
                #    notes[index].play()
                #    playing = True
                #elif playing and z >= -490:
                #    playing = False
                #    index = (index + 1) % len(note)

                print(a,s,x,y,z,t)
                f.write("%d,%d,%d,%d,%d,%d\n" % (a,s,x,y,z,t))
                f.flush()

                #now = time.time()
                #if now > next_update:
                #    next_update = now + RATE
                #    #surface.fill(BLACK)
                #    pygame.draw.rect(surface, GREEN, (x, y, WIDTH, WIDTH))
                #    pygame.display.update()

            except ValueError as e:
                print("Can't unpack:%s" % row)

def sky_test():
    import pygame
    pygame.mixer.pre_init(22050, -16, 2, 1024)
    pygame.mixer.init()

    names = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    notes = []
    for n in names:
        notes.append(pygame.mixer.Sound('sounds/%s.wav' % n))
    #jump = pygame.mixer.Sound('sounds/jump.wav')
    while True:
        data = microbit.read()
        if data is not None:
            print(data)
            notes[0].play()

if __name__ == "__main__":
    sky_test()

