from turtle import *

screensize(2000, 2000)
tracer(0)
left(90)
pendown()
k = 10

for i in range(3):
    fd(7 * k)
    rt(90)
    fd(12 * k)
    rt(90)

penup()
fd(4 * k)
rt(90)
fd(6 * k)
lt(90)
pendown()

for i in range(4):
    fd(83 * k)
    rt(90)
    fd(77 * k)
    rt(90)

penup()

for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3)

done()


