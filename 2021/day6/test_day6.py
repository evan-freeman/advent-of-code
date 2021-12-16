import pytest

from day6 import main


@pytest.mark.parametrize(
    "input, num_days, output",
    [
        ("3,4,3,1,2", 18, 26),
        ("3,4,3,1,2", 80, 5934),
        ("0", 80, 1421),
        ("0", 18, 7),
    ],
)
def test_main(input, num_days, output):
    assert main(input=input, num_days=num_days) == output
