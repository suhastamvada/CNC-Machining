import Slot_square as Sq
import sys


depth = 10
DOC = 0.2
count = int(depth / DOC)
dia = 3.175
xl = 20
yl = 20

sys.stdout = open("Sq_trench.txt", "w")

print("G00 G49 G40.1 G17 G80 G50 G90")
print("G21")
print("M6 T1")
print("M03 S8556")
print("G00 Z2")
print("G01 Z-0.1 F150.0")
z = -0.1
h, v = 1, 1

for j in range(1, count + 1):
    x, y = 0, 0
    Sq.horizontal(xl - dia)
    Sq.vertical(yl - dia)
    Sq.horizontal(0)
    Sq.vertical(0)
    if j < count:
        print("Z", "{:.2f}".format(z - j * DOC), sep='')

print("M05 M09")
print("M30")

sys.stdout.close()
