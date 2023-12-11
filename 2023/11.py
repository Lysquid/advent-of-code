import itertools
import re


def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines


def part1(lines: list[str]):
    xs = set()
    ys = set()
    stars = list()
    for y, line in enumerate(lines):
        for match in re.finditer("#", line):
            x = match.start()
            xs.add(x)
            ys.add(y)
            stars.append([x, y])

    xn = sorted(set(range(len(lines[0]))) - xs)
    yn = sorted(set(range(len(lines))) - ys)

    for i, star in enumerate(stars):
        xi, yi = 0, 0
        for xv in xn:
            if xv < star[0]:
                xi += 1
            else:
                break
        for yv in yn:
            if yv < star[1]:
                yi += 1
            else:
                break
        stars[i][0] += xi
        stars[i][1] += yi

    dist = 0
    for s1, s2 in itertools.combinations(stars, 2):
        d = abs(s1[0] - s2[0]) + abs(s1[1] - s2[1])
        dist += d

    return dist


def part2(lines: list[str]):
    xs = set()
    ys = set()
    stars = list()
    for y, line in enumerate(lines):
        for match in re.finditer("#", line):
            x = match.start()
            xs.add(x)
            ys.add(y)
            stars.append([x, y])

    xn = sorted(set(range(len(lines[0]))) - xs)
    yn = sorted(set(range(len(lines))) - ys)

    expansion = 1000000 - 1
    for i, star in enumerate(stars):
        xi, yi = 0, 0
        for xv in xn:
            if xv < star[0]:
                xi += expansion
            else:
                break
        for yv in yn:
            if yv < star[1]:
                yi += expansion
            else:
                break
        stars[i][0] += xi
        stars[i][1] += yi

    dist = 0
    for s1, s2 in itertools.combinations(stars, 2):
        d = abs(s1[0] - s2[0]) + abs(s1[1] - s2[1])
        dist += d

    return dist



if __name__ == "__main__":
    example_lines = read("example.txt")
    input_lines = read("input.txt")
    print(part1(example_lines))
    print(part1(input_lines))
    print(part2(example_lines))
    print(part2(input_lines))
