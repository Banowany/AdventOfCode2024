import re
from collections import defaultdict
from itertools import combinations
from typing import Set, List


def find_antinodes_for_pair(antena1: (int, int), antena2: (int, int), n: int, m: int,
                            unique_antinodes: Set[tuple[int, int]]):
    unique_antinodes.add(antena1)
    unique_antinodes.add(antena2)

    vec_to_a2 = (antena2[0] - antena1[0], antena2[1] - antena1[1])
    vec_to_a1 = (antena1[0] - antena2[0], antena1[1] - antena2[1])

    atinode_1 = (antena2[0] + vec_to_a2[0], antena2[1] + vec_to_a2[1])
    atinode_2 = (antena1[0] + vec_to_a1[0], antena1[1] + vec_to_a1[1])

    while(atinode_1[0] >= 0 and atinode_1[0] < n and atinode_1[1] >= 0 and atinode_1[1] < m):
        unique_antinodes.add(atinode_1)
        atinode_1 = (atinode_1[0] + vec_to_a2[0], atinode_1[1] + vec_to_a2[1])
    while atinode_2[0] >= 0 and atinode_2[0] < n and atinode_2[1] >= 0 and atinode_2[1] < m:
        unique_antinodes.add(atinode_2)
        atinode_2 = (atinode_2[0] + vec_to_a1[0], atinode_2[1] + vec_to_a1[1])

def solution(input_lines : List[str]):
    grouped_atenas = defaultdict(list)
    for i, line in enumerate(input_lines):
        for match in re.finditer(r'\w', line):
            grouped_atenas[match.group()].append((match.start(), i))

    unique_antinodes = set()
    for key in grouped_atenas.keys():
        for a1, a2 in combinations(grouped_atenas[key], 2):
            find_antinodes_for_pair(a1, a2, len(input_lines[0]), len(input_lines), unique_antinodes)

    print(len(unique_antinodes))