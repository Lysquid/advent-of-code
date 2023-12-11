from sys import argv
with open(argv[1], "r") as file:
    tot = 0
    tab = [set()] * 3
    for i, line in enumerate(file):
        tab[i%3] = set(line.removesuffix("\n"))
        if i % 3 == 2:
            common = list(tab[0].intersection(tab[1]).intersection(tab[2]))[0]
            # print(tab[0], tab[1], tab[2], common, sep="\n")
            tot += ord(common) - (ord('a') if common.islower() else ord('A') - 26) + 1
    print(tot)
