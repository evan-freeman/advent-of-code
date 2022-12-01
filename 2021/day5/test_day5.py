import pytest

from day5 import generate_points


@pytest.mark.parametrize(
    "input, output",
    [
        (
            {
                "x1": 0,
                "y1": 0,
                "x2": 0,
                "y2": 2,
            },
            {(0, 0), (0, 1), (0, 2)},
        ),
        (
            {
                "x1": 0,
                "y1": 0,
                "x2": 2,
                "y2": 0,
            },
            {(0, 0), (1, 0), (2, 0)},
        ),
        (
            {
                "x1": 0,
                "y1": 0,
                "x2": 2,
                "y2": 2,
            },
            {(0, 0), (1, 1), (2, 2)},
        ),
        # (
        #     {
        #         "x1": 0,
        #         "y1": 2,
        #         "x2": 2,
        #         "y2": 0,
        #     },
        #     {(2, 0), (1, 1), (2, 0)},
        # ),
    ],
)
def test_generate_points(input, output):
    assert generate_points(input) == output
