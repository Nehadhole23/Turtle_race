from turtle import Turtle

FONT = ("courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-270, 250)
        self.update_score()

    def update_score(self):
        self.write(f"Level:{self.level}", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=FONT)
