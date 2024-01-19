from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Represents the player in the turtle race game"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        """Move the player forward by the specified distance"""
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        """Reset the player to the starting position"""
        self.goto(STARTING_POSITION)

