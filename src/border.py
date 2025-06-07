from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.left(90)
        self.forward(300)
        self.pendown()
        self.right(90)
        self.forward(370)
        self.right(90)
        self.forward(600)
        self.right(90)
        self.forward(740)
        self.right(90)
        self.forward(600)
        self.right(90)
        self.forward(370)
        self.hideturtle()