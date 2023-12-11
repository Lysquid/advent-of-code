from sys import argv

with open(argv[1], "r") as file:
    xh, yh = 0, 0
    xt, yt = 0, 0
    pos = set()
    pos.add((xt, yt))
    for line in file:
        move, repeat = line.strip().split()
        for _ in range(int(repeat)):
            match move:
                case "R":
                    xh += 1
                case "L":
                    xh -= 1
                case "U":
                    yh += 1
                case "D":
                    yh -= 1
            if abs(xh - xt) > 1:
                xt = (xh + xt) // 2
                yt = yh
            elif abs(yh - yt) > 1:
                yt = (yh + yt) // 2
                xt = xh
            pos.add((xt, yt))
    print(len(pos))
