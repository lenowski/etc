"""
A game where you can bet on which turtle will win a race.
"""

from random import randint
from turtle import Screen, Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POSITIONS = [-70, -40, -10, 20, 50, 80]
FINISH_LINE = 230


def main():
    """
    Runs the Turtle Race game.
    """
    screen = Screen()
    screen.setup(width=500, height=400)

    all_turtles = [Turtle(shape="turtle") for _ in range(6)]
    for i, turtle in enumerate(all_turtles):
        turtle.penup()
        turtle.color(COLORS[i])
        turtle.goto(-FINISH_LINE, Y_POSITIONS[i])

    is_race_on = bool(
        user_bet := screen.textinput(
            title="Make your bet",
            prompt="Which turtle will win the race? Enter a color: ",
        )
    )
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > FINISH_LINE:
                is_race_on = False
                winning_color = turtle.pencolor()
                print(
                    f"You've {'won' if winning_color == user_bet else 'lost'}! "
                    f"The {winning_color} turtle is the winner!"
                )

            rand_distance = randint(0, 10)
            turtle.forward(rand_distance)

    screen.exitonclick()


if __name__ == "__main__":
    main()
