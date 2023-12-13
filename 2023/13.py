def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines



def part1(lines: list[str]):

    def line_reflect(bloc, fixed_coord, axis_coord, x_axis):
        size = len(bloc[0]) if x_axis else len(bloc)
        for s in range(axis_coord + 1):
            e = axis_coord + (axis_coord - s) + 1
            if e >= size:
                continue
            if x_axis:
                if bloc[fixed_coord][s] != bloc[fixed_coord][e]:
                    return False
            else:
                if bloc[s][fixed_coord] != bloc[e][fixed_coord]:
                    return False
        return True

    def axis_reflect(bloc, axis_coord, x_axis):
        size = len(bloc) if x_axis else len(bloc[0])
        for fixed_coord in range(size):
            if not line_reflect(bloc, fixed_coord, axis_coord, x_axis):
                return False
        return True

    def orientation_reflect(bloc, x_axis):
        size = len(bloc[0]) if x_axis else len(bloc)
        for axis_coord in range(size - 1):
            if axis_reflect(bloc, axis_coord, x_axis):
                return axis_coord + 1
        return 0

    def bloc_reflect(bloc):
        x = orientation_reflect(bloc, True)
        y = orientation_reflect(bloc, False)
        return x + 100 * y

    blocs = []
    bloc = []
    for line in lines:
        if not line:
            blocs.append(bloc)
            bloc = []
        else:
            bloc.append(line)
    blocs.append(bloc)

    tot = 0
    for bloc in blocs:
        tot += bloc_reflect(bloc)

    return tot


def part2(lines: list[str]):

    def line_reflect(bloc, fixed_coord, axis_coord, x_axis):
        size = len(bloc[0]) if x_axis else len(bloc)
        counter = 0
        for s in range(axis_coord + 1):
            e = axis_coord + (axis_coord - s) + 1
            if e >= size:
                continue
            if ((x_axis and bloc[fixed_coord][s] != bloc[fixed_coord][e])
                    or (not x_axis and bloc[s][fixed_coord] != bloc[e][fixed_coord])):
                return False
        return True

    def axis_reflect(bloc, axis_coord, x_axis):
        size = len(bloc) if x_axis else len(bloc[0])
        counter = 0
        for fixed_coord in range(size):
            if not line_reflect(bloc, fixed_coord, axis_coord, x_axis):
                counter += 1
                if counter > 1:
                    return False
        return counter == 1

    def orientation_reflect(bloc, x_axis):
        size = len(bloc[0]) if x_axis else len(bloc)
        for axis_coord in range(size - 1):
            if axis_reflect(bloc, axis_coord, x_axis):
                return axis_coord + 1
        return 0

    def bloc_reflect(bloc):
        x = orientation_reflect(bloc, True)
        y = orientation_reflect(bloc, False)
        return x + 100 * y

    blocs = []
    bloc = []
    for line in lines:
        if not line:
            blocs.append(bloc)
            bloc = []
        else:
            bloc.append(line)
    blocs.append(bloc)

    tot = 0
    for bloc in blocs:
        tot += bloc_reflect(bloc)

    return tot



if __name__ == "__main__":
    example_lines = read("example.txt")
    input_lines = read("input.txt")
    print(part1(example_lines))
    print(part1(input_lines))
    print(part2(example_lines))
    print(part2(input_lines))
