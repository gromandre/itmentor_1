'''
    Добавьте в класс Shapes метод add, который добавляет новую точку в одну из фигур.
    Сделайте так, чтобы добавить точку можно было только через метод Shapes.add(),
    исключив возможность использования метода BasicShapes.add() фигуры, содержащейся внутри Shapes.
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

    @property
    def perimeter(self):
        perimeter = 0
        len_list_points = len(self.points)

        for i in range(len_list_points):
            if i == len_list_points - 1:
                x = self.points[i][0] - self.points[0][0]
                y = self.points[i][1] - self.points[0][1]
            else:
                x = self.points[i + 1][0] - self.points[i][0]
                y = self.points[i + 1][1] - self.points[i][1]

            perimeter += (x ** 2 + y ** 2) ** 0.5

        return perimeter

    @property
    def square(self) -> float:
        len_list_points = len(self.points)
        sum1 = 0
        sum2 = 0

        for i in range(len_list_points):
            if i == len_list_points - 1:
                sum1 += self.points[i][0] * self.points[0][1]
                sum2 += self.points[i][1] * self.points[0][0]
            else:
                sum1 += self.points[i][0] * self.points[i + 1][1]
                sum2 += self.points[i][1] * self.points[i + 1][0]

        return 0.5 * abs(sum1 - sum2)

    def _add(self, coordinate: tuple[float, float]):
        return self.points.append(coordinate)

    def __add__(self, other):
        if not isinstance(other, BasicShape):
            return NotImplemented
        return self.square + other.square


class Quadrilateral(BasicShape):
    @staticmethod
    def get_len_side(point1: tuple[float, float], point2: tuple[float, float]) -> float:
        '''Передаем 2 точки: и возвращаем длину между ними'''

        x1, y1 = point1
        x2, y2 = point2
        x, y = x2 - x1, y2 - y1
        return (x ** 2 + y ** 2) ** 0.5

    def get_sides(self) -> tuple:
        '''Высчитываем длину каждой стороны и диагонали'''

        side_a1 = self.get_len_side(self.points[0], self.points[1])
        side_b1 = self.get_len_side(self.points[1], self.points[2])
        side_a2 = self.get_len_side(self.points[2], self.points[3])
        side_b2 = self.get_len_side(self.points[3], self.points[0])
        diagonal1 = self.get_len_side(self.points[2], self.points[0])
        diagonal2 = self.get_len_side(self.points[3], self.points[1])
        return side_a1, side_b1, side_a2, side_b2, diagonal1, diagonal2

    @property
    def is_rectangle(self) -> bool:
        if not len(self.points) == 4:
            return False

        sides = self.get_sides()
        equality_parties = sides[0] == sides[2] and sides[1] == sides[3]
        equality_diagonals = sides[4] == sides[5]

        if equality_parties and equality_diagonals:
            return True
        else:
            return False

    @property
    def is_square(self) -> bool:
        if len(self.points) != 4 or not self.is_rectangle:
            return False

        sides = self.get_sides()

        if sides[0] == sides[2] == sides[1] == sides[3] and sides[4] == sides[5]:
            return True
        else:
            return False

    def add(self, coordinate: tuple[float, float]):
        raise NotImplementedError('Нельзя добавлять точки в Quadrilateral: фигура должна иметь ровно 4 точки')

class Shapes:
    def __init__(self):
        self._shapes: list[BasicShape] = []

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


sh = Shapes()
sq = BasicShape([(0,0), (0,8), (4,8), (10,0)])
sq2 = BasicShape([(0,0), (0,8), (4,8), (2,0)])
sh.add_shape(sq)
sh.add_shape(sq2)

sh.add(sq, (9,9))
print(sh._shapes[0].__dict__)

