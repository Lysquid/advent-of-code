from sys import argv

with open(argv[1], "r") as file:
    x, y = [0]*10, [0]*10
    pos = set()
    for line in file:
        move, repeat = line.strip().split()
        for _ in range(int(repeat)):
            match move:
                case "R":
                    x[0] += 1
                case "L":
                    x[0] -= 1
                case "U":
                    y[0] += 1
                case "D":
                    y[0] -= 1
            for i in range(1, 10):
                if abs(x[i-1] - x[i]) > 1 and abs(y[i-1] - y[i]) > 1:
                    x[i] = (x[i-1] + x[i]) // 2
                    y[i] = (y[i-1] + y[i]) // 2
                elif abs(x[i-1] - x[i]) > 1:
                    x[i] = (x[i-1] + x[i]) // 2
                    y[i] = y[i-1]
                elif abs(y[i-1] - y[i]) > 1:
                    y[i] = (y[i-1] + y[i]) // 2
                    x[i] = x[i-1]
            pos.add((x[9], y[9]))
    print(len(pos))
