import math
from collections import deque
from timeit import default_timer as timer
from file_reader import read_file_lines
import re
from functools import reduce


def part1(file_lines):
    queue = deque()
    for i, line in enumerate(file_lines):
        for j, let in enumerate(line):
            if let == 'X':
                queue.append((i,j))

    counter = 0
    while queue:
        x,y = queue.popleft()
        let = file_lines[x][y]
        if (x - 3 >= 0
                and file_lines[x-1][y] == 'M' and file_lines[x-2][y] == 'A' and file_lines[x-3][y] == 'S'):
            counter += 1
        if (x - 3 >= 0 and y + 3 < len(file_lines[0])
                and file_lines[x-1][y+1] == 'M' and file_lines[x-2][y+2] == 'A' and file_lines[x-3][y+3] == 'S'):
            counter += 1
        if (y + 3 < len(file_lines[0])
                and file_lines[x][y+1] == 'M' and file_lines[x][y+2] == 'A' and file_lines[x][y+3] == 'S'):
            counter += 1
        if (x + 3 < len(file_lines) and y + 3 < len(file_lines[0])
                and file_lines[x+1][y+1] == 'M' and file_lines[x+2][y+2] == 'A' and file_lines[x+3][y+3] == 'S'):
            counter += 1
        if (x + 3 < len(file_lines)
                and file_lines[x+1][y] == 'M' and file_lines[x+2][y] == 'A' and file_lines[x+3][y] == 'S'):
            counter += 1
        if (x + 3 < len(file_lines) and y - 3 >= 0
                and file_lines[x+1][y-1] == 'M' and file_lines[x+2][y-2] == 'A' and file_lines[x+3][y-3] == 'S'):
            counter += 1
        if (y - 3 >= 0
                and file_lines[x][y-1] == 'M' and file_lines[x][y-2] == 'A' and file_lines[x][y-3] == 'S'):
            counter += 1
        if (x - 3 >= 0 and y - 3 >= 0
                and file_lines[x-1][y-1] == 'M' and file_lines[x-2][y-2] == 'A' and file_lines[x-3][y-3] == 'S'):
            counter += 1


    return counter


def part2(file_lines):
    queue = deque()
    for i, line in enumerate(file_lines):
        for j, let in enumerate(line):
            if let == 'A':
                queue.append((i, j))

    counter = 0
    while queue:
        x, y = queue.popleft()
        if (x - 1 >= 0 and x + 1 < len(file_lines) and y - 1 >= 0 and y + 1 < len(file_lines[0])
                and file_lines[x-1][y-1] == 'M' and file_lines[x-1][y+1] == 'M'
                and file_lines[x+1][y-1] == 'S' and file_lines[x+1][y+1] == 'S'):
            counter += 1
        if (x - 1 >= 0 and x + 1 < len(file_lines) and y - 1 >= 0 and y + 1 < len(file_lines[0])
                and file_lines[x - 1][y - 1] == 'S' and file_lines[x - 1][y + 1] == 'S'
                and file_lines[x + 1][y - 1] == 'M' and file_lines[x + 1][y +1] == 'M'):
            counter += 1
        if (x - 1 >= 0 and x + 1 < len(file_lines) and y - 1 >= 0 and y + 1 < len(file_lines[0])
                and file_lines[x-1][y-1] == 'M' and file_lines[x-1][y+1] == 'S'
                and file_lines[x+1][y-1] == 'M' and file_lines[x+1][y+1] == 'S'):
            counter += 1
        if (x - 1 >= 0 and x + 1 < len(file_lines) and y - 1 >= 0 and y + 1 < len(file_lines[0])
                and file_lines[x-1][y-1] == 'S' and file_lines[x-1][y+1] == 'M'
                and file_lines[x+1][y-1] == 'S' and file_lines[x+1][y+1] == 'M'):
            counter += 1

    return counter




if __name__ == '__main__':
    file_lines = read_file_lines('solution.in')

    start = timer()
    answer1 = part1(file_lines)
    end = timer()
    elapsed = (end - start) * 1000
    print(f'Part 1 run time in ms: {elapsed: .2f}')

    start = timer()
    answer2 = part2(file_lines)
    end = timer()
    elapsed = (end - start) * 1000
    print(f'Part 2 run time in ms: {elapsed: .2f}')


    print(answer1)
    print(answer2)