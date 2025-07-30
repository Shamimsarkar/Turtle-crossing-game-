from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.initial_level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.initial_level}", False, "center", FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game is over", False, "center", FONT)

    def level_up(self):
        self.initial_level += 1
