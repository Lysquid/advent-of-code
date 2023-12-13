import itertools
import time
from multiprocessing import Pool


def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    return lines


def part1(lines: list[str]):

    def possibilities(data, nums, last_was_lava):
        if len(data) == 0:
            if last_was_lava and nums[0] == 0:
                nums.pop(0)
            if len(nums) == 0:
                return 1
            else:
                return 0

        if data[0] == '?':
            return possibilities('.' + data[1:], nums, last_was_lava) + possibilities('#' + data[1:], nums, last_was_lava)

        if data[0] == '.':
            if last_was_lava:
                if nums[0] == 0:
                    nums = nums.copy()
                    nums.pop(0)
                else:
                    return 0
            return possibilities(data[1:], nums, False)

        if data[0] == '#':
            if len(nums) == 0:
                return 0
            nums = nums.copy()
            nums[0] -= 1
            return possibilities(data[1:], nums, True)

    def handle_line(line: str):
        data, nums = line.split()
        nums = list(map(int, nums.split(',')))
        ret = possibilities(data, nums, False)
        return ret

    return sum(map(handle_line, lines))


def possibilities(data, nums, i=0, last_was_lava=False):

    if i == len(data):
        if last_was_lava and nums[0] == 0:
            nums.pop(0)
        if len(nums) > 0:
            return 0

    if len(nums) == 0:
        if data.count('#', i) == 0:
            return 1
        else:
            return 0

    if data[i] == '?':
        return possibilities(data, nums, i, last_was_lava) + possibilities(data, nums, i, last_was_lava)

    if data[i] == '.':
        if last_was_lava:
            if nums[0] == 0:
                nums = nums.copy()
                nums.pop(0)
            else:
                return 0
        return possibilities(data, nums, i+1, False)

    if data[i] == '#':
        if nums[0] <= 0:
            return 0
        nums = nums.copy()
        nums[0] -= 1
        return possibilities(data, nums, i+1, True)



def handle_line(line: str):
    data, nums = line.split()
    nums = list(map(int, nums.split(',')))
    data = "?".join(data for _ in range(5))
    nums = list(itertools.chain(*(nums for _ in range(5))))
    t = time.time()
    ret = possibilities(data, nums, False)
    print(f"{round(time.time() - t, 1)}s", line, ret)
    return ret


def part2(lines: list[str]):
    with Pool(16) as pool:
        ans = pool.map(handle_line, lines)
    return sum(ans)


if __name__ == "__main__":
    example_lines = read("example.txt")
    input_lines = read("input.txt")
    print(part1(example_lines))
    print(part1(input_lines))
    print(part2(example_lines))
    print(part2(input_lines))
