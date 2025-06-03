from turtle import *

screensize(2000, 2000)
tracer(0)
k = 20
left(90)

for i in range(9):
    fd(27 * k)
    rt(90)
    fd(30 * k)
    rt(90)

penup()
fd(3 * k)
rt(90)
fd(6 * k)
lt(90)
pendown()

for i in range(9):
    fd(77 * k)
    rt(90)
    fd(66 * k)
    rt(90)

penup()

for x in range(-50, 50):
    for y in range(-50 ,50):
        goto(x * k, y * k)
        dot(5, "white")

done()

# 48 * 2 = 96