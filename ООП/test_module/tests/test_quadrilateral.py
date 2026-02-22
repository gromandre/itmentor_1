import pytest
from app.quadrilateral import Quadrilateral

@pytest.fixture
def shape():
    return Quadrilateral([(0,0), (0,1), (1,0), (1,1),])

def test_get_len_side(shape):
    assert shape.get_len_side((0,0), (0,1)) == 1.0

def test_is_rectangle(shape):
    assert shape.is_rectangle

def test_add(shape):
    with pytest.raises(NotImplementedError):
        shape.add((0, 0))