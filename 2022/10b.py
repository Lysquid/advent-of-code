from sys import argv
with open(argv[1], "r") as file:
    reg = 1
    cycle = 0
    do_add = False
    pc = 0
    lines = file.readlines()
    total = 0
    while pc < len(lines):
        if abs(reg - cycle) <= 1:
            print("#", end="")
        else:
            print(".", end="")
        if do_add:
            reg += int(lines[pc].strip().split()[1])
            do_add = False
            pc += 1
        elif "addx" in lines[pc]:
            do_add = True
        else:
            pc += 1
        cycle += 1
        if cycle % 40 == 0:
            print()
            cycle = 0
