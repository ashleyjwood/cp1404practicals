from datetime import date


class Project:
    def __init__(self, name="", start_date=date, priority=0, cost_estimate=0.0, completion_percent=0):
        """Initialise a new project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __repr__(self):
        """Return the details of the project as a string."""
        return f"Project({self.name}, {self.start_date}, {self.priority}, {self.cost_estimate}, {self.completion_percent})"

    def __lt__(self, other):
        """
        Evaluate and sort by the priority of the project.
        If projects have the same priority, sort by project name.
        """
        if self.priority == other.priority:
            return self.name < other.name
        return self.priority < other.priority
