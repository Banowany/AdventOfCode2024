import math
from collections import deque
from timeit import default_timer as timer
from file_reader import read_file_lines
import re
from functools import reduce, cmp_to_key
import networkx

def get_after_number(relations, num):
    return {relation[1] for relation in relations if relation[0]==num}

def is_correct_order(relations, ptp):
    return all(set(ptp[i + 1:]).issubset(get_after_number(relations, ptp[i])) for i in range(len(ptp) - 1))

def part1(page_ordering, pages_to_produce_list):
    relations = []

    for page_order in page_ordering:
        before, after = [int(num) for num in re.findall(r'\d+', page_order)]
        relations.append((before, after))

    good_pages_to_produce = []
    for pages_to_produce in pages_to_produce_list:
        pages_to_produce = [int(num) for num in pages_to_produce.split(',')]
        if is_correct_order(relations, pages_to_produce):
            good_pages_to_produce.append(pages_to_produce)
    return sum(int(gptp[len(gptp)//2]) for gptp in good_pages_to_produce)

def is_x_before_y(x, y, relations):
    if y in get_after_number(relations, x):
        return -1
    return 1

def part2(page_ordering, pages_to_produce_list):
    relations = []

    for page_order in page_ordering:
        before, after = [int(num) for num in re.findall(r'\d+', page_order)]
        relations.append((before, after))

    not_good_pages_to_produce = []
    for pages_to_produce in pages_to_produce_list:
        pages_to_produce = [int(num) for num in pages_to_produce.split(',')]
        if not is_correct_order(relations, pages_to_produce):
            not_good_pages_to_produce.append(pages_to_produce)

    result = 0
    for tmp in not_good_pages_to_produce:
        tmp.sort(key=cmp_to_key(lambda x, y: is_x_before_y(x, y, relations)))
        result += tmp[len(tmp)//2]
    return result

    # return sum(int(gptp[len(gptp) // 2]) for gptp in not_good_pages_to_produce)




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