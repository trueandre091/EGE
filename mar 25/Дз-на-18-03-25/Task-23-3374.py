from functools import lru_cache

@lru_cache(None)
def f(s, e, t):
    if (s == e) and (len(set(t)) == len(t)):
        return 1
    if s < -50 or s > 50 or len(set(t)) != len(t):
        return 0
    return f(s+2, e, t + (s + 2,)) + f(s - 3, e, t + (s - 3,))

print(f(1, 30, (1,)))
