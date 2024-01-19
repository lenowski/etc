import time
from turtle import Screen

from turtle_crossing.car_manager import CarManager
from turtle_crossing.player import Player
from turtle_crossing.scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SLEEP_TIME = 0.1
COLLISION_DISTANCE = 25


def initialise_game():
    """Initialise the game components and return them"""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    screen.bgcolor("black")

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.move, "Up")

    return screen, player, car_manager, scoreboard


def check_collision(player, car_manager):
    """Check for collisions between the turtle and cars"""
    for car in car_manager.garage:
        if (
            abs(car.xcor() - player.xcor()) < COLLISION_DISTANCE
            and abs(car.ycor() - player.ycor()) < COLLISION_DISTANCE
        ):
            return True
    return False


def main():
    """Run the main game loop"""
    screen, player, car_manager, scoreboard = initialise_game()

    game_is_on = True
    while game_is_on:
        time.sleep(SLEEP_TIME)
        screen.update()
        car_manager.spawn_car()
        car_manager.move()

        # Detect successful street crossing
        if player.ycor() >= SCREEN_HEIGHT / 2:
            player.level_up()
            scoreboard.level_up()
            car_manager.speed_up()

        # Detect collision with car
        if check_collision(player, car_manager):
            game_is_on = False
            scoreboard.game_over()
            screen.update()  # Force screen update

    screen.exitonclick()


if __name__ == "__main__":
    main()
