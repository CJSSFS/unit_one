import turtle
def draw_an_octagon():


    for x in range(8):
        turtle.forward(70)
        turtle.left(45)


turtle.color("orange")
turtle.begin_fill()
draw_an_octagon()
turtle.end_fill()

turtle.up()
turtle.forward(200)
turtle.down()

turtle.color("green")
turtle.begin_fill()
draw_an_octagon()
turtle.end_fill()

turtle.up()
turtle.left(90)
turtle.forward(250)
turtle.down()

turtle.color("red")
turtle.begin_fill()
draw_an_octagon()
turtle.end_fill()


turtle.exitonclick()




