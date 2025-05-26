import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor('black')

# Set up turtle
turtle.speed(3)
turtle.pensize(3)
turtle.color('red', 'pink')

def fun():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

# Start drawing
turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)  # Left diagonal
fun()  # Left curve
turtle.left(120)
fun()  # Right curve
turtle.forward(111.65)  # Right diagonal

turtle.end_fill()
turtle.hideturtle()
turtle.done()
