import pytest
from main import *

@pytest.mark.parametrize(
    'number, expected',
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (10, 55),
    ]
)
def test_search_num_fibo(number, expected):
    assert search_num_fibo(number) == expected


@pytest.mark.parametrize(
    'number, expected',
    [
        (7, True),
        (10, False),
    ]
)
def test_search_simple_num(number, expected):
    assert search_simple_num(number) == expected

@pytest.mark.parametrize(
    "number, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
    ]
)
def test_search_factorial(number, expected):
    assert search_factorial(number) == expected



