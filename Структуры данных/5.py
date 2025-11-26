import random
from itertools import count


# Реализуйте Пузырьковую сортировку

def buble_sort(list):
    swapped = False
    len_list = len(list)

    for i in range(len_list):
        for j in range(len_list - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True

        if not swapped:
            break

    return list

# Сортировка ставкой

def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp

    return alist





counts = 10
numbers = [random.randint(1, 10) for num in range(1, counts + 1)]

print(numbers)
# print(buble_sort(numbers))
print(insertion_sort(numbers))