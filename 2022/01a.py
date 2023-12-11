from sys import argv
sums = []
with open(argv[1], "r") as file:
    summ = 0
    for line in file:
        if line == "\n":
            sums.append(summ)
            summ = 0
            continue
        summ += int(line)
    print(max(sums))
