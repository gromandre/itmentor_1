import pytest
from app.basicshape import BasicShape

# test __init__
def test_init_points_must_be_list():
    with pytest.raises(TypeError, match="points должен быть списком точек"):
        BasicShape(points="not a list")

def test_init_min_3_points():
    with pytest.raises(ValueError, match="Для многоугольника нужно минимум 3 точки"):
        BasicShape(points=[(0,0),(0,1)])

@pytest.mark.parametrize("bad_point", [
    ("1", 2),
    (1, None),
    (object(), 2),
])
def test_init_point_coords_must_be_numbers(bad_point):
    with pytest.raises(TypeError, match=r"Координаты точки 0 должны быть числами"):
        BasicShape(points=[bad_point, (0,0), (0,1)])

def test_init_success_saves_points():
    pts = [(0, 0), (1, 0), (0, 1)]
    shape = BasicShape(points=pts)
    assert shape.points == pts

# test perimeter
def test_perimeter_square_1x1():
    shape = BasicShape(points=[(0, 0), (1, 0), (1, 1), (0, 1)])
    assert shape.perimeter == pytest.approx(4.0, rel=1e-9)

def test_perimeter_triangle_3_4_5():
    # стороны: 3, 4, 5
    shape = BasicShape(points=[(0, 0), (3, 0), (3, 4)])
    assert shape.perimeter == pytest.approx(12.0, rel=1e-9)

# test square
def test_square_square_2x2():
    shape = BasicShape(points=[(0, 0), (2, 0), (2, 2), (0, 2)])
    assert shape.square == pytest.approx(4.0, rel=1e-9)

# test _add
def test_add_appends_point_and_changes_perimeter_and_square():
    shape = BasicShape(points=[(0, 0), (1, 0), (0, 1)])
    old_points_len = len(shape.points)
    old_perimeter = shape.perimeter
    old_square = shape.square

    assert shape._add((1, 1)) is None
    assert len(shape.points) == old_points_len + 1
    assert shape.points[-1] == (1, 1)

    assert len(shape.points) == 4
    assert shape.perimeter != old_perimeter
    assert shape.square != old_square

# test _add_
def test_add_two_shapes_returns_sum_of_areas():
    a = BasicShape(points=[(0, 0), (2, 0), (2, 2), (0, 2)])   # 4
    b = BasicShape(points=[(0, 0), (1, 0), (0, 1)])           # 0.5
    assert (a + b) == pytest.approx(4.5, rel=1e-9)

def test_add_with_non_shape_returns_not_implemented():
    shape = BasicShape(points=[(0, 0), (1, 0), (0, 1)])
    assert shape.__add__(123) is NotImplemented

    # и "нормальное" сложение тогда должно упасть TypeError
    with pytest.raises(TypeError):
        _ = shape + 123