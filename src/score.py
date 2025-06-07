from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier", 35, "bold"

class Score(Turtle):
    def __init__(self, sc_pos):
        super().__init__()
        self.scr = 0
        self.color("white")
        self.penup() 
        self.goto(sc_pos)
        self.Update_score()
        self.hideturtle()
    
    def Update_score(self):
        self.clear()
        self.write(f"{self.scr}", align=ALIGNMENT, font=FONT)
        