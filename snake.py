from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake():


    def __init__(self):

        self.creatures = []
        self.create_snake()
        self.head = self.creatures[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.increase_size(i)
    def increase_size(self,position):
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)
        self.creatures.append(new_segment)
    def add_body(self):
        self.increase_size(self.creatures[-1].position())

    def move(self):
        for i in range(len(self.creatures) - 1, 0, -1):
            n_x = self.creatures[i - 1].xcor()
            n_y = self.creatures[i - 1].ycor()
            self.creatures[i].goto(n_x, n_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)