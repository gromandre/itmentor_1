'''
    Даны два целых числа: D(день) и M (месяц), определяющие правильную дату невисокосного года.
    Вывести значения D и M для даты, следующей за указанной.
'''

def get_days_in_month(number_month: int) -> int:
    match number_month:
        case 2:
            return 28
        case 4 | 6 | 9 | 11:
            return 30
        case _:
            return 31


def get_second_day(day: int, month: int) -> str:

    days_in_month = get_days_in_month(month)

    if day < days_in_month:
        return f'D{day+1} M{month}'
    elif month < 12:
        return f'D{1} M{month + 1}'
    else:
        return f'D{1} M{1}'

d = 28
m = 2

try:
    print(get_second_day(d, m))
except Exception as e:
    print(e)

