

def tree(distance):
    distance = int(distance)
    if (distance > 4):
        forward(distance)
        right(25)
        tree(distance*0.8-2)
        left(45)
        tree(distance-10)
        right(20)
        back(distance)
    tree(90)