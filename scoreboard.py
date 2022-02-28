from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.goto(-50, 270)
        self.color("white")
        self.ht()
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score} High score = {self.high_score}", move=False, font=("courier", 18, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(-90, 0)
    #     self.write("GAME OVER", move=False, font=("courier", 25, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def update_highest_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{self.high_score}")