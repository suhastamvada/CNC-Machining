import sys


def horizontal(xm):
    print("X", "{:.2f}".format(xm), sep='')


def vertical(ym):
    print("Y", "{:.2f}".format(ym), sep='')


depth = 50
DOC = 0.1
count = int(depth / DOC)
dia = 3.175
xl = 20
yl = 20

sys.stdout = open("PTFE_slot.txt", "w")

print("G00 G49 G40.1 G17 G80 G50 G90")
print("G21")
print("M6 T1")
print("M03 S8556")
print("G00 Z2")
print("G01 Z-0.05 F100.0")
z = -0.05
h, v = 1, 1

for j in range(1, count+1):
    x, y = 0, 0
    for i in range(1, 6):
        horizontal(i * dia * h)
        if i < 5:
            vertical(i * dia * v)
        x = i * dia
        y = i * dia
        h = h * (-1)
        v = v * (-1)

    horizontal(x + 2.0625)
    vertical(y + 2.0625)
    x = x + 2.0625
    y = y + 2.0625
    horizontal(-1 * (x + 2 * 2.0625))
    vertical(-1 * (y + 2 * 2.0625))
    horizontal(x)
    vertical(0)
    horizontal(0)
    print("Z", "{:.2f}".format(z-j*DOC), sep='')

print("M05 M09")
print("M30")

sys.stdout.close()
