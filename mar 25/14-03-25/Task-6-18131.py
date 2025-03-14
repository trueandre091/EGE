from turtle import *

screensize(2000, 2000)
tracer(0)
k = 10
left(90)

for i in range(9):
    fd(22 * k)
    rt(90)
    fd(6 * k)
    rt(90)

penup()
fd(1 * k)
rt(90)
fd(5 * k)
lt(90)
pendown()

for i in range(9):
    fd(53 * k)
    rt(90)
    fd(75 * k)
    rt(90)

penup()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3)

done()







