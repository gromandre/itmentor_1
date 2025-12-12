'''
Написать программу для нахождения среднего арифметического списка чисел.
Если при вводе списка чисел была допущена ошибка (например, был передан не список, а строка),
программа должна корректно обработать эту ошибку и выдать соответствующее сообщение.
 Информация об ошибках должна быть записана в лог.
'''

import logging

FORMAT = '%(name)s %(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s'
fail_handler = logging.FileHandler('errors.log', mode='w', encoding='utf-8')
fail_handler.setLevel(logging.ERROR)

logging.basicConfig(level=logging.ERROR, format=FORMAT, handlers=[fail_handler])

logger = logging.getLogger()
def search_average_arithmetic_number(user_list: list) -> float:
    if not isinstance(user_list, list):
        logger.error(f'user_list не является списком: {user_list!r}')
        raise Exception('Нужно передать именно список')

    len_list = len(user_list)
    if len_list == 0:
        logger.error(f'Список пуст: len_list=={len_list}')
        raise Exception('Переданный список пуст')

    summ_numbers = 0

    for num in user_list:
        if not isinstance(num, (int, float)):
            logger.error(f'Список содержит не только числа: {user_list}')
            raise Exception('Список должен содержать только числа!')
        summ_numbers += num

    return summ_numbers / len_list


alist = 1 #[1, 2, 3, '']

try:
    result = search_average_arithmetic_number(alist)
    print(result)
except Exception as e:
    print("Ошибка:", e)

