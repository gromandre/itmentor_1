'''
    Напишите программу для вывода таблицы умножения от 0 до 9.
    Используйте вложенный цикл for, print и range
    Пример:
    0*1 = 0
    0 *2 = 0
    …..
    9*1 = 9
    9*2=18
'''

def print_table_multiplication() -> None:
    for fist_num in range(10):
        for two_num in range(1, 10):
            end_char = " |" if two_num < 9 else ""
            print(f' {fist_num} * {two_num} = {fist_num*two_num:2}', end=end_char)
        print()

print_table_multiplication()