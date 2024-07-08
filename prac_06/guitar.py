class Guitar:
    """Represents a guitar object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self, current_year):
        guitar_age = current_year - self.year
        return guitar_age

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50

    def __str__(self):
        """Return a string representation of the instance."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"
