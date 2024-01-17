"""The legendary Snake game"""

import time
from turtle import Screen

from snake.food import Food
from snake.scoreboard import Scoreboard
from snake.snake import Snake

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FOOD_COLLISION = 15
WALL_COLLISION = 280
TAIL_COLLISION = 10

def main():
    """Runs the legend"""

    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    screen.bgcolor("black")
    screen.title("Snake")

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < FOOD_COLLISION:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall.
        if (
            snake.head.xcor() > WALL_COLLISION
            or snake.head.xcor() < -WALL_COLLISION
            or snake.head.ycor() > WALL_COLLISION
            or snake.head.ycor() < -WALL_COLLISION
        ):
            scoreboard.reset()
            snake.reset()

        # Detect collision with tail.
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < TAIL_COLLISION:
                scoreboard.reset()
                snake.reset()

    screen.exitonclick()


if __name__ == "__main__":
    main()

