from turtle import *

screensize(2000, 2000)
tracer(0)
k = 20
left(90)
penup()

for i in range(2):
    pendown()
    for j in range(2):
        fd(8 * k)
        rt(90)
        fd(8 * k)
        rt(90)
    penup()
    fd(6 * k)
    rt(90)
    fd(6 * k)
    lt(90)

rt(180)
fd(4 * k)
pendown()
for i in range(4):
    fd(8 * k)
    rt(270)

penup()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(10, "white")

done()















