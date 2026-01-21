'''Создайте систему валидации данных, используя функции высшего порядка'''
from charset_normalizer.utils import unicode_range


# Функцию `create_validator()`, которая принимает условие и возвращает функцию-валидатор
def create_validator(condition):
    def validator(value):
        return condition(value)
    return validator

# Функцию `compose_validators()`, которая объединяет несколько валидаторов
def compose_validators(*validators):
    def combined(value):
        return all(fn(value) for fn in validators)
    return combined

# Функцию `validate_data()`, которая применяет валидаторы к данным
def validate_data(value, validator):
    return validator(value)


# Создайте несколько различных валидаторов (длина строки, диапазон чисел, email формат)

# длина строки
def len_str_validator(n: int):
    return create_validator(lambda a_str: len(a_str) == n)

len_12 = len_str_validator(12)

print("Длина строки")
print(f"len_5('qwertyqwerty'): {len_12('qwertyqwerty')}")
print(f"len_5('qwerty'): {len_12('qwerty')}")
print()


# диапазон чисел
def number_range_validator(start: int, end: int):
    return create_validator(lambda number: start < number <= end)

range_1_10 = number_range_validator(1, 10)
true_range = range_1_10(5)
false_range = range_1_10(11)

print("Диапазон чисел")
print("{}: {}".format("range_1_10(5)", true_range))
print("{}: {}".format("range_1_10(11)", false_range))
print()


# email формат
def email_format_validator(domain):
    return create_validator(lambda email: email.endswith(domain))

gmail_validator = email_format_validator('@gmail.com')
print("email формат")
print("{}: {}".format("gmail_validator('123@gmail.com')", gmail_validator('123@gmail.com')))
print("{}: {}".format("gmail_validator('123@@.com')", gmail_validator('123@@.com')))
print()

# композиция
gmail_and_len = compose_validators(len_12, gmail_validator)

# применение
res = validate_data("12@gmail.com", gmail_and_len)
print("12@gmail.com", res)



