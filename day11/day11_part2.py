import re
from collections import deque
from functools import cache
from typing import List

class Solution:
    @cache
    def _num_of_stones_after(self, stone, blinks):
        if blinks == 0:
            return 1

        if len(stone) % 2 == 0:
            result = (
                self._num_of_stones_after(str(int(stone[:len(stone)//2])), blinks - 1)
                + self._num_of_stones_after(str(int(stone[len(stone)//2:])), blinks - 1)
            )
        elif int(stone) == 0:
            result = self._num_of_stones_after('1', blinks - 1)
        else:
            result = self._num_of_stones_after(str(int(stone)*2024), blinks - 1)

        return result

    def num_of_stones_after(self, stones, blinks):
        self.stones = stones
        result = 0
        for stone in stones:
            result += self._num_of_stones_after(stone, blinks)

        return result

def solution(input_lines : List[str]):
    stones = re.findall(r"\d+", input_lines[0])
    sol = Solution()
    return sol.num_of_stones_after(stones, 75)