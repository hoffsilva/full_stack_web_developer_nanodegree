import turtle


def draw_square() :
    window = turtle.Screen()
    window.bgcolor("red")
    turtle.shape("turtle")
    turtle.color("yellow")
    turtle.speed(0)
    brad = turtle.Turtle()
    angie = turtle.Turtle()
    triangle = turtle.Turtle()

    times = 1
    while times<=1000 :
        brad.forward(100)
        brad.right(90)

        angie.circle(100)
        angie.left(2)
        times += 1

    window.exitonclick()


draw_square()