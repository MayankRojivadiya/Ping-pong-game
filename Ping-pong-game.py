from turtle import Turtle, Screen
from src.paddle import Paddle
from src.ball import Ball
from src.border import Border
from src.score import Score
from src.circle import Circle
import time

timmy = Turtle()
timmy.color("white")
timmy.left(90)
timmy.penup()
timmy.forward(300)
timmy.setheading(270)
timmy.pendown()
def dotted():
    for _ in range(30):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
dotted()
timmy.hideturtle()


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 650)
screen.tracer(0)
is_on = True


l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
border = Border()
circle = Circle()
r_score = Score((40, 250))
l_score = Score((-45, 250))


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

while is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x() 
    
    if ball.xcor() > 370 :
        ball.reset_position()
        l_score.scr += 1
        l_score.Update_score()

    if ball.xcor() < -370 :
        ball.reset_position()
        r_score.scr += 1
        r_score.Update_score()
    

screen.exitonclick() 