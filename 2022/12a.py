from sys import argv
from queue import PriorityQueue
from operator import add

with open(argv[1], "r") as file:
    start = ()
    end = ()
    hmap = []
    for y, line in enumerate(file):
        hline = []
        for x, char in enumerate(line.strip()):
            if char == 'S':
                hline.append(-1)
                start = (y, x)
            elif char == 'E':
                hline.append(ord('z') - ord('a'))
                end = (y, x)
            else:
                hline.append(ord(char) - ord('a'))
        hmap.append(hline)
    visited = set()
    
    def pdebug():
        for y, line in enumerate(hmap):
            for x, h in enumerate(line):
                if (y, x) in visited:
                    print(chr(h + ord('A')), end='')
                else:
                    print(chr(h + ord('a')), end='')
            print()

    pqueue = PriorityQueue()
    pqueue.put((0, start))
    while not pqueue.empty():
        parc, pos = pqueue.get()
        if pos == end:
            print(parc)
            break
        parc += 1
        for dp in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            np = tuple(map(add, pos, dp))
            if 0 <= np[0] < len(hmap) and 0 <= np[1] < len(hmap[0]):
                if pos not in visited:
                    if hmap[pos[0]][pos[1]] == -1 or hmap[np[0]][np[1]] - hmap[pos[0]][pos[1]] <= 1:
                        pqueue.put((parc, np))
        visited.add(pos)

