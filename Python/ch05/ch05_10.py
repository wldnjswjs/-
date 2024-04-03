import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')

for _ in range(30):
    direction = random.randrange(2)
    if direction == 0:
        my_turtle.left(90)
        my_turtle.forward(50)
    else:
        my_turtle.right(90)
        my_turtle.forward(50)

turtle.done()

