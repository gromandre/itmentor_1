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

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} заняла {end - start:.6f} секунд')
        return result
    return wrapper

# Сортировка выбором
@timer
def selection_sort(list):
    new_list = []

    for num in range(1, len(list)+1):
        min_num = serch_min_and_max_num(list)[0]
        index_min_num = list.index(min_num)
        new_list.append(list.pop(index_min_num))

    return new_list

# Генерация списка из 10 случайных чисел от 1 до 99
random_list = [random.randint(1,100) for num in range(1, 11)]

min_num, max_num = serch_min_and_max_num(random_list)

print(random_list)
print(selection_sort(random_list))
