## Шпоргалки

### #2
```python
from itertools import product, permutations

def f(x, y, z, w):
    return (x or (not y)) and (not (x == z)) and w


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    # repeat и кол-во переменных = количеству неизвестных ячеек
    table = [(a1, 0, 0, 1), (0, 0, 1, 1), (0, a2, a3, a4)]  # заполняем уникальными переменными
    if len(set(table)) == len(table):
        for p in permutations("xyzw"):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]
            # для каждой строчки проверяем фукнцию и сравниваем с результатов ф из условия
            if u:
                print(*p)
```

### #1
```python
from itertools import permutations

graph = "GF FE ED DA AG BG BA BC CB CD".split() 
# все возможные соединения (можно повторяться)
mat = "26 147 456 236 37 134 25".split()        
# номера заполненных столбцов каждой строки из условия (строго по таблице)

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    # перебираем все возможные пары: номер пункта (индекс) - буква
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
    # проверяем по каждому соединению, что их индексы есть в матрице соединений
    # нужно чтобы совпали все
        print(*i)
```

### #13
```python
from ipaddress import *
```

1. Определить адрес сети
```python
net = ip_network("IP/MASK", 0)
print(net)
```

2. Наиб / Наим кол-во 0 / 1 в bin записи маски подсети
```python
for mask in range(33):
    net = ip_network(f"IP/{mask}", 0)
    print(net, net.netmask)
    # 1.1.1.1/1 255.255.255.255
```

3. Определить сколько ip в сети
```python
net = ip_network('IP/MASK', 0)
c = 0
for ip in net:
    if CON in f'{ip:b}':
        c += 1

print(c)
```

4. Два узла в одной сети
```python
for mask in range(33):
    net1 = ip_network(f"IP1/{mask}", 0)
    net2 = ip_network(f"IP2/{mask}", 0)
    if net1 == net2:
        print(net1.netmask)
```

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
    # Первый any всегда. Во втором, если ход неудачный, то any.
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

- from sympy:
  - divisors - все делители числа (с 1 и самим числом)
  - factorint - разложение на простые делители (без 1 и самого числа)
- from re:
  - .match(pattern, str)
  - .split(pattern, str)
  - .findall(pattern, str)
    ```
    re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
    >>> ['foot', 'fell', 'fastest']
    re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
    >>> [('width', '20'), ('height', '10')]
    ```
  - .search(pattern, str)
