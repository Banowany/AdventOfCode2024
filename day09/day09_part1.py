import re
from collections import defaultdict, deque
from itertools import combinations
from typing import List, Set

def solution(input_lines : List[str]):
    disk_map = input_lines[0]

    representation = deque()
    for i, let in enumerate(disk_map):
        if i % 2 == 0:
            for _ in range(int(let)):
                representation.append(i//2)
        else:
            for _ in range(int(let)):
                representation.append(-1)

    i = 0
    result = 0
    while representation:
        el = representation.popleft()
        while el == -1 and representation:
            el = representation.pop()
        if not representation:
            break
        result += i * el
        i+=1

    return result


