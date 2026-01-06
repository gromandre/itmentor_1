class Example:
    def __init__(self):
        self.existing = "существующий атрибут"

    def __getattr__(self, name):
        print(f"__getattr__ вызван для {name}")
        return f"значение по умолчанию для {name}"


obj = Example()
#print(obj.existing)  # напрямую возвращает "существующий атрибут"
print(obj.missing)  # вызывает __getattr__("missing")