from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


def on_quit():
    global game_is_on
    game_is_on = False
    screen._root.after(100, screen._root.destroy)


screen._root.protocol("WM_DELETE_WINDOW", on_quit)

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.2)

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset()
        scoreboard.clear()
        scoreboard.reset()

    # Detect collision with tail
    for segment in snake.all_segments[1:]:

        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.clear()
            scoreboard.reset()

screen.mainloop()
