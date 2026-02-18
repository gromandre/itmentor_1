import pytest

from app.shapes import Shapes
from app.quadrilateral import Quadrilateral


@pytest.fixture
def rect1():
    # квадрат 1x1: площадь 1, периметр 4
    return Quadrilateral([(0, 0), (0, 1), (1, 1), (1, 0)])


@pytest.fixture
def rect2():
    # прямоугольник 2x1: площадь 2, периметр 6
    return Quadrilateral([(0, 0), (0, 1), (2, 1), (2, 0)])


def test_add_shape_ok(rect1):
    s = Shapes()
    s.add_shape(rect1)
    assert s.square == 1.0


def test_add_shape_type_error():
    s = Shapes()
    with pytest.raises(TypeError):
        s.add_shape("not shape")


def test_square_sum(rect1, rect2):
    s = Shapes()
    s.add_shape(rect1)
    s.add_shape(rect2)
    assert s.square == 3.0


def test_perimeter_sum(rect1, rect2):
    s = Shapes()
    s.add_shape(rect1)
    s.add_shape(rect2)
    assert s.perimeter == 10.0  # 4 + 6


def test_remove_shape(rect1):
    s = Shapes()
    s.add_shape(rect1)
    s.remove_shape(rect1)
    assert s.square == 0


def test_add_point_ok(rect1):
    s = Shapes()
    s.add_shape(rect1)
    s.add(rect1, (2, 2))
    assert rect1.points[-1] == (2, 2)


def test_add_point_shape_not_in_shapes(rect1):
    s = Shapes()
    with pytest.raises(ValueError):
        s.add(rect1, (2, 2))


def test_add_point_invalid_type(rect1):
    s = Shapes()
    s.add_shape(rect1)
    with pytest.raises(TypeError):
        s.add(rect1, [2, 2])  # не tuple


def test_add_point_invalid_coords(rect1):
    s = Shapes()
    s.add_shape(rect1)
    with pytest.raises(TypeError):
        s.add(rect1, ("2", 2))  # координаты не числа