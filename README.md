## Шпоргалки

### #19-21

Одна куча:
```python
def f(s, m):                # s - количество камней; m - количество оставшихся ходов
    if s > Z:               # условие окончания игры
        return m % 2 == 0   # на чьём ходу закончилась игра: если на ходу второго (True) - победил первый
    if m == 0:              
        return 0
    h = [f(s - 2, m - 1), f(s // 3, m - 1), f(s - 5, m - 1)]    # все возможные ходы
    return any(h) if m % 2 != 0 else all(h)
    # Для победы первого нужно чтобы хотя бы один ход вёл к победе, для второго - все
```

Две кучи + нельзя два раза подряд ходить одним ходом:
```python
def f(a, b, m, p):
    # a, b - количество камней в двух кучах; m - количество оставшихся ходов; p - обозначение последнего сделанного хода
    if a + b > Z:           # условие окончания игры
        return m % 2 == 0
    if m == 0: 
        return 0
    h = []
    if p != '11': h += [f(a-4, b, m-1, '11')]
    if p != '21': h += [f(a, b - 4, m-1, '21')]
    if p != '12': h += [f(a//3, b, m-1, '12')]
    if p != '22': h += [f(a, b//3, m-1, '22')]
    # Та же логика всех возможных ходов, но мы не учитываем повторный ход
    return any(h) if m % 2 != 0 else all(h)
```

### #23

```python
from sys import setrecursionlimit
setrecursionlimit(10**6)

def f(start, end):                  # от какого до какого числа нужно дойти
    if start < end or start == Z:   # Z - числа, которые НЕ должны быть в пути, если есть
        return 0
    if start == end:
        return 1
    if start > end:
        return f(start-1, end) + f(start//3, end) + f(start//4, end)    # все возможные ходы складываем

print(f(START, R) * f(R, END)) # R - числа, которые должны быть в пути, если есть
```

### Общее 
Полезные функции:

- from sympy: factorint
- from re: 
  - .match(pattern, str) \
    .split(pattern, str) \
    .findall(pattern, str) \
    ```
    re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
    >>> ['foot', 'fell', 'fastest']
    re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
    >>> [('width', '20'), ('height', '10')]
    ```
    .search(pattern, str)