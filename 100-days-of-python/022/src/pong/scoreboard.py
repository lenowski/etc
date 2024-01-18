"""Defines the Scoreboard class using the Turtle graphics library"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 60, "normal")


class Scoreboard(Turtle):
    """Manages scoring"""

    def __init__(self):
        """Initialise the scoreboard"""
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard display"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display game over message"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def l_point(self):
        """Increase the score of the left player by 1 point"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increase the score of the right player by 1 point"""
        self.r_score += 1
        self.update_scoreboard()
