"""Defines the Ball class using the Turtle graphics library"""

from turtle import Turtle


class Ball(Turtle):
    """Handles moving and bouncing the ball"""

    def __init__(self):
        """Initialise the ball"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(40)
        self.move_speed = 0.08

    def move(self):
        """Move the ball forward"""
        self.forward(10)

    def bounce_y(self):
        """Bounce the ball off the top or bottom edge"""
        self.setheading(360 - self.heading())
        self.move_speed *= 0.9

    def bounce_x(self):
        """Bounce the ball off the left or right edge"""
        self.setheading(180 - self.heading())
        self.move_speed *= 0.9

    def reset(self):
        """Reset the ball to the center"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
