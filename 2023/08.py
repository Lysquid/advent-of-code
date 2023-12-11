import math
import re
from itertools import cycle


def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines


def part1(lines: list[str]):
    ins = lines[0]
    dir = {}
    for match in re.finditer(r"(\w{3}) = \((\w{3}), (\w{3})\)", "\n".join(lines[2:])):
        src, left, right = match.groups()
        dir[src] = (left, right)

    pos = "AAA"
    i = 0
    while pos != "ZZZ":
        pos = dir[pos][int(ins[i % len(ins)] == "R")]
        i += 1

    return i


def part2(lines: list[str]):
    instr = tuple(0 if c == "L" else 1 for c in lines[0])
    paths = {}
    for match in re.finditer(r"(\w{3}) = \((\w{3}), (\w{3})\)", "\n".join(lines[2:])):
        src, left, right = match.groups()
        paths[src] = (left, right)

    def count_cycle(node):
        i = 0
        while not node.endswith("Z"):
            node = paths[node][instr[i % len(instr)]]
            i += 1
        return i

    poss = [pos for pos in paths if pos.endswith("A")]

    return math.lcm(*map(count_cycle, poss))


if __name__ == "__main__":
    example_lines = read("example.txt")
    input_lines = read("input.txt")
    # print(part1(example_lines))
    # print(part1(input_lines))
    print(part2(example_lines))
    print(part2(input_lines))
