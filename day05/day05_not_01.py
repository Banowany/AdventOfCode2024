import math
from collections import deque
from timeit import default_timer as timer
from file_reader import read_file_lines
import re
from functools import reduce
import networkx


def is_correct_order(number_to_place, pages_to_produce):
    tmp = list(map(lambda x: number_to_place[x], [int(num) for num in pages_to_produce]))
    return all(tmp[i] < tmp[i+1] for i in range(len(tmp) - 1))

def part1(page_ordering, pages_to_produce_list):
    page_relation = networkx.DiGraph()

    for page_order in page_ordering:
        before, after = [int(num) for num in re.findall(r'\d+', page_order)]
        page_relation.add_edge(before, after)

    perfect_page_order = list(networkx.topological_sort(page_relation))
    number_to_place = {num: i for i, num in enumerate(perfect_page_order)}

    good_pages_to_produce = []
    for pages_to_produce in pages_to_produce_list:
        pages_to_produce = pages_to_produce.split(',')
        if is_correct_order(number_to_place, pages_to_produce):
            good_pages_to_produce.append(pages_to_produce)
    return sum(int(gptp[len(gptp)//2]) for gptp in good_pages_to_produce)







def part2(page_ordering, page_to_produce):
    pass




if __name__ == '__main__':
    page_ordering = read_file_lines('page_ordering.in')
    page_to_produce = read_file_lines('page_produce.in')

    start = timer()
    answer1 = part1(page_ordering, page_to_produce)
    end = timer()
    elapsed = (end - start) * 1000
    print(f'Part 1 run time in ms: {elapsed: .2f}')

    start = timer()
    answer2 = part2(page_ordering, page_to_produce)
    end = timer()
    elapsed = (end - start) * 1000
    print(f'Part 2 run time in ms: {elapsed: .2f}')


    print(answer1)
    print(answer2)