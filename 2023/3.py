import re

def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines


def part1(lines: list[str]):
    t = 0
    for li, l in enumerate(lines):
        for match in re.finditer(r"(\d+)", l):
            good = False
            for y in range(li-1, li+2):
                for x in range(match.span()[0] - 1, match.span()[1] + 1):
                    try:
                        c = lines[y][x]
                        if not c.isnumeric() and c != '.':
                            good = True
                    except:
                        pass
            if good:
                t += int(match.group())
    return t


def part2(lines: list[str]):
    t = 0
    pos = {}
    for li, l in enumerate(lines):
        for match in re.finditer(r"(\d+)", l):
            good = False
            for y in range(li-1, li+2):
                for x in range(match.span()[0] - 1, match.span()[1] + 1):
                    try:
                        c = lines[y][x]
                        if c == '*':
                            if (x, y) in pos:
                                t += int(match.group()) * pos[(x, y)]
                                del pos[(x, y)]
                            else:
                                pos[(x, y)] = int(match.group())
                    except:
                        pass
    return t


if __name__ == "__main__":
    example_lines = read("example.txt")
    input_lines = read("input.txt")
    print(part1(example_lines))
    print(part1(input_lines))
    print(part2(example_lines))
    print(part2(input_lines))
