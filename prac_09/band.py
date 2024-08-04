class Band:
    """Band class to handle a group of musicians."""

    def __init__(self, name=""):
        """Initialise the band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band with its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Iterate through the musicians and have them play their instrument."""
        return "\n".join(musician.play() for musician in self.musicians)
