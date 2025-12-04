'''
    Создайте список с разными значениями,
    пройдитесь по нему в цикле и выведите на экран.
    (Сделайте тоже самое со словарем и выведите ключ и значение)
'''

my_list = [42, "hello", 3.14, True, None, [1, 2, 3], {"a": 1}, (5, 6), {1, 2, 3}, -7]

my_dict = {
    "name": "Alice",
    "age": 25,
    "height": 1.72,
    "is_active": True,
    "hobbies": ["music", "coding", "travel"],
    "score": None,
    "settings": {"theme": "dark", "volume": 80},
    "coords": (45.2, 12.8),
    "tags": {"python", "developer"},
    "balance": 1050.75
}

for el in my_list:
    print(el)
print()
for key, value in my_dict.items():
    print(key, ':', value)

