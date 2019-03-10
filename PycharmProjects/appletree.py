# 目标：画一棵会掉果子的苹果树
# 思路：先用递归函数画出树干及树枝，再在树上的某些位置画果子，最后使果子从树上掉下来

import turtle
from random import randint
#import random
#import math

# use turtle.
turtle.speed(9)
#设置速度，1-9中，9最快

#画树的主干和枝丫部分，递归函数
def appletree(distance):
    distance = int(distance)

    if (distance >= 4):
        if distance < 40:
            turtle.color('green')

        else:
            turtle.color('black')

        turtle.forward(distance)
        turtle.right(25)
        appletree(distance-15)
        turtle.left(45)
        appletree(distance-10)
        turtle.right(20)
        turtle.backward(distance)

        if distance < 40:
            turtle.color('green')

        else:
            turtle.color('black')

#画苹果，这里用random库，生成随机数，也就是随机生成果子在树上的位置

# turtle.color('red')
#
# turtle.fillcolor('red')
# turtle.penup()
# turtle.goto(-300, 50)
# turtle.pendown()
# turtle.circle(9)
# turtle.penup()
# turtle.goto(-200, 55)
# turtle.pendown()
# turtle.circle(9)
# turtle.penup()
# turtle.goto(-255, 70)
# turtle.pendown()
# turtle.circle(9)
# turtle.penup()
# turtle.goto(-160, 63)
# turtle.pendown()
# turtle.circle(9)
# turtle.penup()
# turtle.goto(-100, 70)
# turtle.pendown()
# turtle.circle(9)
# turtle.penup()
# turtle.goto(-50,75 )
# turtle.pendown()
# turtle.circle(9)
# turtle.penup()
# turtle.goto(85, 80)
# turtle.pendown()
# turtle.circle(9)
# turtle.penup()
# turtle.goto(150, 90)
# turtle.pendown()
# turtle.circle(9)
# turtle.penup()
# turtle.goto(0, 100)
# turtle.pendown()
# turtle.circle(9)
# turtle.penup()
# turtle.goto(50, 110)
# turtle.pendown()
# turtle.circle(9)
# turtle.penup()
# turtle.goto(80, 100)
# turtle.pendown()
# turtle.circle(9)
# turtle.penup()
# turtle.goto(100, 50)
# turtle.pendown()
# turtle.circle(9)
#
# turtle.penup()
# turtle.home()
# turtle.pendown()

def main():
    turtle.pu()
    turtle.left(90)
    turtle.backward(250)
    turtle.pd()
    turtle.color('black')
    # turtle.colormode(255)  # 颜色模式为真彩色
    # r = randint(0, 255)
    # g = randint(0, 255)
    # b = randint(0, 255)
    # turtle.pencolor(r, g, b)  # 画笔颜色每次随机
    turtle.pensize(3)
    distance = 100
    appletree(distance)
    turtle.exitonclick()

if __name__ == '__main__':
    main()


