from sys import argv
with open(argv[1], "r") as file:
    nb = 4
    for line in file:
        for i in range(len(line) - nb):
            if len(set(line[i:i+nb])) == nb:
                print(i+nb)
                break
