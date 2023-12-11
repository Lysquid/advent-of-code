import re

def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines


def part1(lines: list[str]):
    vals = {"red": 12, "green": 13, "blue": 14}
    t = 0
    for i, l in enumerate(lines):
        for match in re.finditer(r"(\d+) (\w+)", l):
            num, color = match.groups()
            if int(num) > vals[color]:
                break
        else:
            t += i+1
    return t


def part2(lines: list[str]):
    t = 0
    for i, l in enumerate(lines):
        vals = {"red": 0, "blue": 0, "green": 0}
        for match in re.finditer(r"(\d+) (\w+)", l):
            num, color = match.groups()
            vals[color] = max(vals[color], int(num))
        t += vals["red"] * vals["blue"] * vals["green"]
    return t


if __name__ == "__main__":
    example_lines = read("example.txt")
    input_lines = read("input.txt")
    print(part1(example_lines))
    print(part1(input_lines))
    print(part2(example_lines))
    print(part2(input_lines))
