from turtle import *

screensize(2000, 2000)
tracer(0)
k = 20
left(90)
pendown()

for i in range(7):
    fd(9 * k)
    rt(90)
    fd(16 * k)
    rt(90)

penup()

fd(3 * k)
rt(90)
fd(4 * k)
lt(90)
pendown()

for i in range(4):
    fd(7 * k)
    rt(90)
    fd(13 * k)
    rt(90)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(5, "white")

done()



