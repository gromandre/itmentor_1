'''Создайте систему для обработки большого потока данных, используя генераторы. Реализуйте:'''

# Генератор, который имитирует чтение данных из файла (генерирует числа от 1 до 1000000)

def read_file(n: int = 1_000_000):
    for i in range(1, n + 1):
        yield i

# Генератор для фильтрации данных (только четные числа)

def filter_data(data):
    for el in data:
        if el % 2 == 0:
            yield el

# Генератор для преобразования данных (возведение в квадрат)

def pow_el_data(data):
    for el in data:
        yield el ** 2

# Функцию для агрегации результатов (сумма первых N элементов)
def agregate_el(data, n: int) -> int:
    result = 0
    i = 0

    for _ in data:
        if i < n:
            result += _
            i += 1
        else:
            break
    return result


data = read_file(10)
data = filter_data(data)
data = pow_el_data(data)
result_sum = agregate_el(data, 3)
print(result_sum)