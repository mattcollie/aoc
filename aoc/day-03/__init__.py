import re
from functools import reduce

from aoc.utils import read_test_data, read_data


def main():
    print(f"\nTest result: {test()}")
    print(f"\nTest result: {test()}\nPart One result: {part_one()}\nPart Two result: {part_two()}\n")


def test():
    result = 0

    input_data = read_test_data()
    LINE_LENGTH = len(input_data[0])
    MATRIX = [-LINE_LENGTH - 1, -LINE_LENGTH, -LINE_LENGTH+1, -1, 1, LINE_LENGTH-1, LINE_LENGTH, LINE_LENGTH+1]

    flattened = ''.join(input_data)

    nums_found = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer('[0-9]+', flattened)]
    print(flattened)
    print(nums_found)

    gears = {}

    for n in nums_found:
        found_at = None
        for r in range(n[0], n[1]):
            for m in MATRIX:
                if r - m < 0 or r - m >= len(flattened):
                    continue

                if flattened[r-m] in ['*']:
                    found_at = r-m

        if found_at is not None:
            if found_at not in gears:
                gears[found_at] = []

            gears[found_at].append(int(n[2]))
            print('FOUND: ', n[2])
            result += int(n[2])

    result = reduce(lambda a, b: (b[0] * b[1]) + a, filter(lambda x: len(x) > 1, gears.values()), 0)

    for i, data in enumerate(input_data):
        print(f"data[{i}] -> {data}")

    print(gears)
    # TOO LOW 524798
    return result


def part_one():
    result = 0

    input_data = read_data()
    LINE_LENGTH = len(input_data[0])
    MATRIX = [-LINE_LENGTH - 1, -LINE_LENGTH, -LINE_LENGTH+1, -1, 1, LINE_LENGTH-1, LINE_LENGTH, LINE_LENGTH+1]

    flattened = ''.join(input_data)

    nums_found = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer('[0-9]+', flattened)]

    for n in nums_found:
        ok = False
        for r in range(n[0], n[1]):
            for m in MATRIX:
                if r - m < 0 or r - m >= len(flattened):
                    continue

                if flattened[r-m] in ['%', '*', '/', '=', '&', '#', '-', '+', '$', '@']:
                    ok = True

        if ok:
            result += int(n[2])

    return result


def part_two():
    result = 0

    input_data = read_data()
    LINE_LENGTH = len(input_data[0])
    MATRIX = [-LINE_LENGTH - 1, -LINE_LENGTH, -LINE_LENGTH+1, -1, 1, LINE_LENGTH-1, LINE_LENGTH, LINE_LENGTH+1]

    flattened = ''.join(input_data)

    nums_found = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer('[0-9]+', flattened)]
    print(flattened)
    print(nums_found)

    gears = {}

    for n in nums_found:
        found_at = None
        for r in range(n[0], n[1]):
            for m in MATRIX:
                if r - m < 0 or r - m >= len(flattened):
                    continue

                if flattened[r-m] in ['*']:
                    found_at = r-m

        if found_at is not None:
            if found_at not in gears:
                gears[found_at] = []

            gears[found_at].append(int(n[2]))
            print('FOUND: ', n[2])
            result += int(n[2])

    result = reduce(lambda a, b: (b[0] * b[1]) + a, filter(lambda x: len(x) > 1, gears.values()), 0)

    for i, data in enumerate(input_data):
        print(f"data[{i}] -> {data}")

    return result


if __name__ == '__main__':
    main()
