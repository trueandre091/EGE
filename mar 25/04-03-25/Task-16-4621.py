from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 3: return 2
    if n > 2 and n % 2 == 0:
        return 2 * f(n - 2) - f(n - 1) + 2
    return 2 * f(n - 1) - f(n - 2) - 2


print(f(17))
