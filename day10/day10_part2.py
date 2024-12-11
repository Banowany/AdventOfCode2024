import heapq
import re
from collections import defaultdict, deque
from itertools import combinations
from typing import Set, List

def is_up(position, board):
    return position[0] - 1 >=0

def is_right(position, board):
    return position[1] + 1 < len(board[0])

def is_down(position, board):
    return position[0] + 1 < len(board)

def is_left(position, board):
    return position[1] - 1 >= 0

def get_up(position, board):
    if is_up(position, board) and board[position[0] - 1][position[1]]!='.':
        return position[0] - 1, position[1]

def get_right(position, board):
    if is_right(position, board) and board[position[0]][position[1]+1]!='.':
        return position[0], position[1] + 1

def get_down(position, board):
    if is_down(position, board) and board[position[0] + 1][position[1]]!='.':
        return position[0] + 1, position[1]

def get_left(position, board):
    if is_left(position, board) and board[position[0]][position[1]-1]!='.':
        return position[0], position[1]-1

def find_begins(board):
    result = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '0':
                result.append((i,j))
    return result

def single_solution(beg, input_lines):
    q = deque([beg])
    counter = 0
    while q:
        row, col = q.popleft()
        val = int(input_lines[row][col])
        if val == 9:
            counter += 1
            continue
        pos_up = get_up((row, col), input_lines)
        if pos_up is not None:
            val_up = int(input_lines[pos_up[0]][pos_up[1]])
            if val_up - val == 1:
                q.append(pos_up)
        pos_right = get_right((row, col), input_lines)
        if pos_right is not None:
            val_right = int(input_lines[pos_right[0]][pos_right[1]])
            if val_right - val == 1:
                q.append(pos_right)
        pos_down = get_down((row, col), input_lines)
        if pos_down is not None:
            val_down = int(input_lines[pos_down[0]][pos_down[1]])
            if val_down - val == 1:
                q.append(pos_down)
        pos_left = get_left((row, col), input_lines)
        if pos_left is not None:
            val_left = int(input_lines[pos_left[0]][pos_left[1]])
            if val_left - val == 1:
                q.append(pos_left)
    return counter

def solution(input_lines : List[str]):
    return sum(single_solution(beg, input_lines) for beg in find_begins(input_lines))