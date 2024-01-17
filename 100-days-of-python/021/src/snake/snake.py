"""Defines the Snake class using the Turtle graphics library"""

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Represents the snake, a player-controlled legend"""

    def __init__(self):
        """Initialise the snake segments list and create the snake"""
        self.segments = []
        self._create_snake()
        self.head = self.segments[0]

    def _create_snake(self):
        """Create the initial snake body"""
        for position in STARTING_POSITIONS:
            self._add_segment(position)

    def _add_segment(self, position):
        """Add a new segment to the snake body at the given position"""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        """Reset the snake after collision"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self._create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Add a new segment to the snake"""
        self._add_segment(self.segments[-1].position())

    def move(self):
        """Move each segment to the position of the one in front of it"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Set heading up unless already going down"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Set heading down unless already going up"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Set heading left unless already going right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Set heading right unless already going left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

