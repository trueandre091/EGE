from turtle import *


screensize(2000, 5000)
tracer(0)
k = 45
left(90)
pendown()

penup()
for i in range(10):
    rt(120)
    fd(10 * k)

pendown()
for i in range(7):
    fd(15 * k)
    rt(90)

for i in range(5):
    rt(60)
    fd(20 * k)
    rt(30)

penup()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(2)

done()