from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.width(20)
        self.penup()
        self.goto(0,0)
        self.speed(0)
        self.y=10
        self.x=10

    def move_ball(self):
        new_y = self.ycor()+self.y
        new_x = self.xcor()+self.x
        self.goto(new_x,new_y)

    def collide_y(self):
        self.y *= -1

    def collide_x(self):
        self.x *= -1

    def collide_with_right_walls(self):
        self.goto(0, 0)
        self.x = -10
        self.y = 10

    def collide_with_left_wall(self):
        self.goto(0, 0)
        self.x = 10
        self.y = 10
