def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines


def part1(lines: list[str]):
    times = map(int, lines[0].split()[1:])
    dists = map(int, lines[1].split()[1:])
    tot = 1
    for t, d in zip(times, dists):
        n = 0
        for h in range(1, t):
            nd = (t - h) * h
            if nd > d:
                n += 1
        tot *= n
    return tot


def part2(lines: list[str]):
    time = int("".join(lines[0].split()[1:]))
    dist = int("".join(lines[1].split()[1:]))
    n = 0
    for h in range(1, time):
        nd = (time - h) * h
        if nd > dist:
            n += 1
    return n


if __name__ == "__main__":
    example_lines = read("example.txt")
    input_lines = read("input.txt")
    print(part1(example_lines))
    print(part1(input_lines))
    print(part2(example_lines))
    print(part2(input_lines))
