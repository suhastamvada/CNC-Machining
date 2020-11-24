import sys


# All numbers and dimensions are in mm
dia = 2.38125  # (tool diameter)
depth = 2  # (total depth)
DOC = 0.05  # Depth of cut
count = int(depth / DOC)


def move(m):
    print("X", "{:.2f}".format(m), sep='')


def downward(zm):
    print("Z", "{:.2f}".format(zm), sep='')


sys.stdout = open("line_cut.txt", "w")

print("G00 G49 G40.1 G17 G80 G50 G90")
print("G21")
print("M6 T1")
print("M03 S8556")
print("G00 Z2")
print("G01 Z-0.05 F100.0")
z = - DOC
d = 1
for i in range(1, count+1):
    move(d*(5-(dia/2)))
    d = -1*d
    move(d*(5-(dia/2)))
    d = -1*d
    move(d*(5-(dia/2)))
    z = z - DOC
    if i < count:
        downward(z)

print("M05 M09")
print("M30")

sys.stdout.close()
