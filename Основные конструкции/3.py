'''
    Напишите программу для подсчета среднего числа всех введенных пользователям чисел.
    Ввод пользователя должен осуществляться с помощью input. Если пользователь вводит ноль, то на экран
'''

from typing import List, Optional
def calculating_average_number() -> Optional[float]:
    """
       Функция запрашивает у пользователя числа до ввода 0.
       Возвращает среднее арифметическое введённых чисел.

       Returns:
           float: среднее арифметическое введённых чисел,
                  или None, если пользователь не ввёл ни одного числа.
       """
    count_user_input: int = 0
    user_numbers: List[float] = []

    while True:
        try:
            user_input: float = float(input('Введите число, \nдля отмены введите 0: '))
            if user_input == 0:
                break
            user_numbers.append(user_input)
            count_user_input += 1
        except ValueError:
            print('Упс. Вы ввели не число, попробуйте еще раз.')

    if count_user_input == 0:
        return None

    return sum(user_numbers)/count_user_input

print(calculating_average_number())