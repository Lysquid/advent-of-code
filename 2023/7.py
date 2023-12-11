from collections import Counter
from functools import cmp_to_key

def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines


def part1(lines: list[str]):
    bids = {l.split()[0]: int(l.split()[1]) for l in lines}
    cards = list(bids.keys())
    strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def key(card):
        count = Counter(card)
        com = count.most_common()
        s = []
        if com[0][1] == 5:
            s.append(0)
        elif com[0][1] == 4:
            s.append(1)
        elif len(com) >= 2 and com[0][1] == 3 and com[1][1] == 2:
            s.append(2)
        elif com[0][1] == 3:
            s.append(3)
        elif len(com) >= 2 and com[0][1] == 2 and com[1][1] == 2:
            s.append(4)
        elif com[0][1] == 2:
            s.append(5)
        elif len(com) == 5:
            s.append(6)
        else:
            s.append(7)

        for let in card:
            s.append(strength.index(let))

        return s

    cards.sort(key=key, reverse=True)
    return sum((i+1) * bids[card] for i, card in enumerate(cards))


def part2(lines: list[str]):
    bids = {l.split()[0]: int(l.split()[1]) for l in lines}
    cards = list(bids.keys())
    strength = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    def key(card):
        count = Counter(card)
        js = count.get("J", 0)
        count["J"] = 0
        com = count.most_common()
        s = []
        if com[0][1] + js == 5:
            s.append(0)
        elif com[0][1] + js == 4:
            s.append(1)
        elif com[0][1] + js == 3 and com[1][1] == 2:
            s.append(2)
        elif com[0][1] + js == 3:
            s.append(3)
        elif com[0][1] + js == 2 and com[1][1] == 2:
            s.append(4)
        elif com[0][1] + js == 2:
            s.append(5)
        elif len(set(card)) == 5:
            s.append(6)
        else:
            s.append(7)

        for let in card:
            s.append(strength.index(let))

        return s

    cards.sort(key=key, reverse=True)
    return sum((i+1) * bids[card] for i, card in enumerate(cards))


if __name__ == "__main__":
    example_lines = read("example.txt")
    input_lines = read("input.txt")
    print(part1(example_lines))
    print(part1(input_lines))
    print(part2(example_lines))
    print(part2(input_lines))
