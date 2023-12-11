def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines


def part1(lines: list[str]):
    def is_num(x: str):
        return x.isnumeric()
    t = 0
    for l in lines:
        f = list(filter(is_num, l))
        t += int(f[0] + f[-1])
    return t


def part2(lines: list[str]):
    num = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    t = 0
    for l in lines:
        n = []
        for i in range(len(l)):
            if l[i].isnumeric():
                n.append(l[i])
            for j, nu in enumerate(num):
                if l[i:].startswith(nu):
                    n.append(str(j+1))
        t += int(n[0] + n[-1])
    return t


if __name__ == "__main__":
    example_lines = read("example.txt")
    input_lines = read("input.txt")
    # print(part1(example_lines))
    print(part1(input_lines))
    print(part2(example_lines))
    print(part2(input_lines))
