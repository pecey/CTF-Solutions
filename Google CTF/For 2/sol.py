#!/usr/bin/python

import sys
import matplotlib.pyplot as plt
plt.xlim(-1000, 1000)
plt.ylim(-500, 500)

filename = "coordinates.txt"

def compliment(h):
    i = int(h, 16)
    return i - ((0x80 & i) << 1)

def main():
    tx = 0
    ty = 0
    i = 0
    x= []
    y = []

    for line in open(filename).readlines():
        if len(line) > 1:
            status, dx, dy, junk = line.split(":")
            tx += compliment(dx)
            ty += compliment(dy)
            if status != "00":
                i = i+1
                x.append(tx)
                y.append(ty)
                print "%02d: %d %d" % (i, tx, ty)

    plt.plot(x,y,marker=".")
    plt.show()

main()