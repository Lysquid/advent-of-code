def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines


def part1(lines: list[str]):

    nums = list(map(int, lines[0].split()[1:]))
    table = []
    layer = []
    for line in lines[1:] + ["map"]:
        if not line:
            continue
        if "map" in line:
            table.append(layer)
            layer = []
        else:
            layer.append(tuple(map(int, line.split())))

    def conversion(seed: int, depth=0) -> int:
        if depth == len(table):
            # print()
            return seed
        soil = seed
        for dest, src, rang in table[depth]:
            if src <= seed < src + rang:
                soil = dest + seed - src
                break
            elif dest <= seed < src:
                soil += rang
        # print(soil, end=" ")
        return conversion(soil, depth+1)

    return min(map(conversion, nums))


def part2(lines: list[str]):

    nums = list(map(int, lines[0].split()[1:]))
    table = []
    layer = []
    for line in lines[1:] + ["map"]:
        if not line:
            continue
        if "map" in line:
            if layer:
                table.append(layer)
                layer = []
        else:
            layer.append(tuple(map(int, line.split())))

    def conversion(seed_beg: int, seed_rang, depth=0) -> int:
        if depth == len(table):
            return seed_beg

        seed_end = seed_beg + seed_rang
        for dest_beg, src_beg, rang in table[depth]:
            src_end = src_beg + rang

            # Cas compris dans src
            if src_beg <= seed_beg and seed_end <= src_end:
                soil_beg = dest_beg + (seed_beg - src_beg)
                return conversion(soil_beg, seed_rang, depth+1)

            # A cheval à gauche
            elif seed_beg <= src_beg < seed_end <= src_end:
                return min(
                    conversion(seed_beg, src_beg - seed_beg, depth),
                    conversion(src_beg, seed_end - src_beg, depth)
                )

            # A cheval à droite
            elif src_beg <= seed_beg < src_end <= seed_end:
                return min(
                    conversion(seed_beg, src_end - seed_beg, depth),
                    conversion(src_end, seed_end - src_end, depth)
                )

        # Aucun warp, on applique juste les décalages
        soil_beg = seed_beg
        for dest_beg, src_beg, rang in table[depth]:
            if dest_beg <= seed_beg and seed_end < src_beg:
                soil_beg += rang

        return conversion(soil_beg, seed_rang, depth+1)

    vals = []
    for num, num_rang in zip(nums[0::2], nums[1::2]):
        vals.append(conversion(num, num_rang))

    return min(vals)





    # def conversion(table: list[tuple[int, ...]], seeds: list[tuple[int]]) -> list[int]:
    #     soil = []
    #     for seed_beg, seed_rang in seeds:
    #         seed_end = seed_beg + seed_rang
    #         val = seed
    #         for dest, src, rang in table:
    #             if src <= seed < src + rang:
    #                 val = dest + seed - src
    #                 break
    #             elif dest <= src < src:
    #                 val += rang
    #         soil.append(val)
    #     return soil
    #
    # nums = list(map(int, lines[0].split()[1:]))
    # table = []
    # for line in lines[1:]:
    #     if not line:
    #         continue
    #     if "map" in line:
    #         if table:
    #             print(f"{line.split()[0].split('-')[0].ljust(12)} {' '.join(map(str, nums))}")
    #             nums = conversion(table, nums)
    #         table = []
    #     else:
    #         table.append(tuple(map(int, line.split())))
    # nums = conversion(table, nums)
    # print(f"{'location'.ljust(12)} {' '.join(map(str, nums))}")
    #
    # return min(nums)


if __name__ == "__main__":
    example_lines = read("example.txt")
    input_lines = read("input.txt")
    print(part1(example_lines))
    print(part1(input_lines))
    print(part2(example_lines))
    print(part2(input_lines))
