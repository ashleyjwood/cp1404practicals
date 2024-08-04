from random import randint
from car import Car


class UnreliableCar(Car):
    """Specialised version of a Car which has a reliability attribute."""

    def __init__(self, name, fuel: int, reliability: float):
        """Initialise the unreliable car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}"

    def drive(self, distance):
        """Drive the car a given distance if it is reliable enough."""
        if randint(0, 100) < self.reliability:
            super().drive(distance)
