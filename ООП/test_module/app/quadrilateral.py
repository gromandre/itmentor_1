from app.basicshape import BasicShape

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