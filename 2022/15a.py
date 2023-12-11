from sys import argv
import re

def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

with open(argv[1], "r") as file:
    ly = 2000000
    lx = set()
    mlx = set()
    for line in file:
        sx, sy, bx, by = list(map(int, re.findall(r'-?\d+', line)))
        if by == ly:
            mlx.add(bx)
        closestD = dist(sx, sy, bx, by)
        lineD = dist(sx, sy, sx, ly)
        if lineD <= closestD:
            for dx in range(closestD - lineD + 1):
                lx.add(sx + dx)
                lx.add(sx - dx)
    lx.difference_update(mlx)
    print(len(lx))
