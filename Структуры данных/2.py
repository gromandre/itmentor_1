import random
import time

# Функция поиска минимального и минимального числа
def serch_min_and_max_num(list):

    min_num, max_num = None, None

    for num in list:
        if not min_num:
            min_num, max_num = num, num
        
        if min_num > num:
            min_num = num
        if max_num < num:
            max_num = num

    return min_num, max_num

import time

def timer(func):
    def wrapper(*args, **kwargs):
        # Если это НЕ рекурсивный уровень → измеряем время
        if not kwargs.get("_is_recursive"):
            start = time.perf_counter()

            # Первый вызов: помечаем рекурсию
            result = func(*args, **kwargs, _is_recursive=True)

            end = time.perf_counter()
            print(f'{func.__name__} заняла {end - start:.6f} секунд')
            return result
        else:
            # Рекурсивные вызовы: ничего не меряем
            return func(*args, **kwargs)
    return wrapper


# Сортировка выбором
@timer
def selection_sort(list, _is_recursive=False):
    copy_list = list[:]
    new_list = []

    for num in range(1, len(copy_list)+1):
        min_num = serch_min_and_max_num(copy_list)[0]
        index_min_num = copy_list.index(min_num)
        new_list.append(copy_list.pop(index_min_num))

    return new_list

# Быстрая сортировака
@timer
# 2 1 3
def q_sort(list, _is_recursive=False):
    if len(list) < 2:
        return list
    else:
        separator = list[0]
        prev = [num for num in list[1:] if separator >= num]
        second = [num for num in list[1:] if separator < num]
        return  q_sort(prev, _is_recursive=True) + [separator] + q_sort(second, _is_recursive=True)

# Генерация списка из 10 случайных чисел от 1 до 99
random_list = [random.randint(1,100) for num in range(1, 11)]

min_num, max_num = serch_min_and_max_num(random_list)

print(f'Рандомный список: {random_list}')
print(f'Сортировка выбором: {selection_sort(random_list)}')
print(f'Быстрая сортировка: {q_sort(random_list)}')


