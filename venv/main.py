from turtle import Turtle, Screen

timy = Turtle()
screen = Screen()


def move_forward():
    """Function to trigger with .onkey() """
    timy.forward(10)


# Make screen awake of events
screen.listen()
screen.onkey(key="space", fun=move_forward)

# keep windows active until you click on it
screen.exitonclick()