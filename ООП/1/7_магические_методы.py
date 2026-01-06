class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Пример зачем это может быть нужно
    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Доступ запрещен')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('Недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)

try:
    a = Point(1,2)
    a1 = a.y = 5

    print(a1)
except Exception as e:
    print(e)

try:
    a = Point(1,2)
    a1 = a.z = 5

    print(a1)
except Exception as e:
    print(e)