def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines


def part1(lines: list[str]):
    
    def all0(l):
        for e in l:
            if e != 0:
                return False
        return True

    def inter(l):
        diff = [tuple(map(int, l.split()))]
        while not all0(diff[-1]):
            ld = diff[-1]
            diff.append(tuple(ld[i+1] - ld[i] for i in range(len(ld)-1)))
        n = 0
        for i in reversed(range(len(diff)-1)):
            n = n + diff[i][-1]
        return n

    return sum(map(inter, lines))


def part2(lines: list[str]):
    def all0(l):
        for e in l:
            if e != 0:
                return False
        return True

    def inter(l):
        diff = [tuple(map(int, l.split()))]
        while not all0(diff[-1]):
            ld = diff[-1]
            diff.append(tuple(ld[i+1] - ld[i] for i in range(len(ld)-1)))
        n = 0
        for i in reversed(range(len(diff)-1)):
            n = diff[i][0] - n
        return n

    return sum(map(inter, lines))



if __name__ == "__main__":
    example_lines = read("example.txt")
    input_lines = read("input.txt")
    print(part1(example_lines))
    print(part1(input_lines))
    print(part2(example_lines))
    print(part2(input_lines))
