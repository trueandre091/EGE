from turtle import *

screensize(1000, 1000)
tracer(0)
lt(90)
pendown()
k = 20

for i in range(2):
    rt(120)
    fd(7 * k)

rt(300)

for i in range(2):
    rt(120)
    fd(7 * k)

penup()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k,y * k)
        dot(3)

done()

# 42

