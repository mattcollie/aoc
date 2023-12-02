def read_test_data():
    with open(f"./test.dat", 'r') as f:
        return f.read().split('\n')


def read_data():
    with open(f"./input.dat", 'r') as f:
        return f.read().split('\n')
