def read_test_data(day):
    with open(f"./{day}/test1.dat", 'r') as f:
        return f.read().split('\n')


def read_data(day):
    with open(f"./{day}/input.dat", 'r') as f:
        return f.read().split('\n')
