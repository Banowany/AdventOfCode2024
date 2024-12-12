import re
from collections import deque, defaultdict
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
    def bfs(curr, acc):
        q = deque([curr])
        while q:
            row, col = q.popleft()
            curr = (row, col)
            for change_r, change_c in [(-1,0), (0, 1), (1, 0), (0, -1)]:
                point = (row+change_r, col+change_c)
                if is_in_map(point):
                    if point not in visited:
                        if get_val_from_point(point) == get_val_from_point(curr):
                            visited.add(point)
                            acc.append(point)
                            q.append(point)

    ranges = []
    for row in range(n):
        for col in range(n):
            start = (row, col)
            if start not in visited:
                candidate = [start]
                visited.add(start)
                bfs(start, candidate)
                ranges.append(candidate)

    return ranges





class Area:
    def __init__(self):
        self.left_fance = True
        self.right_fance = True
        self.down_fance = True
        self.up_fance = True

    def is_left_fance(self):
        return self.left_fance

    def is_right_fance(self):
        return self.right_fance

    def is_down_fance(self):
        return self.down_fance

    def is_up_fance(self):
        return self.up_fance

    def __setitem__(self, key, value):
        if key == (-1, 0):
            self.up_fance = value
        if key == (1, 0):
            self.down_fance = value
        if key == (0, 1):
            self.right_fance = value
        if key == (0, -1):
            self.left_fance = value

    def __getitem__(self, key):
        if key == (-1, 0):
            return self.up_fance
        if key == (1, 0):
            return self.down_fance
        if key == (0, 1):
            return self.right_fance
        if key == (0, -1):
            return self.left_fance


def solution(input_lines : List[str]):
    regions = find_regions(input_lines)

    def count_sides(single_region):
        visited = set()
        areas = defaultdict(Area)
        for row, col in single_region:
            curr_point = (row, col)
            visited.add(curr_point)
            for change_r, change_c in [(-1,0), (0, 1), (1, 0), (0, -1)]:
                another_point = (row + change_r, col + change_c)
                if is_in_map(another_point, len(input_lines)):
                    if another_point in visited:
                        areas[curr_point][(change_r, change_c)] = False
                        areas[another_point][(-change_r, -change_c)] = False

        result = 0

        visited = set()
        for row, col in single_region:
            point = (row, col)
            visited.add(point)
            num_of_fances = sum(1 for change in [(-1,0), (0, 1), (1, 0), (0, -1)] if areas[point][change] == True)

            #Do add the up fence
            left = (row, col - 1)
            right = (row, col + 1)
            is_deleted = False
            if is_in_map(left, len(input_lines)):
                if left in visited:
                    if areas[left].up_fance and areas[point].up_fance and not is_deleted:
                        num_of_fances -= 1
                        is_deleted = True

            if is_in_map(right, len(input_lines)):
                if right in visited:
                    if areas[right].up_fance and areas[point].up_fance and not is_deleted:
                        num_of_fances -= 1
                        is_deleted = True

            # Do add the down fence
            left = (row, col - 1)
            right = (row, col + 1)
            is_deleted = False
            if is_in_map(left, len(input_lines)):
                if left in visited:
                    if areas[left].down_fance and areas[point].down_fance and not is_deleted:
                        num_of_fances -= 1
                        is_deleted = True

            if is_in_map(right, len(input_lines)):
                if right in visited:
                    if areas[right].down_fance and areas[point].down_fance and not is_deleted:
                        num_of_fances -= 1
                        is_deleted = True

            # Do add the left fence
            up = (row - 1, col)
            down = (row + 1, col)
            is_deleted = False
            if is_in_map(up, len(input_lines)):
                if up in visited:
                    if areas[up].left_fance and areas[point].left_fance and not is_deleted:
                        num_of_fances -= 1
                        is_deleted = True

            if is_in_map(down, len(input_lines)):
                if down in visited:
                    if areas[down].left_fance and areas[point].left_fance and not is_deleted:
                        num_of_fances -= 1
                        is_deleted = True

            # Do add the right fence
            up = (row - 1, col)
            down = (row + 1, col)
            is_deleted = False
            if is_in_map(up, len(input_lines)):
                if up in visited:
                    if areas[up].right_fance and areas[point].right_fance and not is_deleted:
                        num_of_fances -= 1
                        is_deleted = True

            if is_in_map(down, len(input_lines)):
                if down in visited:
                    if areas[down].right_fance and areas[point].right_fance and not is_deleted:
                        num_of_fances -= 1
                        is_deleted = True

            result += num_of_fances

        return result
            # for change_r, change_c in [(-1,0), (0, 1), (1, 0), (0, -1)]:
            #     another_point = (row + change_r, col + change_c)
            #     if is_in_map(another_point, len(input_lines)):
            #         if another_point in visited:
            #             if (change_r, change_c) == (-1,0) or (change_r, change_c) == (1,0):
            #
            #             else:
            #                 pass




    result = 0
    for single_region in regions:
        price = count_sides(single_region) * len(single_region)
        result += price

    return result