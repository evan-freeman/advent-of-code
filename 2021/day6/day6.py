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
        fishes = simulate_day(fishes)
        day += 1
    return fishes


def main(file=None, input=None, num_days=80):
    total_start = time.perf_counter()
    if not input:
        input = read_input(file)
    fishes = clean_input(input)
    fishes = simulate_n_days(num_days, fishes)
    num_fishes = len(fishes)
    total_end = time.perf_counter()
    total_total_time = total_end - total_start
    return num_fishes


if __name__ == "__main__":
    # file = "2021/day6/input.txt"
    input = "3,4,3,1,2"
    num_days = 80
    num_fishes = main(input=input, num_days=80)
    print(f"After {num_days} days, there are {num_fishes} fish.")
