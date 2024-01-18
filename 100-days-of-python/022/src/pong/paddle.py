"""Defines the Paddle class using the Turtle graphics library"""

from turtle import Turtle


class Paddle(Turtle):
    """Handles moving the paddle"""

    def __init__(self, coords):
        """Initialise the paddle"""
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.goto(coords)

    def up(self):
        """Move the paddle up"""
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        """Move the paddle down"""
        self.goto(self.xcor(), self.ycor() - 20)
