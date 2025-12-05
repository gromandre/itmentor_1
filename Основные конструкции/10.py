'''
Вывести значения функции y=x^2 от 1 до 10 с шагом 0.5
'''

start, end, step = 1, 10, 0.5

x = start

while x <= end:
    print(f'y: {x**2}, x: {x}')
    x += step