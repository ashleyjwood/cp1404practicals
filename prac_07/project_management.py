"""
Estimated Time: 4 hours
Actual Time:
"""

from project import Project
import datetime

FILENAME = "projects.txt"

NAME_INDEX = 0
DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_ESTIMATE_INDEX = 3
COMPLETION_INDEX = 4

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Main docstring."""
    print("Welcome to Pythonic Project Management")
    projects = load_entries()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            print_entries(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_entries(projects)
    print("Thank you for using custom-built project management software.")


def load_entries():
    """Read entries from a file."""
    projects = []
    try:
        with open(FILENAME, "r", encoding="utf-8") as in_file:
            in_file.readline()
            for line in in_file:
                parts = line.split('\t')
                name, start_date, priority, cost_estimate, completion_percentage = parts
                projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
            projects.sort()
            print(f"{len(projects)} projects loaded.")
    except FileNotFoundError:
        print(f"{FILENAME} not found.")
    return projects


def get_valid_string(prompt):
    """Get a non-empty string from the user."""
    string = input(prompt)
    while not string:
        print("Input can not be blank")
        string = input(prompt)
    return string


def get_valid_number(prompt):
    """Get an integer from user which is greater than zero."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Input must be > 0")
            else:
                is_valid_number = True
        except ValueError:
            print("Invalid input - please enter a valid number")
    return number  # No risk of reference before assignment


def get_valid_entry_number(projects):
    """Get an entry number from the list."""
    entry_number = get_valid_number(">>> ")

    while not entry_number <= len(projects):
        print("Invalid entry number")
        entry_number = get_valid_number(">>> ")

    return entry_number


def add_entry(projects):
    """Add a new entry to the list and sort the list based selected indices."""
    name = get_valid_string("Name: ")
    start_date = get_valid_string("Start Date: ")
    priority = get_valid_number("Priority: ")
    cost_estimate = get_valid_number("Cost Estimate: ")
    completion_percentage = 0

    projects.append([name, start_date, priority, cost_estimate, completion_percentage])
    projects.sort()
    print(f"{name} {start_date} {priority} {cost_estimate} {completion_percentage} added.")


def print_entries(projects):
    """Print the entry list (sorted by priority) and information about the entries."""
    print("Incomplete Projects: ")
    incomplete_projects = [project for project in projects if project.completion_percent != 100]
    for entry_number, project in enumerate(incomplete_projects):
        print(
            f"{(entry_number + 1):1}. {project.name}, start: {project.start_date}, "
            f"priority {project.priority}, estimate: ${project.cost_estimate}, "
            f"completion: {project.completion_percent}%")

    print("\nCompleted Projects: ")
    completed_projects = [project for project in projects if project.completion_percent == 100]
    for entry_number, project in enumerate(completed_projects):
        print(
            f"{(entry_number + 1):1}. {project.name}, start: {project.start_date}, "
            f"priority {project.priority}, estimate: ${project.cost_estimate}, "
            f"completion: {project.completion_percent}%\n")


def save_entries(projects):
    """Save the entry list to a CSV file."""
    with open(FILENAME, "w", encoding="utf-8") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(
                f"{project.name}\t{project.start_date}\t{project.priority}\t"
                f"{project.cost_estimate}\t{project.completion_percent}\n")
    print(f"{len(projects)} saved to {FILENAME}")


if __name__ == '__main__':
    main()
