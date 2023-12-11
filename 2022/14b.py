from sys import argv

with open(argv[1], "r") as file:
    l = [[False for _x in range(1000)] for _y in range(200)]

    def pdeb():
        for y in range(0, 10):
            for x in range(494, 504):
                if l[y][x]:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()

    my = 0
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
            my = max(my, y)
            px, py = x, y
    for x in range(len(l[0])):
        l[my+2][x] = True


    count = 0
    while not l[0][500]:
        x, y = 500, 0
        while True:
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
    print(count)
