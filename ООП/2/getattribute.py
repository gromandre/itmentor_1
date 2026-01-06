class Example:
    def __init__(self):
        self.existing = "существующий атрибут"

    def __getattribute__(self, name):
        print(f"__getattribute__ вызван для {name}")
        # Важно: используем super() для избежания рекурсии
        return super().__getattribute__(name)


obj = Example()
print(obj.existing)  # всегда вызывает __getattribute__