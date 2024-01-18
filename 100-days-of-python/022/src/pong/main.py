"""The Pong game"""

import time
from turtle import Screen

from pong.ball import Ball
from pong.paddle import Paddle
from pong.scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WALL_COLLISION_YCOR = 280
PADDLE_COLLISION_DIST = 50
PADDLE_BOUNCE_EDGE_XCOR = 330
SCORE_XCOR = 380


def setup_screen():
    """Set up the game screen"""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    screen.bgcolor("black")
    screen.title("Pong")
    return screen


def setup_game():
    """Set up the game elements (paddles, ball, scoreboard)"""
    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()
    return r_paddle, l_paddle, ball, scoreboard


def handle_key_events(screen, r_paddle, l_paddle):
    """Handle key events for paddle movement"""
    screen.listen()
    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down, "Down")
    screen.onkey(l_paddle.up, "w")
    screen.onkey(l_paddle.down, "s")


def handle_wall_collision(ball):
    """Handle ball collisions with the top and bottom walls"""
    if ball.ycor() > WALL_COLLISION_YCOR or ball.ycor() < -WALL_COLLISION_YCOR:
        ball.bounce_y()


def handle_paddle_collision(ball, r_paddle, l_paddle):
    """Handle ball collisions with paddles"""
    if (
        ball.distance(r_paddle) < PADDLE_COLLISION_DIST
        and ball.xcor() > PADDLE_BOUNCE_EDGE_XCOR
        or ball.distance(l_paddle) < PADDLE_COLLISION_DIST
        and ball.xcor() < -PADDLE_BOUNCE_EDGE_XCOR
    ):
        ball.bounce_x()


def ensure_paddles_on_screen(l_paddle, r_paddle):
    """Ensure paddles stay within the screen boundaries."""
    boundary_limit = SCREEN_HEIGHT / 2 - PADDLE_COLLISION_DIST
    l_paddle.sety(max(min(l_paddle.ycor(), boundary_limit), -boundary_limit))
    r_paddle.sety(max(min(r_paddle.ycor(), boundary_limit), -boundary_limit))


def handle_score(ball, scoreboard):
    """Handle scoring and resetting the ball"""
    if ball.xcor() > SCORE_XCOR:
        ball.reset()
        scoreboard.l_point()
    elif ball.xcor() < -SCORE_XCOR:
        ball.reset()
        scoreboard.r_point()


def main():
    """Run the game"""

    screen, r_paddle, l_paddle, ball, scoreboard = setup_screen(), *setup_game()
    handle_key_events(screen, r_paddle, l_paddle)

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        handle_wall_collision(ball)
        handle_paddle_collision(ball, r_paddle, l_paddle)
        handle_score(ball, scoreboard)
        ensure_paddles_on_screen(l_paddle, r_paddle)
    screen.exitonclick()


if __name__ == "__main__":
    main()
