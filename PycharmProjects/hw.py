# 小人张开手发射爱心，爱心向前移动

#倒入所需要用的库
import turtle as t
import time


# 先画小人，定义小人函数
def draw_LittleMan():
# 画头
    t.pensize(5)
    t.pu()
    t.goto(0,-60)
    t.pd()
    t.circle(60)
    t.pu()
    t.goto(-5,-10)
    t.pd()
# 画眼睛,椭圆（循环）
# 先画左边的眼睛
    t.pensize(0.1)
    t.begin_fill()
    t.fillcolor('black')
    a = 0.375
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a += 0.0005
            t.left(3)
            t.fd(a)
        else:
            a -=0.0005
            t.left(3)
            t.fd(a)
    t.end_fill()
# 以相同的方式画右边的眼睛
    t.pu()
    t.goto(25,-10)
    t.pd()
    t.begin_fill()
    t.fillcolor('black')
    b = 0.375
    for i in range(120):
        if 0 <= i <30 or 60 <= i <90:
            b += 0.0005
            t.left(3)
            t.fd(b)
        else:
            b -= 0.0005
            t.left(3)
            t.fd(b)
    t.end_fill()
    t.pu()
    t.home()
# 画身子
    # 躯干
    t.pensize(8)
    t.pu()
    t.goto(0,-60)
    t.pd()
    t.right(90)
    t.fd(120)
    # 腿
    t.left(90)
    t.fd(60)
    t.right(90)
    t.fd(40)
    t.pu()
    t.goto(0,-180)
    t.pd()
    t.right(45)
    t.fd(75)
    # 手
    t.pu()
    t.goto(0,-100)
    t.left(135)
    t.pd()
    t.fd(65)
    t.left(45)
    t.fd(40)
    t.pu()
    t.goto(0,-130)
    t.right(45)
    t.pd()
    t.fd(65)
    t.right(45)
    t.fd(40)
    t.pu()
    t.home()


# 画爱心,并让它向前飘动一段距离
def draw_heart(i):
    t.pensize(5)
    t.pu()
    t.goto(100+5*i, -144)  # 爱心不断向右走
    t.pd()
    t.color('purple','purple')  # 设定笔和填充的颜色
    t.begin_fill()
    t.left(140)
    t.fd(27.9125)
    for i in range(200):  # 循环，画出左边爱心的弧度
        t.right(1)
        t.forward(0.25)
    t.color('purple','purple')
    t.left(120)
    for i in range(200):  # 同理画出右边弧度
        t.right(1)
        t.forward(0.25)
    t.color('purple','purple')
    t.fd(27.9125)
    t.end_fill()


# 动画
def move():

    t.tracer(False)

    for i in range(200):
        t.reset()
        draw_LittleMan()
        draw_heart(i)
        t.update()
        time.sleep(0.2)  # 延迟0.2秒


move()
t.exitonclick()  # 点击之后再退出
