from turtle import *

screensize(2000, 2000)
tracer(0)
left(90)
pendown()
k = 30

rt(30)
for i in range(3):
    rt(150)
    fd(6 * k)
    rt(30)
    fd(12 * k)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto( x * k, y * k)
        dot(3)

done()

