from turtle import Turtle

FONT = ("ARIAL", 24, "bold")


class Scoreboard(Turtle):
    """Represents the game scoreboard"""

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update and display the current level on the scoreboard"""
        self.clear()
        self.goto(-295, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        """Display 'GAME OVER' at the center of the screen"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def level_up(self):
        """Increment the level by 1 and update the scoreboard"""
        self.level += 1
        self.update_scoreboard()
