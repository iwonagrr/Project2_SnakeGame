from snake import Snake
from consts import *


class MySnake(Snake):
    def check_upper_wall(self):
        return self.head.ycor() > UPPER_LIMIT

    def check_lower_wall(self):
        return self.head.ycor() <= LOWER_LIMIT

    def check_left_wall(self):
        return self.head.xcor() < LEFT_LIMIT

    def check_right_wall(self):
        return self.head.xcor() > RIGHT_LIMIT

    def can_snake_eat_food(self, food):
        return self.head.distance(food) < SNAKE_EATING_DISTANCE

    def eating_own_tail(self):
        for segment in self.all_segments[2:]:
            return self.head.distance(segment) < MIN_TAIL_DISTANCE
