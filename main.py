import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(491, 596)
screen.bgpic("snake2.png")
screen.title("🐍🐍SNAKEGAME🐍🐍")
screen.tracer(0)
s = ScoreBoard()

snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")

screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 20:
        food.new_food()
        snake.add_body()
        s.increase_score()
    if snake.head.xcor() > 220 or snake.head.xcor() < -220 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        game_is_on = False
        s.game_over()

    for i in snake.creatures:
        if i == snake.head:
            pass
        elif snake.head.distance(i) < 10:
            game_is_on = False
            s.game_over()

screen.exitonclick()
