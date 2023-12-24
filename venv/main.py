import turtle
from turtle import Turtle, Screen

timy = Turtle()
screen = Screen()


def move_forward():
    """Function to trigger with .onkey() """
    timy.forward(10)


def reset_screen():
    turtle.reset()


# Make screen awake of events
screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.onkey(key='c', fun=reset_screen)

# keep windows active until you click on it
screen.exitonclick()