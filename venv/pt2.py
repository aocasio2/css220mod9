from turtle import *
rt(-90)

angle = 30

def yTree(size,depth):
    if depth > 0:
        fd(size)
        rt(angle)

        yTree(0.9 * size, depth - 1)
        lt(2*angle)
        yTree(0.9 * size, depth - 1)

        pencolor(0, 225 // depth, 0)

        rt(angle)
        fd(-size)
yTree(100,10)
Screen().extionclick()
