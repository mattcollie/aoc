import re
from operator import mul
from functools import reduce

from aoc.utils import read_test_data, read_data


def main():
    # run_test()
    # run_part_one()
    run_part_two()


def run_part_two():
    total_sum = 0
    for line in read_data():
        all_cubes = re.findall('(\\d+ blue|\\d+ red|\\d+ green)', line)
        running_total = {
            'red': 0,
            'blue': 0,
            'green': 0
        }
        for cube in all_cubes:
            cube_number, cube_colour = cube.split(' ')
            if running_total[cube_colour] < int(cube_number):
                running_total[cube_colour] = int(cube_number)
        total_sum += reduce(mul, running_total.values(), 1)
    print(total_sum)


def run_part_one():
    CUBE_DICT = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    valid_game = 0
    for line in read_data():
        game_id = get_game_id(line)
        all_cubes = re.findall('(\\d+ blue|\\d+ red|\\d+ green)', line)
        valid_game += check_cube_number(CUBE_DICT, game_id, all_cubes)
        print(f"Game ID: {game_id}, cubes: {all_cubes} -> {line}")
    print(valid_game)


def run_test():
    CUBE_DICT = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    valid_game = 0
    for line in read_test_data():
        game_id = get_game_id(line)
        all_cubes = re.findall('(\\d+ blue|\\d+ red|\\d+ green)', line)
        valid_game += check_cube_number(CUBE_DICT, game_id, all_cubes)
        print(f"Game ID: {game_id}, cubes: {all_cubes} -> {line}")
    print(valid_game)


def get_game_id(input: str) -> int:
    return int(input[4:input.index(':')])


def check_cube_number(cube_master, game_id, all_cubes):
    for cube in all_cubes:
        cube_number, cube_colour = cube.split(' ')
        if cube_master[cube_colour] < int(cube_number):
            print(cube_master[cube_colour], int(cube_number))
            return 0
    return game_id


if __name__ == '__main__':
    main()
