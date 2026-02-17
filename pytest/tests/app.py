def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Only numbers allowed")
    if b == 0:
        raise ValueError("ccc")
    return a / b