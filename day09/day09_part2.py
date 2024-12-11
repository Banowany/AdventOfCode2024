import heapq
import re
from collections import defaultdict, deque
from itertools import combinations
from typing import Set, List

def solution(input_lines : List[str]):
    disk_map = input_lines[0]

    free_spaces = deque()
    files_by_size = defaultdict(set)
    start_index = 0
    for i, let in enumerate(disk_map):
        if i % 2 == 0:
            files_by_size[int(let)].add((start_index, i // 2, int(let)))
        else:
            free_spaces.append((start_index, int(let)))
        start_index += int(let)


    while free_spaces:
        start_index, n = free_spaces.popleft()
        file_candidates = sorted([x for n_2 in range(1, n+1) for x in files_by_size[n_2] if x[0] > start_index], key=lambda x: x[1], reverse=True)
        if file_candidates:
            good_file = file_candidates[0]
            remaining_space = n - good_file[2]
            if remaining_space != 0:
                free_spaces.appendleft((start_index + good_file[2], remaining_space))
            files_by_size[good_file[2]].remove(good_file)
            files_by_size[good_file[2]].add((start_index, good_file[1], good_file[2]))

    result = 0
    for i in range(1, 10):
        for start_index, id, n in files_by_size[i]:
            for curr_index in range(start_index, start_index + n):
                result += curr_index * id





    return result