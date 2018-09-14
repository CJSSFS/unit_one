# Chad Scott
# 9/13/18
# assignment_one.py
# This is the first option to draw four differently colored octagons


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
# I am telling the turtle to go to the next point and draw the next octagon
turtle.up()
turtle.forward(200)
turtle.down()

turtle.color("green")
turtle.begin_fill()
draw_an_octagon()
turtle.end_fill()

turtle.up()
turtle.back(250)
turtle.right(90)
turtle.forward(100)
turtle.down()

turtle.color("red")
turtle.begin_fill()
draw_an_octagon()
turtle.end_fill()

turtle.up()
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.down()


turtle.color("yellow")
turtle.begin_fill()
draw_an_octagon()
turtle.end_fill()

turtle.exitonclick()




