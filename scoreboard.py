from turtle import Turtle
from turtle import Screen

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.pensize(2)
        self.write(arg=f"Score: {self.score}",align="center",font=('Arial',15,"normal" ))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}",align="center",font=('Arial',15,"normal" ))

    def game_over(self):

        self.goto(0,0)
        self.color("red")
        self.write(arg="GAME OVER!",align="center",font=('Comic Sans MS',45,"bold" ))
