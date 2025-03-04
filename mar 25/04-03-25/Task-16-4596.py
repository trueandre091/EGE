from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 3: return 1
    if n > 2 and n % 2 == 0: f(n - 1) + n - 1
    return f(n - 2) + 2*n - 1

print(f(34))

