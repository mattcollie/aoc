import re

from aoc.utils import read_test_data, read_data


def main():
    print(f"\nTest result: {test()}\nPart One result: {part_one()}\nPart Two result: {part_two()}\n")


def test():
    result = None

    for data in read_test_data():
        print(f"data -> {data}")

    return result


def part_one():
    result = 0

    for row in read_data():
        filtered = re.sub('[a-zA-Z]', '', row)
        number = int(filtered[0] + filtered[-1])
        result = result + number

    return result


def part_two():
    result = 0

    for row in read_data():
        print(row)
        result += replace_for_word(row)

    return result


def replace_for_word(value):
    WORD_TO_DIGIT = dict(
        zero=0,
        one=1,
        two=2,
        three=3,
        four=4,
        five=5,
        six=6,
        seven=7,
        eight=8,
        nine=9
    )
    i_order = []
    for k, v in WORD_TO_DIGIT.items():
        i = [m.start() for m in re.finditer(k, value)]
        if len(i) > 0:
            for index_instance in i:
                i_order.append([index_instance, v])

        i = [m.start() for m in re.finditer(str(v), value)]
        if len(i) > 0:
            for index_instance in i:
                i_order.append([index_instance, v])

    result = ''
    for o in sorted(i_order):
        result += str(o[1])
    print(result)
    x = int(result[0] + result[-1])
    print(x)
    return x


if __name__ == '__main__':
    main()
