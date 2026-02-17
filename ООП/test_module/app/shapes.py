from app.basicshape import BasicShape

class Shapes:
    def __init__(self):
        self._shapes: list[BasicShape] = []

    def __enter__(self):
        # возвращаем объект, с которым будем работать в with
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Суммарная площадь фигур: {self.square}')
        # False → исключения (если были) не подавляются
        return False

    def add_shape(self, shape: BasicShape):
        if not isinstance(shape, BasicShape):
            raise TypeError ('Можно добавлять только объекты BasicShape')
        self._shapes.append(shape)

    @property
    def square(self):
        return sum(shape.square for shape in self._shapes)

    @property
    def perimeter(self):
        return sum(shape.perimeter for shape in self._shapes)

    def remove_shape(self, shape: BasicShape):
        self._shapes.remove(shape)

    def add(self, shape: BasicShape, point: tuple[float, float]):
        if shape not in self._shapes:
            raise ValueError('Фигура не принадлежит Shapes')

        if not (isinstance(point, tuple) and len(point) == 2):
            raise TypeError('Точка должна быть кортежем из двух чисел')

        if not all(isinstance(c, (int, float)) for c in point):
            raise TypeError('Координаты должны быть числами')

        shape._add(point)