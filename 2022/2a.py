from sys import argv
shapes = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}
with open(argv[1], "r") as file:
    tot = 0
    for line in file:
        them, you = list(map(lambda x: shapes[x], line.split()))
        if them == you:
            tot += 3
        elif you == (them)%3+1:
            tot += 6
        tot += you
    print(tot)
