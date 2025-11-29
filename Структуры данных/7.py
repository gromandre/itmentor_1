def demo_hashing():
    print("1. Хэширование разных типов данных")

    values = [
        42,                     # int
        3.14,                   # float
        "hello",                # str
        (1, 2, 3),              # tuple
        True,                   # bool
    ]

    for v in values:
        print(f"Значение: {v!r:10}  | тип: {type(v).__name__:10} | hash: {hash(v)}")

    print("\n2. Почему некоторые типы нельзя использовать как ключи")

    try:
        bad_dict = { [1, 2, 3]: "list" }
    except TypeError as e:
        print("Ошибка при использовании списка как ключа:", e)

    try:
        bad_dict = { {1, 2, 3}: "set" }
    except TypeError as e:
        print("Ошибка при использовании множества как ключа:", e)


    print("\n3. Коллизии хэш-функции")

    # Пример искусственной коллизии
    class BadHash:
        def __init__(self, value):
            self.value = value
        def __hash__(self):
            return 1  # Все объекты имеют одинаковый хэш
        def __eq__(self, other):
            return self.value == other.value

    a = BadHash("A")
    b = BadHash("B")

    print(f"Хэш объекта a: {hash(a)}")
    print(f"Хэш объекта b: {hash(b)}")

    print("\nДобавляем объекты в словарь:")
    d = {a: "Первый", b: "Второй"}

    print("Результат словаря:", d)



if __name__ == "__main__":
    demo_hashing()
