from turtle import *

screensize(2000, 2000)
tracer(0)
k = 20
left(90)


for i in range(3):
    fd(2 * k)
    rt(90)
    fd(3 * k)
    lt(90)

rt(180)
fd(6 * k)
rt(90)
fd(9 * k)

penup()
bk(3 * k)
rt(90)
pendown()

for i in range(2):
    fd(1 * k)
    rt(90)
    fd(2 * k)
    lt(90)

rt(180)
fd(3 * k)
rt(90)
fd(4 * k)
rt(90)
fd(1 * k)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(5, "white")

done()


