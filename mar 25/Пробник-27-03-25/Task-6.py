from turtle import *

screensize(2000, 2000)
tracer(0)
k = 20
left(90)
pendown()

for i in range(9):
    fd(17 * k)
    lt(90)
    fd(8 * k)
    lt(90)
    fd(17 * k)

penup()
lt(90)
fd( 3 * k)
rt(90)
fd(5 * k)
lt(90)
pendown()

for i in range(4):
    fd(97 * k)
    rt(90)
    fd(132 * k)
    rt(90)

penup()

for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(5, "white")

done()