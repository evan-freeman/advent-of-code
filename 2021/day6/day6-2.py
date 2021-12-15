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


def simulate_n_days(n, fishes):
    """This function simulates n days of fishes breeding"""
    day = 1
    while day <= n:
        print(day)
        fishes = simulate_day(fishes)
        day += 1
    return fishes


def main(file=None, input=None, n=80):
    if not input:
        input = read_input(file)
    fishes = clean_input(input)
    fishes = simulate_n_days(n, fishes)
    num_fishes = len(fishes)
    # print(fishes)
    print(f"{num_fishes=}")


if __name__ == "__main__":
    # file = "2021/day6/input.txt"
    input = "3,4,3,1,2"
    main(input=input, n=18)
