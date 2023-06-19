from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('score_data.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("White")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('score_data.txt', mode='w') as score_data:
                score_data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.color("White")
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
