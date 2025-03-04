from turtle import *

screensize(1000, 1000)
tracer(0)
k = 20
left(90)
pendown()

for i in range(2):
    fd(5 * k)
    lt(90)
    back(13 * k)
    lt(90)

penup()
back(10 * k)
rt(90)
fd(9 * k)
lt(90)
pendown()

for i in range(2):
    fd(11 * k)
    rt(90)
    fd(7 * k)
    rt(90)

penup()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3)

done()
