from turtle import *

screensize(1000, 1000)
tracer(0)
k = 20
left(90)
pendown()

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
for x in range(-20, 40):
    for y in range(-20, 40):
        setpos(x * k, y * k)
        dot(3)

done()

print((21 + 1) * 2)
