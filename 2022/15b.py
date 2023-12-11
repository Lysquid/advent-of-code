from sys import argv
import re

def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

with open(argv[1], "r") as file:
    pairs = []
    m = 4000000
    for line in file:
        pairs.append(list(map(int, re.findall(r'-?\d+', line))))
    for sx, sy, bx, by in pairs:
        d = dist(sx, sy, bx, by) + 2
        for mx, my in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            for i in range(d):
                tx = sx + mx * i
                ty = sy + my * (d - i - 1)
                if 0 <= tx < m and 0 <= ty < m:
                    for sx2, sy2, bx2, by2 in pairs:
                        if dist(sx2, sy2, tx, ty) <= dist(sx2, sy2, bx2, by2):
                            break
                    else:
                        print(tx*m+ty)
                        exit(0)
