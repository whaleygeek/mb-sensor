import microbit # will auto connect

FILENAME = "log.csv"
f = open(FILENAME, "a+")

while True:
    row = microbit.read()
    if row is not None:
        try:
            x,y,z = row.split(' ')
            x,y,z = int(x), int(y), int(z)
            print(x,y,z)
            f.write("%d,%d,%d\n" % (x,y,z))
            f.flush()
        except ValueError as e:
            print("Can't unpack:%s" % row)

