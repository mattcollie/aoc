import csv
import re


def main():
    with open('C:/repos/aoc/day-01/input1.txt', 'r') as f:
        reader = csv.reader(f)
        data = [d[0] for d in reader]
        # part_one(data)
        part_two(data)


def part_one(data):
    result = 0
    for row in data:
        filtered = re.sub('[a-zA-Z]', '', row)
        number = int(filtered[0] + filtered[-1])
        result = result + number
    print(result)


def part_two(data):
    result = 0
    for row in data:
        print(row)
        result += replace_for_word(row)
    print(result)


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
