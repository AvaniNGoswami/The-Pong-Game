from turtle import Turtle
WIDTH = 20
HEIGHT = 5


class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.goto(x,y)
        self.penup()
        self.color("white")
        self.width(WIDTH)
        self.shapesize(HEIGHT, 1)

    def up(self):
        new_y = self.ycor()+30
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
