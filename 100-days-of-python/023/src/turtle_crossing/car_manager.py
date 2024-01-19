import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Manages the spawning, movement, and speed of cars in a game"""

    def __init__(self):
        super().__init__()
        self.garage = []
        self._move_speed = STARTING_MOVE_DISTANCE
        self._new_car()

    def spawn_car(self):
        """Spawn a new car if conditions are met"""
        if random.randint(1, 2) == 1 and self.garage[-1].xcor() < 250:
            self._new_car()

    def move(self):
        """Move all cars in the garage"""
        for car in self.garage:
            car.backward(self._move_speed)

    def speed_up(self):
        """Increase the movement speed of cars"""
        self._move_speed += MOVE_INCREMENT

    def _new_car(self):
        new_car = Turtle(shape="square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(310, random.randint(-250, 250))
        self.garage.append(new_car)
