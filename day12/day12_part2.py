import re
from collections import deque, defaultdict
from itertools import combinations
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


class Area:
    def __init__(self):
        self.left = True
        self.right = True
        self.up = True
        self.down = True

def solution(input_lines : List[str]):
    regions = find_regions(input_lines)

    def count_sides(single_region):
        visited = set()
        areas = {}

        for point in single_region:
            visited.add(point)
            row, col = point

            areas[point] = Area()

            #up (-1, 0)
            a_point = (row -1, col)
            if a_point in visited:
                areas[point].up = False
                areas[a_point].down = False

            # right (0, 1)
            a_point = (row, col + 1)
            if a_point in visited:
                areas[point].right = False
                areas[a_point].left = False

            # down (1, 0)
            a_point = (row + 1, col)
            if a_point in visited:
                areas[point].down = False
                areas[a_point].up = False

            # left (0, -1)
            a_point = (row, col - 1)
            if a_point in visited:
                areas[point].left = False
                areas[a_point].right = False

        up_sides = set()
        down_sides = set()
        left_sides = set()
        right_sides = set()

        for key, val in areas.items():
            if val.up:
                up_sides.add(key)
            if val.down:
                down_sides.add(key)
            if val.right:
                right_sides.add(key)
            if val.left:
                left_sides.add(key)

        result = 0

        tmp = len(up_sides)
        for p1, p2 in combinations(up_sides, 2):
            r1, c1 = p1
            r2, c2 = p2
            if r1 == r2 and abs(c1 - c2) == 1:
                tmp -= 1

        result += tmp

        tmp = len(down_sides)
        for p1, p2 in combinations(down_sides, 2):
            r1, c1 = p1
            r2, c2 = p2
            if r1 == r2 and abs(c1 - c2) == 1:
                tmp -= 1

        result += tmp

        tmp = len(left_sides)
        for p1, p2 in combinations(left_sides, 2):
            r1, c1 = p1
            r2, c2 = p2
            if c1 == c2 and abs(r1 - r2) == 1:
                tmp -= 1

        result += tmp

        tmp = len(right_sides)
        for p1, p2 in combinations(right_sides, 2):
            r1, c1 = p1
            r2, c2 = p2
            if c1 == c2 and abs(r1 - r2) == 1:
                tmp -= 1

        result += tmp

        # up_rows_indexes = set(row for row, _ in up_sides)
        # # up_cols_indexes = set(col for _, col in up_sides)
        # up_rows = [[col for row, col in up_sides if row == curr_row] for curr_row in up_rows_indexes]
        # # up_cols = [[row for row, col in up_sides if col == curr_col] for curr_col in up_cols_indexes]
        # for up_row in up_rows:
        #     result += 1
        #     for up_col1, up_col2 in zip(up_row, up_row[1:]):
        #         if up_col2 - up_col1 == 1:
        #             result += 1
        #
        # down_rows_indexes = set(row for row, _ in down_sides)
        # # up_cols_indexes = set(col for _, col in up_sides)
        # down_rows = [[col for row, col in down_sides if row == curr_row] for curr_row in down_rows_indexes]
        # # up_cols = [[row for row, col in up_sides if col == curr_col] for curr_col in up_cols_indexes]
        # for up_row in down_rows:
        #     result += 1
        #     for up_col1, up_col2 in zip(up_row, up_row[1:]):
        #         if up_col2 - up_col1 == 1:
        #             result += 1
        #
        # # down_rows_indexes = set(row for row, _ in down_sides)
        # left_cols_indexes = set(col for _, col in left_sides)
        # # down_rows = [[col for row, col in down_sides if row == curr_row] for curr_row in down_rows_indexes]
        # left_cols = [[row for row, col in left_sides if col == curr_col] for curr_col in left_cols_indexes]
        # for up_row in left_cols:
        #     result += 1
        #     for up_col1, up_col2 in zip(up_row, up_row[1:]):
        #         if up_col2 - up_col1 == 1:
        #             result += 1
        #
        # # down_rows_indexes = set(row for row, _ in down_sides)
        # right_cols_indexes = set(col for _, col in right_sides)
        # # down_rows = [[col for row, col in down_sides if row == curr_row] for curr_row in down_rows_indexes]
        # right_cols = [[row for row, col in right_sides if col == curr_col] for curr_col in
        #              right_cols_indexes]
        # for up_row in right_cols:
        #     result += 1
        #     for up_col1, up_col2 in zip(up_row, up_row[1:]):
        #         if up_col2 - up_col1 == 1:
        #             result += 1

        return result

    result = 0
    for single_region in regions:
        price = count_sides(single_region) * len(single_region)
        result += price

    return result