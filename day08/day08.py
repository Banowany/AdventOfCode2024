from timeit import default_timer as timer
from file_reader import read_file_lines
from day08_part1 import solution as part1
from day08_part2 import solution as part2

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