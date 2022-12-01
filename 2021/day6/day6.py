import time
from os.path import exists

import pandas as pd


def read_input(file):
    with open(file) as f:
        input = f.read()
    return input


def clean_input(input):
    return [int(x) for x in input.split(",")]


def multiples_less_than_or_equal(divisor, upper_limit):
    return [x for x in range(upper_limit + 1) if x % divisor == 0]


def simulate_one_fish(fish, num_days):
    value = fish["value"]
    starting_day = fish["starting_day"]
    displacement = value + starting_day + 1
    upper_limit = num_days - displacement
    multiples = multiples_less_than_or_equal(7, upper_limit=upper_limit)
    breeding_days = [day + displacement for day in multiples]
    return breeding_days


def simulate_fishes(fishes, num_days):
    num_fishes = 0
    while fishes:
        fish = fishes.pop(0)
        breeding_days = simulate_one_fish(fish, num_days)
        fishes += [{"value": 8, "starting_day": day} for day in breeding_days]
        num_fishes += 1
    return num_fishes


def solve_day_6(file=None, input=None, num_days=80):
    if not input:
        input = read_input(file)
    fish_values = clean_input(input)
    fishes = [{"value": value, "starting_day": 0} for value in fish_values]
    num_fishes = simulate_fishes(fishes, num_days)
    return num_fishes


def time_trials(input, max_num_days, filepath, interval=None):
    for num_days in range(max_num_days):
        if not exists(filepath):
            df = pd.DataFrame(
                {
                    "input": pd.Series(dtype="string"),
                    "num_days": pd.Series(dtype="int64"),
                    "num_fishes": pd.Series(dtype="int64"),
                    "solve_time": pd.Series(dtype="float"),
                }
            )
            df.to_csv(filepath, index=False)
        df = pd.read_csv(
            filepath,
            dtype={
                # "input": pd.Series(dtype="string"),
                "num_days": pd.Series(dtype="int64"),
                "num_fishes": pd.Series(dtype="int64"),
                "solve_time": pd.Series(dtype="float"),
            },
        )
        start = time.perf_counter()
        num_fishes = solve_day_6(input=input, num_days=num_days)
        end = time.perf_counter()
        solve_time = end - start
        df = df.append(
            {
                "input": input,
                "num_days": int(num_days),
                "num_fishes": int(num_fishes),
                "solve_time": round(solve_time, 4),
            },
            ignore_index=True,
        )
        df.to_csv(filepath, index=False)


if __name__ == "__main__":
    input = "0"
    filepath = "2021/day6/data.csv"
    max_num_days = 256
    time_trials(input=input, filepath=filepath, max_num_days=max_num_days)
