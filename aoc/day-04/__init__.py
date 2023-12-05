from aoc.utils import read_test_data, read_data


def main():
    print(f"\nTest result: {test()}\nPart One result: {part_one()}\nPart Two result: {part_two()}\n")


def test():
    result = 0
    pre_re = []
    for i, data in enumerate(read_test_data()):
        row = [[int(d) for d in d.split(' ') if d] for d in data.split(':')[1].strip().split(' | ')]
        a, b = row
        f = []
        for x in a:
            if x in b:
                f.append(i + len(f)+1)
        pre_re.append(f)

    def search_tree(curr, cx, result=0):
        # print('Search Tree:', curr, cx)
        if len(curr) == 0:
            # print('result for: ', 1, cx)
            return 1

        for card_id in curr:
            result += search_tree(pre_re[card_id], card_id)

        # print('result for: ', result, cx)
        return result + 1

    o = pre_re.copy()
    print(pre_re)
    for card_id, matched in enumerate(pre_re):
        points = search_tree(matched, card_id)
        # print('card', card_id+1, 'matches', matched, 'total points', points)
        result += points
        # print('='*80)
    return result


def part_one():
    result = 0

    for data in read_data():
        row = [[int(d) for d in d.split(' ') if d] for d in data.split(':')[1].strip().split(' | ')]
        a, b = row
        f = 0
        for x in a:
            if x in b:
                f += 1
        if f > 0:
            result += pow(2, f-1)

    return result


def part_two():
    result = 0
    pre_re = []
    for i, data in enumerate(read_data()):
        row = [[int(d) for d in d.split(' ') if d] for d in data.split(':')[1].strip().split(' | ')]
        a, b = row
        f = []
        for x in a:
            if x in b:
                f.append(i + len(f)+1)
        pre_re.append(f)

    def search_tree(curr, cx, result=0):
        if len(curr) == 0:
            return 1

        for card_id in curr:
            result += search_tree(pre_re[card_id], card_id)

        return result + 1

    o = pre_re.copy()
    print(pre_re)
    for card_id, matched in enumerate(pre_re):
        points = search_tree(matched, card_id)
        result += points
    return result


def flatten_extend(matrix):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    return flat_list


if __name__ == '__main__':
    main()
