"""
Estimated Time: 4 hours
Actual Time:
"""

from project import Project
import datetime

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
    """Program to keep track of your projects, modify priority and completion percentage, and save to a .txt file."""
    print("Welcome to Pythonic Project Management")
    projects = []
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_entries()
        elif choice == "S":
            save_entries(projects)
        elif choice == "D":
            print_entries(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_entry(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_entries():
    """Read entries from a file."""
    projects = []
    filename = f"{input(f"Textfile name: ")}.txt"  # Assumed: .txt file with \t delimiters
    try:
        with open(filename, "r", encoding="utf-8") as in_file:
            in_file.readline()
            for line in in_file:
                parts = line.split('\t')
                name, start_date, priority, cost_estimate, completion_percent = parts
                projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percent)))
            projects.sort()
            print(f"{len(projects)} projects loaded.")
    except FileNotFoundError:
        print(f"{filename} not found.")
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
            if number < 0:
                print("Input must be >= 0")
            else:
                is_valid_number = True
        except ValueError:
            print("Invalid input - please enter a valid number")
    return number  # No risk of reference before assignment


def get_valid_entry_number(projects):
    """Get an entry number from the list."""
    entry_number = get_valid_number(">>> ")

    while not 0 < entry_number <= len(projects):
        print("Invalid entry number")
        entry_number = get_valid_number(">>> ")

    return entry_number


def add_entry(projects):
    """Add a new entry to the list and sort the list based selected indices."""
    print("Let's add a new project")
    name = get_valid_string("Name: ")
    start_date = get_valid_string("Start Date (DD/MM/YYYY): ")
    priority = get_valid_number("Priority: ")
    cost_estimate = float(get_valid_number("Cost Estimate: $"))
    completion_percent = 0

    projects.append(Project(name, start_date, priority, cost_estimate, completion_percent))
    projects.sort()
    print(f"Project '{name}' added successfully with start date {start_date}, priority {priority}, "
          f"cost estimate ${cost_estimate:,.2f}, and completion percentage {completion_percent}%.")


def print_entries(projects):
    """Print the entry list (sorted by priority) and information about the entries."""
    while not projects:
        print("Project list cannot be blank")
        return None
    print("Incomplete Projects: ")
    incomplete_projects = [project for project in projects if project.completion_percent != 100]
    print_entries_layout(incomplete_projects)

    print("\nCompleted Projects: ")
    completed_projects = [project for project in projects if project.completion_percent == 100]
    print_entries_layout(completed_projects)
    print()  # Spacing for readability


def print_entries_layout(projects):
    """Define the layout for the entries when printed."""
    for project in projects:
        print(
            f"  {project.name}, start: {project.start_date}, "
            f"priority {project.priority}, estimate: ${project.cost_estimate:,.2f}, "
            f"completion: {project.completion_percent}%")


def update_project(projects):
    """Update priority or completion percentage of a project."""
    if not projects:
        print("No projects to update.")
        return

    print("Select project number to update: ")
    for i, project in enumerate(projects):
        print(f"{i + 1}. {project.name}")
    project_number = get_valid_entry_number(projects) - 1

    project_to_update = projects[project_number]
    print(f"Selected project: {project_to_update.name}")

    print("Update (P)riority or (C)ompletion percentage?")
    update_project_menu(project_to_update)

    projects.sort()
    print(f"Project '{project_to_update.name}' updated.")


def update_project_menu(project_to_update):
    """Menu to update the priority and completion percentage."""
    choice = input(">>> ").upper()
    is_valid_choice = False
    while not is_valid_choice:
        if choice == "P":
            print(f"Current priority is: {project_to_update.priority}")
            new_priority = get_valid_number("New priority: ")
            project_to_update.priority = new_priority
            is_valid_choice = True
        elif choice == "C":
            print(f"Current completion percentage is: {project_to_update.completion_percent}%")
            new_completion = get_valid_number("New completion percentage: ")
            project_to_update.completion_percent = new_completion
            is_valid_choice = True
        else:
            print("Invalid choice")
            choice = input(">>> ").upper()


def save_entries(projects):
    """Save the entry list to a CSV file."""
    filename = f"{input("Textfile name to save: ")}.txt"
    with open(filename, "w", encoding="utf-8") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(
                f"{project.name}\t{project.start_date}\t{project.priority}\t"
                f"{project.cost_estimate}\t{project.completion_percent}\n")
    print(f"{len(projects)} saved to {filename}")


def filter_projects_by_date(projects):
    """Filter and display projects that start after a given date."""
    DATE_FORMAT = "%d/%m/%Y"
    date_string = get_valid_string("Show projects that start after date (DD/MM/YYYY): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()
        filtered_projects = [project for project in projects if
                             datetime.datetime.strptime(project.start_date, DATE_FORMAT).date() > filter_date]
        print_entries(filtered_projects)
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY.")


if __name__ == '__main__':
    main()
