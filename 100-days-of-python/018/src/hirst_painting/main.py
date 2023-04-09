"""
Generates a grid of dots with random colors in the style of
Damien Hirst's 'Spot Paintings' using the turtle module.
"""

import random
import turtle

from hirst_painting.data import COLORS


def main():
    """
    Creates a grid of dots with randomly chosen colors.
    """

    turtle.colormode(255)
    tim = turtle.Turtle(visible=False)
    tim.speed("fastest")
    tim.penup()

    x, y = -250, -250
    for _ in range(10):
        tim.setpos(x, y)
        for _ in range(10):
            tim.dot(20, random.choice(COLORS))
            tim.forward(50)
        y += 50

    turtle.Screen().exitonclick()


if __name__ == "__main__":
    main()
