class ProgrammingLanguage:
    """Represents a programming language object."""

    def __init__(self, name="", typing="", reflection=bool, year=0):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns boolean of the programming language typing state."""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def is_reflection(self):
        """Returns boolean of the programming language reflection state."""
        if self.reflection:
            return True
        else:
            return False

    def __str__(self):
        """Return a string representation of the instance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.is_reflection()}, First appeared in {self.year}"
