from sys import argv
with open(argv[1], "r") as file:
    tot = 0
    for line in file:
        p1, p2 = line.split(",")
        def parse(p):
            return tuple(map(int, p.split("-")))
        mi1, ma1 = parse(p1)
        mi2, ma2 = parse(p2)
        if not (mi2 > ma1 or mi1 > ma2):
            tot += 1
    print(tot)
