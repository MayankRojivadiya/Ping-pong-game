from turtle import Turtle

class Circle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.width(8)
        self.penup()
        self.right(90)
        self.forward(10)
        self.setheading(0)
        self.pendown()
        self.circle(20)
        self.hideturtle()