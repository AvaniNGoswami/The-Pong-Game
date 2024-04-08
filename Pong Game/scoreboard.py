from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.hideturtle()
        self.l_score = 0
        self.goto(x,y)
        self.write(f"score : {self.l_score}",font = 24)

    def increase_score(self):
        self.clear()
        self.l_score+=1
        self.write(f"score : {self.l_score}", font=24)


    def game_over(self):
        self.goto(-20,20)
        #self.write("GAME OVER", font=24)
        self.write("GAME OVER ", font=24)