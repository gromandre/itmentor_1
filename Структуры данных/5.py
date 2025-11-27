import random
import time

def generate_alist(counts):
    return [random.randint(1, 100) for num in range(1, counts + 1)]
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Время выполнения функции {func.__name__} составило {end - start:.6f} секунд')
        return result
    return wrapper





# Реализуйте Пузырьковую сортировку
@timer
def buble_sort(alist):
    swapped = False
    len_alist = len(alist)

    for i in range(len_alist):
        for j in range(len_alist - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                swapped = True

        if not swapped:
            break

    return alist

# Сортировка ставкой
@timer
def insertion_sort(alist):
    index = None
    for i in range(len(alist)):
        min_num = alist[i]
        for j in range(i +1, len(alist) ):
            alist_j = alist[j]
            if alist[j] < min_num:
                min_num = alist[j]
                index = j

        if min_num != alist[i]:
            alist[i], alist[index] = alist[index], alist[i]

    return alist
nums1 = generate_alist(10)
nums2 = nums1.copy()

print(nums1)
print(buble_sort(nums1))
print('--------')
print(nums2)
print(insertion_sort(nums2))

