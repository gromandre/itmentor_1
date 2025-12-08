'''
Напишите рекурсивную функцию, которая находит факториалы чисел от 1 до 5 (включительно).
'''

def factorial(n):
    if n == 1:
        return n

    return n * factorial(n - 1)

print(factorial(5))
