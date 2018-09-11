import turtle
turtle.speed(50)
def draw_an_octagon():


    for x in range(8):
        turtle.forward(70)
        turtle.left(45)


turtle.color("orange")
turtle.begin_fill()
draw_an_octagon()
turtle.end_fill()

turtle.up()
turtle.right(90)
turtle.forward(90)
turtle.down()
draw_an_octagon()


turtle.exitonclick()




