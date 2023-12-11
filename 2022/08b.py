from sys import argv

with open(argv[1]) as file:
    trees = []
    maxi = 0
    for line in file:
        trees.append(list(map(int, list(line.strip()))))
    for y in range(len(trees)):
        for x in range(len(trees[0])):
            view = 1
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                i = 1
                while True:
                    nx = x+i*dx
                    ny = y+i*dy
                    if 0 <= nx < len(trees[0]) and 0 <= ny < len(trees):
                        if trees[y+i*dy][x+i*dx] >= trees[y][x]:
                            break
                    else:
                        i -= 1
                        break
                    i += 1
                view *= i
            maxi = max(maxi, view)
    print(maxi)
