'''
    Напишите программу для вывода на экран чисел от 0 до 100
    Вам понадобится цикл for, конструкция range и print
'''

def print_nums(user_num: int) -> None:
    for num in range(user_num + 1):
        print(num)

print_nums(10)
