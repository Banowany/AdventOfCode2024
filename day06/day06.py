import math
from collections import deque
from timeit import default_timer as timer
import copy

from setuptools.command.rotate import rotate

from file_reader import read_file_lines
import re
from functools import reduce, cmp_to_key
import networkx

def part1(input_lines):
    # obstructions_x = {}
    # obstructions_y = {}
    obstructions = set()
    for i, line in enumerate(input_lines):
        for j, let in enumerate(line):
            if let == '#':
                # if j in obstructions_x:
                #     obstructions_x[j].append(i)
                # else:
                #     obstructions_x[j] = [i]
                #
                # if i in obstructions_y:
                #     obstructions_y[i].append(j)
                # else:
                #     obstructions_y[i] = [j]
                obstructions.add((j, i))
            elif let == '^':
                guard_position = (j, i)

    visited = set()
    stack = deque()
    stack.append((guard_position, 0, -1))
    while stack:
        # guard_position, focus_x, focus_y = stack.popleft()
        # if focus_x != 0:
        #     candidates = list(filter(lambda x: focus_x * (x - guard_position[0]) > 0, obstructions_y[guard_position[1]]))
        #     if len(candidates) == 0:
        #     candidates.sort(key=lambda x: focus_x * (x - guard_position[0]))
        #
        # else:#focus_y != 0
        #     pass
        guard_position, focus_x, focus_y = stack.popleft()
        if (guard_position[0] < 0 or
            guard_position[0] >= len(input_lines[0]) or
            guard_position[1] < 0 or
            guard_position[1] >= len(input_lines)):
            pass
        else:
            visited.add(guard_position)
            next_destination = (guard_position[0] + focus_x, guard_position[1] + focus_y)
            if next_destination in obstructions:
                stack.append((guard_position, -focus_y, focus_x))
            else:
                stack.append((next_destination, focus_x, focus_y))

    return len(visited)

# def part2(input_lines):
#     obstructions = set()
#     for i, line in enumerate(input_lines):
#         for j, let in enumerate(line):
#             if let == '#':
#                 # if j in obstructions_x:
#                 #     obstructions_x[j].append(i)
#                 # else:
#                 #     obstructions_x[j] = [i]
#                 #
#                 # if i in obstructions_y:
#                 #     obstructions_y[i].append(j)
#                 # else:
#                 #     obstructions_y[i] = [j]
#                 obstructions.add((j, i))
#             elif let == '^':
#                 guard_position = (j, i)
#
#     visited = set()
#     stack = deque()
#     stack.append((guard_position, 0, -1))
#     counter = 0
#     while stack:
#         guard_position, focus_x, focus_y = stack.popleft()
#         if (guard_position[0] < 0 or
#                 guard_position[0] >= len(input_lines[0]) or
#                 guard_position[1] < 0 or
#                 guard_position[1] >= len(input_lines)):
#             pass
#         else:
#             visited.add((guard_position, focus_x, focus_y))
#             next_destination = (guard_position[0] + focus_x, guard_position[1] + focus_y)
#             if next_destination in obstructions:
#                 stack.append((guard_position, -focus_y, focus_x))
#             else:
#                 stack.append((next_destination, focus_x, focus_y))
#                 rotate_direction_x = -focus_y
#                 rotate_direction_y = focus_x
#                 # candidates_for_creating_loop = []
#                 for visited_field, visited_focus_x, visited_focus_y in visited:
#                     if (visited_focus_x == rotate_direction_x
#                             and visited_focus_y == rotate_direction_y):
#                         if (guard_position[0] == 4 and guard_position[1]==6):
#                             pass
#
#                         if rotate_direction_x == 0:
#                             if visited_field[0] == guard_position[0]:
#                                 if (visited_field[1] - guard_position[1]) * rotate_direction_y > 0:
#                                     counter+=1
#                                     break
#                         if rotate_direction_y == 0:
#                             if visited_field[1] == guard_position[1]:
#                                 if (visited_field[0] - guard_position[0]) * rotate_direction_x > 0:
#                                     counter+=1
#                                     break
#
#     return counter

def is_cycle(guard_position, obstructions_x, obstructions_y, xlen, ylen):
    visited_begin = set()
    visited_end = set()
    stack = deque()
    stack.append((guard_position, 0, -1))
    while stack:
        guard_position, focus_x, focus_y = stack.popleft()
        visited_begin.add((guard_position, focus_x, focus_y))#tu ewentualnie kierunki dodac
        if focus_x != 0:
            if guard_position[1] not in obstructions_y:
                return False
            candidates_x = list(
                filter(lambda x: focus_x * (x - guard_position[0]) > 0, obstructions_y[guard_position[1]]))
            if len(candidates_x) == 0:
                return False
            candidates_x.sort(key=lambda x: focus_x * (x - guard_position[0]))
            candidate_x = candidates_x[0] - focus_x
            if ((candidate_x, guard_position[1]), -focus_y, focus_x) in visited_begin:
                return True
            visited_end.add(((candidate_x, guard_position[1]), -focus_y, focus_x))
            stack.append(((candidate_x, guard_position[1]), -focus_y, focus_x))
        else:
            if guard_position[0] not in obstructions_x:
                return False
            candidates_y = list(
                filter(lambda y: focus_y * (y - guard_position[1]) > 0, obstructions_x[guard_position[0]]))
            if len(candidates_y) == 0:
                return False
            candidates_y.sort(key=lambda y: focus_y * (y - guard_position[1]))
            candidate_y = candidates_y[0] - focus_y
            if ((guard_position[0], candidate_y), -focus_y, focus_x) in visited_begin:
                return True
            visited_end.add(((guard_position[0], candidate_y), -focus_y, focus_x))
            stack.append(((guard_position[0], candidate_y), -focus_y, focus_x))

def part2(input_lines):
    obstructions_x = {}
    obstructions_y = {}
    # obstructions = set()
    for i, line in enumerate(input_lines):
        for j, let in enumerate(line):
            if let == '#':
                if j in obstructions_x:
                    obstructions_x[j].append(i)
                else:
                    obstructions_x[j] = [i]

                if i in obstructions_y:
                    obstructions_y[i].append(j)
                else:
                    obstructions_y[i] = [j]
                # obstructions.add((j, i))
            elif let == '^':
                guard_position = (j, i)


    counter = 0
    for i in range(len(input_lines)):
        for j in range(len(input_lines[0])):
            if i == 1 and j == 5:
                pass
            tmp_obstructions_x = copy.deepcopy(obstructions_x)
            tmp_obstructions_y = copy.deepcopy(obstructions_y)
            if j in tmp_obstructions_x:
                if i not in tmp_obstructions_x[j]:
                    tmp_obstructions_x[j].append(i)
            else:
                tmp_obstructions_x[j] = [i]
            if i in tmp_obstructions_y:
                if j not in tmp_obstructions_y[i]:
                    tmp_obstructions_y[i].append(j)
            else:
                tmp_obstructions_y[i] = [j]
            if is_cycle(copy.deepcopy(guard_position), tmp_obstructions_x, tmp_obstructions_y, len(input_lines[0]), len(input_lines)):
                counter+=1
    return counter




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