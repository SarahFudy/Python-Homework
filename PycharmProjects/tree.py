import turtle

turtle.speed(9)

#画分形树，递归函数
def appletree(distance):
    distance = int(distance)

    if (distance >= 4):

        if distance < 40:
            turtle.color('green')

        else:
            turtle.color('black')  # 主干黑色，最外枝干绿色

        turtle.forward(distance)
        turtle.right(25)
        appletree(distance-15)  #递归参数设定
        turtle.left(45)
        appletree(distance-10)
        turtle.right(20)
        turtle.backward(distance)

        if distance < 40:
            turtle.color('green')

        else:
            turtle.color('black')  # 这里有个问题，不知道问什么上下都有这个条件语句才能得到想要的图案

def main():
    turtle.pu()
    turtle.left(90)
    turtle.backward(250)
    turtle.pd()
    turtle.color('black')
    turtle.pensize(3)
    distance = 100
    appletree(distance)
    turtle.exitonclick()

if __name__ == '__main__':
    main()


