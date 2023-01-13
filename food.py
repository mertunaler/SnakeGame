from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5,0.5)

        x_c = random.randint(-200,200)
        y_c = random.randint(-200,200)
        self.goto(x_c, y_c)

    def new_food(self):
        x_c = random.randint(-200, 200)
        y_c = random.randint(-200, 200)
        self.goto(x_c, y_c)
