def r(n):
    return n **0.5 == int(n**0.5)
ans = {}
def f(s, e, h):
    if s == e:
        if h not in ans:
            ans[h] = 1
        else:
            ans[h] += 1
    if s > e:
        return
    f(s + 2 - r(s + 2), e, h + r(s + 2))
    f(s + 3 - r(s + 3), e, h + r(s + 3))
    f(s * 3 - r(s * 3), e, h + r(s * 3))

f(5, 50, 0)
print(ans)

