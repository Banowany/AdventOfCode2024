import re
from collections import deque
from typing import List


def solution(input_lines : List[str]):
    stones = re.findall(r"\d+", input_lines[0])
    q = deque([(0, stone) for stone in stones])
    counter = 0
    while q:
        blink, strnum = q.popleft()

        if blink == 25:
            counter += 1
            continue

        if len(strnum) % 2 == 0:
            q.append((blink+1, str(int(strnum[:len(strnum)//2]))))
            q.append((blink + 1, str(int(strnum[len(strnum) // 2:]))))
        elif int(strnum) == 0:
            q.append((blink+1, "1"))
        else:
            q.append((blink + 1, str(int(strnum)*2024)))

    return counter