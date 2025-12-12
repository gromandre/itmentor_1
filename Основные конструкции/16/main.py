'''
Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0.

 Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользователю
 попробовать еще раз с другими коэффициентами.

 При выполнении скрипта в лог должна записываться  информация о успехе или неудаче операции.
'''
import logging
import math

logger = logging.getLogger()
FORMAT = '%(name)s %(asctime)s %(levelname)s %(message)s'

file_handler = logging.FileHandler(f'{__name__}.log', mode='w')
file_handler.setLevel(logging.DEBUG)

logging.basicConfig(level=logging.DEBUG, format=FORMAT, handlers=[file_handler])

logger.debug(f"Тест логгера в {__name__}...")

a = 1
b = 6
c = 8


def solve_quadratic_equation(a: float, b: float, c: float) -> tuple:
    discriminant = (b ** 2) - (4 * a * c)

    if discriminant > 0:
        x1 = ((-b - math.sqrt(discriminant)) / (2 * a))
        x2 = ((-b + math.sqrt(discriminant)) / (2 * a))

        logger.info(f"Successful with result: x1: {x1}, x2: {x2}.")
        return x1, x2

    elif discriminant == 0:
        x = -b / (2 * a)
        logger.info(f"Successful with result: x: {x}.")
        return (x,)

    else:
        logger.error(f'Дискриминант {discriminant} меньше 0, уравнение не имеет действительных корней')
        print(f'Дискриминант {discriminant} отрицателен, попробуйте еще раз с другими коэффициентами')
        return None


print(solve_quadratic_equation(a, b, c))
