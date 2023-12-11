def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines


def part1(lines: list[str]):
    t = 0
    for line in lines:
        beg, end = line[line.index(":")+1:].split("|")
        winning = set(map(int, beg.split()))
        count = sum(num in winning for num in map(int, end.split()))
        t += 2**count//2 if count else 0
    return t


def part2(lines: list[str]):
    t = 0
    copies = {i: 1 for i in range(len(lines))}
    for i, line in enumerate(lines):
        beg, end = line[line.index(":")+1:].split("|")
        winning = set(map(int, beg.split()))
        count = sum(num in winning for num in map(int, end.split()))
        for j in range(count):
            if i+1+j < len(copies):
                copies[i+1+j] += copies[i]
        t += copies[i]
    return t


if __name__ == "__main__":
    example_lines = read("example.txt")
    input_lines = read("input.txt")
    print(part1(example_lines))
    print(part1(input_lines))
    print(part2(example_lines))
    print(part2(input_lines))
