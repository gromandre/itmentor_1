import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} заняла {end - start:.6f} секунд')
        return result
    return wrapper

@timer
def linear_search(list, target):
    for index in range(len(list)):
        if list[index] == target:
            return index
    else:
        return -1


@timer
def binari_search(list, target):
    left = 0
    right = len(list)-1

    while(left <= right):
        index = int((right + left)/2)

        if list[index] == target:
            return index
        if list[index] > target:
            right = index - 1
        if list[index] < target:
            left = index + 1
    else:
        return -1

cont = 1000000
numbers = [num for num in range(1, cont+1)]

print(linear_search (numbers, cont-10))
print(binari_search(numbers, cont-10))
