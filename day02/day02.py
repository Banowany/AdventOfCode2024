from file_reader import read_file_lines
import re
from functools import reduce

def is_increasing(nums, min_diff, max_diff):
    diffs = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    for diff in diffs:
        if diff < min_diff or diff > max_diff:
            return False
    return True

def is_decreasing(nums, min_diff, max_diff):
    diffs = [nums[i] - nums[i+1] for i in range(len(nums)-1)]
    for diff in diffs:
        if diff < min_diff or diff > max_diff:
            return False
    return True


def part1(file_lines):
    all_levels = [[int(j) for j in re.findall(r'\d+', i)] for i in file_lines]
    counter = 0
    for levels in all_levels:
        counter += 1 if is_increasing(levels, 1, 3) or is_decreasing(levels, 1, 3) else 0
    return counter


def subarrays_one_less(arr):
    """
    Zwraca wszystkie podtablice o długości o jeden mniejszej niż oryginalna tablica.

    :param arr: Lista wejściowa
    :return: Lista podtablic
    """
    n = len(arr)
    return [arr[:i] + arr[i + 1:] for i in range(n)]

def part2(file_lines):
    all_levels = [[int(j) for j in re.findall(r'\d+', i)] for i in file_lines]
    counter = 0
    for levels in all_levels:
        if reduce(lambda acc, x: acc or is_increasing(x,1,3) or is_decreasing(x,1,3), subarrays_one_less(levels) + [levels], False):
            counter += 1
    return counter

if __name__ == '__main__':
    file_lines = read_file_lines('solution.in')
    print(part1(file_lines))
    print(part2(file_lines))