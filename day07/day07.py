import math
from collections import deque
from timeit import default_timer as timer
import copy
from typing import List

from setuptools.command.rotate import rotate

from file_reader import read_file_lines
import re
from functools import reduce, cmp_to_key, cache
import networkx

@cache
def is_possible_to_create(nums, expected_result: int):
    n = len(nums)
    if n == 0:
        return expected_result == 0

    last = nums[len(nums)-1]
    if expected_result % last == 0:
        is_times_for_last = is_possible_to_create(nums[:n-1], (expected_result//last))
        if is_times_for_last:
            return True
    is_add_for_last = is_possible_to_create(nums[:n-1], expected_result - last)
    return is_add_for_last


def part1(input_lines : List[str]):
    end_sum = 0
    for line in input_lines:
        result_str, nums_str = line.split(": ")
        result = int(result_str)
        nums = [int(x) for x in re.findall(r'\d+', nums_str)]
        end_sum += result if is_possible_to_create(tuple(nums), result) else 0

    return end_sum

@cache
def is_possible_to_create_p2(nums, expected_result: int):
    n = len(nums)
    if n == 0:
        return expected_result == 0

    last = nums[len(nums)-1]

    num_of_digit_last = len(str(last))
    # is_conncatenate_for_last = False
    if last == (expected_result % (10**num_of_digit_last)):
        if is_possible_to_create_p2(nums[:n-1], expected_result // (10**num_of_digit_last)):
            return True

    if expected_result % last == 0:
        is_times_for_last = is_possible_to_create_p2(nums[:n-1], (expected_result//last))
        if is_times_for_last:
            return True
    is_add_for_last = is_possible_to_create_p2(nums[:n-1], expected_result - last)
    return is_add_for_last

def part2(input_lines):
    end_sum = 0
    for line in input_lines:
        result_str, nums_str = line.split(": ")
        result = int(result_str)
        nums = [int(x) for x in re.findall(r'\d+', nums_str)]
        end_sum += result if is_possible_to_create_p2(tuple(nums), result) else 0

    return end_sum




if __name__ == '__main__':
    input_lines = read_file_lines('solution.in')

    start = timer()
    answer1 = part1(input_lines)
    end = timer()
    elapsed = (end - start) * 1000
    print(f'Part 1 run time in ms: {elapsed: .2f}')

    start = timer()
    answer2 = part2(input_lines)
    end = timer()
    elapsed = (end - start) * 1000
    print(f'Part 2 run time in ms: {elapsed: .2f}')


    print(answer1)
    print(answer2)