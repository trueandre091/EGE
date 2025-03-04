from turtle import *

screensize(2000, 2000)
tracer(0)
k = 20
left(90)
penup() # заметил

for i in range(9):
    fd(15 * k)
    rt(90)
    fd(25 * k)
    rt(90)

penup()
back(10 * k)
rt(90)
pendown()

for i in range(8):
    fd(15 * k)
    lt(90)
    fd(25 * k)
    lt(90)

penup()
fd(6 * k)
lt(90)
pendown()
for i in range(7):
    fd(15 * k)
    rt(90)
    fd(25 * k)
    rt(90)

penup()
for x in range(-25, 40):
    for y in range(-25, 40):
        goto(x * k, y * k)
        dot(3)

done()

# 112




