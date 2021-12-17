import pytest

from day6 import multiples_less_than_or_equal, simulate_one_fish, solve_day_6
from day6slow import slow_solve_day_6


@pytest.mark.parametrize(
    "divisor, upper_limit, output",
    [
        (5, 15, [0, 5, 10, 15]),
    ],
)
def test_multiples_less_than_or_equal(divisor, upper_limit, output):
    assert multiples_less_than_or_equal(divisor, upper_limit) == output


@pytest.mark.parametrize(
    "input, num_days, output",
    [
        ("3,4,3,1,2", 18, 26),
        ("3,4,3,1,2", 80, 5934),
        ("0", 80, 1421),
        ("0", 18, 7),
    ],
)
def test_slow_solve_day_6(input, num_days, output):
    assert slow_solve_day_6(input=input, num_days=num_days) == output


@pytest.mark.parametrize(
    "fish, num_days, starting_days",
    [
        ({"value": 0, "starting_day": 0}, 18, [1, 8, 15]),
        ({"value": 8, "starting_day": 1}, 18, [10, 17]),
    ],
)
def test_simulate_one_fish(fish, num_days, starting_days):
    assert simulate_one_fish(fish, num_days) == starting_days


@pytest.mark.parametrize(
    "input, num_days, output",
    [
        ("3,4,3,1,2", 18, 26),
        ("3,4,3,1,2", 80, 5934),
        ("0", 80, 1421),
        ("0", 18, 7),
    ],
)
def test_solve_day_6(input, num_days, output):
    assert solve_day_6(input=input, num_days=num_days) == output
