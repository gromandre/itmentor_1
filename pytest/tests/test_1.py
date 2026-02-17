from app import divide
import pytest

@pytest.mark.parametrize("a, b, result", [
    (6, 3, 2),
    (5, 2, 2.5),
    (10, 4, 2.5),
])
def test_divide(a, b, result):
    assert divide(a,b) == result


@pytest.mark.parametrize("a, b", [
    ("5", 2),
    (5, "2"),
    ("5", "2"),
])
def test_divide_invalid_type(a, b):
    with pytest.raises(TypeError, match='Only numbers allowed'):
        divide(a, b)


def test_divide_zero():
    with pytest.raises(ValueError, match='ccc'):
        divide(10, 0)

