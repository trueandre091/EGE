from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 1: return 0
    if n % 2: return f(n - 1) + 3 * n**2
    return n // 2 + f(n - 1) + 2

print(f(49))

