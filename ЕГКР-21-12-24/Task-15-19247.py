for A in range(1, 10000):
  flag = True
  for x in range(1, 1000):
    for y in range(1, 1000):
      k1 = x - 3*y < A
      k2 = y > 400
      k3 = x > 56
      if not (k1 or k2 or k3):
        flag = False
        break
  if flag:
    print(A)
    break

# 12

