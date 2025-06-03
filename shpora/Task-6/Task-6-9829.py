from turtle import *

tracer(0)
screensize(2000, 2000)
k = 20
left(90)
rt(90)
dot(6)
for i in range(3):
    rt(45)
    fd(10 * k)
    rt(45)

rt(315)
fd(10 * k)
for i in range(2):
    rt(90)
    fd(10 * k)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto( x * k, y * k)
        dot(3)

done()

