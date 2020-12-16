from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
#Don't add parenthesis to function parameter, else it will trigger immediately
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()