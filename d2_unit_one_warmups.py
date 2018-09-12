import turtle


def draw_a_hexagon():

    for x in range(6):
        turtle.forward(100)
        turtle.left(60)

for x in range(3):
    draw_a_hexagon()
    turtle.left(20)

turtle.exitonclick()
