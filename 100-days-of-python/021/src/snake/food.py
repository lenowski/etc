"""Defines the Food class using the Turtle graphics library"""

import random
from turtle import Turtle


class Food(Turtle):
    """Handles spawning food at random locations"""

    def __init__(self):
        """Initialise the food"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Spawn food at random location"""
        self.goto(random.randint(-200, 200), random.randint(-200, 200))

