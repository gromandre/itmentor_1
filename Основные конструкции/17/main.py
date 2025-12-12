'''
Написать программу для генерации случайных чисел в заданном диапазоне.
Если пользователь ввел недопустимые границы диапазона (например, меньше нуля),
программа должна вывести ошибку и попросить ввести диапазон заново.
Информация об ошибках должна быть записана в лог.
'''

import random
import logging

FORMAT = '%(name)s %(asctime)s %(levelname)s %(message)s'
file_handler = logging.FileHandler('errors.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.ERROR)

logging.basicConfig(level=logging.ERROR, format=FORMAT, handlers=[file_handler])
logger = logging.getLogger()
def check_user_input(border: str) -> int:
    while True:
        try:
            user_input = int(input(f'Введите {border} границу диапазона: '))

            if user_input < 0:
                logger.error(f'Число пользователя меньше 0: "{user_input}"')
                print('Число должно быть больше 0')
                continue

            return user_input

        except ValueError as e:
            logger.error(f'Пользователь ввел не число: {e}')
            print(f'Вы ввели не число')
def generate_number_in_range() -> int:
    while True:
        low_border = check_user_input('нижнюю')
        high_border = check_user_input('верхнюю')

        if low_border <= high_border:
            return random.randrange(low_border, high_border)
        else:
            print('Ошибка! Нижний дипазон больше верхнего')
            logger.error(f'Нижний дипазон больше верхнего: {low_border} > {high_border}' )



result = generate_number_in_range()
print(result)