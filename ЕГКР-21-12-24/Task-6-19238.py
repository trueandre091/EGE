from turtle import *
tracer(0)
screensize(2000, 2000)
left(90)
pendown()
k = 30

for i in range(8):
  fd(16*k)
  rt(90)
  fd(22*k)
  rt(90)

penup()
fd(5*k)
rt(90)
fd(5*k)
lt(90)
pendown()

for i in range(8):
  fd(52*k)
  rt(90)
  fd(77*k)
  rt(90)

penup()
for x in range(-100, 100):
  for y in range(-100, 100):
    goto(x*k, y*k)
    dot(3)

done()

# 11 * 17 = 187
