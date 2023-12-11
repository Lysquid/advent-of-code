from sys import argv

with open(argv[1], "r") as file:
    hauteur = 9
    st = [[] for _ in range(hauteur)]
    for i, line in enumerate(file):
        if i < 8:
            for j in range(hauteur):
                pos = 1 + 4*j
                if len(line) > pos:
                    c = line[pos]
                    if c != " ":
                        st[j].insert(0, c)
        elif i > hauteur:
            nb, src, dst = list(map(int, line.split()[1::2]))
            src -= 1
            dst -= 1
            for j in range(nb):
                st[dst].append(st[src].pop())
    print("".join([s[-1] for s in st if s]))
