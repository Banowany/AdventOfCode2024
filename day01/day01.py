from file_reader import read_file_lines
import re

def part1(file_lines):
    list1 = []
    list2 = []
    for line in file_lines:
        tmp = re.findall(r'\d+', line)
        list1.append(int(tmp[0]))
        list2.append(int(tmp[1]))

    list1 = sorted(list1)
    list2 = sorted(list2)

    return sum(abs(e1-e2) for e1, e2 in zip(list1, list2))

def part2(file_lines):
    list1 = []
    list2 = []
    for line in file_lines:
        tmp = re.findall(r'\d+', line)
        list1.append(int(tmp[0]))
        list2.append(int(tmp[1]))

    list1 = sorted(list1)

    return sum(list2.count(e)*e for e in list1)

if __name__ == '__main__':
    file_lines = read_file_lines('solution.in')
    print(part1(file_lines))
    print(part2(file_lines))