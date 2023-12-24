import turtle
from turtle import Turtle, Screen

timy = Turtle()
screen = Screen()


def move_forward():
    """Function to trigger with .onkey() """
    timy.forward(10)


def move_backward():
    timy.backward(10)



def turn_left():
    timy.left(10)


def turn_right():
    timy.right(10)


def clear_screen():
    timy.clear()
    timy.home()


# Make screen awake of events
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)


screen.onkey(key='c', fun=clear_screen)

# keep windows active until you click on it
screen.exitonclick()