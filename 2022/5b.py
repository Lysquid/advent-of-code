from sys import argv

with open(argv[1], "r") as file:
    if argv[1] == "input":
        hauteur = 8
        lageur = 9
    else:
        hauteur = 3
        lageur = 3
    st = [[] for _ in range(lageur)]
    for i, line in enumerate(file):
        if i < hauteur:
            for j in range(lageur):
                pos = 1 + 4*j
                if len(line) > pos:
                    c = line[pos]
                    if c != " ":
                        st[j].insert(0, c)
        elif i > hauteur + 1:
            nb, src, dst = list(map(int, line.split()[1::2]))
            src -= 1
            dst -= 1
            st[dst].extend(st[src][-nb::])
            st[src] = st[src][:-nb:]
    print("".join([s[-1] for s in st if s]))
