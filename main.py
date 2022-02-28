from turtle import Screen
from my_own_snake import MySnake
from food import Food
from scoreboard import Scoreboard
from consts import *
import time

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0)

snake = MySnake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.extend, "c")


def on_quit():
    global game_is_on
    scoreboard.update_highest_score()
    game_is_on = False
    screen._root.after(100, screen._root.destroy)


def reset_game():
    snake.reset()
    scoreboard.clear()
    scoreboard.reset()
    food.refresh()


screen._root.protocol("WM_DELETE_WINDOW", on_quit)

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.2)

    if snake.can_snake_eat_food(food):
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.eating_own_tail() or snake.check_upper_wall() or snake.check_lower_wall() or snake.check_left_wall() or snake.check_right_wall():
        reset_game()

screen.mainloop()
