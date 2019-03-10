from turtle import *
speed(1)
# make it slow to demo

def drawpolygon(n):
    '''

    :param n: the number of sides
    '''
    a = 360/n
    for i in range(n):
        forward(30)
        left(a)
for i in range(3,7):
    if i % 2:
        pencolor('red')
    else:
        pencolor('blue')
    drawpolygon(i)
    penup()
    forward(60)
    pendown()
exitonclick()

# 画三角形
# def draw_triangle(l) :
#     for i in range(3) :
#         t.forward(l)
#         t.right(120)

# 画任意多边形，其中l为边长，n为边的个数
# 计算机中规定36条边是圆
# def polygon(l, n) :
#     angle = 360 / n
#     for i in range(n) :
#         t.forward(l)
#         t.right(angle)

# 画五角星
# def five_star(l) :
#     t.fillcolor('red')
#     t.begin_fill()
#     for i in range(5) :
#         t.forward(l)
#         t.right(144)
#     t.end_fill()

# 画正方形
# def square(x, y, l) :
#     setpen(x, y)
#     for i in range(4) :
#         t.forward(l)
#         t.right(90)

# 画一条正方形
# def square_line(x, y, l, n, d) :
#     for i in range(n) :
#         inner_x = x + (l + d) * i
#         square(inner_x, y, l)

# square_line(-100, 100, 60, 5, 10)

# 画语文作业本
# def square_matrix(x, y, l, n, d, m) :
#     for i in range(m) :
#         inner_y = y - (l + d) * i
#         square_line(x, inner_y, l, n, d)

# square_matrix(-100, 200, 50, 5, 10, 5)
# five_star(100)

# 一个好玩的画
# for i in range(500) :
#     t.forward(i)
#     t.left(91)

