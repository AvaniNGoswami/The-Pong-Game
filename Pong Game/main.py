from turtle import Screen,Turtle
from paddle1 import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard_l = Scoreboard(-200, 250)
scoreboard_r = Scoreboard(200, 250)
write = Turtle()

write.penup()
write.hideturtle()
write.color("white")
write.goto(-20, -20)


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

speed = 0.1

game = True
while game:
    time.sleep(speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collide_y()
    if (r_paddle.distance(ball) < 50 and ball.xcor() > 320) or (l_paddle.distance(ball) < 50 and ball.xcor() < -320):
        ball.collide_x()
        speed -= 0.002
        time.sleep(speed)
        ball.speed(10)
    if ball.xcor() > 385:
        ball.collide_with_right_walls()
        scoreboard_l.increase_score()
    if ball.xcor() < -385:
        ball.collide_with_left_wall()
        scoreboard_r.increase_score()
    if scoreboard_l.l_score == 11:
        game = False
        scoreboard_l.game_over()
        write.write("Left player won", font = 24)
        break
    if scoreboard_r.l_score == 11:
        game = False
        scoreboard_l.game_over()
        write.write("Right player won", font = 24)
        break


screen.exitonclick()
