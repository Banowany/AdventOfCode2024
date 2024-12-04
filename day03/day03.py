import math

from file_reader import read_file_lines
import re
from functools import reduce


def part1(file_lines):
    muls = []
    for line in file_lines:
        muls = muls + re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)

    prods = []
    for mul in muls:
        prods.append(int(mul[0]) * int(mul[1]))

    return sum(prods)


def part2(file_lines):
    one_line = reduce(lambda acc, x: acc + x, file_lines, "")
    pattern = r"(don't\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\))"
    matches = re.findall(pattern, one_line)
    result = [match[0] for match in matches]

    prods = []
    enabled = True
    for el in result:
        if el == r"do()":
            enabled = True
        elif el == r"don't()":
            enabled = False
        else:
            if enabled:
                mul = re.findall(r'\d+', el)
                prods.append(int(mul[0]) * int(mul[1]))

    return sum(prods)




if __name__ == '__main__':
    file_lines = read_file_lines('solution.in')
    print(part1(file_lines))
    print(part2(file_lines))