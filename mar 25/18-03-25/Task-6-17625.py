from turtle import *
tracer(0)
screensize(2000, 2000)
k = 20
left(90)

for i in range(10):
    fd(22 * k)
    rt(90)
    fd(16 * k)
    rt(90)
penup()
fd(1 * k)
rt(90)
fd(1 * k)
lt(90)
pendown()
for i in range(10):
    fd(72 * k)
    rt(90)
    fd(79 * k)
    rt(90)

penup()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(5, "white")

done()