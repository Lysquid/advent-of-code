from sys import argv
with open(argv[1], "r") as file:
    tot = 0
    for line in file:
        l = len(line) // 2
        common = list(set(line[:l]).intersection(set(line[l:])))[0]
        tot += ord(common) - (ord('a') if common.islower() else ord('A') - 26) + 1
    print(tot)
