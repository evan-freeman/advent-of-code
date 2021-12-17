import time


def read_input(file):
    with open(file) as f:
        input = f.read()
    return input


def clean_input(input):
    return [int(x) for x in input.split(",")]


def simulate_day(fishes):
    """This function simulates one day of fishes breeding"""
    for i, fish in enumerate(fishes[:]):
        if fish > 0:
            fishes[i] -= 1
        else:
            fishes[i] = 6
            fishes.append(8)
    return fishes


def simulate_n_days(num_days, fishes):
    """This function simulates n days of fishes breeding"""
    day = 1
    while day <= num_days:
        print(f"{day=}")
        print(f"{fishes=}")
        fishes = simulate_day(fishes)
        day += 1
    return fishes


def slow_solve_day_6(file=None, input=None, num_days=80):
    if not input:
        input = read_input(file)
    fishes = clean_input(input)
    fishes = simulate_n_days(num_days, fishes)
    num_fishes = len(fishes)
    return num_fishes


if __name__ == "__main__":
    # file = "2021/day6/input.txt"
    input = "0"
    output = slow_solve_day_6(input=input, num_days=18)
    print(output)
