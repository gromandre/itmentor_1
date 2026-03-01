from functools import lru_cache


def search_num_fibo(n):
    if n < 2:
        return n
    return search_num_fibo(n-1) + search_num_fibo(n-2)

def search_simple_num(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def search_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result




