#导入turtle库
import turtle
#设置屏幕大小
screen = turtle.Screen()
screen.setup(800,600)
#获取画笔并设置一些属性：圆形、红色、快
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
#抬起画笔
circle.up()
#重新获取画笔
square = turtle.Turtle()
#重新设置画笔属性：四方形、绿色、快
square.shape('square')
square.color('green')
square.speed('fastest')
#重新抬起画笔
square.up()
#跳到指定坐标位置
circle.goto(0,280)
#复制当前图形
circle.stamp()
k = 0
for i in range(1, 17):
    y = 30*i
    for j in range(i-k):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()
    if i % 4 == 0:
        x = 30*(j+1)
        circle.color('red')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()
        k += 2
    if i % 4 == 3:
        x = 30*(j+1)
        circle.color('yellow')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()
square.color('brown')
for i in range(17,20):
    y = 30*i
    for j in range(3):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()
turtle.exitonclick()