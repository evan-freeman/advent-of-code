def process_input():
    with open("2021/day6/input.txt") as f:
        input = f.read()
    input = [int(x) for x in input.split(",")]
    return input


def simulate_day(fish):
    """This function simulates one day of fish breeding"""
    pass


def simulate_n_days(n, fish):
    """This function simulates n days of fish breeding"""
    day = 1
    while day <= n:
        simulate_day(fish)
    return fish


def main():
    fish = process_input()
    fish = simulate_n_days(80, fish)
    num_fish = len(fish)
    print(num_fish)


if __name__ == "__main__":
    main()
