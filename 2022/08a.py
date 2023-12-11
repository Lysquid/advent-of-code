from sys import argv

with open(argv[1]) as file:
    trees = []
    total = 0
    for line in file:
        trees.append(list(map(int, list(line.strip()))))
    for y in range(len(trees)):
        for x in range(len(trees[0])):
            visible = False
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                i = 1
                while True:
                    nx = x+i*dx
                    ny = y+i*dy
                    if 0 <= nx < len(trees[0]) and 0 <= ny < len(trees):
                        if trees[y+i*dy][x+i*dx] >= trees[y][x]:
                            break
                    else:
                        visible = True
                        break
                    i += 1
                if visible:
                    total += 1
                    break
    print(total)
