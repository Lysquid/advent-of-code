from sys import argv

with open(argv[1], "r") as file:
    l = [[False for _x in range(600)] for _y in range(200)]

    def pdeb():
        for y in range(0, 10):
            for x in range(494, 504):
                if l[y][x]:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()

    for line in file:
        px, py = None, None
        for point in line.strip().split(" -> "):
            x, y = list(map(int, point.split(",")))
            if px is not None and py is not None:
                if px == x:
                    for fy in range(min(y, py), max(y, py)+1):
                        l[fy][x] = True
                elif py == y:
                    for fx in range(min(x, px), max(x, px)+1):
                        l[y][fx] = True
            px, py = x, y


    count = 0
    while True:
        x, y = 500, 0
        while y < 199:
            fy = y + 1
            for dx in [0, -1, 1]:
                fx = x + dx
                if not l[fy][fx]:
                    x = fx
                    y = fy
                    break
            else:
                l[y][x] = True
                # pdeb()
                count += 1
                break
        else:
            break
    print(count)
