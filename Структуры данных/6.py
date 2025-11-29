import sys

def create_tuple_and_list(len):
    atuple = tuple(range(1, len + 1))
    alist = list(atuple)
    return atuple, alist

def add_el(arr, el):
    result = arr.append(el)
    print(f'Список {arr} после добавления {el} занимает {sys.getsizeof(arr)} байт')
    return result

my_tuple, my_list = create_tuple_and_list(8)
print(f'Кортеж: {my_tuple} занимает {sys.getsizeof(my_tuple)} байт')
print(f'Список: {my_list} занимает {sys.getsizeof(my_list)} байт')


add_el(my_list, 3)