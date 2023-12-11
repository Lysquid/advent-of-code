import itertools


def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines


cor = {
    '|': ((0, 1), (0, -1)),
    '-': ((1, 0), (-1, 0)),
    'L': ((0, -1), (1, 0)),
    'J': ((0, -1), (-1, 0)),
    '7': ((0, 1), (-1, 0)),
    'F': ((0, 1), (1, 0)),
}


corner = {
    '|': 0,
    'L': -1,
    'J': -1,
    '7': 1,
    'F': 1,
}


def next(grid, px, py, x, y):
    exits = cor[grid[y][x]]
    move = (px-x, py-y)
    i = exits.index(move)
    dx, dy = exits[(i+1) % 2]
    return x+dx, y+dy


def find_s(grid):
    for y, l in enumerate(grid):
        try:
            return l.index('S'), y
        except ValueError:
            pass


def find_dir(grid, x, y, rev=False):
    for dx, dy in sorted(((0, 1), (0, -1), (1, 0), (-1, 0)), reverse=rev):
        if y+dy >= 0 and x+dx >= 0:
            sym = grid[y + dy][x + dx]
            if sym != '.':
                if (-dx, -dy) in cor[sym]:
                    return x+dx, y+dy


def part1(lines: list[str]):

    x, y = find_s(lines)
    px1, py1 = x, y
    px2, py2 = x, y
    x1, y1 = find_dir(lines, x, y, False)
    x2, y2 = find_dir(lines, x, y, True)

    i = 1
    while not (x1 == x2 and y1 == y2):
        x, y = next(lines, px1, py1, x1, y1)
        px1, py1, x1, y1 = x1, y1, x, y
        x, y = next(lines, px2, py2, x2, y2)
        px2, py2, x2, y2 = x2, y2, x, y
        i += 1
    return i

def part2(lines: list[str]):
    ix, iy = find_s(lines)
    px, py = ix, iy
    x, y = find_dir(lines, ix, iy)

    loop = {(ix, iy), (x, y)}
    while not (x == ix and y == iy):
        tx, ty = next(lines, px, py, x, y)
        px, py, x, y = x, y, tx, ty
        loop.add((x, y))

    lines[iy] = lines[iy].replace('S', '|')

    count = 0
    for y, line in enumerate(lines):
        inside = False
        enter_corner = 0
        for x, sym in enumerate(line):
            if (x, y) in loop:
                # Entering the pipe
                if (-1, 0) not in cor[sym]:
                    enter_corner = corner[sym]
                # Exiting the pipe
                if (1, 0) not in cor[sym]:
                    if corner[sym] == 0 or corner[sym] != enter_corner:
                        inside = not inside

                print(sym, end='')
            else:
                if inside:
                    count += 1
                print('I' if inside else sym, end='')
        print()
    return count


if __name__ == "__main__":
    example_lines = read("example.txt")
    input_lines = read("input.txt")
    print(part1(example_lines))
    print(part1(input_lines))
    print(part2(example_lines))
    print(part2(input_lines))
