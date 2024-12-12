import re
from collections import deque
from typing import List


def is_in_map(point, n):
    row, col = point
    return n > row >= 0 and n > col >= 0

def find_regions(mymap):
    regions = []
    visited = set()
    n = len(mymap)

    def is_in_map(point):
        row,col = point
        return n > row >= 0 and n > col >= 0
    def get_val_from_point(point):
        row, col = point
        return mymap[row][col]
    def dfs(curr, acc):
        row, col = curr
        for change_r, change_c in [(-1,0), (0, 1), (1, 0), (0, -1)]:
            point = (row+change_r, col+change_c)
            if is_in_map(point):
                if point not in visited:
                    if get_val_from_point(point) == get_val_from_point(curr):
                        visited.add(point)
                        acc.append(point)
                        dfs(point, acc)

    ranges = []
    for row in range(n):
        for col in range(n):
            start = (row, col)
            if start not in visited:
                candidate = [start]
                visited.add(start)
                dfs(start, candidate)
                ranges.append(candidate)

    return ranges






def solution(input_lines : List[str]):
    regions = find_regions(input_lines)

    def count_perimeter(single_region):
        result = 0
        visited = set()
        for point in single_region:
            result += 4
            visited.add(point)
            row, col = point
            for change_r, change_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                another_point = (row + change_r, col + change_c)
                if is_in_map(another_point, len(input_lines)):
                    if another_point in visited:
                        result -= 2
        return result

    result = 0
    for single_region in regions:
        price = count_perimeter(single_region) * len(single_region)
        result += price

    return result