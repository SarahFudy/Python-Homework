from turtle import *

speed(1)

def fillBox(sideLength):
    begin_fill()
    for i in range(4):
        forward(sideLength)
        left(90)
    end_fill()
fillcolor('red')
backward(300)
s=20
while s<100:
    print(s)
    fillBox(s)
    penup()
    forward(s*1.2)
    pendown()
    s+=10
