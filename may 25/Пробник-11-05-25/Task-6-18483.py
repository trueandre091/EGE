from turtle import *

screensize(2000, 2000)
tracer(0)
k = 20
left(90)

for i in range(4):
    fd(16 * k)
    lt(90)
    fd(20 * k)
    lt(90)

penup()

fd(4 * k)
lt(90)
fd(8 * k)
rt(180)

pendown()
for i in range(3):
    fd(35 * k)
    lt(90)
    fd(6 * k)
    lt(90)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto( x * k, y * k)
        dot(5, "white")

done()

# (16 + 20) * 2 + (35 + 6) * 2
# Out: 154
# 154 - (8 + 6) * 2
# Out: 126
