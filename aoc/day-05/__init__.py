from aoc.utils import read_test_data, read_data


def main():
    print(f"\nTest result: {test()}")
    # print(f"\nTest result: {test()}\nPart One result: {part_one()}\nPart Two result: {part_two()}\n")


def test():
    result = None
    SEEDS = []
    MAPS = {}
    current_map = None
    for i, data in enumerate([m for m in read_data() if m]):
        if i == 0:
            SEEDS = [int(d) for d in data[7:].split(' ')]
            continue

        if not data[0].isdigit():
            current_map = data.split(' ')[0]
            MAPS[current_map] = []
            continue

        MAPS[current_map].append([int(d) for d in data.split(' ')])
        print(f"data -> {data}")

    print(SEEDS)
    print(MAPS)
    final_matches = []
    for s1, s2 in zip(SEEDS[0::2], SEEDS[1::2]):
        print('SEEDS::', s1, s2)
        si1 = s1
        si2 = s2
        for k, v in MAPS.items():
            source_input = find_source_range_destiantion_in_map(si1, si2, v)
        # print('RESULT: ', source_input)
        final_matches.append(source_input)
        # break
    result = min(final_matches)
    return result


def part_one():
    result = None
    SEEDS = []
    MAPS = {}
    current_map = None
    for i, data in enumerate([m for m in read_data() if m]):
        if i == 0:
            SEEDS = [int(d) for d in data[7:].split(' ')]
            continue

        if not data[0].isdigit():
            current_map = data.split(' ')[0]
            MAPS[current_map] = []
            continue

        MAPS[current_map].append([int(d) for d in data.split(' ')])
        print(f"data -> {data}")

    print(SEEDS)
    print(MAPS)
    final_matches = []
    for seed in SEEDS:
        source_input = seed
        for k, v in MAPS.items():
            source_input = find_destiantion_in_map(source_input, k, v)
        print('RESULT: ', source_input)
        final_matches.append(source_input)
        # break
    result = min(final_matches)
    return result


def part_two():
    result = None
    SEEDS = []
    MAPS = {}
    current_map = None
    for i, data in enumerate([m for m in read_data() if m]):
        if i == 0:
            SEEDS = [int(d) for d in data[7:].split(' ')]
            continue

        if not data[0].isdigit():
            current_map = data.split(' ')[0]
            MAPS[current_map] = []
            continue

        MAPS[current_map].append([int(d) for d in data.split(' ')])
        print(f"data -> {data}")

    print(SEEDS)
    print(MAPS)
    final_matches = []
    for seed_start, seed_end in zip(SEEDS[0::2], SEEDS[1::2]):
        print('SEEDS::', seed_start, seed_end)
        source_input = seed_start
        for k, v in MAPS.items():
            source_input = find_destiantion_in_map(source_input, k, v)
        # print('RESULT: ', source_input)
        final_matches.append(source_input)
        # break
    result = min(final_matches)
    return result


def find_destiantion_in_map(input, map_name, map_value):
    # print('CHECKING MAP:', input, map_name, map_value)
    for map in map_value:
        destination, source, range_length = map
        if input in range(source, source+range_length):
            source_input = destination + (input - source)
            # print('Found input: ', input, ' in range: ', range(source, source+range_length))
            return source_input
    return input


def find_source_range_destiantion_in_map(s1, s2, map_value):
    for map in map_value:
        destination, source, range_length = map
        mr1 = source
        mr2 = source+range_length
        """
            S1 <--------> S2
                   M1 <--------> M2
                   
                S1 <---?
            M1 <--------> M2
                   
            S1 <-----------------> S2
                ?--------> M2
        """
        if s1 <= mr1 <= s2 <= mr2:
            return destination + (mr1 - source)
        elif mr1 <= s1 <= mr2:
            return destination + (s1 - source)
        elif s1 <= mr2 <= s2:
            return destination + (s1 - source)
        # print('Found input: ', input, ' in range: ', range(source, source+range_length))
    return s1


if __name__ == '__main__':
    # TOO HIGH: 641329181
    main()
