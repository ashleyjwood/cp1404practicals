from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi which includes a fanciness factor."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        """Return a string representation of the car including the flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate and return the fare for the taxi trip, including the flagfall."""
        return super().get_fare() + SilverServiceTaxi.flagfall
