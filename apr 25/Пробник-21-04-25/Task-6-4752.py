from turtle import *

screensize(2000, 2000)
tracer(0)
k = 50
left(90)
pendown()

dot(5)

for i in range(15):
    fd(4 * k)
    rt(60)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3)

done()


