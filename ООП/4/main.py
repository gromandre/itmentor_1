'''
    Для класса BasicShape напишите методы perimeter и square, вычисляющие периметр и площадь фигуры
    соответственно (считаем, что две последовательно идущие точки, переданные при инициализации объекта,
    образуют грань, а последняя точка образует грань с первой в списке). Для вычисления площади используется
    Формула площади Гаусса.
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

    def square(self):
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


shape = BasicShape([(0,0), (4,0), (4,3), (0,3)])
print(shape.perimeter())  # 14.0
print(shape.square())     # 12.0
