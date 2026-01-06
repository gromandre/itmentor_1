'''
    Создайте класс BasicShape. Данный класс представляет из себя многогранник с любым количеством точек,
    переданных при инициализации в формате [(x1, y1), (x2, y2), (x3, y3), …].
'''

class BasicShape:
    def __init__(self, points: list[tuple[float, float]]):
        if not isinstance(points, list):
            raise TypeError('points должен быть списком точек')

        if len(points) < 3:
            raise ValueError('Для многоугольника нужно минимум 3 точки')

        for i, point in enumerate(points):
            if not (isinstance(point, tuple) and len(point) == 2):
                raise TypeError(f'Точка {i} должна быть кортежем из двух чисел')
            if not all(isinstance(cord, (int, float)) for cord in point):
                raise TypeError(f'Координаты точки {i} должны быть числами')

        self.points = points

# shape = BasicShape([(0,0), (4,0), (4,3)])
# shape = BasicShape([(0,0), (4,0)])
# shape = BasicShape([(0,0), (4,'a'), (4,3)])

